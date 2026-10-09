"""
statistical_tests.py - Các statistical tests cho calibration validation.

Bao gồm:
1. Binomial test: Kiểm tra observed DR có phù hợp với expected PD
2. Homogeneity test: Kiểm tra sự phân biệt giữa các grades
"""
import numpy as np
from scipy.stats import binom


def compute_binomial_one_tail_failures(
    observed_bads: np.ndarray,
    totals: np.ndarray,
    expected_pds: np.ndarray,
    confidence_level: float = 0.95
) -> int:
    """
    Kiểm tra binomial one-tailed: observed bads > critical value.
    
    H0: True PD = expected PD
    H1: True PD > expected PD (one-tailed, conservative)
    
    Args:
        observed_bads: Số defaults quan sát, shape (n_grades,)
        totals: Số observations mỗi grade, shape (n_grades,)
        expected_pds: PD kỳ vọng mỗi grade (mid_pd), shape (n_grades,)
        confidence_level: Mức tin cậy
        
    Returns:
        Số grades fail test
    """
    # Critical value tại quantile = confidence_level
    critical_values = binom.ppf(confidence_level, totals, expected_pds)
    
    # Fail nếu observed > critical
    failures = observed_bads > critical_values
    
    return int(failures.sum())


def compute_binomial_two_tail_failures(
    observed_bads: np.ndarray,
    totals: np.ndarray,
    expected_pds: np.ndarray,
    confidence_level: float = 0.95
) -> int:
    """
    Kiểm tra binomial two-tailed: observed bads nằm ngoài confidence interval.
    
    Args:
        observed_bads: Số defaults quan sát, shape (n_grades,)
        totals: Số observations mỗi grade, shape (n_grades,)
        expected_pds: PD kỳ vọng mỗi grade, shape (n_grades,)
        confidence_level: Mức tin cậy
        
    Returns:
        Số grades fail test
    """
    alpha = 1 - confidence_level
    
    # Confidence interval
    lower_bound = binom.ppf(alpha / 2, totals, expected_pds)
    upper_bound = binom.ppf(1 - alpha / 2, totals, expected_pds)
    
    # Fail nếu nằm ngoài interval
    failures = (observed_bads < lower_bound) | (observed_bads > upper_bound)
    
    return int(failures.sum())


def compute_homogeneity_failures(
    default_rates: np.ndarray,
    totals: np.ndarray,
    lower_quantile: float = 0.025,
    upper_quantile: float = 0.975
) -> int:
    """
    Kiểm tra homogeneity: Confidence intervals của adjacent grades không overlap.
    
    Nếu CI của grade i overlap với CI của grade i+1, các grades không phân biệt rõ.
    
    Args:
        default_rates: DR mỗi grade, sorted từ tốt đến xấu
        totals: Số observations mỗi grade
        lower_quantile: Quantile dưới cho CI
        upper_quantile: Quantile trên cho CI
        
    Returns:
        Số cặp grades fail test
    """
    # Tính confidence intervals cho DR
    lower_bounds = binom.ppf(lower_quantile, totals, default_rates) / np.maximum(totals, 1)
    upper_bounds = binom.ppf(upper_quantile, totals, default_rates) / np.maximum(totals, 1)
    
    # So sánh upper bound của grade i với lower bound của grade i+1
    # Fail nếu upper[i] >= lower[i+1] (CI overlap - grades không phân biệt rõ)
    failures = upper_bounds[:-1] >= lower_bounds[1:]
    
    return int(failures.sum())


# ============================================================================
# Batch versions cho vectorized computation
# ============================================================================

def compute_binomial_one_tail_failures_batch(
    observed_bads_batch: np.ndarray,
    totals_batch: np.ndarray,
    expected_pds: np.ndarray,
    confidence_level: float = 0.95
) -> np.ndarray:
    """
    Binomial one-tail test cho nhiều simulations.
    
    Args:
        observed_bads_batch: Shape (n_simulations, n_grades)
        totals_batch: Shape (n_simulations, n_grades)
        expected_pds: Shape (n_grades,)
        confidence_level: Mức tin cậy
        
    Returns:
        Array số failures, shape (n_simulations,)
    """
    # Broadcasting expected_pds
    expected_pds_2d = expected_pds[np.newaxis, :]
    
    critical_values = binom.ppf(confidence_level, totals_batch, expected_pds_2d)
    failures = observed_bads_batch > critical_values
    
    return failures.sum(axis=1).astype(int)


def compute_binomial_two_tail_failures_batch(
    observed_bads_batch: np.ndarray,
    totals_batch: np.ndarray,
    expected_pds: np.ndarray,
    confidence_level: float = 0.95
) -> np.ndarray:
    """
    Binomial two-tail test cho nhiều simulations.
    """
    alpha = 1 - confidence_level
    expected_pds_2d = expected_pds[np.newaxis, :]
    
    lower_bound = binom.ppf(alpha / 2, totals_batch, expected_pds_2d)
    upper_bound = binom.ppf(1 - alpha / 2, totals_batch, expected_pds_2d)
    
    failures = (observed_bads_batch < lower_bound) | (observed_bads_batch > upper_bound)
    
    return failures.sum(axis=1).astype(int)


def compute_homogeneity_failures_batch(
    default_rates_batch: np.ndarray,
    totals_batch: np.ndarray,
    lower_quantile: float = 0.025,
    upper_quantile: float = 0.975
) -> np.ndarray:
    """
    Homogeneity test cho nhiều simulations.
    """
    safe_totals = np.maximum(totals_batch, 1)
    
    lower_bounds = binom.ppf(lower_quantile, totals_batch, default_rates_batch) / safe_totals
    upper_bounds = binom.ppf(upper_quantile, totals_batch, default_rates_batch) / safe_totals
    
    # Compare adjacent grades: CI overlap khi upper[i] >= lower[i+1]
    failures = upper_bounds[:, :-1] >= lower_bounds[:, 1:]
    
    return failures.sum(axis=1).astype(int)