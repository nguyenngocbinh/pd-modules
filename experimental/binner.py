"""Backward-compatible import for the canonical preprocessing binner.

The maintained implementation lives in :mod:`preprocessing.binner`.
Keep experimental-specific experiments in separate modules rather than
duplicating the production binning implementation here.
"""

from preprocessing.binner import DynamicBinningProcess

__all__ = ["DynamicBinningProcess"]
