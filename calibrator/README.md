# Calibration Module

Module thực hiện calibration PD cho mô hình credit scoring.

---

## 1. Cấu trúc Files

```
calibration/
├── calibration_types.py         # Data structures (MasterScale, ObservedData, Results)
├── config.py                    # Configuration (SimulationGridConfig, StatisticalTestConfig)
├── data_preparer.py             # Chuẩn bị dữ liệu đầu vào
├── beta_distribution.py         # Tính cumulative probabilities từ Beta distribution
├── default_rate_calculator.py   # Tính default rates và score cutoffs
├── accuracy_ratio.py            # Tính Accuracy Ratio (Gini)
├── statistical_tests.py         # Binomial test, Homogeneity test
├── condition_checker.py         # Kiểm tra monotonicity, max PD violations
└── simulation_runner.py         # Orchestrate toàn bộ simulation
```

---

## 2. Luồng Chạy (Pipeline)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          INPUT                                          │
│  • scores (sorted descending)                                           │
│  • labels (0/1)                                                         │
│  • master_scale (n_grades, mid_pds, max_pds)                           │
│  • grid_config (alpha_range, beta_range, step)                         │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 1: prepare_observed_data()                                        │
│  • Sort scores descending                                               │
│  • Tính cumulative_bads, cumulative_totals                             │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 2: generate_simulation_grid()                                     │
│  • Tạo grid (alpha, beta) combinations                                  │
│  • Output: alphas[], betas[] arrays                                     │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 3: compute_grade_probabilities_batch()                            │
│  • Tính Beta CDF cho mỗi (alpha, beta, grade)                          │
│  • Output: cum_probs shape (n_sims, n_grades)                          │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 3b: precompute_score_tie_boundaries()                             │
│  • Pre-compute boundary positions để xử lý score ties                   │
│  • Output: adjusted_boundaries array                                    │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 4: compute_grade_statistics_batch()                               │
│  • Tính bads, totals, default_rates cho mỗi grade                      │
│  • Vectorized với precomputed boundaries                               │
│  • Output: bads, totals, default_rates, to_indices                     │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 5: compute_score_cutoffs_batch()                                  │
│  • Tính score cutoffs từ to_indices                                    │
│  • Output: cutoffs shape (n_sims, n_grades + 1)                        │
│  • Format: [+Inf, c1, c2, ..., c_{n-1}, -Inf]                          │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 6: Statistical Tests & Condition Checks                           │
│  • compute_accuracy_ratio_batch()                                       │
│  • binomial_test_batch(), homogeneity_test_batch()                     │
│  • check_monotonicity_batch(), check_max_pd_batch()                    │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          OUTPUT                                         │
│  FullSimulationResult:                                                  │
│  • alphas, betas, implied_pds, accuracy_ratios                         │
│  • n_max_pd_violations, n_monotonicity_violations                      │
│  • n_binomial_one_tail, n_homogeneity                                  │
│  • score_cutoffs: shape (n_sims, n_grades + 1)                         │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Các Hàm Chính

### 3.1. Data Preparation

| Hàm | Input | Output |
|-----|-------|--------|
| `prepare_observed_data()` | `scores`, `labels` | `ObservedData` |

### 3.2. Beta Distribution

| Hàm | Input | Output |
|-----|-------|--------|
| `compute_grade_probabilities_batch()` | `alphas`, `betas`, `mid_pds` | `cum_probs (n_sims, n_grades)` |

### 3.3. Default Rate Calculator

| Hàm | Input | Output |
|-----|-------|--------|
| `precompute_score_tie_boundaries()` | `scores` | `adjusted_boundaries (n_obs + 1,)` |
| `compute_grade_statistics_batch()` | `observed_data`, `cum_probs_batch`, `precomputed_boundaries` | `bads`, `totals`, `default_rates`, `to_indices` |
| `compute_score_cutoffs_batch()` | `observed_data`, `to_indices_batch` | `cutoffs (n_sims, n_grades + 1)` |

### 3.4. Statistical Tests

| Hàm | Input | Output |
|-----|-------|--------|
| `binomial_test_batch()` | `default_rates`, `totals`, `mid_pds`, `alpha_level` | `n_failures (n_sims,)` |
| `homogeneity_test_batch()` | `default_rates`, `totals`, `quantiles` | `n_failures (n_sims,)` |

### 3.5. Condition Checker

| Hàm | Input | Output |
|-----|-------|--------|
| `check_monotonicity_batch()` | `default_rates` | `n_violations (n_sims,)` |
| `check_max_pd_batch()` | `default_rates`, `max_pds` | `n_violations (n_sims,)` |

### 3.6. Accuracy Ratio

| Hàm | Input | Output |
|-----|-------|--------|
| `compute_accuracy_ratio_batch()` | `bads`, `totals` | `accuracy_ratios (n_sims,)` |

---

## 4. Score Cutoffs Convention

**Quy ước**: Grade i có score trong khoảng `[cutoff[i+1], cutoff[i])` (dấu = ở cận DƯỚI)

**Format với 10 grades**:
```
cutoffs = [+Inf, c1, c2, c3, c4, c5, c6, c7, c8, c9, -Inf]
           │                                          │
        cận trên            9 score cutoffs        cận dưới
        (vô cực)                thực               (vô cực)
```

**Grade assignment**:
| Grade | Score Range |
|-------|-------------|
| AAA (1) | `c1 <= score < +Inf` |
| AA (2) | `c2 <= score < c1` |
| ... | ... |
| D (10) | `-Inf <= score < c9` |

---

## 5. Sử dụng

```python
from calibration import (
    CalibrationSimulationRunner,
    SimulationGridConfig,
    StatisticalTestConfig,
    prepare_observed_data
)

# 1. Prepare data
observed_data = prepare_observed_data(scores, labels)

# 2. Configure
grid_config = SimulationGridConfig(
    alpha_start=0.3, alpha_stop=6.0,
    beta_start=0.3, beta_stop=6.0,
    step=0.005
)
test_config = StatisticalTestConfig(confidence_level=0.95)

# 3. Run simulation
runner = CalibrationSimulationRunner(
    master_scale=master_scale,
    observed_data=observed_data,
    grid_config=grid_config,
    test_config=test_config
)
results = runner.run()

# 4. Access results
print(results.alphas)           # Shape: (n_sims,)
print(results.score_cutoffs)    # Shape: (n_sims, n_grades + 1)
```