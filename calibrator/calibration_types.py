"""
types.py - Định nghĩa các data structures dùng trong calibration.

Sử dụng NumPy structured arrays và dataclasses để:
- Type safety
- Memory efficient
- Dễ hiểu và maintain
"""
from dataclasses import dataclass
from typing import NamedTuple
import numpy as np


# ============================================================================
# Named Tuples cho immutable data
# ============================================================================

class MasterScaleGrade(NamedTuple):
    """Một grade trong master scale."""
    grade_name: str
    grade_num: int
    min_pd: float
    max_pd: float
    mid_pd: float


class SimulationParameter(NamedTuple):
    """Một bộ parameters (alpha, beta) cho simulation."""
    alpha: float
    beta: float
    simulation_id: str


# ============================================================================
# Dataclasses cho mutable/complex data
# ============================================================================

@dataclass
class MasterScale:
    """
    Master scale với n grades.
    
    Attributes:
        grade_names: Tên các grades (AAA, AA, A, ...)
        grade_nums: Số thứ tự grades (1, 2, 3, ...)
        min_pds: PD tối thiểu mỗi grade
        max_pds: PD tối đa mỗi grade
        mid_pds: PD trung bình mỗi grade
    """
    grade_names: np.ndarray  # shape: (n_grades,), dtype: str
    grade_nums: np.ndarray   # shape: (n_grades,), dtype: int
    min_pds: np.ndarray      # shape: (n_grades,), dtype: float
    max_pds: np.ndarray      # shape: (n_grades,), dtype: float
    mid_pds: np.ndarray      # shape: (n_grades,), dtype: float
    
    @property
    def n_grades(self) -> int:
        return len(self.grade_names)
    
    def __post_init__(self):
        """Validate data consistency."""
        lengths = [len(self.grade_names), len(self.grade_nums), 
                   len(self.min_pds), len(self.max_pds), len(self.mid_pds)]
        if len(set(lengths)) != 1:
            raise ValueError("Tất cả arrays phải có cùng độ dài")


@dataclass
class ObservedData:
    """
    Dữ liệu quan sát đã được sắp xếp theo score giảm dần.
    
    Attributes:
        scores: Điểm của từng observation
        labels: Label default (0 hoặc 1)
        cumulative_bads: Số lượng bad tích lũy tại mỗi vị trí
        cumulative_totals: Số lượng total tích lũy tại mỗi vị trí
    """
    scores: np.ndarray           # shape: (n_obs,)
    labels: np.ndarray           # shape: (n_obs,)
    cumulative_bads: np.ndarray  # shape: (n_obs,)
    cumulative_totals: np.ndarray # shape: (n_obs,)
    
    @property
    def n_observations(self) -> int:
        return len(self.scores)
    
    @property
    def observed_default_rate(self) -> float:
        return self.labels.mean()


@dataclass
class SimulationResult:
    """
    Kết quả simulation cho một bộ (alpha, beta).
    
    Attributes:
        alpha, beta: Parameters của beta distribution
        grade_probabilities: Xác suất rơi vào mỗi grade
        grade_totals: Số lượng observations trong mỗi grade
        grade_bads: Số lượng defaults trong mỗi grade
        grade_default_rates: Default rate của mỗi grade
        implied_pd: PD ngụ ý từ distribution
        accuracy_ratio: AR (Gini coefficient)
    """
    alpha: float
    beta: float
    grade_probabilities: np.ndarray   # shape: (n_grades,)
    grade_totals: np.ndarray          # shape: (n_grades,)
    grade_bads: np.ndarray            # shape: (n_grades,)
    grade_default_rates: np.ndarray   # shape: (n_grades,)
    score_thresholds: np.ndarray      # shape: (n_grades,)
    implied_pd: float
    accuracy_ratio: float


@dataclass
class ValidationResult:
    """
    Kết quả validation cho một simulation.
    
    Attributes:
        n_max_pd_violations: Số grades có DR > max_pd
        n_monotonicity_violations: Số grades vi phạm monotonicity
        n_binomial_failures: Số grades fail binomial test
        n_homogeneity_failures: Số grades fail homogeneity test
    """
    n_max_pd_violations: int
    n_monotonicity_violations: int
    n_binomial_one_tail_failures: int
    n_binomial_two_tail_failures: int
    n_homogeneity_failures: int
    
    @property
    def is_valid(self) -> bool:
        """Check nếu tất cả validations đều pass."""
        return (self.n_max_pd_violations == 0 and 
                self.n_monotonicity_violations == 0)