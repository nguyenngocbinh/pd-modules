"""
simulation_runner.py - Chạy toàn bộ calibration simulation.

Orchestrate các bước:
1. Tạo simulation grid (alpha × beta)
2. Tính grade probabilities
3. Tính default rates từ observed data
4. Tính AR và validation metrics
5. Tổng hợp kết quả
"""
import numpy as np
from dataclasses import dataclass
from typing import Optional
import time

from .calibration_types import MasterScale, ObservedData, ValidationResult
from .config import SimulationGridConfig, StatisticalTestConfig
from . import (
    beta_distribution,
    default_rate_calculator,
    accuracy_ratio,
    condition_checker,
    statistical_tests,
)


@dataclass
class CalibrationResult:
    """Kết quả đầy đủ của simulation."""
    # Parameters
    alphas: np.ndarray           # shape: (n_simulations,)
    betas: np.ndarray            # shape: (n_simulations,)
    
    # Distributions
    grade_probabilities: np.ndarray    # shape: (n_sims, n_grades)
    cumulative_probabilities: np.ndarray  # shape: (n_sims, n_grades)
    
    # Score Cutoffs - SINGLE SOURCE OF TRUTH cho grade assignment
    # Quy ước: Grade i có score trong khoảng [cutoff[i+1], cutoff[i])
    # (dấu = ở cận DƯỚI, scores sorted descending)
    # Score cao hơn thì vào grade tốt hơn (index nhỏ hơn)
    score_cutoffs: np.ndarray        # shape: (n_sims, n_grades + 1)
    
    # Statistics
    grade_bads: np.ndarray         # shape: (n_sims, n_grades)
    grade_totals: np.ndarray       # shape: (n_sims, n_grades)
    grade_default_rates: np.ndarray  # shape: (n_sims, n_grades)
    
    # Metrics
    implied_pds: np.ndarray        # shape: (n_simulations,)
    accuracy_ratios: np.ndarray    # shape: (n_simulations,)
    
    # Validations
    n_max_pd_violations: np.ndarray     # shape: (n_simulations,)
    n_monotonicity_violations: np.ndarray  # shape: (n_simulations,)
    n_binomial_one_tail: np.ndarray     # shape: (n_simulations,)
    n_homogeneity: np.ndarray           # shape: (n_simulations,) - đếm số cặp grades fail (CI overlap)
    
    # Concentration metrics
    min_concentration: np.ndarray       # shape: (n_simulations,) - tỷ trọng grade nhỏ nhất
    max_concentration: np.ndarray       # shape: (n_simulations,) - tỷ trọng grade lớn nhất
    
    # Metadata
    master_scale: MasterScale
    n_observations: int
    elapsed_time: float


