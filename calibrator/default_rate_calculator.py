"""
default_rate_calculator.py - Tính default rate từ observed data.

Mapping: Grade probabilities -> Observation boundaries -> Default rates
"""
import numpy as np

from .calibration_types import ObservedData


def precompute_score_tie_boundaries(scores: np.ndarray) -> np.ndarray:
    """
    Pre-compute adjusted boundary positions để tránh cắt giữa các scores giống nhau.
    
    Với mỗi index i, tính adjusted_boundary[i] = index nhỏ nhất j > i 
    sao cho scores[j] != scores[i] (hoặc n_obs nếu không tìm thấy).
    
    Điều này cho phép vectorize boundary adjustment thay vì dùng while loop.
    
    Args:
        scores: Array scores đã sort giảm dần, shape (n_obs,)
        
    Returns:
        adjusted_boundaries: shape (n_obs + 1,)
        Với i trong [0, n_obs]: adjusted_boundaries[i] là boundary đã adjust
        
    Example:
        >>> scores = [100, 100, 90, 90, 90, 80]  # 6 obs
        >>> boundaries = precompute_score_tie_boundaries(scores)
        >>> # boundaries[0] = 0 (boundary tại 0 → 0)
        >>> # boundaries[1] = 2 (boundary tại 1 → 2 vì scores[1]=scores[0]=100)
        >>> # boundaries[2] = 2 (boundary tại 2 → 2 vì scores[2]=90 khác scores[1]=100)
        >>> # boundaries[3] = 5 (boundary tại 3 → 5 vì scores[3]=scores[4]=90)
        >>> # boundaries[5] = 5 (boundary tại 5 → 5)
        >>> # boundaries[6] = 6 (boundary tại n_obs = n_obs)
    """
    n_obs = len(scores)
    
    if n_obs == 0:
        return np.array([0])
    
    # Tìm vị trí các score changes (nơi score khác với observation trước)
    # diff[i] = True nếu scores[i] != scores[i-1]
    score_changes = np.concatenate([[True], scores[:-1] != scores[1:]])
    
    # Cumulative count của số lần score change từ đầu
    # Điều này tạo ra một "group id" cho mỗi observation
    group_ids = np.cumsum(score_changes)  # shape: (n_obs,)
    
    # Tìm index cuối cùng của mỗi group
    # Với mỗi group g, last_of_group[g] = index cuối cùng có group_id = g
    # Số groups = group_ids[-1]
    n_groups = group_ids[-1]
    
    # Tìm first index của mỗi group (= last index của group trước + 1)
    # first_of_next_group[g] = index đầu tiên của group (g+1), hoặc n_obs nếu g là group cuối
    group_starts = np.zeros(n_groups + 1, dtype=int)
    group_starts[:-1] = np.where(score_changes)[0]
    group_starts[-1] = n_obs
    
    # adjusted_boundaries[i] = first index của group tiếp theo sau group chứa (i-1)
    # Với i = 0: adjusted_boundaries[0] = 0 (no adjustment needed)
    # Với i > 0: 
    #   - Tìm group của observation (i-1): g = group_ids[i-1]
    #   - adjusted = group_starts[g] = first index của group sau g
    
    adjusted_boundaries = np.zeros(n_obs + 1, dtype=int)
    adjusted_boundaries[0] = 0
    adjusted_boundaries[1:] = group_starts[group_ids - 1 + 1]  # group_ids là 1-indexed
    
    return adjusted_boundaries


