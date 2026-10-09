import pytest
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from estimators.binary.logistic import SMLogit

def test_smlogit_fit_predict():
    X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_redundant=2, random_state=42)
    df = pd.DataFrame(X, columns=[f"feat_{i}" for i in range(10)])
    
    # Initialize and fit
    model = SMLogit(fit_intercept=True)
    # Ensure sufficient variance
    model.fit(df, y)
    
    # Predict
    y_pred = model.predict(df)
    y_proba = model.predict_proba(df)
    
    # Assertions
    assert y_pred.shape == (100,)
    assert y_proba.shape == (100, 2)
    assert np.all((y_proba >= 0) & (y_proba <= 1))
    assert model.score(df, y) > 0.5  # Should be better than random

def test_smlogit_standardized_coef():
    X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_redundant=2, random_state=42)
    df = pd.DataFrame(X, columns=[f"f{i}" for i in range(10)])
    
    model = SMLogit()
    model.fit(df, y)
    
    std_coefs = model.get_standardized_coef()
    
    # Assertions
    assert "const" in std_coefs.index
    assert "f0" in std_coefs.index
    assert "f1" in std_coefs.index
    assert len(std_coefs) == 11 # 1 constant + 10 features
