# pd-modules

A library of machine learning tools, including preprocessing, feature selection, estimators, and model monitoring.

## Installation

To install `pd-modules` as a package in your environment:

```bash
# Clone the repository and navigate to the root directory
# Run the following command in editable mode
pip install -e . --no-deps
```

> [!NOTE]
> Ensure all dependencies (`numpy`, `pandas`, `scikit-learn`, etc.) are already installed in your Python environment as per the `environment.yml` file.

## Usage

Once installed, you can import the modules directly in your Python code:

```python
from calibrator import CalibrationSimulationRunner
from preprocessing.imputer import CustomNAFiller

# Example usage
# runner = CalibrationSimulationRunner(...)
```

## Developer Information

### Testing
To run tests, execute `pytest` in the root directory:
```bash
pytest
```

### Development Workflow
- **Branching:** Always work on a separate feature branch.
- **Rules:**
  - Never commit directly to `main`.
  - Always run tests before committing.
  - Follow Scikit-learn API (inherit `BaseEstimator`, `TransformerMixin`).
  - Use Type Hints and Google-style docstrings.
  - Use `black` for formatting.
  - Follow Semantic Versioning with Git tags (`vX.Y.Z`).
