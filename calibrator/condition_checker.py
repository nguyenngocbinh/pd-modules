"""
condition_checker.py - Kiểm tra các điều kiện của calibration.

Các điều kiện:
1. DR không vượt quá max_pd của grade
2. DR tăng đơn điệu từ AAA đến D (monotonicity)
"""
import numpy as np


def count_max_pd_violations(
    default_rates: np.ndarray,
    max_pds: np.ndarray
) -> int:
    """
    Đếm số grades có default rate vượt quá max_pd cho phép.
    
    Args:
        default_rates: DR mỗi grade, shape (n_grades,)
        max_pds: Max PD mỗi grade, shape (n_grades,)
        
    Returns:
        Số lượng violations
    """
    violations = default_rates > max_pds
    return int(violations.sum())


def count_monotonicity_violations(
    default_rates: np.ndarray
) -> int:
    """
    Đếm số grades vi phạm monotonicity (DR không tăng đơn điệu).
    
    Grades được sắp xếp từ AAA (index 0) đến D (index -1).
    Violation xảy ra khi DR[i] >= DR[i+1].
    
    Args:
        default_rates: DR mỗi grade, sorted từ tốt đến xấu
        
    Returns:
        Số lượng violations
    """
    # So sánh mỗi DR với DR của grade trước đó
    dr_shifted = np.concatenate([[0], default_rates[:-1]])
    
    # Violation nếu DR hiện tại <= DR trước đó (trừ grade đầu tiên)
    violations = (default_rates[1:] <= dr_shifted[1:])
    
    return int(violations.sum())


def count_max_pd_violations_batch(
    default_rates_batch: np.ndarray,
    max_pds: np.ndarray
) -> np.ndarray:
    """
    Đếm max_pd violations cho nhiều simulations (vectorized).
    
    Args:
        default_rates_batch: Shape (n_simulations, n_grades)
        max_pds: Shape (n_grades,)
        
    Returns:
        Array số violations, shape (n_simulations,)
    """
    violations = default_rates_batch > max_pds[np.newaxis, :]
    return violations.sum(axis=1).astype(int)


def count_monotonicity_violations_batch(
    default_rates_batch: np.ndarray
) -> np.ndarray:
    """
    Đếm monotonicity violations cho nhiều simulations (vectorized).
    
    Args:
        default_rates_batch: Shape (n_simulations, n_grades)
        
    Returns:
        Array số violations, shape (n_simulations,)
    """
    # Shift DR to compare with previous grade
    dr_shifted = np.concatenate([
        np.zeros((default_rates_batch.shape[0], 1)),
        default_rates_batch[:, :-1]
    ], axis=1)
    
    # Violations từ grade thứ 2 trở đi
    violations = default_rates_batch[:, 1:] <= dr_shifted[:, 1:]
    
    return violations.sum(axis=1).astype(int)