# PD Modules

Python utilities for **credit risk / Probability of Default (PD) modelling**: data preprocessing, feature selection, estimators, calibration, and model monitoring.

## Modules

| Module | Purpose |
| --- | --- |
| `preprocessing/` | Missing-value imputation and binning |
| `feature_selection/` | Univariate and multivariate feature selection (Gini, IV, missing rate, correlation, VIF, PCA, beam search) |
| `estimators/` | Binary and multiclass estimators |
| `calibrator/` | PD calibration utilities, statistical checks, and simulation |
| `monitor/` | Model performance and PSI monitoring |
| `eda/` | Exploratory data summaries |
| `utils/` | Scoring, pipeline, and pickle helpers |
| `experimental/` | Experimental utilities |

## Requirements

- Python 3.10+
- Dependencies are declared in `pyproject.toml`
- A Conda environment is also provided in `environment.yml`

## Setup

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/nguyenngocbinh/pd-modules.git
cd pd-modules
pip install -e .
```

Alternatively, create the Conda environment:

```bash
conda env create -f environment.yml
conda activate env_ml
pip install -e .
```

## Example

```python
from calibrator import CalibrationSimulationRunner
from preprocessing.imputer import CustomNAFiller

# Import the utilities you need and configure them for your dataset.
```

See `calibrator/README.md` and the notebooks in `notebooks/` for more details and examples.

## Tests

Run the test suite from the repository root:

```bash
pytest
```

## Development

Use a feature branch and open a pull request instead of committing directly to `main`. Add or update tests for changes, and follow the existing type hints and code style.

---

This project is a collection of reusable modelling utilities; review each module's documentation for supported inputs and behaviour.
