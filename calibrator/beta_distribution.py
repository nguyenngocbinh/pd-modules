"""
beta_distribution.py - Tính toán xác suất từ Beta distribution.

Beta distribution được dùng để mô hình phân bố khách hàng vào các grades.
"""
import numpy as np
from scipy.stats import beta as beta_dist


def compute_grade_probabilities(
    alpha: float, 
    beta: float, 
    n_grades: int
) -> np.ndarray:
    """
    Tính xác suất rơi vào mỗi grade từ Beta distribution.
    
    Mỗi grade chiếm 1/n_grades của CDF, từ 0 đến 1.
    Grade 1 (AAA): [0, 1/n]
    Grade 2 (AA): [1/n, 2/n]
    ...
    Grade n (D): [(n-1)/n, 1]
    
    Args:
        alpha: Tham số alpha của Beta distribution
        beta: Tham số beta của Beta distribution
        n_grades: Số lượng grades
        
    Returns:
        Array xác suất cho mỗi grade, shape (n_grades,)
        
    Example:
        >>> probs = compute_grade_probabilities(2.0, 3.0, 10)
        >>> probs.sum()  # Tổng xác suất = 1
        1.0
    """
    # Boundaries cho mỗi grade
    grade_nums = np.arange(1, n_grades + 1)
    upper_bounds = grade_nums / n_grades      # [0.1, 0.2, ..., 1.0]
    lower_bounds = (grade_nums - 1) / n_grades  # [0.0, 0.1, ..., 0.9]
    
    # Tính CDF tại các boundaries
    cdf_upper = beta_dist.cdf(upper_bounds, alpha, beta)
    cdf_lower = beta_dist.cdf(lower_bounds, alpha, beta)
    
    # Xác suất = CDF(upper) - CDF(lower)
    probabilities = cdf_upper - cdf_lower
    
    return probabilities


def compute_grade_probabilities_batch(
    alphas: np.ndarray,
    betas: np.ndarray,
    n_grades: int
) -> np.ndarray:
    """
    Tính xác suất cho nhiều bộ (alpha, beta) cùng lúc (vectorized).
    
    Args:
        alphas: Array các giá trị alpha, shape (n_simulations,)
        betas: Array các giá trị beta, shape (n_simulations,)
        n_grades: Số lượng grades
        
    Returns:
        Array xác suất, shape (n_simulations, n_grades)
        
    Example:
        >>> alphas = np.array([1.0, 2.0, 3.0])
        >>> betas = np.array([2.0, 3.0, 4.0])
        >>> probs = compute_grade_probabilities_batch(alphas, betas, 10)
        >>> probs.shape
        (3, 10)
    """
    n_simulations = len(alphas)
    
    # Tạo grade boundaries
    grade_nums = np.arange(1, n_grades + 1)
    upper_bounds = grade_nums / n_grades
    lower_bounds = (grade_nums - 1) / n_grades
    
    # Expand dimensions để broadcasting
    # alphas: (n_sims,) -> (n_sims, 1)
    # bounds: (n_grades,) -> (1, n_grades)
    alphas_2d = alphas[:, np.newaxis]
    betas_2d = betas[:, np.newaxis]
    upper_2d = upper_bounds[np.newaxis, :]
    lower_2d = lower_bounds[np.newaxis, :]
    
    # Tính CDF - scipy.stats.beta.cdf đã hỗ trợ broadcasting
    cdf_upper = beta_dist.cdf(upper_2d, alphas_2d, betas_2d)
    cdf_lower = beta_dist.cdf(lower_2d, alphas_2d, betas_2d)
    
    probabilities = cdf_upper - cdf_lower
    
    return probabilities


def compute_implied_pd(
    grade_probabilities: np.ndarray,
    mid_pds: np.ndarray
) -> float:
    """
    Tính Implied PD từ phân bố xác suất và mid_pd của mỗi grade.
    
    Implied PD = Σ (probability_i × mid_pd_i)
    
    Args:
        grade_probabilities: Xác suất mỗi grade, shape (n_grades,)
        mid_pds: Mid PD của mỗi grade, shape (n_grades,)
        
    Returns:
        Implied PD (scalar)
    """
    return np.dot(grade_probabilities, mid_pds)


def compute_implied_pd_batch(
    grade_probabilities_batch: np.ndarray,
    mid_pds: np.ndarray
) -> np.ndarray:
    """
    Tính Implied PD cho nhiều simulations (vectorized).
    
    Args:
        grade_probabilities_batch: Shape (n_simulations, n_grades)
        mid_pds: Shape (n_grades,)
        
    Returns:
        Array implied PDs, shape (n_simulations,)
    """
    # Matrix multiplication: (n_sims, n_grades) @ (n_grades,) = (n_sims,)
    return grade_probabilities_batch @ mid_pds