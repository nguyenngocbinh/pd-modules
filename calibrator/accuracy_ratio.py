"""
accuracy_ratio.py - Tính Accuracy Ratio (Gini coefficient).

AR đo lường khả năng phân biệt của mô hình rating.
AR = 1: Perfect discrimination
AR = 0: Random model
"""
import numpy as np


def compute_accuracy_ratio(
    default_rates: np.ndarray,
    totals: np.ndarray
) -> float:
    """
    Tính Accuracy Ratio từ default rates và totals của các grades.
    
    Grades phải được sắp xếp từ rủi ro cao đến thấp (D -> AAA).
    
    Formula:
        AR = (1 / (PD × (1-PD))) × (AR_1 + AR_2) - 1
        
    Trong đó:
        - PD: Portfolio default rate
        - AR_1: Phần đóng góp từ cumulative distribution
        - AR_2: Phần đóng góp từ within-grade variance
    
    Args:
        default_rates: DR mỗi grade (sorted worst to best), shape (n_grades,)
        totals: Số lượng mỗi grade, shape (n_grades,)
        
    Returns:
        Accuracy Ratio (scalar, thường trong khoảng [0, 1])
    """
    # Tính portfolio proportions
    portfolio_size = totals.sum()
    if portfolio_size == 0:
        return 0.0
    
    proportions = totals / portfolio_size
    
    # Portfolio PD
    portfolio_pd = np.dot(default_rates, proportions)
    
    # Tránh divide by zero
    denominator = portfolio_pd * (1 - portfolio_pd)
    if denominator == 0:
        return 0.0
    
    # Tính AR_1: contribution từ cumulative distribution
    cumulative_pd_proportion = np.cumsum(default_rates * proportions)
    # Shift để lấy giá trị trước mỗi grade
    cumulative_pd_shifted = np.concatenate([[0], cumulative_pd_proportion[:-1]])
    ar_1 = 2 * np.sum((1 - default_rates) * proportions * cumulative_pd_shifted)
    
    # Tính AR_2: contribution từ within-grade variance
    ar_2 = np.sum(default_rates * (1 - default_rates) * proportions * proportions)
    
    # AR total
    ar = (1 / denominator) * (ar_1 + ar_2) - 1
    
    return ar


def compute_accuracy_ratio_batch(
    default_rates_batch: np.ndarray,
    totals_batch: np.ndarray
) -> np.ndarray:
    """
    Tính AR cho nhiều simulations cùng lúc (fully vectorized).
    
    Args:
        default_rates_batch: Shape (n_simulations, n_grades), sorted worst to best
        totals_batch: Shape (n_simulations, n_grades)
        
    Returns:
        Array AR values, shape (n_simulations,)
    """
    # Portfolio sizes và proportions
    # Shape: (n_sims, 1)
    portfolio_sizes = totals_batch.sum(axis=1, keepdims=True)
    
    # Avoid division by zero
    safe_sizes = np.where(portfolio_sizes == 0, 1, portfolio_sizes)
    proportions = totals_batch / safe_sizes
    
    # Portfolio PD: (n_sims, 1)
    portfolio_pd = (default_rates_batch * proportions).sum(axis=1, keepdims=True)
    
    # Denominator: PD × (1 - PD)
    denominator = portfolio_pd * (1 - portfolio_pd)
    
    # Cumulative PD proportions (shifted)
    # cumsum along grades axis
    cum_pd_prop = np.cumsum(default_rates_batch * proportions, axis=1)
    # Shift: insert 0 at beginning, remove last
    cum_pd_shifted = np.concatenate([
        np.zeros((cum_pd_prop.shape[0], 1)),
        cum_pd_prop[:, :-1]
    ], axis=1)
    
    # AR_1
    ar_1 = 2 * ((1 - default_rates_batch) * proportions * cum_pd_shifted).sum(
        axis=1, keepdims=True
    )
    
    # AR_2
    ar_2 = (default_rates_batch * (1 - default_rates_batch) * proportions * proportions).sum(
        axis=1, keepdims=True
    )
    
    # AR total với safe division
    ar = np.divide(
        ar_1 + ar_2, denominator,
        out=np.zeros_like(denominator),
        where=denominator != 0
    ) - 1
    
    return np.abs(ar.flatten())