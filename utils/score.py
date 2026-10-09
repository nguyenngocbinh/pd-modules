import numpy as np
import pandas as pd


def rescale_score(pd, base_odds=120, pdo=100, base_point=500, ndigit=2):
    # Clip PD to avoid log(0) or division by zero
    pd = np.clip(pd, 1e-6, 1 - 1e-6)
    
    odds = (1 - pd) / pd
    factor = pdo / np.log(2)
    offset = base_point - factor * np.log(base_odds)
    score = np.round(offset + factor * np.log(odds), ndigit)
    
    # Explicitly handle edge cases for pd=0 (high score) and pd=1 (low/zero score)
    # Re-calculate based on extreme odds
    if isinstance(pd, (list, np.ndarray)):
        # For array input, handle after
        return np.where(pd >= 0.999999, 0.0, score)
    elif pd >= 0.999999:
        return 0.0
    return score