def compute_observation_boundaries(
    cumulative_probabilities: np.ndarray,
    n_observations: int,
    scores: np.ndarray = None
) -> tuple[np.ndarray, np.ndarray]:
    """
    Tính boundaries (from_idx, to_idx) cho mỗi grade dựa trên cumulative probability.
    
    Args:
        cumulative_probabilities: Cum prob cho mỗi grade, shape (n_grades,)
        n_observations: Tổng số observations
        scores: Optional - array of scores (sorted descending) để adjust boundaries khi có ties
        
    Returns:
        Tuple (from_indices, to_indices), mỗi array có shape (n_grades,)
        
    Example:
        >>> cum_probs = np.array([0.1, 0.3, 0.6, 1.0])
        >>> from_idx, to_idx = compute_observation_boundaries(cum_probs, 100)
        >>> from_idx  # [0, 10, 30, 60]
        >>> to_idx    # [10, 30, 60, 100]
    """
    # Tính cumulative observation indices
    cum_indices = np.ceil(cumulative_probabilities * n_observations).astype(int)
    cum_indices = np.clip(cum_indices, 0, n_observations)
    
    # Adjust boundaries để tránh cắt giữa các scores giống nhau
    # Move boundary về PHẢI: Tất cả identical scores vào grade bên PHẢI (worse grade)
    # Điều này phù hợp với cutoff assignment rule: cutoff[i+1] <= score < cutoff[i]
    if scores is not None:
        for i in range(len(cum_indices) - 1):  # Không adjust grade cuối
            idx = cum_indices[i]
            if idx > 0 and idx < n_observations:
                # Score tại boundary - 1 (score cuối cùng của grade hiện tại)
                boundary_score = scores[idx - 1]
                
                # Move boundary về PHẢI để include tất cả identical scores vào grade hiện tại
                while idx < n_observations and scores[idx] == boundary_score:
                    idx += 1
                
                cum_indices[i] = idx
    
    # to_indices = cum_indices
    to_indices = cum_indices
    
    # from_indices = shifted cum_indices (grade trước đó)
    from_indices = np.concatenate([[0], cum_indices[:-1]])
    
    # Đảm bảo from <= to
    from_indices = np.minimum(from_indices, to_indices)
    
    return from_indices, to_indices


