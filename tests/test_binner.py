import numpy as np
import pandas as pd
import pytest

from preprocessing.binner import DynamicBinningProcess as CanonicalBinner
from experimental.binner import DynamicBinningProcess as CompatibilityBinner


def make_data(n=500, seed=42):
    rng = np.random.default_rng(seed)
    x1 = rng.normal(size=n)
    x2 = rng.normal(size=n)
    category = rng.choice(["A", "B", "C"], size=n)
    logits = 1.2 * x1 - 0.6 * x2 + (category == "C") * 0.7
    probabilities = 1 / (1 + np.exp(-logits))
    y = rng.binomial(1, probabilities)
    X = pd.DataFrame({"x1": x1, "x2": x2, "category": category})
    return X, pd.Series(y, name="target")


def test_compatibility_import_points_to_canonical_class():
    assert CompatibilityBinner is CanonicalBinner


def test_fit_transform_without_selection_preserves_all_features():
    X, y = make_data()
    binner = CanonicalBinner(
        binning_process_params={"max_n_bins": 5, "min_bin_size": 0.05},
        n_jobs=1,
    )

    transformed = binner.fit_transform(X, y)

    assert list(transformed.columns) == list(X.columns)
    assert list(binner.get_feature_names_out()) == list(X.columns)
    assert binner.get_binning_summary() is not None


def test_iv_feature_selection_and_output_feature_names():
    X, y = make_data()
    binner = CanonicalBinner(
        selection_metric="iv",
        metric_min=0.0,
        metric_max=None,
        binning_process_params={"max_n_bins": 5, "min_bin_size": 0.05},
        n_jobs=1,
        verbose=False,
    )

    transformed = binner.fit_transform(X, y)
    summary = binner.get_selection_summary()

    assert list(transformed.columns) == list(binner.selected_features)
    assert list(binner.get_feature_names_out()) == list(transformed.columns)
    assert set(summary["feature"]) == set(X.columns)
    assert set(summary["selection_status"]).issubset({"Selected", "Not Selected"})


def test_selection_threshold_can_remove_all_features():
    X, y = make_data()
    binner = CanonicalBinner(
        selection_metric="iv",
        metric_min=1e9,
        binning_process_params={"max_n_bins": 5, "min_bin_size": 0.05},
        n_jobs=1,
        verbose=False,
    )

    transformed = binner.fit_transform(X, y)

    assert transformed.shape[1] == 0
    assert list(binner.get_feature_names_out()) == []


def test_unfitted_transform_raises_sklearn_validation_error():
    from sklearn.exceptions import NotFittedError

    binner = CanonicalBinner()
    X, _ = make_data(n=20)
    with pytest.raises(NotFittedError):
        binner.transform(X)
