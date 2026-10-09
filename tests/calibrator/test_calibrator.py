import pytest
import numpy as np
from calibrator import CalibrationSimulationRunner
from calibrator.config import SimulationGridConfig, StatisticalTestConfig, create_default_master_scale
from calibrator.data_preparer import prepare_observed_data

def test_calibrator_smoke():
    # Create dummy data
    np.random.seed(42)
    n_obs = 1000
    scores = np.random.uniform(300, 850, n_obs)
    labels = (scores < 500).astype(int)  # Lower scores = higher probability of default (bads)
    
    # Prepare data
    observed_data = prepare_observed_data(scores, labels)
    
    # Prepare scale
    master_scale = create_default_master_scale()
    
    # Config - tiny grid for speed
    grid_config = SimulationGridConfig(
        alpha_start=0.5, alpha_stop=1.5,
        beta_start=0.5, beta_stop=1.5,
        step=0.5
    )
    test_config = StatisticalTestConfig()
    
    # Run
    runner = CalibrationSimulationRunner(
        master_scale=master_scale,
        observed_data=observed_data,
        grid_config=grid_config,
        test_config=test_config,
        verbose=False
    )
    
    results = runner.run()
    
    assert results is not None
    assert len(results.alphas) > 0
    assert results.score_cutoffs.shape == (len(results.alphas), master_scale.n_grades + 1)
    assert results.accuracy_ratios.shape == (len(results.alphas),)
