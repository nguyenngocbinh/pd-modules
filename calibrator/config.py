"""
config.py - Cấu hình cho calibration simulation.
"""
from dataclasses import dataclass, field
from typing import Tuple
import numpy as np

from .calibration_types import MasterScale


@dataclass(frozen=True)
class SimulationGridConfig:
    """
    Cấu hình cho grid simulation (alpha, beta ranges).
    
    Attributes:
        alpha_start: Giá trị bắt đầu của alpha
        alpha_stop: Giá trị kết thúc của alpha
        beta_start: Giá trị bắt đầu của beta
        beta_stop: Giá trị kết thúc của beta
        step: Bước nhảy cho cả alpha và beta
    """
    alpha_start: float = 0.3
    alpha_stop: float = 6.0
    beta_start: float = 0.3
    beta_stop: float = 6.0
    step: float = 0.01
    
    def generate_alpha_values(self) -> np.ndarray:
        """Tạo array các giá trị alpha."""
        return np.arange(self.alpha_start, self.alpha_stop, self.step)
    
    def generate_beta_values(self) -> np.ndarray:
        """Tạo array các giá trị beta."""
        return np.arange(self.beta_start, self.beta_stop, self.step)
    
    @property
    def n_alpha(self) -> int:
        return len(self.generate_alpha_values())
    
    @property
    def n_beta(self) -> int:
        return len(self.generate_beta_values())
    
    @property
    def n_simulations(self) -> int:
        return self.n_alpha * self.n_beta


@dataclass(frozen=True)
class StatisticalTestConfig:
    """
    Cấu hình cho các statistical tests.
    
    Attributes:
        confidence_level: Mức tin cậy (default 95%)
        homogeneity_lower_quantile: Quantile dưới cho homogeneity test
        homogeneity_upper_quantile: Quantile trên cho homogeneity test
    """
    confidence_level: float = 0.95
    homogeneity_lower_quantile: float = 0.025
    homogeneity_upper_quantile: float = 0.975
    
    @property
    def alpha_level(self) -> float:
        """Alpha level = 1 - confidence_level."""
        return 1 - self.confidence_level


def create_default_master_scale() -> MasterScale:
    """
    Tạo master scale mặc định với 10 grades.
    
    Returns:
        MasterScale với các grades từ AAA đến D
    """
    grade_names = np.array(["AAA", "AA", "A", "BBB", "BB", "B", "CCC", "CC", "C", "D"])
    max_pds = np.array([
        0.00143254768933339, 0.00279481499339845, 0.0054525171521232,
        0.0106375353518648, 0.0207531962220622, 0.0404882464955491,
        0.0789901510467888, 0.154105067580055, 0.300649784044422,
        0.586549774549114
    ])
    
    min_pds = np.concatenate([[0.0], max_pds[:-1]])
    mid_pds = (min_pds + max_pds) / 2
    grade_nums = np.arange(1, len(grade_names) + 1)
    
    return MasterScale(
        grade_names=grade_names,
        grade_nums=grade_nums,
        min_pds=min_pds,
        max_pds=max_pds,
        mid_pds=mid_pds
    )