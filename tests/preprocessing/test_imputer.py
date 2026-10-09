import pytest
import pandas as pd
import numpy as np
from preprocessing.imputer import CustomNAFiller

def test_custom_na_filler():
    data = {
        'A': [1.0, np.nan, 3.0],
        'B': [np.nan, 2.0, 3.0],
        'C': [1.0, 2.0, np.nan],
        'D': [np.nan, np.nan, np.nan]
    }
    df = pd.DataFrame(data)
    
    filler = CustomNAFiller(
        fill_zero_cols=['A'],
        fill_median_cols=['B'],
        fill_mode_cols=['C'],
        fill_dict={'D': 99}
    )
    
    df_filled = filler.fit_transform(df)
    
    # Assertions
    assert df_filled['A'].iloc[1] == 0.0
    assert df_filled['B'].iloc[0] == 2.5  # Median of [2.0, 3.0]
    assert df_filled['C'].iloc[2] == 1.0  # Mode of [1.0, 2.0] is ambiguous, default first
    assert df_filled['D'].iloc[0] == 99.0

def test_case_insensitivity():
    df = pd.DataFrame({'a': [np.nan]})
    filler = CustomNAFiller(fill_zero_cols=['A']) # A instead of a
    df_filled = filler.fit_transform(df)
    # After fit_transform, columns are converted to uppercase
    assert df_filled['A'].iloc[0] == 0.0
