import pytest
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from preprocessing.binner import DynamicBinningProcess

def test_dynamic_binning_process():
    # Setup
    X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_redundant=2, random_state=42)
    df = pd.DataFrame(X, columns=[f"Feature_{i}" for i in range(10)])
    
    binning_params = {"max_n_bins": 3, "monotonic_trend": 'auto'}
    
    # Initialize and fit
    binner = DynamicBinningProcess(binning_process_params=binning_params)
    binner.fit(df, y)
    
    # Transform
    X_binned = binner.transform(df)
    
    # Assertions
    assert X_binned.shape == (100, 10)
    assert hasattr(binner, "feature_names_in_")
    assert binner.feature_names_in_ == [f"Feature_{i}" for i in range(10)]

def test_not_fitted_error():
    binner = DynamicBinningProcess()
    with pytest.raises(AttributeError, match="not fitted yet"):
        binner.get_feature_names_in()
