"""
data_preparer.py - Chuẩn bị và validate input data.
"""
import numpy as np
from .calibration_types import ObservedData, MasterScale


def prepare_observed_data(
    scores: np.ndarray,
    labels: np.ndarray
) -> ObservedData:
    """
    Chuẩn bị observed data từ raw scores và labels.
    
    Steps:
    1. Sort theo score giảm dần (best to worst)
    2. Tính cumulative bads và totals
    
    Args:
        scores: Array điểm số, shape (n_obs,)
        labels: Array labels (0=good, 1=bad), shape (n_obs,)
        
    Returns:
        ObservedData đã được sort và tính cumulative
    """
    scores = np.asarray(scores)
    labels = np.asarray(labels)
    
    # Sort giảm dần theo score
    sort_indices = np.argsort(-scores)  # Negative để sort giảm dần
    sorted_scores = scores[sort_indices]
    sorted_labels = labels[sort_indices]
    
    # Tính cumulative statistics theo từng unique score
    unique_scores, inverse_indices = np.unique(sorted_scores, return_inverse=True)
    unique_scores = unique_scores[::-1]  # Reverse để giảm dần
    
    # Group by score và tính cumulative
    n_unique = len(unique_scores)
    cum_bads = np.zeros(len(sorted_scores))
    cum_totals = np.zeros(len(sorted_scores))
    
    running_bad = 0
    running_total = 0
    
    # Dùng pandas-like groupby logic với pure numpy
    score_to_stats = {}
    current_score = sorted_scores[0]
    current_bad = 0
    current_n = 0
    
    for i, (score, label) in enumerate(zip(sorted_scores, sorted_labels)):
        if score != current_score:
            # Lưu stats cho score trước
            score_to_stats[current_score] = (current_bad, current_n)
            current_score = score
            current_bad = 0
            current_n = 0
        current_bad += label
        current_n += 1
    # Lưu score cuối
    score_to_stats[current_score] = (current_bad, current_n)
    
    # Tính cumulative
    running_bad = 0
    running_total = 0
    processed_scores = set()
    
    for i, score in enumerate(sorted_scores):
        if score not in processed_scores:
            bad_count, n_count = score_to_stats[score]
            running_bad += bad_count
            running_total += n_count
            processed_scores.add(score)
        cum_bads[i] = running_bad
        cum_totals[i] = running_total
    
    return ObservedData(
        scores=sorted_scores,
        labels=sorted_labels,
        cumulative_bads=cum_bads.astype(int),
        cumulative_totals=cum_totals.astype(int)
    )


def validate_input_data(scores: np.ndarray, labels: np.ndarray) -> None:
    """
    Validate input data trước khi processing.
    
    Raises:
        ValueError: Nếu data không hợp lệ
    """
    if len(scores) != len(labels):
        raise ValueError(f"scores và labels phải có cùng độ dài: {len(scores)} vs {len(labels)}")
    
    if len(scores) == 0:
        raise ValueError("scores không được rỗng")
    
    unique_labels = np.unique(labels)
    if not np.all(np.isin(unique_labels, [0, 1])):
        raise ValueError(f"labels chỉ được chứa 0 và 1, nhận được: {unique_labels}")
    
    if np.any(np.isnan(scores)):
        raise ValueError("scores chứa giá trị NaN")