class CalibrationSimulationRunner:
    """
    Runner cho calibration simulation.
    
    Sử dụng fully vectorized NumPy operations để maximize performance.
    """
    
    def __init__(
        self,
        master_scale: MasterScale,
        observed_data: ObservedData,
        grid_config: Optional[SimulationGridConfig] = None,
        test_config: Optional[StatisticalTestConfig] = None,
        verbose: bool = True
    ):
        """
        Khởi tạo runner.
        
        Args:
            master_scale: Master scale configuration
            observed_data: Dữ liệu quan sát đã chuẩn bị
            grid_config: Config cho simulation grid
            test_config: Config cho statistical tests
            verbose: In progress logs
        """
        self.master_scale = master_scale
        self.observed_data = observed_data
        self.grid_config = grid_config or SimulationGridConfig()
        self.test_config = test_config or StatisticalTestConfig()
        self.verbose = verbose
    
    def _log(self, message: str):
        """Print log nếu verbose=True."""
        if self.verbose:
            timestamp = time.strftime("%H:%M:%S")
            print(f"[{timestamp}] {message}")
    
    def run(self) -> CalibrationResult:
        """
        Chạy toàn bộ simulation.
        
        Returns:
            CalibrationResult chứa tất cả kết quả
        """
        start_time = time.time()
        
        # Step 1: Tạo simulation grid
        self._log("Step 1: Tạo simulation grid (alpha × beta)")
        alphas, betas = self._create_parameter_grid()
        n_simulations = len(alphas)
        self._log(f"  -> Tổng số simulations: {n_simulations:,}")
        
        # Step 2: Tính grade probabilities
        self._log("Step 2: Tính grade probabilities từ Beta distribution")
        grade_probs = beta_distribution.compute_grade_probabilities_batch(
            alphas, betas, self.master_scale.n_grades
        )
        cum_probs = np.cumsum(grade_probs, axis=1)
        
        # Step 3: Tính implied PD
        self._log("Step 3: Tính implied PD")
        implied_pds = beta_distribution.compute_implied_pd_batch(
            grade_probs, self.master_scale.mid_pds
        )
        
        # Step 3b: Pre-compute score tie boundaries (một lần cho tất cả simulations)
        self._log("Step 3b: Pre-compute score tie boundaries")
        precomputed_boundaries = default_rate_calculator.precompute_score_tie_boundaries(
            self.observed_data.scores
        )
        
        # Step 4: Tính grade statistics từ observed data (FULLY VECTORIZED)
        self._log("Step 4: Tính grade statistics (bads, totals, default rates)")
        bads, totals, default_rates, to_indices = default_rate_calculator.compute_grade_statistics_batch(
            self.observed_data, cum_probs, precomputed_boundaries
        )
        
        # Step 4b: Tính score cutoffs từ adjusted boundaries (SINGLE SOURCE OF TRUTH)
        self._log("Step 4b: Tính score cutoffs từ adjusted boundaries")
        score_cutoffs = default_rate_calculator.compute_score_cutoffs_batch(
            self.observed_data, to_indices
        )
        
        # Step 5: Tính Accuracy Ratio
        self._log("Step 5: Tính Accuracy Ratio (Gini)")
        # Sort theo grade từ xấu đến tốt (reverse order) để tính AR
        dr_reversed = default_rates[:, ::-1]
        totals_reversed = totals[:, ::-1]
        ar_values = accuracy_ratio.compute_accuracy_ratio_batch(dr_reversed, totals_reversed)
        
        # Step 6: Kiểm tra điều kiện
        self._log("Step 6: Kiểm tra điều kiện (max_pd, monotonicity)")
        n_max_pd = condition_checker.count_max_pd_violations_batch(
            default_rates, self.master_scale.max_pds
        )
        n_monotonicity = condition_checker.count_monotonicity_violations_batch(default_rates)
        
        # Step 7: Statistical tests
        self._log("Step 7: Chạy statistical tests")
        n_binom_1 = statistical_tests.compute_binomial_one_tail_failures_batch(
            bads, totals, self.master_scale.mid_pds, self.test_config.confidence_level
        )
        n_homo = statistical_tests.compute_homogeneity_failures_batch(
            default_rates, totals,
            self.test_config.homogeneity_lower_quantile,
            self.test_config.homogeneity_upper_quantile
        )
        
        # Step 8: Tính concentration metrics
        self._log("Step 8: Tính concentration metrics (min/max grade proportion)")
        # Tỷ trọng từng grade = totals / tổng observations
        concentrations = totals / totals.sum(axis=1, keepdims=True)
        min_concentration = concentrations.min(axis=1)
        max_concentration = concentrations.max(axis=1)
        
        elapsed = time.time() - start_time
        self._log(f"Hoàn thành! Thời gian: {elapsed:.2f}s")
        
        return CalibrationResult(
            alphas=alphas,
            betas=betas,
            grade_probabilities=grade_probs,
            cumulative_probabilities=cum_probs,
            score_cutoffs=score_cutoffs,
            grade_bads=bads,
            grade_totals=totals,
            grade_default_rates=default_rates,
            implied_pds=implied_pds,
            accuracy_ratios=ar_values,
            n_max_pd_violations=n_max_pd,
            n_monotonicity_violations=n_monotonicity,
            n_binomial_one_tail=n_binom_1,
            n_homogeneity=n_homo,
            min_concentration=min_concentration,
            max_concentration=max_concentration,
            master_scale=self.master_scale,
            n_observations=self.observed_data.n_observations,
            elapsed_time=elapsed
        )
    
    def _create_parameter_grid(self) -> tuple[np.ndarray, np.ndarray]:
        """
        Tạo grid các cặp (alpha, beta) cho simulation.
        
        Returns:
            Tuple (alphas, betas), mỗi array có shape (n_alpha × n_beta,)
        """
        alpha_values = self.grid_config.generate_alpha_values()
        beta_values = self.grid_config.generate_beta_values()
        
        # Meshgrid và flatten
        alpha_grid, beta_grid = np.meshgrid(alpha_values, beta_values)
        
        return alpha_grid.flatten(), beta_grid.flatten()