def compute_grade_statistics(
    observed_data: ObservedData,
    from_indices: np.ndarray,
    to_indices: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Tính bad, total, default_rate cho mỗi grade từ boundaries.
    
    Args:
        observed_data: Dữ liệu quan sát đã sort
        from_indices: Chỉ số bắt đầu mỗi grade
        to_indices: Chỉ số kết thúc mỗi grade
        
    Returns:
        Tuple (bads, totals, default_rates)
    """
    # Thêm 0 vào đầu cumulative arrays để xử lý from_idx = 0
    cum_bads_extended = np.concatenate([[0], observed_data.cumulative_bads])
    cum_totals_extended = np.concatenate([[0], observed_data.cumulative_totals])
    
    # Tính statistics cho mỗi grade
    bads = cum_bads_extended[to_indices] - cum_bads_extended[from_indices]
    totals = cum_totals_extended[to_indices] - cum_totals_extended[from_indices]
    
    # Safe division để tránh divide by zero
    default_rates = np.divide(
        bads, totals,
        out=np.zeros_like(bads, dtype=float),
        where=totals != 0
    )
    
    return bads, totals, default_rates


def compute_score_thresholds(
    observed_data: ObservedData,
    to_indices: np.ndarray,
    n_grades: int
) -> np.ndarray:
    """
    Lấy score threshold cho mỗi grade.
    
    Args:
        observed_data: Dữ liệu quan sát
        to_indices: Chỉ số kết thúc mỗi grade
        n_grades: Số lượng grades
        
    Returns:
        Array score thresholds, shape (n_grades,)
    """
    # Clip indices để tránh out of bounds
    safe_indices = np.clip(to_indices - 1, 0, observed_data.n_observations - 1)
    thresholds = observed_data.scores[safe_indices]
    
    # Grade cuối cùng có threshold = -inf
    thresholds[-1] = -np.inf
    
    return thresholds


def compute_score_cutoffs(
    observed_data: ObservedData,
    cumulative_probabilities: np.ndarray
) -> np.ndarray:
    """
    Tính score cutoffs cho một calibration cụ thể.
    
    Score cutoffs là ngưỡng score thực tế để phân chia grades.
    Quy ước: Grade i có score trong khoảng [cutoff[i+1], cutoff[i])
    (dấu = ở cận DƯỚI, scores sorted descending)
    
    Lưu ý: Score cao hơn thì vào grade tốt hơn (index nhỏ hơn)
    
    IMPORTANT: Để đảm bảo consistency với index-based boundaries,
    cutoffs được adjust để tránh cắt giữa các observations có cùng score.
    
    Args:
        observed_data: Dữ liệu quan sát đã sort theo score giảm dần
        cumulative_probabilities: Cumulative probabilities cho mỗi grade, shape (n_grades,)
        
    Returns:
        Array score cutoffs, shape (n_grades + 1,)
        Format: [+Inf, cutoff_1, cutoff_2, ..., cutoff_{n-1}, -Inf]
        Với n_grades = 10: [+Inf, c1, c2, ..., c9, -Inf] = 11 giá trị
        
    Example:
        >>> cum_probs = np.array([0.1, 0.3, 0.6, 1.0])  # 4 grades
        >>> cutoffs = compute_score_cutoffs(observed_data, cum_probs)
        >>> # cutoffs = [+Inf, 850, 700, 550, -Inf]  # 5 cutoffs cho 4 grades
        >>> # Grade 1: 850 <= score < +Inf  (dấu = ở cận dưới)
        >>> # Grade 2: 700 <= score < 850
        >>> # Grade 3: 550 <= score < 700
        >>> # Grade 4: -Inf <= score < 550
    """
    n_obs = observed_data.n_observations
    n_grades = len(cumulative_probabilities)
    scores = observed_data.scores
    
    # Tính boundary indices
    cum_indices = np.ceil(cumulative_probabilities * n_obs).astype(int)
    cum_indices = np.clip(cum_indices, 0, n_obs)
    
    # Adjust boundaries để tránh cắt giữa các scores giống nhau
    # Move boundary về PHẢI: Tất cả identical scores vào grade hiện tại (bên trái boundary)
    # Phù hợp với cutoff assignment rule: cutoff[i+1] <= score < cutoff[i]
    for i in range(n_grades - 1):  # Không adjust grade cuối
        idx = cum_indices[i]
        if idx > 0 and idx < n_obs:
            # Score cuối cùng của grade hiện tại
            boundary_score = scores[idx - 1]
            
            # Move boundary về PHẢI để include tất cả identical scores vào grade hiện tại
            while idx < n_obs and scores[idx] == boundary_score:
                idx += 1
            
            cum_indices[i] = idx
    
    # Cutoffs array: [+Inf, cutoff_1, cutoff_2, ..., -Inf]
    # Format: n_grades + 1 values = 1 (+Inf) + (n_grades - 1) cutoffs + 1 (-Inf)
    cutoffs = np.zeros(n_grades + 1)
    
    # Cận trên (vô cực dương)
    cutoffs[0] = np.inf
    
    # FIXED: Các cutoffs giữa = score CUỐI CÙNG của grade (= scores[to_idx - 1])
    # Thay vì score đầu tiên của grade tiếp theo (= scores[to_idx])
    for i in range(n_grades - 1):
        idx = cum_indices[i]  # to_idx của grade i
        if idx > 0:
            # Score của observation CUỐI CÙNG của grade i
            cutoffs[i + 1] = scores[idx - 1]
        else:
            cutoffs[i + 1] = scores[0]
    
    # Cận dưới (vô cực âm)
    cutoffs[-1] = -np.inf
    
    return cutoffs


def compute_grade_statistics_batch(
    observed_data: ObservedData,
    cumulative_probabilities_batch: np.ndarray,
    precomputed_boundaries: np.ndarray = None
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Tính statistics cho nhiều simulations cùng lúc (FULLY VECTORIZED).
    
    Đã được optimize để loại bỏ nested loops bằng cách:
    1. Pre-compute score tie boundaries một lần
    2. Vectorized lookup thay vì while loops
    
    Args:
        observed_data: Dữ liệu quan sát
        cumulative_probabilities_batch: Shape (n_simulations, n_grades)
        precomputed_boundaries: Optional pre-computed boundaries từ precompute_score_tie_boundaries()
                               Nếu None, sẽ tự động compute
        
    Returns:
        Tuple (bads_batch, totals_batch, default_rates_batch, to_indices)
        Mỗi array có shape (n_simulations, n_grades)
    """
    n_simulations, n_grades = cumulative_probabilities_batch.shape
    n_obs = observed_data.n_observations
    scores = observed_data.scores
    
    # Tính indices cho tất cả simulations
    # Shape: (n_sims, n_grades)
    cum_indices = np.ceil(cumulative_probabilities_batch * n_obs).astype(int)
    cum_indices = np.clip(cum_indices, 0, n_obs)
    
    # ===== OPTIMIZED: Vectorized boundary adjustment =====
    # Pre-compute score tie boundaries nếu chưa có
    if precomputed_boundaries is None:
        precomputed_boundaries = precompute_score_tie_boundaries(scores)
    
    # Vectorized lookup: adjusted_indices[i] = precomputed_boundaries[cum_indices[i]]
    # Chỉ adjust các grades trừ grade cuối (grade cuối luôn = n_obs)
    adjusted_indices = cum_indices.copy()
    adjusted_indices[:, :-1] = precomputed_boundaries[cum_indices[:, :-1]]
    
    to_indices = adjusted_indices
    from_indices = np.concatenate([
        np.zeros((n_simulations, 1), dtype=int),
        adjusted_indices[:, :-1]
    ], axis=1)
    from_indices = np.minimum(from_indices, to_indices)
    
    # Extended cumulative arrays
    cum_bads_ext = np.concatenate([[0], observed_data.cumulative_bads])
    cum_totals_ext = np.concatenate([[0], observed_data.cumulative_totals])
    
    # Vectorized lookup
    bads = cum_bads_ext[to_indices] - cum_bads_ext[from_indices]
    totals = cum_totals_ext[to_indices] - cum_totals_ext[from_indices]
    
    default_rates = np.divide(
        bads, totals,
        out=np.zeros_like(bads, dtype=float),
        where=totals != 0
    )
    
    return bads, totals, default_rates, to_indices


def compute_score_cutoffs_batch(
    observed_data: ObservedData,
    to_indices_batch: np.ndarray
) -> np.ndarray:
    """
    Tính score cutoffs cho tất cả simulations từ adjusted boundary indices.
    
    FULLY VECTORIZED - không có loop.
    
    SINGLE SOURCE OF TRUTH: Sử dụng to_indices đã được adjust từ compute_grade_statistics_batch
    để đảm bảo consistency giữa index-based và score-based assignment.
    
    Quy ước: Grade i có score trong khoảng [cutoff[i+1], cutoff[i])
    (dấu = ở cận DƯỚI, scores sorted descending)
    
    Logic cutoff:
    - cutoff[g+1] = scores[to_idx[g] - 1] = score của observation CUỐI CÙNG của grade g
    - Với quy ước cutoff[g+1] <= score: observation cuối của grade g thỏa mãn (thuộc grade g ✓)
    - Observation đầu của grade g+1 có score < cutoff[g+1] nên không thỏa mãn (ở grade g+1 ✓)
    
    Lưu ý: Score cao hơn thì vào grade tốt hơn (index nhỏ hơn)
    
    Args:
        observed_data: Dữ liệu quan sát đã sort theo score giảm dần
        to_indices_batch: Adjusted boundary indices, shape (n_simulations, n_grades)
        
    Returns:
        Array score cutoffs, shape (n_simulations, n_grades + 1)
        Format: [+Inf, cutoff_1, cutoff_2, ..., cutoff_{n-1}, -Inf]
        Với n_grades = 10: [+Inf, c1, c2, ..., c9, -Inf] = 11 giá trị
    """
    n_simulations, n_grades = to_indices_batch.shape
    n_obs = observed_data.n_observations
    scores = observed_data.scores
    
    # Cutoffs array: shape (n_sims, n_grades + 1)
    # Format: [+Inf, cutoff_1, cutoff_2, ..., -Inf]
    cutoffs = np.zeros((n_simulations, n_grades + 1))
    
    # Cận trên (vô cực dương)
    cutoffs[:, 0] = np.inf
    
    # ===== FIXED: cutoff = score CUỐI CÙNG của grade (không phải đầu tiên của grade+1) =====
    # Các cutoffs giữa: lấy score tại vị trí to_idx[g] - 1 (observation cuối của grade g)
    # Chỉ lấy n_grades - 1 cột đầu tiên (grade cuối không cần cutoff giữa)
    middle_to_indices = to_indices_batch[:, :-1]  # shape: (n_sims, n_grades - 1)
    
    # FIXED: Lấy index của observation CUỐI CÙNG của grade (= to_idx - 1)
    last_obs_indices = middle_to_indices - 1  # shape: (n_sims, n_grades - 1)
    
    # Safe lookup: clip indices (đảm bảo >= 0)
    safe_indices = np.clip(last_obs_indices, 0, n_obs - 1)
    
    # Vectorized score lookup
    cutoffs[:, 1:-1] = scores[safe_indices]
    
    # Cận dưới (vô cực âm)
    cutoffs[:, -1] = -np.inf
    
    return cutoffs