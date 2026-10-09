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

```
pd-modules
├─ AGENTS.md
├─ archive
│  ├─ calibrator
│  │  ├─ calibrator.py
│  │  └─ __init__.py
│  └─ feature_selection_old.py
├─ calibrator
│  ├─ accuracy_ratio.py
│  ├─ beta_distribution.py
│  ├─ calibration_types.py
│  ├─ condition_checker.py
│  ├─ config.py
│  ├─ data_preparer.py
│  ├─ default_rate_calculator.py
│  ├─ README.md
│  ├─ simulation_runner.py
│  ├─ statistical_tests.py
│  └─ __init__.py
├─ eda
│  ├─ summary.py
│  └─ __init__.py
├─ environment.yml
├─ estimators
│  ├─ binary
│  │  ├─ logistic.py
│  │  ├─ mlp.py
│  │  └─ __init__.py
│  └─ multiclass
│     ├─ mlp.py
│     └─ __init__.py
├─ experimental
│  └─ binner.py
├─ feature_selection
│  ├─ multivariate
│  │  ├─ auc_corr.py
│  │  ├─ beamsearch.py
│  │  ├─ pca.py
│  │  ├─ vif.py
│  │  └─ __init__.py
│  └─ univariate
│     ├─ gini.py
│     ├─ indentical_rate.py
│     ├─ iv.py
│     ├─ missing_rate.py
│     ├─ subset.py
│     └─ __init__.py
├─ monitor
│  ├─ performance.py
│  ├─ psi.py
│  └─ __init__.py
├─ notebooks
│  ├─ beta_distribution_visualization.ipynb
│  ├─ calibration_example.ipynb
│  └─ test_nb.ipynb
├─ preprocessing
│  ├─ binner.py
│  ├─ imputer.py
│  └─ __init__.py
├─ pyproject.toml
├─ README.md
├─ setup.py
├─ tests
│  ├─ calibrator
│  │  └─ test_calibrator.py
│  ├─ estimators
│  │  └─ binary
│  │     └─ test_logistic.py
│  ├─ preprocessing
│  │  ├─ test_binner.py
│  │  └─ test_imputer.py
│  ├─ utils
│  │  └─ test_score.py
│  └─ __init__.py
├─ utils
│  ├─ pickle.py
│  ├─ pipeline.py
│  ├─ score.py
│  └─ __init__.py
└─ venv
   ├─ .lock
   ├─ CACHEDIR.TAG
   ├─ Include
   ├─ Lib
   │  └─ site-packages
   │     ├─ absl
   │     │  ├─ app.py
   │     │  ├─ app.pyi
   │     │  ├─ command_name.py
   │     │  ├─ flags
   │     │  │  ├─ argparse_flags.py
   │     │  │  ├─ _argument_parser.py
   │     │  │  ├─ _defines.py
   │     │  │  ├─ _exceptions.py
   │     │  │  ├─ _flag.py
   │     │  │  ├─ _flagvalues.py
   │     │  │  ├─ _helpers.py
   │     │  │  ├─ _validators.py
   │     │  │  ├─ _validators_classes.py
   │     │  │  └─ __init__.py
   │     │  ├─ logging
   │     │  │  ├─ converter.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ py.typed
   │     │  ├─ testing
   │     │  │  ├─ absltest.py
   │     │  │  ├─ flagsaver.py
   │     │  │  ├─ parameterized.py
   │     │  │  ├─ xml_reporter.py
   │     │  │  ├─ _bazelize_command.py
   │     │  │  ├─ _pretty_print_reporter.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ absl_py-2.5.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ AUTHORS
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ astunparse
   │     │  ├─ printer.py
   │     │  ├─ unparser.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ astunparse-1.6.3.dist-info
   │     │  ├─ AUTHORS.rst
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ certifi
   │     │  ├─ cacert.pem
   │     │  ├─ core.py
   │     │  ├─ py.typed
   │     │  ├─ tests
   │     │  │  ├─ test_certify.py
   │     │  │  └─ __init__.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ certifi-2026.7.22.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ cffi
   │     │  ├─ api.py
   │     │  ├─ backend_ctypes.py
   │     │  ├─ cffi_opcode.py
   │     │  ├─ commontypes.py
   │     │  ├─ cparser.py
   │     │  ├─ error.py
   │     │  ├─ ffiplatform.py
   │     │  ├─ gen_src.py
   │     │  ├─ lock.py
   │     │  ├─ model.py
   │     │  ├─ parse_c_type.h
   │     │  ├─ pkgconfig.py
   │     │  ├─ recompiler.py
   │     │  ├─ setuptools_ext.py
   │     │  ├─ vengine_cpy.py
   │     │  ├─ vengine_gen.py
   │     │  ├─ verifier.py
   │     │  ├─ _cffi_errors.h
   │     │  ├─ _cffi_gen_src.py
   │     │  ├─ _cffi_include.h
   │     │  ├─ _embedding.h
   │     │  ├─ _imp_emulation.py
   │     │  ├─ _shimmed_dist_utils.py
   │     │  └─ __init__.py
   │     ├─ cffi-2.1.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ charset_normalizer
   │     │  ├─ api.py
   │     │  ├─ cd.py
   │     │  ├─ cli
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ constant.py
   │     │  ├─ legacy.py
   │     │  ├─ md.py
   │     │  ├─ models.py
   │     │  ├─ py.typed
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ charset_normalizer-3.5.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ clang
   │     │  ├─ cindex.py
   │     │  ├─ enumerations.py
   │     │  ├─ native
   │     │  │  ├─ libclang.dll
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ clarabel
   │     │  └─ __init__.py
   │     ├─ clarabel-0.11.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.md
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ colorama
   │     │  ├─ ansi.py
   │     │  ├─ ansitowin32.py
   │     │  ├─ initialise.py
   │     │  ├─ tests
   │     │  │  ├─ ansitowin32_test.py
   │     │  │  ├─ ansi_test.py
   │     │  │  ├─ initialise_test.py
   │     │  │  ├─ isatty_test.py
   │     │  │  ├─ utils.py
   │     │  │  ├─ winterm_test.py
   │     │  │  └─ __init__.py
   │     │  ├─ win32.py
   │     │  ├─ winterm.py
   │     │  └─ __init__.py
   │     ├─ colorama-0.4.6.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ contourpy
   │     │  ├─ array.py
   │     │  ├─ chunk.py
   │     │  ├─ convert.py
   │     │  ├─ dechunk.py
   │     │  ├─ enum_util.py
   │     │  ├─ py.typed
   │     │  ├─ typecheck.py
   │     │  ├─ types.py
   │     │  ├─ util
   │     │  │  ├─ bokeh_renderer.py
   │     │  │  ├─ bokeh_util.py
   │     │  │  ├─ data.py
   │     │  │  ├─ mpl_renderer.py
   │     │  │  ├─ mpl_util.py
   │     │  │  ├─ renderer.py
   │     │  │  └─ __init__.py
   │     │  ├─ _contourpy.cp310-win_amd64.lib
   │     │  ├─ _contourpy.pyi
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ contourpy-1.3.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ cvxpy
   │     │  ├─ atoms
   │     │  │  ├─ affine
   │     │  │  │  ├─ add_expr.py
   │     │  │  │  ├─ affine_atom.py
   │     │  │  │  ├─ binary_operators.py
   │     │  │  │  ├─ bmat.py
   │     │  │  │  ├─ broadcast_to.py
   │     │  │  │  ├─ concatenate.py
   │     │  │  │  ├─ conj.py
   │     │  │  │  ├─ conv.py
   │     │  │  │  ├─ cumsum.py
   │     │  │  │  ├─ diag.py
   │     │  │  │  ├─ diff.py
   │     │  │  │  ├─ hstack.py
   │     │  │  │  ├─ imag.py
   │     │  │  │  ├─ index.py
   │     │  │  │  ├─ kron.py
   │     │  │  │  ├─ partial_trace.py
   │     │  │  │  ├─ partial_transpose.py
   │     │  │  │  ├─ promote.py
   │     │  │  │  ├─ real.py
   │     │  │  │  ├─ reshape.py
   │     │  │  │  ├─ sum.py
   │     │  │  │  ├─ trace.py
   │     │  │  │  ├─ transpose.py
   │     │  │  │  ├─ unary_operators.py
   │     │  │  │  ├─ upper_tri.py
   │     │  │  │  ├─ vec.py
   │     │  │  │  ├─ vstack.py
   │     │  │  │  ├─ wraps.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ atom.py
   │     │  │  ├─ axis_atom.py
   │     │  │  ├─ condition_number.py
   │     │  │  ├─ cummax.py
   │     │  │  ├─ cumprod.py
   │     │  │  ├─ cvar.py
   │     │  │  ├─ dist_ratio.py
   │     │  │  ├─ dotsort.py
   │     │  │  ├─ elementwise
   │     │  │  │  ├─ abs.py
   │     │  │  │  ├─ ceil.py
   │     │  │  │  ├─ elementwise.py
   │     │  │  │  ├─ entr.py
   │     │  │  │  ├─ exp.py
   │     │  │  │  ├─ huber.py
   │     │  │  │  ├─ inv_pos.py
   │     │  │  │  ├─ kl_div.py
   │     │  │  │  ├─ log.py
   │     │  │  │  ├─ log1p.py
   │     │  │  │  ├─ loggamma.py
   │     │  │  │  ├─ logistic.py
   │     │  │  │  ├─ log_normcdf.py
   │     │  │  │  ├─ maximum.py
   │     │  │  │  ├─ minimum.py
   │     │  │  │  ├─ neg.py
   │     │  │  │  ├─ pos.py
   │     │  │  │  ├─ power.py
   │     │  │  │  ├─ rel_entr.py
   │     │  │  │  ├─ scalene.py
   │     │  │  │  ├─ sqrt.py
   │     │  │  │  ├─ square.py
   │     │  │  │  ├─ xexp.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ errormsg.py
   │     │  │  ├─ eye_minus_inv.py
   │     │  │  ├─ gen_lambda_max.py
   │     │  │  ├─ geo_mean.py
   │     │  │  ├─ gmatmul.py
   │     │  │  ├─ harmonic_mean.py
   │     │  │  ├─ inv_prod.py
   │     │  │  ├─ lambda_max.py
   │     │  │  ├─ lambda_min.py
   │     │  │  ├─ lambda_sum_largest.py
   │     │  │  ├─ lambda_sum_smallest.py
   │     │  │  ├─ length.py
   │     │  │  ├─ log_det.py
   │     │  │  ├─ log_sum_exp.py
   │     │  │  ├─ matrix_frac.py
   │     │  │  ├─ max.py
   │     │  │  ├─ min.py
   │     │  │  ├─ mixed_norm.py
   │     │  │  ├─ norm.py
   │     │  │  ├─ norm1.py
   │     │  │  ├─ norm_inf.py
   │     │  │  ├─ norm_nuc.py
   │     │  │  ├─ one_minus_pos.py
   │     │  │  ├─ perspective.py
   │     │  │  ├─ pf_eigenvalue.py
   │     │  │  ├─ pnorm.py
   │     │  │  ├─ prod.py
   │     │  │  ├─ ptp.py
   │     │  │  ├─ quad_form.py
   │     │  │  ├─ quad_over_lin.py
   │     │  │  ├─ quantum_cond_entr.py
   │     │  │  ├─ quantum_rel_entr.py
   │     │  │  ├─ sigma_max.py
   │     │  │  ├─ sign.py
   │     │  │  ├─ stats.py
   │     │  │  ├─ sum_largest.py
   │     │  │  ├─ sum_smallest.py
   │     │  │  ├─ sum_squares.py
   │     │  │  ├─ suppfunc.py
   │     │  │  ├─ total_variation.py
   │     │  │  ├─ tr_inv.py
   │     │  │  ├─ von_neumann_entr.py
   │     │  │  └─ __init__.py
   │     │  ├─ constraints
   │     │  │  ├─ cones.py
   │     │  │  ├─ constraint.py
   │     │  │  ├─ exponential.py
   │     │  │  ├─ finite_set.py
   │     │  │  ├─ nonpos.py
   │     │  │  ├─ power.py
   │     │  │  ├─ psd.py
   │     │  │  ├─ second_order.py
   │     │  │  ├─ utilities.py
   │     │  │  ├─ zero.py
   │     │  │  └─ __init__.py
   │     │  ├─ cvxcore
   │     │  │  ├─ python
   │     │  │  │  ├─ canonInterface.py
   │     │  │  │  ├─ cppbackend.py
   │     │  │  │  ├─ cvxcore.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ error.py
   │     │  ├─ expressions
   │     │  │  ├─ constants
   │     │  │  │  ├─ callback_param.py
   │     │  │  │  ├─ constant.py
   │     │  │  │  ├─ parameter.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cvxtypes.py
   │     │  │  ├─ expression.py
   │     │  │  ├─ leaf.py
   │     │  │  ├─ variable.py
   │     │  │  └─ __init__.py
   │     │  ├─ interface
   │     │  │  ├─ base_matrix_interface.py
   │     │  │  ├─ matrix_utilities.py
   │     │  │  ├─ numpy_interface
   │     │  │  │  ├─ matrix_interface.py
   │     │  │  │  ├─ ndarray_interface.py
   │     │  │  │  ├─ sparse_matrix_interface.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ lin_ops
   │     │  │  ├─ canon_backend.py
   │     │  │  ├─ lin_constraints.py
   │     │  │  ├─ lin_op.py
   │     │  │  ├─ lin_utils.py
   │     │  │  ├─ tree_mat.py
   │     │  │  └─ __init__.py
   │     │  ├─ problems
   │     │  │  ├─ iterative.py
   │     │  │  ├─ objective.py
   │     │  │  ├─ param_prob.py
   │     │  │  ├─ problem.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ reductions
   │     │  │  ├─ canonicalization.py
   │     │  │  ├─ chain.py
   │     │  │  ├─ complex2real
   │     │  │  │  ├─ canonicalizers
   │     │  │  │  │  ├─ abs_canon.py
   │     │  │  │  │  ├─ aff_canon.py
   │     │  │  │  │  ├─ constant_canon.py
   │     │  │  │  │  ├─ equality_canon.py
   │     │  │  │  │  ├─ inequality_canon.py
   │     │  │  │  │  ├─ matrix_canon.py
   │     │  │  │  │  ├─ param_canon.py
   │     │  │  │  │  ├─ pnorm_canon.py
   │     │  │  │  │  ├─ psd_canon.py
   │     │  │  │  │  ├─ soc_canon.py
   │     │  │  │  │  ├─ variable_canon.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ complex2real.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cone2cone
   │     │  │  │  ├─ affine2direct.py
   │     │  │  │  ├─ approximations.py
   │     │  │  │  ├─ exotic2common.py
   │     │  │  │  ├─ soc2psd.py
   │     │  │  │  ├─ soc_dim3.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cvx_attr2constr.py
   │     │  │  ├─ dcp2cone
   │     │  │  │  ├─ canonicalizers
   │     │  │  │  │  ├─ entr_canon.py
   │     │  │  │  │  ├─ exp_canon.py
   │     │  │  │  │  ├─ geo_mean_canon.py
   │     │  │  │  │  ├─ huber_canon.py
   │     │  │  │  │  ├─ indicator_canon.py
   │     │  │  │  │  ├─ kl_div_canon.py
   │     │  │  │  │  ├─ lambda_max_canon.py
   │     │  │  │  │  ├─ lambda_sum_largest_canon.py
   │     │  │  │  │  ├─ log1p_canon.py
   │     │  │  │  │  ├─ logistic_canon.py
   │     │  │  │  │  ├─ log_canon.py
   │     │  │  │  │  ├─ log_det_canon.py
   │     │  │  │  │  ├─ log_sum_exp_canon.py
   │     │  │  │  │  ├─ matrix_frac_canon.py
   │     │  │  │  │  ├─ mul_canon.py
   │     │  │  │  │  ├─ normNuc_canon.py
   │     │  │  │  │  ├─ perspective_canon.py
   │     │  │  │  │  ├─ pnorm_canon.py
   │     │  │  │  │  ├─ power_canon.py
   │     │  │  │  │  ├─ quad_form_canon.py
   │     │  │  │  │  ├─ quad_over_lin_canon.py
   │     │  │  │  │  ├─ quantum_rel_entr_canon.py
   │     │  │  │  │  ├─ rel_entr_canon.py
   │     │  │  │  │  ├─ sigma_max_canon.py
   │     │  │  │  │  ├─ suppfunc_canon.py
   │     │  │  │  │  ├─ tr_inv_canon.py
   │     │  │  │  │  ├─ von_neumann_entr_canon.py
   │     │  │  │  │  ├─ xexp_canon.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ cone_matrix_stuffing.py
   │     │  │  │  ├─ dcp2cone.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ dgp2dcp
   │     │  │  │  ├─ canonicalizers
   │     │  │  │  │  ├─ add_canon.py
   │     │  │  │  │  ├─ constant_canon.py
   │     │  │  │  │  ├─ cumprod_canon.py
   │     │  │  │  │  ├─ div_canon.py
   │     │  │  │  │  ├─ exp_canon.py
   │     │  │  │  │  ├─ eye_minus_inv_canon.py
   │     │  │  │  │  ├─ finite_set_canon.py
   │     │  │  │  │  ├─ geo_mean_canon.py
   │     │  │  │  │  ├─ gmatmul_canon.py
   │     │  │  │  │  ├─ log_canon.py
   │     │  │  │  │  ├─ mulexpression_canon.py
   │     │  │  │  │  ├─ mul_canon.py
   │     │  │  │  │  ├─ nonpos_constr_canon.py
   │     │  │  │  │  ├─ norm1_canon.py
   │     │  │  │  │  ├─ norm_inf_canon.py
   │     │  │  │  │  ├─ one_minus_pos_canon.py
   │     │  │  │  │  ├─ parameter_canon.py
   │     │  │  │  │  ├─ pf_eigenvalue_canon.py
   │     │  │  │  │  ├─ pnorm_canon.py
   │     │  │  │  │  ├─ power_canon.py
   │     │  │  │  │  ├─ prod_canon.py
   │     │  │  │  │  ├─ quad_form_canon.py
   │     │  │  │  │  ├─ quad_over_lin_canon.py
   │     │  │  │  │  ├─ sum_canon.py
   │     │  │  │  │  ├─ trace_canon.py
   │     │  │  │  │  ├─ xexp_canon.py
   │     │  │  │  │  ├─ zero_constr_canon.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ dgp2dcp.py
   │     │  │  │  ├─ util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ discrete2mixedint
   │     │  │  │  ├─ valinvec2mixedint.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ dqcp2dcp
   │     │  │  │  ├─ dqcp2dcp.py
   │     │  │  │  ├─ inverse.py
   │     │  │  │  ├─ sets.py
   │     │  │  │  ├─ tighten.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ eliminate_pwl
   │     │  │  │  ├─ canonicalizers
   │     │  │  │  │  ├─ abs_canon.py
   │     │  │  │  │  ├─ cummax_canon.py
   │     │  │  │  │  ├─ cumsum_canon.py
   │     │  │  │  │  ├─ dotsort_canon.py
   │     │  │  │  │  ├─ maximum_canon.py
   │     │  │  │  │  ├─ max_canon.py
   │     │  │  │  │  ├─ minimum_canon.py
   │     │  │  │  │  ├─ min_canon.py
   │     │  │  │  │  ├─ norm1_canon.py
   │     │  │  │  │  ├─ norm_inf_canon.py
   │     │  │  │  │  ├─ sum_largest_canon.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ eliminate_pwl.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ eval_params.py
   │     │  │  ├─ flip_objective.py
   │     │  │  ├─ inverse_data.py
   │     │  │  ├─ matrix_stuffing.py
   │     │  │  ├─ qp2quad_form
   │     │  │  │  ├─ canonicalizers
   │     │  │  │  │  ├─ huber_canon.py
   │     │  │  │  │  ├─ power_canon.py
   │     │  │  │  │  ├─ quad_form_canon.py
   │     │  │  │  │  ├─ quad_over_lin_canon.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ qp2symbolic_qp.py
   │     │  │  │  ├─ qp_matrix_stuffing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ reduction.py
   │     │  │  ├─ solution.py
   │     │  │  ├─ solvers
   │     │  │  │  ├─ bisection.py
   │     │  │  │  ├─ compr_matrix.py
   │     │  │  │  ├─ conic_solvers
   │     │  │  │  │  ├─ cbc_conif.py
   │     │  │  │  │  ├─ clarabel_conif.py
   │     │  │  │  │  ├─ conic_solver.py
   │     │  │  │  │  ├─ copt_conif.py
   │     │  │  │  │  ├─ cplex_conif.py
   │     │  │  │  │  ├─ cuclarabel_conif.py
   │     │  │  │  │  ├─ cuopt_conif.py
   │     │  │  │  │  ├─ cvxopt_conif.py
   │     │  │  │  │  ├─ diffcp_conif.py
   │     │  │  │  │  ├─ ecos_bb_conif.py
   │     │  │  │  │  ├─ ecos_conif.py
   │     │  │  │  │  ├─ glop_conif.py
   │     │  │  │  │  ├─ glpk_conif.py
   │     │  │  │  │  ├─ glpk_mi_conif.py
   │     │  │  │  │  ├─ gurobi_conif.py
   │     │  │  │  │  ├─ highs_conif.py
   │     │  │  │  │  ├─ moreau_conif.py
   │     │  │  │  │  ├─ mosek_conif.py
   │     │  │  │  │  ├─ nag_conif.py
   │     │  │  │  │  ├─ pdlp_conif.py
   │     │  │  │  │  ├─ qoco_conif.py
   │     │  │  │  │  ├─ scipy_conif.py
   │     │  │  │  │  ├─ scip_conif.py
   │     │  │  │  │  ├─ scs_conif.py
   │     │  │  │  │  ├─ sdpa_conif.py
   │     │  │  │  │  ├─ xpress_conif.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ constant_solver.py
   │     │  │  │  ├─ defines.py
   │     │  │  │  ├─ intermediate_chain.py
   │     │  │  │  ├─ kktsolver.py
   │     │  │  │  ├─ qp_solvers
   │     │  │  │  │  ├─ copt_qpif.py
   │     │  │  │  │  ├─ cplex_qpif.py
   │     │  │  │  │  ├─ daqp_qpif.py
   │     │  │  │  │  ├─ gurobi_qpif.py
   │     │  │  │  │  ├─ highs_qpif.py
   │     │  │  │  │  ├─ mpax_qpif.py
   │     │  │  │  │  ├─ osqp_qpif.py
   │     │  │  │  │  ├─ piqp_qpif.py
   │     │  │  │  │  ├─ proxqp_qpif.py
   │     │  │  │  │  ├─ qp_solver.py
   │     │  │  │  │  ├─ xpress_qpif.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ solver.py
   │     │  │  │  ├─ solving_chain.py
   │     │  │  │  ├─ solving_chain_utils.py
   │     │  │  │  ├─ utilities.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ utilities.py
   │     │  │  └─ __init__.py
   │     │  ├─ settings.py
   │     │  ├─ tests
   │     │  │  ├─ .tmpP8jcr7
   │     │  │  ├─ base_test.py
   │     │  │  ├─ ram_limited.py
   │     │  │  ├─ solver_test_helpers.py
   │     │  │  ├─ test_atoms.py
   │     │  │  ├─ test_attributes.py
   │     │  │  ├─ test_base_classes.py
   │     │  │  ├─ test_canon_sign.py
   │     │  │  ├─ test_coeff_extractor.py
   │     │  │  ├─ test_complex.py
   │     │  │  ├─ test_cone2cone.py
   │     │  │  ├─ test_conic_solvers.py
   │     │  │  ├─ test_constant.py
   │     │  │  ├─ test_constant_atoms.py
   │     │  │  ├─ test_constraints.py
   │     │  │  ├─ test_convolution.py
   │     │  │  ├─ test_copt_write.py
   │     │  │  ├─ test_copy.py
   │     │  │  ├─ test_curvature.py
   │     │  │  ├─ test_custom_solver.py
   │     │  │  ├─ test_cvxpygen.py
   │     │  │  ├─ test_derivative.py
   │     │  │  ├─ test_dgp.py
   │     │  │  ├─ test_dgp2dcp.py
   │     │  │  ├─ test_dgp_dpp.py
   │     │  │  ├─ test_domain.py
   │     │  │  ├─ test_dpp.py
   │     │  │  ├─ test_dqcp.py
   │     │  │  ├─ test_errors.py
   │     │  │  ├─ test_examples.py
   │     │  │  ├─ test_expressions.py
   │     │  │  ├─ test_expression_methods.py
   │     │  │  ├─ test_grad.py
   │     │  │  ├─ test_gurobi_write.py
   │     │  │  ├─ test_interfaces.py
   │     │  │  ├─ test_KKT.py
   │     │  │  ├─ test_kron_canon.py
   │     │  │  ├─ test_linalg_utils.py
   │     │  │  ├─ test_linear_cone.py
   │     │  │  ├─ test_lin_ops.py
   │     │  │  ├─ test_matrices.py
   │     │  │  ├─ test_matrix_utilities.py
   │     │  │  ├─ test_mip_vars.py
   │     │  │  ├─ test_monotonicity.py
   │     │  │  ├─ test_nonlinear_atoms.py
   │     │  │  ├─ test_objectives.py
   │     │  │  ├─ test_param_cone_prog.py
   │     │  │  ├─ test_param_quad_prog.py
   │     │  │  ├─ test_perspective.py
   │     │  │  ├─ test_power_tools.py
   │     │  │  ├─ test_problem.py
   │     │  │  ├─ test_python_backends.py
   │     │  │  ├─ test_qp_solvers.py
   │     │  │  ├─ test_quadratic.py
   │     │  │  ├─ test_quad_form.py
   │     │  │  ├─ test_quantum_rel_entr.py
   │     │  │  ├─ test_scalarize.py
   │     │  │  ├─ test_semidefinite_vars.py
   │     │  │  ├─ test_shape.py
   │     │  │  ├─ test_sign.py
   │     │  │  ├─ test_soc_dim3.py
   │     │  │  ├─ test_suppfunc.py
   │     │  │  ├─ test_valinvec2mixedint.py
   │     │  │  ├─ test_versioning.py
   │     │  │  ├─ test_von_neumann_entr.py
   │     │  │  └─ __init__.py
   │     │  ├─ transforms
   │     │  │  ├─ indicator.py
   │     │  │  ├─ linearize.py
   │     │  │  ├─ partial_optimize.py
   │     │  │  ├─ scalarize.py
   │     │  │  ├─ suppfunc.py
   │     │  │  └─ __init__.py
   │     │  ├─ utilities
   │     │  │  ├─ canonical.py
   │     │  │  ├─ citations.py
   │     │  │  ├─ coeff_extractor.py
   │     │  │  ├─ coo_array_compat.py
   │     │  │  ├─ cpp
   │     │  │  │  ├─ sparsecholesky
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cvxpy_upgrade.py
   │     │  │  ├─ debug_tools.py
   │     │  │  ├─ deterministic.py
   │     │  │  ├─ grad.py
   │     │  │  ├─ key_utils.py
   │     │  │  ├─ linalg.py
   │     │  │  ├─ performance_utils.py
   │     │  │  ├─ perspective_utils.py
   │     │  │  ├─ power_tools.py
   │     │  │  ├─ replace_quad_forms.py
   │     │  │  ├─ scopes.py
   │     │  │  ├─ shape.py
   │     │  │  ├─ sign.py
   │     │  │  ├─ versioning.py
   │     │  │  └─ __init__.py
   │     │  ├─ version.py
   │     │  └─ __init__.py
   │     ├─ cvxpy-1.7.5.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ cycler
   │     │  ├─ py.typed
   │     │  └─ __init__.py
   │     ├─ cycler-0.12.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ dateutil
   │     │  ├─ easter.py
   │     │  ├─ parser
   │     │  │  ├─ isoparser.py
   │     │  │  ├─ _parser.py
   │     │  │  └─ __init__.py
   │     │  ├─ relativedelta.py
   │     │  ├─ rrule.py
   │     │  ├─ tz
   │     │  │  ├─ tz.py
   │     │  │  ├─ win.py
   │     │  │  ├─ _common.py
   │     │  │  ├─ _factories.py
   │     │  │  └─ __init__.py
   │     │  ├─ tzwin.py
   │     │  ├─ utils.py
   │     │  ├─ zoneinfo
   │     │  │  ├─ dateutil-zoneinfo.tar.gz
   │     │  │  └─ __init__.py
   │     │  ├─ _common.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ distutils-precedence.pth
   │     ├─ exceptiongroup
   │     │  ├─ py.typed
   │     │  ├─ _catch.py
   │     │  ├─ _exceptions.py
   │     │  ├─ _formatting.py
   │     │  ├─ _suppress.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ exceptiongroup-1.3.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ flatbuffers
   │     │  ├─ compat.py
   │     │  ├─ encode.py
   │     │  ├─ flexbuffers.py
   │     │  ├─ number_types.py
   │     │  ├─ packer.py
   │     │  ├─ table.py
   │     │  ├─ util.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ flatbuffers-25.12.19.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ fontTools
   │     │  ├─ afmLib.py
   │     │  ├─ agl.py
   │     │  ├─ annotations.py
   │     │  ├─ cffLib
   │     │  │  ├─ CFF2ToCFF.py
   │     │  │  ├─ CFFToCFF2.py
   │     │  │  ├─ specializer.py
   │     │  │  ├─ transforms.py
   │     │  │  ├─ width.py
   │     │  │  └─ __init__.py
   │     │  ├─ colorLib
   │     │  │  ├─ errors.py
   │     │  │  ├─ geometry.py
   │     │  │  └─ __init__.py
   │     │  ├─ config
   │     │  │  └─ __init__.py
   │     │  ├─ cu2qu
   │     │  │  ├─ benchmark.py
   │     │  │  ├─ cli.py
   │     │  │  ├─ cu2qu.py
   │     │  │  ├─ errors.py
   │     │  │  ├─ ufo.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ designspaceLib
   │     │  │  ├─ split.py
   │     │  │  ├─ statNames.py
   │     │  │  ├─ types.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ diff
   │     │  │  ├─ color.py
   │     │  │  ├─ diff.py
   │     │  │  ├─ utils.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ encodings
   │     │  │  ├─ codecs.py
   │     │  │  ├─ MacRoman.py
   │     │  │  ├─ StandardEncoding.py
   │     │  │  └─ __init__.py
   │     │  ├─ feaLib
   │     │  │  ├─ ast.py
   │     │  │  ├─ error.py
   │     │  │  ├─ lexer.py
   │     │  │  ├─ location.py
   │     │  │  ├─ lookupDebugInfo.py
   │     │  │  ├─ parser.py
   │     │  │  ├─ variableScalar.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ fontBuilder.py
   │     │  ├─ help.py
   │     │  ├─ merge
   │     │  │  ├─ base.py
   │     │  │  ├─ cmap.py
   │     │  │  ├─ layout.py
   │     │  │  ├─ options.py
   │     │  │  ├─ tables.py
   │     │  │  ├─ unicode.py
   │     │  │  ├─ util.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ misc
   │     │  │  ├─ arrayTools.py
   │     │  │  ├─ bezierTools.py
   │     │  │  ├─ classifyTools.py
   │     │  │  ├─ cliTools.py
   │     │  │  ├─ configTools.py
   │     │  │  ├─ cython.py
   │     │  │  ├─ dictTools.py
   │     │  │  ├─ eexec.py
   │     │  │  ├─ encodingTools.py
   │     │  │  ├─ enumTools.py
   │     │  │  ├─ etree.py
   │     │  │  ├─ filenames.py
   │     │  │  ├─ filesystem
   │     │  │  │  ├─ _base.py
   │     │  │  │  ├─ _copy.py
   │     │  │  │  ├─ _errors.py
   │     │  │  │  ├─ _info.py
   │     │  │  │  ├─ _osfs.py
   │     │  │  │  ├─ _path.py
   │     │  │  │  ├─ _subfs.py
   │     │  │  │  ├─ _tempfs.py
   │     │  │  │  ├─ _tools.py
   │     │  │  │  ├─ _walk.py
   │     │  │  │  ├─ _zipfs.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ fixedTools.py
   │     │  │  ├─ iftSparseBitSet.py
   │     │  │  ├─ intTools.py
   │     │  │  ├─ iterTools.py
   │     │  │  ├─ lazyTools.py
   │     │  │  ├─ loggingTools.py
   │     │  │  ├─ macCreatorType.py
   │     │  │  ├─ macRes.py
   │     │  │  ├─ plistlib
   │     │  │  │  ├─ py.typed
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ psCharStrings.py
   │     │  │  ├─ psLib.py
   │     │  │  ├─ psOperators.py
   │     │  │  ├─ py23.py
   │     │  │  ├─ roundTools.py
   │     │  │  ├─ sstruct.py
   │     │  │  ├─ symfont.py
   │     │  │  ├─ testTools.py
   │     │  │  ├─ textTools.py
   │     │  │  ├─ timeTools.py
   │     │  │  ├─ transform.py
   │     │  │  ├─ treeTools.py
   │     │  │  ├─ vector.py
   │     │  │  ├─ visitor.py
   │     │  │  ├─ xmlReader.py
   │     │  │  ├─ xmlWriter.py
   │     │  │  └─ __init__.py
   │     │  ├─ mtiLib
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ otlLib
   │     │  │  ├─ error.py
   │     │  │  ├─ maxContextCalc.py
   │     │  │  ├─ optimize
   │     │  │  │  ├─ gpos.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  └─ __init__.py
   │     │  ├─ pens
   │     │  │  ├─ areaPen.py
   │     │  │  ├─ basePen.py
   │     │  │  ├─ boundsPen.py
   │     │  │  ├─ cairoPen.py
   │     │  │  ├─ cocoaPen.py
   │     │  │  ├─ cu2quPen.py
   │     │  │  ├─ explicitClosingLinePen.py
   │     │  │  ├─ filterPen.py
   │     │  │  ├─ freetypePen.py
   │     │  │  ├─ hashPointPen.py
   │     │  │  ├─ momentsPen.py
   │     │  │  ├─ perimeterPen.py
   │     │  │  ├─ pointInsidePen.py
   │     │  │  ├─ pointPen.py
   │     │  │  ├─ qtPen.py
   │     │  │  ├─ qu2cuPen.py
   │     │  │  ├─ quartzPen.py
   │     │  │  ├─ recordingPen.py
   │     │  │  ├─ reportLabPen.py
   │     │  │  ├─ reverseContourPen.py
   │     │  │  ├─ roundingPen.py
   │     │  │  ├─ statisticsPen.py
   │     │  │  ├─ svgPathPen.py
   │     │  │  ├─ t2CharStringPen.py
   │     │  │  ├─ teePen.py
   │     │  │  ├─ transformPen.py
   │     │  │  ├─ ttGlyphPen.py
   │     │  │  ├─ wxPen.py
   │     │  │  └─ __init__.py
   │     │  ├─ qu2cu
   │     │  │  ├─ benchmark.py
   │     │  │  ├─ cli.py
   │     │  │  ├─ qu2cu.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ subset
   │     │  │  ├─ cff.py
   │     │  │  ├─ svg.py
   │     │  │  ├─ util.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ svgLib
   │     │  │  ├─ path
   │     │  │  │  ├─ arc.py
   │     │  │  │  ├─ parser.py
   │     │  │  │  ├─ shapes.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ t1Lib
   │     │  │  └─ __init__.py
   │     │  ├─ tfmLib.py
   │     │  ├─ ttLib
   │     │  │  ├─ macUtils.py
   │     │  │  ├─ removeOverlaps.py
   │     │  │  ├─ reorderGlyphs.py
   │     │  │  ├─ scaleUpem.py
   │     │  │  ├─ sfnt.py
   │     │  │  ├─ standardGlyphOrder.py
   │     │  │  ├─ tables
   │     │  │  │  ├─ asciiTable.py
   │     │  │  │  ├─ BitmapGlyphMetrics.py
   │     │  │  │  ├─ B_A_S_E_.py
   │     │  │  │  ├─ C_B_D_T_.py
   │     │  │  │  ├─ C_B_L_C_.py
   │     │  │  │  ├─ C_F_F_.py
   │     │  │  │  ├─ C_F_F__2.py
   │     │  │  │  ├─ C_O_L_R_.py
   │     │  │  │  ├─ C_P_A_L_.py
   │     │  │  │  ├─ DefaultTable.py
   │     │  │  │  ├─ D_S_I_G_.py
   │     │  │  │  ├─ D__e_b_g.py
   │     │  │  │  ├─ E_B_D_T_.py
   │     │  │  │  ├─ E_B_L_C_.py
   │     │  │  │  ├─ F_F_T_M_.py
   │     │  │  │  ├─ F__e_a_t.py
   │     │  │  │  ├─ grUtils.py
   │     │  │  │  ├─ G_D_E_F_.py
   │     │  │  │  ├─ G_P_O_S_.py
   │     │  │  │  ├─ G_S_U_B_.py
   │     │  │  │  ├─ G_V_A_R_.py
   │     │  │  │  ├─ G__l_a_t.py
   │     │  │  │  ├─ G__l_o_c.py
   │     │  │  │  ├─ H_V_A_R_.py
   │     │  │  │  ├─ I_F_T_.py
   │     │  │  │  ├─ I_F_T_X_.py
   │     │  │  │  ├─ J_S_T_F_.py
   │     │  │  │  ├─ L_T_S_H_.py
   │     │  │  │  ├─ M_A_T_H_.py
   │     │  │  │  ├─ M_V_A_R_.py
   │     │  │  │  ├─ otBase.py
   │     │  │  │  ├─ otConverters.py
   │     │  │  │  ├─ otData.py
   │     │  │  │  ├─ otDataSchema.py
   │     │  │  │  ├─ otTables.py
   │     │  │  │  ├─ otTraverse.py
   │     │  │  │  ├─ O_S_2f_2.py
   │     │  │  │  ├─ sbixGlyph.py
   │     │  │  │  ├─ sbixStrike.py
   │     │  │  │  ├─ S_T_A_T_.py
   │     │  │  │  ├─ S_V_G_.py
   │     │  │  │  ├─ S__i_l_f.py
   │     │  │  │  ├─ S__i_l_l.py
   │     │  │  │  ├─ table_API_readme.txt
   │     │  │  │  ├─ ttProgram.py
   │     │  │  │  ├─ TupleVariation.py
   │     │  │  │  ├─ T_S_I_B_.py
   │     │  │  │  ├─ T_S_I_C_.py
   │     │  │  │  ├─ T_S_I_D_.py
   │     │  │  │  ├─ T_S_I_J_.py
   │     │  │  │  ├─ T_S_I_P_.py
   │     │  │  │  ├─ T_S_I_S_.py
   │     │  │  │  ├─ T_S_I_V_.py
   │     │  │  │  ├─ T_S_I__0.py
   │     │  │  │  ├─ T_S_I__1.py
   │     │  │  │  ├─ T_S_I__2.py
   │     │  │  │  ├─ T_S_I__3.py
   │     │  │  │  ├─ T_S_I__5.py
   │     │  │  │  ├─ T_T_F_A_.py
   │     │  │  │  ├─ V_A_R_C_.py
   │     │  │  │  ├─ V_D_M_X_.py
   │     │  │  │  ├─ V_O_R_G_.py
   │     │  │  │  ├─ V_V_A_R_.py
   │     │  │  │  ├─ _a_n_k_r.py
   │     │  │  │  ├─ _a_v_a_r.py
   │     │  │  │  ├─ _b_g_c_l.py
   │     │  │  │  ├─ _b_s_l_n.py
   │     │  │  │  ├─ _c_i_d_g.py
   │     │  │  │  ├─ _c_m_a_p.py
   │     │  │  │  ├─ _c_v_a_r.py
   │     │  │  │  ├─ _c_v_t.py
   │     │  │  │  ├─ _f_e_a_t.py
   │     │  │  │  ├─ _f_p_g_m.py
   │     │  │  │  ├─ _f_v_a_r.py
   │     │  │  │  ├─ _g_a_s_p.py
   │     │  │  │  ├─ _g_c_i_d.py
   │     │  │  │  ├─ _g_l_y_f.py
   │     │  │  │  ├─ _g_v_a_r.py
   │     │  │  │  ├─ _h_d_m_x.py
   │     │  │  │  ├─ _h_e_a_d.py
   │     │  │  │  ├─ _h_h_e_a.py
   │     │  │  │  ├─ _h_m_t_x.py
   │     │  │  │  ├─ _k_e_r_n.py
   │     │  │  │  ├─ _l_c_a_r.py
   │     │  │  │  ├─ _l_o_c_a.py
   │     │  │  │  ├─ _l_t_a_g.py
   │     │  │  │  ├─ _m_a_x_p.py
   │     │  │  │  ├─ _m_e_t_a.py
   │     │  │  │  ├─ _m_o_r_t.py
   │     │  │  │  ├─ _m_o_r_x.py
   │     │  │  │  ├─ _n_a_m_e.py
   │     │  │  │  ├─ _o_p_b_d.py
   │     │  │  │  ├─ _p_o_s_t.py
   │     │  │  │  ├─ _p_r_e_p.py
   │     │  │  │  ├─ _p_r_o_p.py
   │     │  │  │  ├─ _s_b_i_x.py
   │     │  │  │  ├─ _t_r_a_k.py
   │     │  │  │  ├─ _v_h_e_a.py
   │     │  │  │  ├─ _v_m_t_x.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ttCollection.py
   │     │  │  ├─ ttFont.py
   │     │  │  ├─ ttGlyphSet.py
   │     │  │  ├─ ttVisitor.py
   │     │  │  ├─ woff2.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ ttx.py
   │     │  ├─ ufoLib
   │     │  │  ├─ converters.py
   │     │  │  ├─ errors.py
   │     │  │  ├─ etree.py
   │     │  │  ├─ filenames.py
   │     │  │  ├─ glifLib.py
   │     │  │  ├─ kerning.py
   │     │  │  ├─ plistlib.py
   │     │  │  ├─ pointPen.py
   │     │  │  ├─ utils.py
   │     │  │  ├─ validators.py
   │     │  │  └─ __init__.py
   │     │  ├─ unicode.py
   │     │  ├─ unicodedata
   │     │  │  ├─ Blocks.py
   │     │  │  ├─ Mirrored.py
   │     │  │  ├─ OTTags.py
   │     │  │  ├─ ScriptExtensions.py
   │     │  │  ├─ Scripts.py
   │     │  │  └─ __init__.py
   │     │  ├─ varLib
   │     │  │  ├─ avar
   │     │  │  │  ├─ map.py
   │     │  │  │  ├─ plan.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ avarPlanner.py
   │     │  │  ├─ cff.py
   │     │  │  ├─ errors.py
   │     │  │  ├─ featureVars.py
   │     │  │  ├─ hvar.py
   │     │  │  ├─ instancer
   │     │  │  │  ├─ featureVars.py
   │     │  │  │  ├─ names.py
   │     │  │  │  ├─ solver.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ interpolatable.py
   │     │  │  ├─ interpolatableHelpers.py
   │     │  │  ├─ interpolatablePlot.py
   │     │  │  ├─ interpolatableTestContourOrder.py
   │     │  │  ├─ interpolatableTestStartingPoint.py
   │     │  │  ├─ interpolate_layout.py
   │     │  │  ├─ iup.py
   │     │  │  ├─ merger.py
   │     │  │  ├─ models.py
   │     │  │  ├─ multiVarStore.py
   │     │  │  ├─ mutator.py
   │     │  │  ├─ mvar.py
   │     │  │  ├─ plot.py
   │     │  │  ├─ stat.py
   │     │  │  ├─ varStore.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ voltLib
   │     │  │  ├─ ast.py
   │     │  │  ├─ error.py
   │     │  │  ├─ lexer.py
   │     │  │  ├─ parser.py
   │     │  │  ├─ voltToFea.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ fonttools-4.63.0.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ LICENSE
   │     │  │  └─ LICENSE.external
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ gast
   │     │  ├─ ast2.py
   │     │  ├─ ast3.py
   │     │  ├─ astn.py
   │     │  ├─ gast.py
   │     │  ├─ unparser.py
   │     │  ├─ version.py
   │     │  └─ __init__.py
   │     ├─ gast-0.7.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ google
   │     │  ├─ protobuf
   │     │  │  ├─ any_pb2.py
   │     │  │  ├─ api_pb2.py
   │     │  │  ├─ compiler
   │     │  │  │  ├─ plugin_pb2.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ descriptor.py
   │     │  │  ├─ descriptor_database.py
   │     │  │  ├─ descriptor_pb2.py
   │     │  │  ├─ descriptor_pool.py
   │     │  │  ├─ duration_pb2.py
   │     │  │  ├─ empty_pb2.py
   │     │  │  ├─ field_mask_pb2.py
   │     │  │  ├─ internal
   │     │  │  │  ├─ api_implementation.py
   │     │  │  │  ├─ containers.py
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  ├─ enum_type_wrapper.py
   │     │  │  │  ├─ extension_dict.py
   │     │  │  │  ├─ field_mask.py
   │     │  │  │  ├─ message_listener.py
   │     │  │  │  ├─ python_edition_defaults.py
   │     │  │  │  ├─ python_message.py
   │     │  │  │  ├─ testing_refleaks.py
   │     │  │  │  ├─ type_checkers.py
   │     │  │  │  ├─ well_known_types.py
   │     │  │  │  ├─ wire_format.py
   │     │  │  │  ├─ _parameterized.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ json_format.py
   │     │  │  ├─ message.py
   │     │  │  ├─ message_factory.py
   │     │  │  ├─ pyext
   │     │  │  │  ├─ cpp_message.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ reflection.py
   │     │  │  ├─ service.py
   │     │  │  ├─ service_reflection.py
   │     │  │  ├─ source_context_pb2.py
   │     │  │  ├─ struct_pb2.py
   │     │  │  ├─ symbol_database.py
   │     │  │  ├─ testdata
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ text_encoding.py
   │     │  │  ├─ text_format.py
   │     │  │  ├─ timestamp_pb2.py
   │     │  │  ├─ type_pb2.py
   │     │  │  ├─ unknown_fields.py
   │     │  │  ├─ util
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ wrappers_pb2.py
   │     │  │  └─ __init__.py
   │     │  └─ _upb
   │     ├─ google_pasta-0.2.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ grpc
   │     │  ├─ aio
   │     │  │  ├─ _base_call.py
   │     │  │  ├─ _base_channel.py
   │     │  │  ├─ _base_server.py
   │     │  │  ├─ _call.py
   │     │  │  ├─ _channel.py
   │     │  │  ├─ _interceptor.py
   │     │  │  ├─ _metadata.py
   │     │  │  ├─ _server.py
   │     │  │  ├─ _typing.py
   │     │  │  ├─ _utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ beta
   │     │  │  ├─ implementations.py
   │     │  │  ├─ interfaces.py
   │     │  │  ├─ utilities.py
   │     │  │  ├─ _client_adaptations.py
   │     │  │  ├─ _metadata.py
   │     │  │  ├─ _server_adaptations.py
   │     │  │  └─ __init__.py
   │     │  ├─ experimental
   │     │  │  ├─ aio
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ gevent.py
   │     │  │  ├─ session_cache.py
   │     │  │  └─ __init__.py
   │     │  ├─ framework
   │     │  │  ├─ common
   │     │  │  │  ├─ cardinality.py
   │     │  │  │  ├─ style.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ foundation
   │     │  │  │  ├─ abandonment.py
   │     │  │  │  ├─ callable_util.py
   │     │  │  │  ├─ future.py
   │     │  │  │  ├─ logging_pool.py
   │     │  │  │  ├─ stream.py
   │     │  │  │  ├─ stream_util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ interfaces
   │     │  │  │  ├─ base
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ utilities.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ face
   │     │  │  │  │  ├─ face.py
   │     │  │  │  │  ├─ utilities.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ _auth.py
   │     │  ├─ _channel.py
   │     │  ├─ _common.py
   │     │  ├─ _compression.py
   │     │  ├─ _cython
   │     │  │  ├─ cygrpc.pyi
   │     │  │  ├─ _credentials
   │     │  │  │  └─ roots.pem
   │     │  │  ├─ _cygrpc
   │     │  │  │  ├─ private_key_signing
   │     │  │  │  │  ├─ private_key_signer_py_wrapper.cc
   │     │  │  │  │  └─ private_key_signer_py_wrapper.h
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ _grpcio_metadata.py
   │     │  ├─ _interceptor.py
   │     │  ├─ _observability.py
   │     │  ├─ _plugin_wrapping.py
   │     │  ├─ _runtime_protos.py
   │     │  ├─ _server.py
   │     │  ├─ _simple_stubs.py
   │     │  ├─ _typing.py
   │     │  ├─ _utilities.py
   │     │  └─ __init__.py
   │     ├─ grpcio-1.83.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ h5py
   │     │  ├─ h5py_warnings.py
   │     │  ├─ hdf5.dll
   │     │  ├─ hdf5_hl.dll
   │     │  ├─ ipy_completer.py
   │     │  ├─ tests
   │     │  │  ├─ common.py
   │     │  │  ├─ conftest.py
   │     │  │  ├─ data_files
   │     │  │  │  ├─ vlen_string_dset.h5
   │     │  │  │  ├─ vlen_string_dset_utc.h5
   │     │  │  │  ├─ vlen_string_s390x.h5
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ test_attribute_create.py
   │     │  │  ├─ test_attrs.py
   │     │  │  ├─ test_attrs_data.py
   │     │  │  ├─ test_base.py
   │     │  │  ├─ test_big_endian_file.py
   │     │  │  ├─ test_completions.py
   │     │  │  ├─ test_dataset.py
   │     │  │  ├─ test_dataset_getitem.py
   │     │  │  ├─ test_dataset_swmr.py
   │     │  │  ├─ test_datatype.py
   │     │  │  ├─ test_dimension_scales.py
   │     │  │  ├─ test_dims_dimensionproxy.py
   │     │  │  ├─ test_dtype.py
   │     │  │  ├─ test_errors.py
   │     │  │  ├─ test_file.py
   │     │  │  ├─ test_file2.py
   │     │  │  ├─ test_file_alignment.py
   │     │  │  ├─ test_file_image.py
   │     │  │  ├─ test_filters.py
   │     │  │  ├─ test_group.py
   │     │  │  ├─ test_h5.py
   │     │  │  ├─ test_h5d_direct_chunk.py
   │     │  │  ├─ test_h5f.py
   │     │  │  ├─ test_h5o.py
   │     │  │  ├─ test_h5p.py
   │     │  │  ├─ test_h5pl.py
   │     │  │  ├─ test_h5s.py
   │     │  │  ├─ test_h5t.py
   │     │  │  ├─ test_h5z.py
   │     │  │  ├─ test_npystrings.py
   │     │  │  ├─ test_objects.py
   │     │  │  ├─ test_ros3.py
   │     │  │  ├─ test_selections.py
   │     │  │  ├─ test_slicing.py
   │     │  │  ├─ test_vds
   │     │  │  │  ├─ test_highlevel_vds.py
   │     │  │  │  ├─ test_lowlevel_vds.py
   │     │  │  │  ├─ test_virtual_source.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ version.py
   │     │  ├─ zlib.dll
   │     │  ├─ _hl
   │     │  │  ├─ attrs.py
   │     │  │  ├─ base.py
   │     │  │  ├─ compat.py
   │     │  │  ├─ dataset.py
   │     │  │  ├─ datatype.py
   │     │  │  ├─ dims.py
   │     │  │  ├─ files.py
   │     │  │  ├─ filters.py
   │     │  │  ├─ group.py
   │     │  │  ├─ selections.py
   │     │  │  ├─ selections2.py
   │     │  │  ├─ vds.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ h5py-3.14.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ LICENSE
   │     │  │  ├─ licenses
   │     │  │  │  ├─ hdf5.txt
   │     │  │  │  ├─ license.txt
   │     │  │  │  ├─ pytables.txt
   │     │  │  │  ├─ python.txt
   │     │  │  │  └─ stdint.txt
   │     │  │  └─ lzf
   │     │  │     └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ highspy
   │     │  ├─ highs.py
   │     │  ├─ py.typed
   │     │  ├─ _core
   │     │  │  ├─ cb.pyi
   │     │  │  ├─ simplex_constants.pyi
   │     │  │  └─ __init__.pyi
   │     │  ├─ __init__.py
   │     │  └─ __init__.pyi
   │     ├─ highspy-1.15.1.dist-info
   │     │  ├─ DELVEWHEEL
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ LICENSE.txt
   │     │  │  └─ THIRD_PARTY_NOTICES.md
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ highspy.libs
   │     │  └─ msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
   │     ├─ idna
   │     │  ├─ cli.py
   │     │  ├─ codec.py
   │     │  ├─ compat.py
   │     │  ├─ core.py
   │     │  ├─ idnadata.py
   │     │  ├─ intranges.py
   │     │  ├─ package_data.py
   │     │  ├─ py.typed
   │     │  ├─ uts46data.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ idna-3.19.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.md
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ immutabledict
   │     │  ├─ py.typed
   │     │  └─ __init__.py
   │     ├─ immutabledict-4.3.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ iniconfig
   │     │  ├─ exceptions.py
   │     │  ├─ py.typed
   │     │  ├─ _parse.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ iniconfig-2.3.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ jinja2
   │     │  ├─ async_utils.py
   │     │  ├─ bccache.py
   │     │  ├─ compiler.py
   │     │  ├─ constants.py
   │     │  ├─ debug.py
   │     │  ├─ defaults.py
   │     │  ├─ environment.py
   │     │  ├─ exceptions.py
   │     │  ├─ ext.py
   │     │  ├─ filters.py
   │     │  ├─ idtracking.py
   │     │  ├─ lexer.py
   │     │  ├─ loaders.py
   │     │  ├─ meta.py
   │     │  ├─ nativetypes.py
   │     │  ├─ nodes.py
   │     │  ├─ optimizer.py
   │     │  ├─ parser.py
   │     │  ├─ py.typed
   │     │  ├─ runtime.py
   │     │  ├─ sandbox.py
   │     │  ├─ tests.py
   │     │  ├─ utils.py
   │     │  ├─ visitor.py
   │     │  ├─ _identifier.py
   │     │  └─ __init__.py
   │     ├─ jinja2-3.1.6.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ joblib
   │     │  ├─ backports.py
   │     │  ├─ compressor.py
   │     │  ├─ disk.py
   │     │  ├─ executor.py
   │     │  ├─ externals
   │     │  │  ├─ cloudpickle
   │     │  │  │  ├─ cloudpickle.py
   │     │  │  │  ├─ cloudpickle_fast.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ loky
   │     │  │  │  ├─ backend
   │     │  │  │  │  ├─ context.py
   │     │  │  │  │  ├─ fork_exec.py
   │     │  │  │  │  ├─ popen_loky_posix.py
   │     │  │  │  │  ├─ popen_loky_win32.py
   │     │  │  │  │  ├─ process.py
   │     │  │  │  │  ├─ queues.py
   │     │  │  │  │  ├─ reduction.py
   │     │  │  │  │  ├─ resource_tracker.py
   │     │  │  │  │  ├─ spawn.py
   │     │  │  │  │  ├─ synchronize.py
   │     │  │  │  │  ├─ utils.py
   │     │  │  │  │  ├─ _posix_reduction.py
   │     │  │  │  │  ├─ _win_reduction.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ cloudpickle_wrapper.py
   │     │  │  │  ├─ initializers.py
   │     │  │  │  ├─ process_executor.py
   │     │  │  │  ├─ reusable_executor.py
   │     │  │  │  ├─ _base.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ func_inspect.py
   │     │  ├─ hashing.py
   │     │  ├─ logger.py
   │     │  ├─ memory.py
   │     │  ├─ numpy_pickle.py
   │     │  ├─ numpy_pickle_compat.py
   │     │  ├─ numpy_pickle_utils.py
   │     │  ├─ parallel.py
   │     │  ├─ pool.py
   │     │  ├─ test
   │     │  │  ├─ common.py
   │     │  │  ├─ data
   │     │  │  │  ├─ create_numpy_pickle.py
   │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py27_np16.gz
   │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py27_np17.gz
   │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py33_np18.gz
   │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py34_np19.gz
   │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py35_np19.gz
   │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl
   │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.bz2
   │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.gzip
   │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.lzma
   │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.xz
   │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl
   │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.bz2
   │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.gzip
   │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.lzma
   │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.xz
   │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl
   │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.bz2
   │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.gzip
   │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.lzma
   │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.xz
   │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl
   │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.bz2
   │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.gzip
   │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.lzma
   │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.xz
   │     │  │  │  ├─ joblib_0.11.0_compressed_pickle_py36_np111.gz
   │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl
   │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.bz2
   │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.gzip
   │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.lzma
   │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.xz
   │     │  │  │  ├─ joblib_0.8.4_compressed_pickle_py27_np17.gz
   │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py27_np16.gz
   │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py27_np17.gz
   │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py34_np19.gz
   │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py35_np19.gz
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_01.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_02.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_03.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_04.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_01.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_02.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_03.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_04.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl
   │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_01.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_02.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_03.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_04.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl
   │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_01.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_02.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_03.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_04.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl
   │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_01.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_02.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_03.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_04.npy
   │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz
   │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_01.npy.z
   │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_02.npy.z
   │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_03.npy.z
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ testutils.py
   │     │  │  ├─ test_backports.py
   │     │  │  ├─ test_cloudpickle_wrapper.py
   │     │  │  ├─ test_config.py
   │     │  │  ├─ test_dask.py
   │     │  │  ├─ test_disk.py
   │     │  │  ├─ test_func_inspect.py
   │     │  │  ├─ test_func_inspect_special_encoding.py
   │     │  │  ├─ test_hashing.py
   │     │  │  ├─ test_init.py
   │     │  │  ├─ test_logger.py
   │     │  │  ├─ test_memmapping.py
   │     │  │  ├─ test_memory.py
   │     │  │  ├─ test_memory_async.py
   │     │  │  ├─ test_missing_multiprocessing.py
   │     │  │  ├─ test_module.py
   │     │  │  ├─ test_numpy_pickle.py
   │     │  │  ├─ test_numpy_pickle_compat.py
   │     │  │  ├─ test_numpy_pickle_utils.py
   │     │  │  ├─ test_parallel.py
   │     │  │  ├─ test_store_backends.py
   │     │  │  ├─ test_testing.py
   │     │  │  ├─ test_utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ testing.py
   │     │  ├─ _cloudpickle_wrapper.py
   │     │  ├─ _dask.py
   │     │  ├─ _memmapping_reducer.py
   │     │  ├─ _multiprocessing_helpers.py
   │     │  ├─ _parallel_backends.py
   │     │  ├─ _store_backends.py
   │     │  ├─ _utils.py
   │     │  └─ __init__.py
   │     ├─ joblib-1.5.3.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ keras
   │     │  ├─ activations
   │     │  │  └─ __init__.py
   │     │  ├─ applications
   │     │  │  ├─ convnext
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ densenet
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ efficientnet
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ efficientnet_v2
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ imagenet_utils
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ inception_resnet_v2
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ inception_v3
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mobilenet
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mobilenet_v2
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mobilenet_v3
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ nasnet
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ resnet
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ resnet50
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ resnet_v2
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vgg16
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vgg19
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ xception
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ backend
   │     │  │  └─ __init__.py
   │     │  ├─ callbacks
   │     │  │  └─ __init__.py
   │     │  ├─ config
   │     │  │  └─ __init__.py
   │     │  ├─ constraints
   │     │  │  └─ __init__.py
   │     │  ├─ datasets
   │     │  │  ├─ boston_housing
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ california_housing
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cifar10
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cifar100
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ fashion_mnist
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ imdb
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mnist
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ reuters
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ distillation
   │     │  │  └─ __init__.py
   │     │  ├─ distribution
   │     │  │  └─ __init__.py
   │     │  ├─ dtype_policies
   │     │  │  └─ __init__.py
   │     │  ├─ export
   │     │  │  └─ __init__.py
   │     │  ├─ initializers
   │     │  │  └─ __init__.py
   │     │  ├─ layers
   │     │  │  └─ __init__.py
   │     │  ├─ legacy
   │     │  │  ├─ saving
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ losses
   │     │  │  └─ __init__.py
   │     │  ├─ metrics
   │     │  │  └─ __init__.py
   │     │  ├─ mixed_precision
   │     │  │  └─ __init__.py
   │     │  ├─ models
   │     │  │  └─ __init__.py
   │     │  ├─ ops
   │     │  │  ├─ image
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ linalg
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ nn
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ numpy
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ optimizers
   │     │  │  ├─ legacy
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ schedules
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ preprocessing
   │     │  │  ├─ image
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sequence
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ quantizers
   │     │  │  └─ __init__.py
   │     │  ├─ random
   │     │  │  └─ __init__.py
   │     │  ├─ regularizers
   │     │  │  └─ __init__.py
   │     │  ├─ saving
   │     │  │  └─ __init__.py
   │     │  ├─ src
   │     │  │  ├─ activations
   │     │  │  │  ├─ activations.py
   │     │  │  │  ├─ activations_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ api_export.py
   │     │  │  ├─ applications
   │     │  │  │  ├─ applications_test.py
   │     │  │  │  ├─ convnext.py
   │     │  │  │  ├─ densenet.py
   │     │  │  │  ├─ efficientnet.py
   │     │  │  │  ├─ efficientnet_v2.py
   │     │  │  │  ├─ imagenet_utils.py
   │     │  │  │  ├─ imagenet_utils_test.py
   │     │  │  │  ├─ inception_resnet_v2.py
   │     │  │  │  ├─ inception_v3.py
   │     │  │  │  ├─ mobilenet.py
   │     │  │  │  ├─ mobilenet_v2.py
   │     │  │  │  ├─ mobilenet_v3.py
   │     │  │  │  ├─ nasnet.py
   │     │  │  │  ├─ resnet.py
   │     │  │  │  ├─ resnet_v2.py
   │     │  │  │  ├─ vgg16.py
   │     │  │  │  ├─ vgg19.py
   │     │  │  │  ├─ xception.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ backend
   │     │  │  │  ├─ common
   │     │  │  │  │  ├─ backend_utils.py
   │     │  │  │  │  ├─ backend_utils_test.py
   │     │  │  │  │  ├─ compute_output_spec_test.py
   │     │  │  │  │  ├─ dtypes.py
   │     │  │  │  │  ├─ dtypes_test.py
   │     │  │  │  │  ├─ global_state.py
   │     │  │  │  │  ├─ global_state_test.py
   │     │  │  │  │  ├─ keras_tensor.py
   │     │  │  │  │  ├─ keras_tensor_test.py
   │     │  │  │  │  ├─ masking.py
   │     │  │  │  │  ├─ masking_test.py
   │     │  │  │  │  ├─ name_scope.py
   │     │  │  │  │  ├─ name_scope_test.py
   │     │  │  │  │  ├─ remat.py
   │     │  │  │  │  ├─ remat_test.py
   │     │  │  │  │  ├─ stateless_scope.py
   │     │  │  │  │  ├─ stateless_scope_test.py
   │     │  │  │  │  ├─ symbolic_scope.py
   │     │  │  │  │  ├─ symbolic_scope_test.py
   │     │  │  │  │  ├─ tensor_attributes.py
   │     │  │  │  │  ├─ thread_safe_test.py
   │     │  │  │  │  ├─ variables.py
   │     │  │  │  │  ├─ variables_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ jax
   │     │  │  │  │  ├─ core.py
   │     │  │  │  │  ├─ core_test.py
   │     │  │  │  │  ├─ distribution_lib.py
   │     │  │  │  │  ├─ distribution_lib_test.py
   │     │  │  │  │  ├─ export.py
   │     │  │  │  │  ├─ image.py
   │     │  │  │  │  ├─ jax_multi_process_distribution_test.py
   │     │  │  │  │  ├─ layer.py
   │     │  │  │  │  ├─ linalg.py
   │     │  │  │  │  ├─ math.py
   │     │  │  │  │  ├─ nn.py
   │     │  │  │  │  ├─ numpy.py
   │     │  │  │  │  ├─ optimizer.py
   │     │  │  │  │  ├─ random.py
   │     │  │  │  │  ├─ rnn.py
   │     │  │  │  │  ├─ sparse.py
   │     │  │  │  │  ├─ tensorboard.py
   │     │  │  │  │  ├─ trainer.py
   │     │  │  │  │  ├─ trainer_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ numpy
   │     │  │  │  │  ├─ core.py
   │     │  │  │  │  ├─ export.py
   │     │  │  │  │  ├─ image.py
   │     │  │  │  │  ├─ layer.py
   │     │  │  │  │  ├─ linalg.py
   │     │  │  │  │  ├─ math.py
   │     │  │  │  │  ├─ nn.py
   │     │  │  │  │  ├─ numpy.py
   │     │  │  │  │  ├─ random.py
   │     │  │  │  │  ├─ rnn.py
   │     │  │  │  │  ├─ trainer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ openvino
   │     │  │  │  │  ├─ core.py
   │     │  │  │  │  ├─ export.py
   │     │  │  │  │  ├─ image.py
   │     │  │  │  │  ├─ layer.py
   │     │  │  │  │  ├─ linalg.py
   │     │  │  │  │  ├─ math.py
   │     │  │  │  │  ├─ nn.py
   │     │  │  │  │  ├─ numpy.py
   │     │  │  │  │  ├─ random.py
   │     │  │  │  │  ├─ rnn.py
   │     │  │  │  │  ├─ trainer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tensorflow
   │     │  │  │  │  ├─ core.py
   │     │  │  │  │  ├─ distribute_test.py
   │     │  │  │  │  ├─ distribution_lib.py
   │     │  │  │  │  ├─ export.py
   │     │  │  │  │  ├─ image.py
   │     │  │  │  │  ├─ layer.py
   │     │  │  │  │  ├─ linalg.py
   │     │  │  │  │  ├─ math.py
   │     │  │  │  │  ├─ name_scope_test.py
   │     │  │  │  │  ├─ nn.py
   │     │  │  │  │  ├─ numpy.py
   │     │  │  │  │  ├─ optimizer.py
   │     │  │  │  │  ├─ optimizer_distribute_test.py
   │     │  │  │  │  ├─ random.py
   │     │  │  │  │  ├─ rnn.py
   │     │  │  │  │  ├─ saved_model_test.py
   │     │  │  │  │  ├─ sparse.py
   │     │  │  │  │  ├─ tensorboard.py
   │     │  │  │  │  ├─ trackable.py
   │     │  │  │  │  ├─ trainer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ compute_output_spec_test.py
   │     │  │  │  │  └─ device_scope_test.py
   │     │  │  │  ├─ torch
   │     │  │  │  │  ├─ core.py
   │     │  │  │  │  ├─ core_test.py
   │     │  │  │  │  ├─ export.py
   │     │  │  │  │  ├─ image.py
   │     │  │  │  │  ├─ layer.py
   │     │  │  │  │  ├─ linalg.py
   │     │  │  │  │  ├─ math.py
   │     │  │  │  │  ├─ nn.py
   │     │  │  │  │  ├─ numpy.py
   │     │  │  │  │  ├─ optimizers
   │     │  │  │  │  │  ├─ torch_adadelta.py
   │     │  │  │  │  │  ├─ torch_adagrad.py
   │     │  │  │  │  │  ├─ torch_adam.py
   │     │  │  │  │  │  ├─ torch_adamax.py
   │     │  │  │  │  │  ├─ torch_adamw.py
   │     │  │  │  │  │  ├─ torch_lion.py
   │     │  │  │  │  │  ├─ torch_nadam.py
   │     │  │  │  │  │  ├─ torch_optimizer.py
   │     │  │  │  │  │  ├─ torch_parallel_optimizer.py
   │     │  │  │  │  │  ├─ torch_rmsprop.py
   │     │  │  │  │  │  ├─ torch_sgd.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ random.py
   │     │  │  │  │  ├─ rnn.py
   │     │  │  │  │  ├─ trainer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ callbacks
   │     │  │  │  ├─ backup_and_restore.py
   │     │  │  │  ├─ backup_and_restore_test.py
   │     │  │  │  ├─ callback.py
   │     │  │  │  ├─ callback_list.py
   │     │  │  │  ├─ callback_test.py
   │     │  │  │  ├─ csv_logger.py
   │     │  │  │  ├─ csv_logger_test.py
   │     │  │  │  ├─ early_stopping.py
   │     │  │  │  ├─ early_stopping_test.py
   │     │  │  │  ├─ history.py
   │     │  │  │  ├─ lambda_callback.py
   │     │  │  │  ├─ lambda_callback_test.py
   │     │  │  │  ├─ learning_rate_scheduler.py
   │     │  │  │  ├─ learning_rate_scheduler_test.py
   │     │  │  │  ├─ model_checkpoint.py
   │     │  │  │  ├─ model_checkpoint_test.py
   │     │  │  │  ├─ monitor_callback.py
   │     │  │  │  ├─ monitor_callback_test.py
   │     │  │  │  ├─ orbax_checkpoint.py
   │     │  │  │  ├─ orbax_checkpoint_test.py
   │     │  │  │  ├─ progbar_logger.py
   │     │  │  │  ├─ reduce_lr_on_plateau.py
   │     │  │  │  ├─ reduce_lr_on_plateau_test.py
   │     │  │  │  ├─ remote_monitor.py
   │     │  │  │  ├─ remote_monitor_test.py
   │     │  │  │  ├─ swap_ema_weights.py
   │     │  │  │  ├─ swap_ema_weights_test.py
   │     │  │  │  ├─ tensorboard.py
   │     │  │  │  ├─ tensorboard_test.py
   │     │  │  │  ├─ terminate_on_nan.py
   │     │  │  │  ├─ terminate_on_nan_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ constraints
   │     │  │  │  ├─ constraints.py
   │     │  │  │  ├─ constraints_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ datasets
   │     │  │  │  ├─ boston_housing.py
   │     │  │  │  ├─ california_housing.py
   │     │  │  │  ├─ cifar.py
   │     │  │  │  ├─ cifar10.py
   │     │  │  │  ├─ cifar100.py
   │     │  │  │  ├─ fashion_mnist.py
   │     │  │  │  ├─ imdb.py
   │     │  │  │  ├─ mnist.py
   │     │  │  │  ├─ npz_utils.py
   │     │  │  │  ├─ npz_utils_test.py
   │     │  │  │  ├─ reuters.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ distillation
   │     │  │  │  ├─ distillation_loss.py
   │     │  │  │  ├─ distillation_loss_test.py
   │     │  │  │  ├─ distiller.py
   │     │  │  │  ├─ distiller_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ distribution
   │     │  │  │  ├─ distribution_lib.py
   │     │  │  │  ├─ distribution_lib_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ dtype_policies
   │     │  │  │  ├─ dtype_policy.py
   │     │  │  │  ├─ dtype_policy_map.py
   │     │  │  │  ├─ dtype_policy_map_test.py
   │     │  │  │  ├─ dtype_policy_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ export
   │     │  │  │  ├─ export_utils.py
   │     │  │  │  ├─ litert.py
   │     │  │  │  ├─ litert_test.py
   │     │  │  │  ├─ litert_torch_test.py
   │     │  │  │  ├─ neptune_model_export_archive.py
   │     │  │  │  ├─ onnx.py
   │     │  │  │  ├─ onnx_test.py
   │     │  │  │  ├─ openvino.py
   │     │  │  │  ├─ openvino_test.py
   │     │  │  │  ├─ saved_model.py
   │     │  │  │  ├─ saved_model_export_archive.py
   │     │  │  │  ├─ saved_model_test.py
   │     │  │  │  ├─ tf2onnx_lib.py
   │     │  │  │  ├─ tfsm_layer.py
   │     │  │  │  ├─ tfsm_layer_test.py
   │     │  │  │  ├─ torch.py
   │     │  │  │  ├─ torch_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ initializers
   │     │  │  │  ├─ constant_initializers.py
   │     │  │  │  ├─ constant_initializers_test.py
   │     │  │  │  ├─ initializer.py
   │     │  │  │  ├─ initializer_test.py
   │     │  │  │  ├─ random_initializers.py
   │     │  │  │  ├─ random_initializers_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ layers
   │     │  │  │  ├─ activations
   │     │  │  │  │  ├─ activation.py
   │     │  │  │  │  ├─ activation_test.py
   │     │  │  │  │  ├─ elu.py
   │     │  │  │  │  ├─ elu_test.py
   │     │  │  │  │  ├─ leaky_relu.py
   │     │  │  │  │  ├─ leaky_relu_test.py
   │     │  │  │  │  ├─ prelu.py
   │     │  │  │  │  ├─ prelu_test.py
   │     │  │  │  │  ├─ relu.py
   │     │  │  │  │  ├─ relu_test.py
   │     │  │  │  │  ├─ softmax.py
   │     │  │  │  │  ├─ softmax_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ attention
   │     │  │  │  │  ├─ additive_attention.py
   │     │  │  │  │  ├─ additive_attention_test.py
   │     │  │  │  │  ├─ attention.py
   │     │  │  │  │  ├─ attention_test.py
   │     │  │  │  │  ├─ grouped_query_attention.py
   │     │  │  │  │  ├─ grouped_query_attention_test.py
   │     │  │  │  │  ├─ multi_head_attention.py
   │     │  │  │  │  ├─ multi_head_attention_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ convolutional
   │     │  │  │  │  ├─ base_conv.py
   │     │  │  │  │  ├─ base_conv_transpose.py
   │     │  │  │  │  ├─ base_depthwise_conv.py
   │     │  │  │  │  ├─ base_separable_conv.py
   │     │  │  │  │  ├─ conv1d.py
   │     │  │  │  │  ├─ conv1d_transpose.py
   │     │  │  │  │  ├─ conv2d.py
   │     │  │  │  │  ├─ conv2d_transpose.py
   │     │  │  │  │  ├─ conv3d.py
   │     │  │  │  │  ├─ conv3d_transpose.py
   │     │  │  │  │  ├─ conv_test.py
   │     │  │  │  │  ├─ conv_transpose_test.py
   │     │  │  │  │  ├─ depthwise_conv1d.py
   │     │  │  │  │  ├─ depthwise_conv2d.py
   │     │  │  │  │  ├─ depthwise_conv_test.py
   │     │  │  │  │  ├─ separable_conv1d.py
   │     │  │  │  │  ├─ separable_conv2d.py
   │     │  │  │  │  ├─ separable_conv_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ core
   │     │  │  │  │  ├─ dense.py
   │     │  │  │  │  ├─ dense_test.py
   │     │  │  │  │  ├─ einsum_dense.py
   │     │  │  │  │  ├─ einsum_dense_test.py
   │     │  │  │  │  ├─ embedding.py
   │     │  │  │  │  ├─ embedding_test.py
   │     │  │  │  │  ├─ identity.py
   │     │  │  │  │  ├─ identity_test.py
   │     │  │  │  │  ├─ input_layer.py
   │     │  │  │  │  ├─ input_layer_test.py
   │     │  │  │  │  ├─ lambda_layer.py
   │     │  │  │  │  ├─ lambda_layer_test.py
   │     │  │  │  │  ├─ masking.py
   │     │  │  │  │  ├─ masking_test.py
   │     │  │  │  │  ├─ reversible_embedding.py
   │     │  │  │  │  ├─ reversible_embedding_test.py
   │     │  │  │  │  ├─ wrapper.py
   │     │  │  │  │  ├─ wrapper_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ input_spec.py
   │     │  │  │  ├─ layer.py
   │     │  │  │  ├─ layer_test.py
   │     │  │  │  ├─ merging
   │     │  │  │  │  ├─ add.py
   │     │  │  │  │  ├─ average.py
   │     │  │  │  │  ├─ base_merge.py
   │     │  │  │  │  ├─ concatenate.py
   │     │  │  │  │  ├─ dot.py
   │     │  │  │  │  ├─ maximum.py
   │     │  │  │  │  ├─ merging_test.py
   │     │  │  │  │  ├─ minimum.py
   │     │  │  │  │  ├─ multiply.py
   │     │  │  │  │  ├─ subtract.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ normalization
   │     │  │  │  │  ├─ batch_normalization.py
   │     │  │  │  │  ├─ batch_normalization_test.py
   │     │  │  │  │  ├─ group_normalization.py
   │     │  │  │  │  ├─ group_normalization_test.py
   │     │  │  │  │  ├─ layer_normalization.py
   │     │  │  │  │  ├─ layer_normalization_test.py
   │     │  │  │  │  ├─ rms_normalization.py
   │     │  │  │  │  ├─ rms_normalization_test.py
   │     │  │  │  │  ├─ spectral_normalization.py
   │     │  │  │  │  ├─ spectral_normalization_test.py
   │     │  │  │  │  ├─ unit_normalization.py
   │     │  │  │  │  ├─ unit_normalization_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ pooling
   │     │  │  │  │  ├─ adaptive_average_pooling1d.py
   │     │  │  │  │  ├─ adaptive_average_pooling2d.py
   │     │  │  │  │  ├─ adaptive_average_pooling3d.py
   │     │  │  │  │  ├─ adaptive_max_pooling1d.py
   │     │  │  │  │  ├─ adaptive_max_pooling2d.py
   │     │  │  │  │  ├─ adaptive_max_pooling3d.py
   │     │  │  │  │  ├─ adaptive_pooling1d_test.py
   │     │  │  │  │  ├─ adaptive_pooling2d_test.py
   │     │  │  │  │  ├─ adaptive_pooling3d_test.py
   │     │  │  │  │  ├─ average_pooling1d.py
   │     │  │  │  │  ├─ average_pooling2d.py
   │     │  │  │  │  ├─ average_pooling3d.py
   │     │  │  │  │  ├─ average_pooling_test.py
   │     │  │  │  │  ├─ base_adaptive_pooling.py
   │     │  │  │  │  ├─ base_global_pooling.py
   │     │  │  │  │  ├─ base_pooling.py
   │     │  │  │  │  ├─ global_average_pooling1d.py
   │     │  │  │  │  ├─ global_average_pooling2d.py
   │     │  │  │  │  ├─ global_average_pooling3d.py
   │     │  │  │  │  ├─ global_average_pooling_test.py
   │     │  │  │  │  ├─ global_max_pooling1d.py
   │     │  │  │  │  ├─ global_max_pooling2d.py
   │     │  │  │  │  ├─ global_max_pooling3d.py
   │     │  │  │  │  ├─ global_max_pooling_test.py
   │     │  │  │  │  ├─ max_pooling1d.py
   │     │  │  │  │  ├─ max_pooling2d.py
   │     │  │  │  │  ├─ max_pooling3d.py
   │     │  │  │  │  ├─ max_pooling_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ preprocessing
   │     │  │  │  │  ├─ category_encoding.py
   │     │  │  │  │  ├─ category_encoding_test.py
   │     │  │  │  │  ├─ data_layer.py
   │     │  │  │  │  ├─ data_layer_test.py
   │     │  │  │  │  ├─ discretization.py
   │     │  │  │  │  ├─ discretization_test.py
   │     │  │  │  │  ├─ feature_space.py
   │     │  │  │  │  ├─ feature_space_test.py
   │     │  │  │  │  ├─ hashed_crossing.py
   │     │  │  │  │  ├─ hashed_crossing_test.py
   │     │  │  │  │  ├─ hashing.py
   │     │  │  │  │  ├─ hashing_test.py
   │     │  │  │  │  ├─ image_preprocessing
   │     │  │  │  │  │  ├─ aug_mix.py
   │     │  │  │  │  │  ├─ aug_mix_test.py
   │     │  │  │  │  │  ├─ auto_contrast.py
   │     │  │  │  │  │  ├─ auto_contrast_test.py
   │     │  │  │  │  │  ├─ base_image_preprocessing_layer.py
   │     │  │  │  │  │  ├─ base_image_preprocessing_layer_test.py
   │     │  │  │  │  │  ├─ bounding_boxes
   │     │  │  │  │  │  │  ├─ bounding_box.py
   │     │  │  │  │  │  │  ├─ converters.py
   │     │  │  │  │  │  │  ├─ converters_test.py
   │     │  │  │  │  │  │  ├─ formats.py
   │     │  │  │  │  │  │  ├─ iou.py
   │     │  │  │  │  │  │  ├─ iou_test.py
   │     │  │  │  │  │  │  ├─ validation.py
   │     │  │  │  │  │  │  ├─ validation_test.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ center_crop.py
   │     │  │  │  │  │  ├─ center_crop_test.py
   │     │  │  │  │  │  ├─ clahe.py
   │     │  │  │  │  │  ├─ clahe_test.py
   │     │  │  │  │  │  ├─ cut_mix.py
   │     │  │  │  │  │  ├─ cut_mix_test.py
   │     │  │  │  │  │  ├─ equalization.py
   │     │  │  │  │  │  ├─ equalization_test.py
   │     │  │  │  │  │  ├─ max_num_bounding_box.py
   │     │  │  │  │  │  ├─ max_num_bounding_box_test.py
   │     │  │  │  │  │  ├─ mix_up.py
   │     │  │  │  │  │  ├─ mix_up_test.py
   │     │  │  │  │  │  ├─ random_brightness.py
   │     │  │  │  │  │  ├─ random_brightness_test.py
   │     │  │  │  │  │  ├─ random_color_degeneration.py
   │     │  │  │  │  │  ├─ random_color_degeneration_test.py
   │     │  │  │  │  │  ├─ random_color_jitter.py
   │     │  │  │  │  │  ├─ random_color_jitter_test.py
   │     │  │  │  │  │  ├─ random_contrast.py
   │     │  │  │  │  │  ├─ random_contrast_test.py
   │     │  │  │  │  │  ├─ random_crop.py
   │     │  │  │  │  │  ├─ random_crop_test.py
   │     │  │  │  │  │  ├─ random_elastic_transform.py
   │     │  │  │  │  │  ├─ random_elastic_transform_test.py
   │     │  │  │  │  │  ├─ random_erasing.py
   │     │  │  │  │  │  ├─ random_erasing_test.py
   │     │  │  │  │  │  ├─ random_flip.py
   │     │  │  │  │  │  ├─ random_flip_test.py
   │     │  │  │  │  │  ├─ random_gaussian_blur.py
   │     │  │  │  │  │  ├─ random_gaussian_blur_test.py
   │     │  │  │  │  │  ├─ random_grayscale.py
   │     │  │  │  │  │  ├─ random_grayscale_test.py
   │     │  │  │  │  │  ├─ random_hue.py
   │     │  │  │  │  │  ├─ random_hue_test.py
   │     │  │  │  │  │  ├─ random_invert.py
   │     │  │  │  │  │  ├─ random_invert_test.py
   │     │  │  │  │  │  ├─ random_perspective.py
   │     │  │  │  │  │  ├─ random_perspective_test.py
   │     │  │  │  │  │  ├─ random_posterization.py
   │     │  │  │  │  │  ├─ random_posterization_test.py
   │     │  │  │  │  │  ├─ random_rotation.py
   │     │  │  │  │  │  ├─ random_rotation_test.py
   │     │  │  │  │  │  ├─ random_saturation.py
   │     │  │  │  │  │  ├─ random_saturation_test.py
   │     │  │  │  │  │  ├─ random_sharpness.py
   │     │  │  │  │  │  ├─ random_sharpness_test.py
   │     │  │  │  │  │  ├─ random_shear.py
   │     │  │  │  │  │  ├─ random_shear_test.py
   │     │  │  │  │  │  ├─ random_translation.py
   │     │  │  │  │  │  ├─ random_translation_test.py
   │     │  │  │  │  │  ├─ random_zoom.py
   │     │  │  │  │  │  ├─ random_zoom_test.py
   │     │  │  │  │  │  ├─ rand_augment.py
   │     │  │  │  │  │  ├─ rand_augment_test.py
   │     │  │  │  │  │  ├─ resizing.py
   │     │  │  │  │  │  ├─ resizing_test.py
   │     │  │  │  │  │  ├─ solarization.py
   │     │  │  │  │  │  ├─ solarization_test.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ index_lookup.py
   │     │  │  │  │  ├─ index_lookup_test.py
   │     │  │  │  │  ├─ integer_lookup.py
   │     │  │  │  │  ├─ integer_lookup_test.py
   │     │  │  │  │  ├─ mel_spectrogram.py
   │     │  │  │  │  ├─ mel_spectrogram_test.py
   │     │  │  │  │  ├─ normalization.py
   │     │  │  │  │  ├─ normalization_test.py
   │     │  │  │  │  ├─ pipeline.py
   │     │  │  │  │  ├─ pipeline_test.py
   │     │  │  │  │  ├─ rescaling.py
   │     │  │  │  │  ├─ rescaling_test.py
   │     │  │  │  │  ├─ stft_spectrogram.py
   │     │  │  │  │  ├─ stft_spectrogram_test.py
   │     │  │  │  │  ├─ string_lookup.py
   │     │  │  │  │  ├─ string_lookup_test.py
   │     │  │  │  │  ├─ text_vectorization.py
   │     │  │  │  │  ├─ text_vectorization_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ regularization
   │     │  │  │  │  ├─ activity_regularization.py
   │     │  │  │  │  ├─ activity_regularization_test.py
   │     │  │  │  │  ├─ alpha_dropout.py
   │     │  │  │  │  ├─ alpha_dropout_test.py
   │     │  │  │  │  ├─ dropout.py
   │     │  │  │  │  ├─ dropout_test.py
   │     │  │  │  │  ├─ gaussian_dropout.py
   │     │  │  │  │  ├─ gaussian_dropout_test.py
   │     │  │  │  │  ├─ gaussian_noise.py
   │     │  │  │  │  ├─ gaussian_noise_test.py
   │     │  │  │  │  ├─ spatial_dropout.py
   │     │  │  │  │  ├─ spatial_dropout_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ reshaping
   │     │  │  │  │  ├─ cropping1d.py
   │     │  │  │  │  ├─ cropping1d_test.py
   │     │  │  │  │  ├─ cropping2d.py
   │     │  │  │  │  ├─ cropping2d_test.py
   │     │  │  │  │  ├─ cropping3d.py
   │     │  │  │  │  ├─ cropping3d_test.py
   │     │  │  │  │  ├─ flatten.py
   │     │  │  │  │  ├─ flatten_test.py
   │     │  │  │  │  ├─ permute.py
   │     │  │  │  │  ├─ permute_test.py
   │     │  │  │  │  ├─ repeat_vector.py
   │     │  │  │  │  ├─ repeat_vector_test.py
   │     │  │  │  │  ├─ reshape.py
   │     │  │  │  │  ├─ reshape_test.py
   │     │  │  │  │  ├─ up_sampling1d.py
   │     │  │  │  │  ├─ up_sampling1d_test.py
   │     │  │  │  │  ├─ up_sampling2d.py
   │     │  │  │  │  ├─ up_sampling2d_test.py
   │     │  │  │  │  ├─ up_sampling3d.py
   │     │  │  │  │  ├─ up_sampling3d_test.py
   │     │  │  │  │  ├─ zero_padding1d.py
   │     │  │  │  │  ├─ zero_padding1d_test.py
   │     │  │  │  │  ├─ zero_padding2d.py
   │     │  │  │  │  ├─ zero_padding2d_test.py
   │     │  │  │  │  ├─ zero_padding3d.py
   │     │  │  │  │  ├─ zero_padding3d_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ rnn
   │     │  │  │  │  ├─ bidirectional.py
   │     │  │  │  │  ├─ bidirectional_test.py
   │     │  │  │  │  ├─ conv_lstm.py
   │     │  │  │  │  ├─ conv_lstm1d.py
   │     │  │  │  │  ├─ conv_lstm1d_test.py
   │     │  │  │  │  ├─ conv_lstm2d.py
   │     │  │  │  │  ├─ conv_lstm2d_test.py
   │     │  │  │  │  ├─ conv_lstm3d.py
   │     │  │  │  │  ├─ conv_lstm3d_test.py
   │     │  │  │  │  ├─ conv_lstm_test.py
   │     │  │  │  │  ├─ dropout_rnn_cell.py
   │     │  │  │  │  ├─ dropout_rnn_cell_test.py
   │     │  │  │  │  ├─ gru.py
   │     │  │  │  │  ├─ gru_test.py
   │     │  │  │  │  ├─ lstm.py
   │     │  │  │  │  ├─ lstm_test.py
   │     │  │  │  │  ├─ rnn.py
   │     │  │  │  │  ├─ rnn_test.py
   │     │  │  │  │  ├─ simple_rnn.py
   │     │  │  │  │  ├─ simple_rnn_test.py
   │     │  │  │  │  ├─ stacked_rnn_cells.py
   │     │  │  │  │  ├─ stacked_rnn_cells_test.py
   │     │  │  │  │  ├─ time_distributed.py
   │     │  │  │  │  ├─ time_distributed_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ legacy
   │     │  │  │  ├─ backend.py
   │     │  │  │  ├─ layers.py
   │     │  │  │  ├─ losses.py
   │     │  │  │  ├─ preprocessing
   │     │  │  │  │  ├─ image.py
   │     │  │  │  │  ├─ sequence.py
   │     │  │  │  │  ├─ text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ saving
   │     │  │  │  │  ├─ json_utils.py
   │     │  │  │  │  ├─ json_utils_test.py
   │     │  │  │  │  ├─ legacy_h5_format.py
   │     │  │  │  │  ├─ legacy_h5_format_test.py
   │     │  │  │  │  ├─ saving_options.py
   │     │  │  │  │  ├─ saving_utils.py
   │     │  │  │  │  ├─ serialization.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ losses
   │     │  │  │  ├─ loss.py
   │     │  │  │  ├─ losses.py
   │     │  │  │  ├─ losses_test.py
   │     │  │  │  ├─ loss_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ metrics
   │     │  │  │  ├─ accuracy_metrics.py
   │     │  │  │  ├─ accuracy_metrics_test.py
   │     │  │  │  ├─ confusion_metrics.py
   │     │  │  │  ├─ confusion_metrics_test.py
   │     │  │  │  ├─ correlation_metrics.py
   │     │  │  │  ├─ correlation_metrics_test.py
   │     │  │  │  ├─ f_score_metrics.py
   │     │  │  │  ├─ f_score_metrics_test.py
   │     │  │  │  ├─ hinge_metrics.py
   │     │  │  │  ├─ hinge_metrics_test.py
   │     │  │  │  ├─ iou_metrics.py
   │     │  │  │  ├─ iou_metrics_test.py
   │     │  │  │  ├─ metric.py
   │     │  │  │  ├─ metrics_utils.py
   │     │  │  │  ├─ metric_test.py
   │     │  │  │  ├─ probabilistic_metrics.py
   │     │  │  │  ├─ probabilistic_metrics_test.py
   │     │  │  │  ├─ reduction_metrics.py
   │     │  │  │  ├─ reduction_metrics_test.py
   │     │  │  │  ├─ regression_metrics.py
   │     │  │  │  ├─ regression_metrics_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ models
   │     │  │  │  ├─ cloning.py
   │     │  │  │  ├─ cloning_test.py
   │     │  │  │  ├─ functional.py
   │     │  │  │  ├─ functional_test.py
   │     │  │  │  ├─ model.py
   │     │  │  │  ├─ model_test.py
   │     │  │  │  ├─ sequential.py
   │     │  │  │  ├─ sequential_test.py
   │     │  │  │  ├─ variable_mapping.py
   │     │  │  │  ├─ variable_mapping_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ops
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ core_test.py
   │     │  │  │  ├─ einops.py
   │     │  │  │  ├─ einops_test.py
   │     │  │  │  ├─ function.py
   │     │  │  │  ├─ function_test.py
   │     │  │  │  ├─ image.py
   │     │  │  │  ├─ image_test.py
   │     │  │  │  ├─ linalg.py
   │     │  │  │  ├─ linalg_test.py
   │     │  │  │  ├─ math.py
   │     │  │  │  ├─ math_test.py
   │     │  │  │  ├─ nn.py
   │     │  │  │  ├─ nn_test.py
   │     │  │  │  ├─ node.py
   │     │  │  │  ├─ node_test.py
   │     │  │  │  ├─ numpy.py
   │     │  │  │  ├─ numpy_test.py
   │     │  │  │  ├─ operation.py
   │     │  │  │  ├─ operation_test.py
   │     │  │  │  ├─ operation_utils.py
   │     │  │  │  ├─ operation_utils_test.py
   │     │  │  │  ├─ ops_test.py
   │     │  │  │  ├─ symbolic_arguments.py
   │     │  │  │  ├─ symbolic_arguments_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ optimizers
   │     │  │  │  ├─ adadelta.py
   │     │  │  │  ├─ adadelta_test.py
   │     │  │  │  ├─ adafactor.py
   │     │  │  │  ├─ adafactor_test.py
   │     │  │  │  ├─ adagrad.py
   │     │  │  │  ├─ adagrad_test.py
   │     │  │  │  ├─ adam.py
   │     │  │  │  ├─ adamax.py
   │     │  │  │  ├─ adamax_test.py
   │     │  │  │  ├─ adamw.py
   │     │  │  │  ├─ adamw_test.py
   │     │  │  │  ├─ adam_test.py
   │     │  │  │  ├─ base_optimizer.py
   │     │  │  │  ├─ ftrl.py
   │     │  │  │  ├─ ftrl_test.py
   │     │  │  │  ├─ lamb.py
   │     │  │  │  ├─ lamb_test.py
   │     │  │  │  ├─ lion.py
   │     │  │  │  ├─ lion_test.py
   │     │  │  │  ├─ loss_scale_optimizer.py
   │     │  │  │  ├─ loss_scale_optimizer_test.py
   │     │  │  │  ├─ multi_optimizer.py
   │     │  │  │  ├─ multi_optimizer_test.py
   │     │  │  │  ├─ muon.py
   │     │  │  │  ├─ muon_test.py
   │     │  │  │  ├─ nadam.py
   │     │  │  │  ├─ nadam_test.py
   │     │  │  │  ├─ optimizer.py
   │     │  │  │  ├─ optimizer_sparse_test.py
   │     │  │  │  ├─ optimizer_test.py
   │     │  │  │  ├─ rmsprop.py
   │     │  │  │  ├─ rmsprop_test.py
   │     │  │  │  ├─ schedules
   │     │  │  │  │  ├─ learning_rate_schedule.py
   │     │  │  │  │  ├─ learning_rate_schedule_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ schedule_free_adamw.py
   │     │  │  │  ├─ schedule_free_adamw_test.py
   │     │  │  │  ├─ sgd.py
   │     │  │  │  ├─ sgd_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ quantizers
   │     │  │  │  ├─ awq.py
   │     │  │  │  ├─ awq_config.py
   │     │  │  │  ├─ awq_config_test.py
   │     │  │  │  ├─ awq_core.py
   │     │  │  │  ├─ awq_test.py
   │     │  │  │  ├─ gptq.py
   │     │  │  │  ├─ gptq_config.py
   │     │  │  │  ├─ gptq_config_test.py
   │     │  │  │  ├─ gptq_core.py
   │     │  │  │  ├─ gptq_core_test.py
   │     │  │  │  ├─ gptq_test.py
   │     │  │  │  ├─ quantization_config.py
   │     │  │  │  ├─ quantization_config_test.py
   │     │  │  │  ├─ quantizers.py
   │     │  │  │  ├─ quantizers_test.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ utils_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ random
   │     │  │  │  ├─ random.py
   │     │  │  │  ├─ random_test.py
   │     │  │  │  ├─ seed_generator.py
   │     │  │  │  ├─ seed_generator_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ regularizers
   │     │  │  │  ├─ regularizers.py
   │     │  │  │  ├─ regularizers_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ saving
   │     │  │  │  ├─ file_editor.py
   │     │  │  │  ├─ file_editor_test.py
   │     │  │  │  ├─ keras_saveable.py
   │     │  │  │  ├─ object_registration.py
   │     │  │  │  ├─ object_registration_test.py
   │     │  │  │  ├─ orbax_util.py
   │     │  │  │  ├─ saving_api.py
   │     │  │  │  ├─ saving_api_test.py
   │     │  │  │  ├─ saving_lib.py
   │     │  │  │  ├─ saving_lib_test.py
   │     │  │  │  ├─ serialization_lib.py
   │     │  │  │  ├─ serialization_lib_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ testing
   │     │  │  │  ├─ test_case.py
   │     │  │  │  ├─ test_utils.py
   │     │  │  │  ├─ test_utils_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ trainers
   │     │  │  │  ├─ compile_utils.py
   │     │  │  │  ├─ compile_utils_test.py
   │     │  │  │  ├─ data_adapters
   │     │  │  │  │  ├─ array_data_adapter.py
   │     │  │  │  │  ├─ array_data_adapter_test.py
   │     │  │  │  │  ├─ array_slicing.py
   │     │  │  │  │  ├─ data_adapter.py
   │     │  │  │  │  ├─ data_adapter_utils.py
   │     │  │  │  │  ├─ data_adapter_utils_test.py
   │     │  │  │  │  ├─ generator_data_adapter.py
   │     │  │  │  │  ├─ generator_data_adapter_test.py
   │     │  │  │  │  ├─ grain_dataset_adapter.py
   │     │  │  │  │  ├─ grain_dataset_adapter_test.py
   │     │  │  │  │  ├─ py_dataset_adapter.py
   │     │  │  │  │  ├─ py_dataset_adapter_test.py
   │     │  │  │  │  ├─ tf_dataset_adapter.py
   │     │  │  │  │  ├─ tf_dataset_adapter_test.py
   │     │  │  │  │  ├─ torch_data_loader_adapter.py
   │     │  │  │  │  ├─ torch_data_loader_adapter_test.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ epoch_iterator.py
   │     │  │  │  ├─ epoch_iterator_test.py
   │     │  │  │  ├─ trainer.py
   │     │  │  │  ├─ trainer_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tree
   │     │  │  │  ├─ dmtree_impl.py
   │     │  │  │  ├─ optree_impl.py
   │     │  │  │  ├─ torchtree_impl.py
   │     │  │  │  ├─ tree_api.py
   │     │  │  │  ├─ tree_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ utils
   │     │  │  │  ├─ argument_validation.py
   │     │  │  │  ├─ audio_dataset_utils.py
   │     │  │  │  ├─ audio_dataset_utils_test.py
   │     │  │  │  ├─ backend_utils.py
   │     │  │  │  ├─ backend_utils_test.py
   │     │  │  │  ├─ code_stats.py
   │     │  │  │  ├─ code_stats_test.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ dataset_utils.py
   │     │  │  │  ├─ dataset_utils_test.py
   │     │  │  │  ├─ dtype_utils.py
   │     │  │  │  ├─ dtype_utils_test.py
   │     │  │  │  ├─ file_utils.py
   │     │  │  │  ├─ file_utils_test.py
   │     │  │  │  ├─ grain_utils.py
   │     │  │  │  ├─ image_dataset_utils.py
   │     │  │  │  ├─ image_dataset_utils_test.py
   │     │  │  │  ├─ image_utils.py
   │     │  │  │  ├─ image_utils_test.py
   │     │  │  │  ├─ io_utils.py
   │     │  │  │  ├─ io_utils_test.py
   │     │  │  │  ├─ jax_layer.py
   │     │  │  │  ├─ jax_layer_test.py
   │     │  │  │  ├─ jax_utils.py
   │     │  │  │  ├─ model_visualization.py
   │     │  │  │  ├─ module_utils.py
   │     │  │  │  ├─ naming.py
   │     │  │  │  ├─ naming_test.py
   │     │  │  │  ├─ numerical_utils.py
   │     │  │  │  ├─ numerical_utils_test.py
   │     │  │  │  ├─ progbar.py
   │     │  │  │  ├─ progbar_test.py
   │     │  │  │  ├─ python_utils.py
   │     │  │  │  ├─ python_utils_test.py
   │     │  │  │  ├─ rng_utils.py
   │     │  │  │  ├─ rng_utils_test.py
   │     │  │  │  ├─ sequence_utils.py
   │     │  │  │  ├─ sequence_utils_test.py
   │     │  │  │  ├─ summary_utils.py
   │     │  │  │  ├─ summary_utils_test.py
   │     │  │  │  ├─ text_dataset_utils.py
   │     │  │  │  ├─ text_dataset_utils_test.py
   │     │  │  │  ├─ tf_utils.py
   │     │  │  │  ├─ timeseries_dataset_utils.py
   │     │  │  │  ├─ timeseries_dataset_utils_test.py
   │     │  │  │  ├─ torch_utils.py
   │     │  │  │  ├─ torch_utils_test.py
   │     │  │  │  ├─ traceback_utils.py
   │     │  │  │  ├─ tracking.py
   │     │  │  │  ├─ tracking_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ version.py
   │     │  │  ├─ visualization
   │     │  │  │  ├─ draw_bounding_boxes.py
   │     │  │  │  ├─ draw_segmentation_masks.py
   │     │  │  │  ├─ plot_bounding_box_gallery.py
   │     │  │  │  ├─ plot_image_gallery.py
   │     │  │  │  ├─ plot_segmentation_mask_gallery.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ wrappers
   │     │  │  │  ├─ fixes.py
   │     │  │  │  ├─ sklearn_test.py
   │     │  │  │  ├─ sklearn_wrapper.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ tree
   │     │  │  └─ __init__.py
   │     │  ├─ utils
   │     │  │  ├─ bounding_boxes
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ legacy
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ visualization
   │     │  │  └─ __init__.py
   │     │  ├─ wrappers
   │     │  │  └─ __init__.py
   │     │  ├─ _tf_keras
   │     │  │  ├─ keras
   │     │  │  │  ├─ activations
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ applications
   │     │  │  │  │  ├─ convnext
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ densenet
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ efficientnet
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ efficientnet_v2
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ imagenet_utils
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ inception_resnet_v2
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ inception_v3
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ mobilenet
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ mobilenet_v2
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ mobilenet_v3
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ nasnet
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ resnet
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ resnet50
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ resnet_v2
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ vgg16
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ vgg19
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ xception
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ backend
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ callbacks
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ config
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ constraints
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ datasets
   │     │  │  │  │  ├─ boston_housing
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ california_housing
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ cifar10
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ cifar100
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ fashion_mnist
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ imdb
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ mnist
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ reuters
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ distillation
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ distribution
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ dtype_policies
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ export
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ initializers
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ layers
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ legacy
   │     │  │  │  │  ├─ saving
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ losses
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ metrics
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ mixed_precision
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ models
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ops
   │     │  │  │  │  ├─ image
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ linalg
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ nn
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ numpy
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ optimizers
   │     │  │  │  │  ├─ legacy
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ schedules
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ preprocessing
   │     │  │  │  │  ├─ image
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ sequence
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ text
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ quantizers
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ random
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ regularizers
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ saving
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tree
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ utils
   │     │  │  │  │  ├─ bounding_boxes
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ legacy
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ visualization
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ wrappers
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ keras-3.15.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ kiwisolver
   │     │  ├─ exceptions.py
   │     │  ├─ py.typed
   │     │  ├─ _cext.pyi
   │     │  └─ __init__.py
   │     ├─ kiwisolver-1.5.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ libclang-18.1.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.TXT
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ markdown_it
   │     │  ├─ cli
   │     │  │  ├─ parse.py
   │     │  │  └─ __init__.py
   │     │  ├─ common
   │     │  │  ├─ entities.py
   │     │  │  ├─ html_blocks.py
   │     │  │  ├─ html_re.py
   │     │  │  ├─ normalize_url.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ helpers
   │     │  │  ├─ parse_link_destination.py
   │     │  │  ├─ parse_link_label.py
   │     │  │  ├─ parse_link_title.py
   │     │  │  └─ __init__.py
   │     │  ├─ main.py
   │     │  ├─ parser_block.py
   │     │  ├─ parser_core.py
   │     │  ├─ parser_inline.py
   │     │  ├─ port.yaml
   │     │  ├─ presets
   │     │  │  ├─ commonmark.py
   │     │  │  ├─ default.py
   │     │  │  ├─ zero.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ renderer.py
   │     │  ├─ ruler.py
   │     │  ├─ rules_block
   │     │  │  ├─ blockquote.py
   │     │  │  ├─ code.py
   │     │  │  ├─ fence.py
   │     │  │  ├─ heading.py
   │     │  │  ├─ hr.py
   │     │  │  ├─ html_block.py
   │     │  │  ├─ lheading.py
   │     │  │  ├─ list.py
   │     │  │  ├─ paragraph.py
   │     │  │  ├─ reference.py
   │     │  │  ├─ state_block.py
   │     │  │  ├─ table.py
   │     │  │  └─ __init__.py
   │     │  ├─ rules_core
   │     │  │  ├─ block.py
   │     │  │  ├─ inline.py
   │     │  │  ├─ linkify.py
   │     │  │  ├─ normalize.py
   │     │  │  ├─ replacements.py
   │     │  │  ├─ smartquotes.py
   │     │  │  ├─ state_core.py
   │     │  │  ├─ text_join.py
   │     │  │  └─ __init__.py
   │     │  ├─ rules_inline
   │     │  │  ├─ autolink.py
   │     │  │  ├─ backticks.py
   │     │  │  ├─ balance_pairs.py
   │     │  │  ├─ emphasis.py
   │     │  │  ├─ entity.py
   │     │  │  ├─ escape.py
   │     │  │  ├─ fragments_join.py
   │     │  │  ├─ html_inline.py
   │     │  │  ├─ image.py
   │     │  │  ├─ link.py
   │     │  │  ├─ linkify.py
   │     │  │  ├─ newline.py
   │     │  │  ├─ state_inline.py
   │     │  │  ├─ strikethrough.py
   │     │  │  ├─ text.py
   │     │  │  └─ __init__.py
   │     │  ├─ token.py
   │     │  ├─ tree.py
   │     │  ├─ utils.py
   │     │  ├─ _compat.py
   │     │  ├─ _punycode.py
   │     │  └─ __init__.py
   │     ├─ markdown_it_py-4.2.0.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ LICENSE
   │     │  │  └─ LICENSE.markdown-it
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ markupsafe
   │     │  ├─ py.typed
   │     │  ├─ _native.py
   │     │  ├─ _speedups.c
   │     │  ├─ _speedups.pyi
   │     │  └─ __init__.py
   │     ├─ markupsafe-3.0.3.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ matplotlib
   │     │  ├─ .tmpt1YrkT
   │     │  ├─ animation.py
   │     │  ├─ animation.pyi
   │     │  ├─ artist.py
   │     │  ├─ artist.pyi
   │     │  ├─ axes
   │     │  │  ├─ _axes.py
   │     │  │  ├─ _axes.pyi
   │     │  │  ├─ _base.py
   │     │  │  ├─ _base.pyi
   │     │  │  ├─ _secondary_axes.py
   │     │  │  ├─ _secondary_axes.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ axis.py
   │     │  ├─ axis.pyi
   │     │  ├─ backends
   │     │  │  ├─ backend_agg.py
   │     │  │  ├─ backend_cairo.py
   │     │  │  ├─ backend_gtk3.py
   │     │  │  ├─ backend_gtk3agg.py
   │     │  │  ├─ backend_gtk3cairo.py
   │     │  │  ├─ backend_gtk4.py
   │     │  │  ├─ backend_gtk4agg.py
   │     │  │  ├─ backend_gtk4cairo.py
   │     │  │  ├─ backend_macosx.py
   │     │  │  ├─ backend_mixed.py
   │     │  │  ├─ backend_nbagg.py
   │     │  │  ├─ backend_pdf.py
   │     │  │  ├─ backend_pgf.py
   │     │  │  ├─ backend_ps.py
   │     │  │  ├─ backend_qt.py
   │     │  │  ├─ backend_qt5.py
   │     │  │  ├─ backend_qt5agg.py
   │     │  │  ├─ backend_qt5cairo.py
   │     │  │  ├─ backend_qtagg.py
   │     │  │  ├─ backend_qtcairo.py
   │     │  │  ├─ backend_svg.py
   │     │  │  ├─ backend_template.py
   │     │  │  ├─ backend_tkagg.py
   │     │  │  ├─ backend_tkcairo.py
   │     │  │  ├─ backend_webagg.py
   │     │  │  ├─ backend_webagg_core.py
   │     │  │  ├─ backend_wx.py
   │     │  │  ├─ backend_wxagg.py
   │     │  │  ├─ backend_wxcairo.py
   │     │  │  ├─ qt_compat.py
   │     │  │  ├─ qt_editor
   │     │  │  │  ├─ figureoptions.py
   │     │  │  │  ├─ _formlayout.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ registry.py
   │     │  │  ├─ web_backend
   │     │  │  │  ├─ all_figures.html
   │     │  │  │  ├─ css
   │     │  │  │  │  ├─ boilerplate.css
   │     │  │  │  │  ├─ fbm.css
   │     │  │  │  │  ├─ mpl.css
   │     │  │  │  │  └─ page.css
   │     │  │  │  ├─ ipython_inline_figure.html
   │     │  │  │  ├─ js
   │     │  │  │  │  ├─ mpl.js
   │     │  │  │  │  ├─ mpl_tornado.js
   │     │  │  │  │  └─ nbagg_mpl.js
   │     │  │  │  └─ single_figure.html
   │     │  │  ├─ _backend_agg.pyi
   │     │  │  ├─ _backend_gtk.py
   │     │  │  ├─ _backend_pdf_ps.py
   │     │  │  ├─ _backend_tk.py
   │     │  │  ├─ _macosx.pyi
   │     │  │  ├─ _tkagg.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ backend_bases.py
   │     │  ├─ backend_bases.pyi
   │     │  ├─ backend_managers.py
   │     │  ├─ backend_managers.pyi
   │     │  ├─ backend_tools.py
   │     │  ├─ backend_tools.pyi
   │     │  ├─ bezier.py
   │     │  ├─ bezier.pyi
   │     │  ├─ category.py
   │     │  ├─ cbook.py
   │     │  ├─ cbook.pyi
   │     │  ├─ cm.py
   │     │  ├─ cm.pyi
   │     │  ├─ collections.py
   │     │  ├─ collections.pyi
   │     │  ├─ colorbar.py
   │     │  ├─ colorbar.pyi
   │     │  ├─ colorizer.py
   │     │  ├─ colorizer.pyi
   │     │  ├─ colors.py
   │     │  ├─ colors.pyi
   │     │  ├─ container.py
   │     │  ├─ container.pyi
   │     │  ├─ contour.py
   │     │  ├─ contour.pyi
   │     │  ├─ dates.py
   │     │  ├─ dviread.py
   │     │  ├─ dviread.pyi
   │     │  ├─ figure.py
   │     │  ├─ figure.pyi
   │     │  ├─ font_manager.py
   │     │  ├─ font_manager.pyi
   │     │  ├─ ft2font.pyi
   │     │  ├─ gridspec.py
   │     │  ├─ gridspec.pyi
   │     │  ├─ hatch.py
   │     │  ├─ hatch.pyi
   │     │  ├─ image.py
   │     │  ├─ image.pyi
   │     │  ├─ inset.py
   │     │  ├─ inset.pyi
   │     │  ├─ layout_engine.py
   │     │  ├─ layout_engine.pyi
   │     │  ├─ legend.py
   │     │  ├─ legend.pyi
   │     │  ├─ legend_handler.py
   │     │  ├─ legend_handler.pyi
   │     │  ├─ lines.py
   │     │  ├─ lines.pyi
   │     │  ├─ markers.py
   │     │  ├─ markers.pyi
   │     │  ├─ mathtext.py
   │     │  ├─ mathtext.pyi
   │     │  ├─ mlab.py
   │     │  ├─ mlab.pyi
   │     │  ├─ mpl-data
   │     │  │  ├─ fonts
   │     │  │  │  ├─ afm
   │     │  │  │  │  ├─ cmex10.afm
   │     │  │  │  │  ├─ cmmi10.afm
   │     │  │  │  │  ├─ cmr10.afm
   │     │  │  │  │  ├─ cmsy10.afm
   │     │  │  │  │  ├─ cmtt10.afm
   │     │  │  │  │  ├─ pagd8a.afm
   │     │  │  │  │  ├─ pagdo8a.afm
   │     │  │  │  │  ├─ pagk8a.afm
   │     │  │  │  │  ├─ pagko8a.afm
   │     │  │  │  │  ├─ pbkd8a.afm
   │     │  │  │  │  ├─ pbkdi8a.afm
   │     │  │  │  │  ├─ pbkl8a.afm
   │     │  │  │  │  ├─ pbkli8a.afm
   │     │  │  │  │  ├─ pcrb8a.afm
   │     │  │  │  │  ├─ pcrbo8a.afm
   │     │  │  │  │  ├─ pcrr8a.afm
   │     │  │  │  │  ├─ pcrro8a.afm
   │     │  │  │  │  ├─ phvb8a.afm
   │     │  │  │  │  ├─ phvb8an.afm
   │     │  │  │  │  ├─ phvbo8a.afm
   │     │  │  │  │  ├─ phvbo8an.afm
   │     │  │  │  │  ├─ phvl8a.afm
   │     │  │  │  │  ├─ phvlo8a.afm
   │     │  │  │  │  ├─ phvr8a.afm
   │     │  │  │  │  ├─ phvr8an.afm
   │     │  │  │  │  ├─ phvro8a.afm
   │     │  │  │  │  ├─ phvro8an.afm
   │     │  │  │  │  ├─ pncb8a.afm
   │     │  │  │  │  ├─ pncbi8a.afm
   │     │  │  │  │  ├─ pncr8a.afm
   │     │  │  │  │  ├─ pncri8a.afm
   │     │  │  │  │  ├─ pplb8a.afm
   │     │  │  │  │  ├─ pplbi8a.afm
   │     │  │  │  │  ├─ pplr8a.afm
   │     │  │  │  │  ├─ pplri8a.afm
   │     │  │  │  │  ├─ psyr.afm
   │     │  │  │  │  ├─ ptmb8a.afm
   │     │  │  │  │  ├─ ptmbi8a.afm
   │     │  │  │  │  ├─ ptmr8a.afm
   │     │  │  │  │  ├─ ptmri8a.afm
   │     │  │  │  │  ├─ putb8a.afm
   │     │  │  │  │  ├─ putbi8a.afm
   │     │  │  │  │  ├─ putr8a.afm
   │     │  │  │  │  ├─ putri8a.afm
   │     │  │  │  │  ├─ pzcmi8a.afm
   │     │  │  │  │  └─ pzdr.afm
   │     │  │  │  ├─ pdfcorefonts
   │     │  │  │  │  ├─ Courier-Bold.afm
   │     │  │  │  │  ├─ Courier-BoldOblique.afm
   │     │  │  │  │  ├─ Courier-Oblique.afm
   │     │  │  │  │  ├─ Courier.afm
   │     │  │  │  │  ├─ Helvetica-Bold.afm
   │     │  │  │  │  ├─ Helvetica-BoldOblique.afm
   │     │  │  │  │  ├─ Helvetica-Oblique.afm
   │     │  │  │  │  ├─ Helvetica.afm
   │     │  │  │  │  ├─ readme.txt
   │     │  │  │  │  ├─ Symbol.afm
   │     │  │  │  │  ├─ Times-Bold.afm
   │     │  │  │  │  ├─ Times-BoldItalic.afm
   │     │  │  │  │  ├─ Times-Italic.afm
   │     │  │  │  │  ├─ Times-Roman.afm
   │     │  │  │  │  └─ ZapfDingbats.afm
   │     │  │  │  └─ ttf
   │     │  │  │     ├─ cmb10.ttf
   │     │  │  │     ├─ cmex10.ttf
   │     │  │  │     ├─ cmmi10.ttf
   │     │  │  │     ├─ cmr10.ttf
   │     │  │  │     ├─ cmss10.ttf
   │     │  │  │     ├─ cmsy10.ttf
   │     │  │  │     ├─ cmtt10.ttf
   │     │  │  │     ├─ DejaVuSans-Bold.ttf
   │     │  │  │     ├─ DejaVuSans-BoldOblique.ttf
   │     │  │  │     ├─ DejaVuSans-Oblique.ttf
   │     │  │  │     ├─ DejaVuSans.ttf
   │     │  │  │     ├─ DejaVuSansDisplay.ttf
   │     │  │  │     ├─ DejaVuSansMono-Bold.ttf
   │     │  │  │     ├─ DejaVuSansMono-BoldOblique.ttf
   │     │  │  │     ├─ DejaVuSansMono-Oblique.ttf
   │     │  │  │     ├─ DejaVuSansMono.ttf
   │     │  │  │     ├─ DejaVuSerif-Bold.ttf
   │     │  │  │     ├─ DejaVuSerif-BoldItalic.ttf
   │     │  │  │     ├─ DejaVuSerif-Italic.ttf
   │     │  │  │     ├─ DejaVuSerif.ttf
   │     │  │  │     ├─ DejaVuSerifDisplay.ttf
   │     │  │  │     ├─ LICENSE_DEJAVU
   │     │  │  │     ├─ LICENSE_STIX
   │     │  │  │     ├─ STIXGeneral.ttf
   │     │  │  │     ├─ STIXGeneralBol.ttf
   │     │  │  │     ├─ STIXGeneralBolIta.ttf
   │     │  │  │     ├─ STIXGeneralItalic.ttf
   │     │  │  │     ├─ STIXNonUni.ttf
   │     │  │  │     ├─ STIXNonUniBol.ttf
   │     │  │  │     ├─ STIXNonUniBolIta.ttf
   │     │  │  │     ├─ STIXNonUniIta.ttf
   │     │  │  │     ├─ STIXSizFiveSymReg.ttf
   │     │  │  │     ├─ STIXSizFourSymBol.ttf
   │     │  │  │     ├─ STIXSizFourSymReg.ttf
   │     │  │  │     ├─ STIXSizOneSymBol.ttf
   │     │  │  │     ├─ STIXSizOneSymReg.ttf
   │     │  │  │     ├─ STIXSizThreeSymBol.ttf
   │     │  │  │     ├─ STIXSizThreeSymReg.ttf
   │     │  │  │     ├─ STIXSizTwoSymBol.ttf
   │     │  │  │     └─ STIXSizTwoSymReg.ttf
   │     │  │  ├─ images
   │     │  │  │  ├─ back-symbolic.svg
   │     │  │  │  ├─ back.pdf
   │     │  │  │  ├─ back.png
   │     │  │  │  ├─ back.svg
   │     │  │  │  ├─ back_large.png
   │     │  │  │  ├─ filesave-symbolic.svg
   │     │  │  │  ├─ filesave.pdf
   │     │  │  │  ├─ filesave.png
   │     │  │  │  ├─ filesave.svg
   │     │  │  │  ├─ filesave_large.png
   │     │  │  │  ├─ forward-symbolic.svg
   │     │  │  │  ├─ forward.pdf
   │     │  │  │  ├─ forward.png
   │     │  │  │  ├─ forward.svg
   │     │  │  │  ├─ forward_large.png
   │     │  │  │  ├─ hand.pdf
   │     │  │  │  ├─ hand.png
   │     │  │  │  ├─ hand.svg
   │     │  │  │  ├─ help-symbolic.svg
   │     │  │  │  ├─ help.pdf
   │     │  │  │  ├─ help.png
   │     │  │  │  ├─ help.svg
   │     │  │  │  ├─ help_large.png
   │     │  │  │  ├─ home-symbolic.svg
   │     │  │  │  ├─ home.pdf
   │     │  │  │  ├─ home.png
   │     │  │  │  ├─ home.svg
   │     │  │  │  ├─ home_large.png
   │     │  │  │  ├─ matplotlib.pdf
   │     │  │  │  ├─ matplotlib.png
   │     │  │  │  ├─ matplotlib.svg
   │     │  │  │  ├─ matplotlib_large.png
   │     │  │  │  ├─ move-symbolic.svg
   │     │  │  │  ├─ move.pdf
   │     │  │  │  ├─ move.png
   │     │  │  │  ├─ move.svg
   │     │  │  │  ├─ move_large.png
   │     │  │  │  ├─ qt4_editor_options.pdf
   │     │  │  │  ├─ qt4_editor_options.png
   │     │  │  │  ├─ qt4_editor_options.svg
   │     │  │  │  ├─ qt4_editor_options_large.png
   │     │  │  │  ├─ subplots-symbolic.svg
   │     │  │  │  ├─ subplots.pdf
   │     │  │  │  ├─ subplots.png
   │     │  │  │  ├─ subplots.svg
   │     │  │  │  ├─ subplots_large.png
   │     │  │  │  ├─ zoom_to_rect-symbolic.svg
   │     │  │  │  ├─ zoom_to_rect.pdf
   │     │  │  │  ├─ zoom_to_rect.png
   │     │  │  │  ├─ zoom_to_rect.svg
   │     │  │  │  └─ zoom_to_rect_large.png
   │     │  │  ├─ kpsewhich.lua
   │     │  │  ├─ matplotlibrc
   │     │  │  ├─ plot_directive
   │     │  │  │  └─ plot_directive.css
   │     │  │  ├─ sample_data
   │     │  │  │  ├─ axes_grid
   │     │  │  │  │  └─ bivariate_normal.npy
   │     │  │  │  ├─ data_x_x2_x3.csv
   │     │  │  │  ├─ eeg.dat
   │     │  │  │  ├─ embedding_in_wx3.xrc
   │     │  │  │  ├─ goog.npz
   │     │  │  │  ├─ grace_hopper.jpg
   │     │  │  │  ├─ jacksboro_fault_dem.npz
   │     │  │  │  ├─ logo2.png
   │     │  │  │  ├─ membrane.dat
   │     │  │  │  ├─ Minduka_Present_Blue_Pack.png
   │     │  │  │  ├─ msft.csv
   │     │  │  │  ├─ README.txt
   │     │  │  │  ├─ s1045.ima.gz
   │     │  │  │  ├─ Stocks.csv
   │     │  │  │  └─ topobathy.npz
   │     │  │  └─ stylelib
   │     │  │     ├─ bmh.mplstyle
   │     │  │     ├─ classic.mplstyle
   │     │  │     ├─ dark_background.mplstyle
   │     │  │     ├─ fast.mplstyle
   │     │  │     ├─ fivethirtyeight.mplstyle
   │     │  │     ├─ ggplot.mplstyle
   │     │  │     ├─ grayscale.mplstyle
   │     │  │     ├─ petroff10.mplstyle
   │     │  │     ├─ seaborn-v0_8-bright.mplstyle
   │     │  │     ├─ seaborn-v0_8-colorblind.mplstyle
   │     │  │     ├─ seaborn-v0_8-dark-palette.mplstyle
   │     │  │     ├─ seaborn-v0_8-dark.mplstyle
   │     │  │     ├─ seaborn-v0_8-darkgrid.mplstyle
   │     │  │     ├─ seaborn-v0_8-deep.mplstyle
   │     │  │     ├─ seaborn-v0_8-muted.mplstyle
   │     │  │     ├─ seaborn-v0_8-notebook.mplstyle
   │     │  │     ├─ seaborn-v0_8-paper.mplstyle
   │     │  │     ├─ seaborn-v0_8-pastel.mplstyle
   │     │  │     ├─ seaborn-v0_8-poster.mplstyle
   │     │  │     ├─ seaborn-v0_8-talk.mplstyle
   │     │  │     ├─ seaborn-v0_8-ticks.mplstyle
   │     │  │     ├─ seaborn-v0_8-white.mplstyle
   │     │  │     ├─ seaborn-v0_8-whitegrid.mplstyle
   │     │  │     ├─ seaborn-v0_8.mplstyle
   │     │  │     ├─ Solarize_Light2.mplstyle
   │     │  │     ├─ tableau-colorblind10.mplstyle
   │     │  │     ├─ _classic_test_patch.mplstyle
   │     │  │     ├─ _mpl-gallery-nogrid.mplstyle
   │     │  │     └─ _mpl-gallery.mplstyle
   │     │  ├─ offsetbox.py
   │     │  ├─ offsetbox.pyi
   │     │  ├─ patches.py
   │     │  ├─ patches.pyi
   │     │  ├─ path.py
   │     │  ├─ path.pyi
   │     │  ├─ patheffects.py
   │     │  ├─ patheffects.pyi
   │     │  ├─ projections
   │     │  │  ├─ geo.py
   │     │  │  ├─ geo.pyi
   │     │  │  ├─ polar.py
   │     │  │  ├─ polar.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ py.typed
   │     │  ├─ pylab.py
   │     │  ├─ pyplot.py
   │     │  ├─ quiver.py
   │     │  ├─ quiver.pyi
   │     │  ├─ rcsetup.py
   │     │  ├─ rcsetup.pyi
   │     │  ├─ sankey.py
   │     │  ├─ sankey.pyi
   │     │  ├─ scale.py
   │     │  ├─ scale.pyi
   │     │  ├─ sphinxext
   │     │  │  ├─ figmpl_directive.py
   │     │  │  ├─ mathmpl.py
   │     │  │  ├─ plot_directive.py
   │     │  │  ├─ roles.py
   │     │  │  └─ __init__.py
   │     │  ├─ spines.py
   │     │  ├─ spines.pyi
   │     │  ├─ stackplot.py
   │     │  ├─ stackplot.pyi
   │     │  ├─ streamplot.py
   │     │  ├─ streamplot.pyi
   │     │  ├─ style
   │     │  │  ├─ core.py
   │     │  │  ├─ core.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ table.py
   │     │  ├─ table.pyi
   │     │  ├─ testing
   │     │  │  ├─ compare.py
   │     │  │  ├─ compare.pyi
   │     │  │  ├─ conftest.py
   │     │  │  ├─ conftest.pyi
   │     │  │  ├─ decorators.py
   │     │  │  ├─ decorators.pyi
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ jpl_units
   │     │  │  │  ├─ Duration.py
   │     │  │  │  ├─ Epoch.py
   │     │  │  │  ├─ EpochConverter.py
   │     │  │  │  ├─ StrConverter.py
   │     │  │  │  ├─ UnitDbl.py
   │     │  │  │  ├─ UnitDblConverter.py
   │     │  │  │  ├─ UnitDblFormatter.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ widgets.py
   │     │  │  ├─ widgets.pyi
   │     │  │  ├─ _markers.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ tests
   │     │  │  ├─ conftest.py
   │     │  │  ├─ test_afm.py
   │     │  │  ├─ test_agg.py
   │     │  │  ├─ test_agg_filter.py
   │     │  │  ├─ test_animation.py
   │     │  │  ├─ test_api.py
   │     │  │  ├─ test_arrow_patches.py
   │     │  │  ├─ test_artist.py
   │     │  │  ├─ test_axes.py
   │     │  │  ├─ test_axis.py
   │     │  │  ├─ test_backends_interactive.py
   │     │  │  ├─ test_backend_bases.py
   │     │  │  ├─ test_backend_cairo.py
   │     │  │  ├─ test_backend_gtk3.py
   │     │  │  ├─ test_backend_inline.py
   │     │  │  ├─ test_backend_macosx.py
   │     │  │  ├─ test_backend_nbagg.py
   │     │  │  ├─ test_backend_pdf.py
   │     │  │  ├─ test_backend_pgf.py
   │     │  │  ├─ test_backend_ps.py
   │     │  │  ├─ test_backend_qt.py
   │     │  │  ├─ test_backend_registry.py
   │     │  │  ├─ test_backend_svg.py
   │     │  │  ├─ test_backend_template.py
   │     │  │  ├─ test_backend_tk.py
   │     │  │  ├─ test_backend_tools.py
   │     │  │  ├─ test_backend_webagg.py
   │     │  │  ├─ test_basic.py
   │     │  │  ├─ test_bbox_tight.py
   │     │  │  ├─ test_bezier.py
   │     │  │  ├─ test_category.py
   │     │  │  ├─ test_cbook.py
   │     │  │  ├─ test_collections.py
   │     │  │  ├─ test_colorbar.py
   │     │  │  ├─ test_colors.py
   │     │  │  ├─ test_compare_images.py
   │     │  │  ├─ test_constrainedlayout.py
   │     │  │  ├─ test_container.py
   │     │  │  ├─ test_contour.py
   │     │  │  ├─ test_cycles.py
   │     │  │  ├─ test_dates.py
   │     │  │  ├─ test_datetime.py
   │     │  │  ├─ test_determinism.py
   │     │  │  ├─ test_doc.py
   │     │  │  ├─ test_dviread.py
   │     │  │  ├─ test_figure.py
   │     │  │  ├─ test_fontconfig_pattern.py
   │     │  │  ├─ test_font_manager.py
   │     │  │  ├─ test_ft2font.py
   │     │  │  ├─ test_getattr.py
   │     │  │  ├─ test_gridspec.py
   │     │  │  ├─ test_image.py
   │     │  │  ├─ test_legend.py
   │     │  │  ├─ test_lines.py
   │     │  │  ├─ test_marker.py
   │     │  │  ├─ test_mathtext.py
   │     │  │  ├─ test_matplotlib.py
   │     │  │  ├─ test_mlab.py
   │     │  │  ├─ test_multivariate_colormaps.py
   │     │  │  ├─ test_offsetbox.py
   │     │  │  ├─ test_patches.py
   │     │  │  ├─ test_path.py
   │     │  │  ├─ test_patheffects.py
   │     │  │  ├─ test_pickle.py
   │     │  │  ├─ test_png.py
   │     │  │  ├─ test_polar.py
   │     │  │  ├─ test_preprocess_data.py
   │     │  │  ├─ test_pyplot.py
   │     │  │  ├─ test_quiver.py
   │     │  │  ├─ test_rcparams.py
   │     │  │  ├─ test_sankey.py
   │     │  │  ├─ test_scale.py
   │     │  │  ├─ test_simplification.py
   │     │  │  ├─ test_skew.py
   │     │  │  ├─ test_sphinxext.py
   │     │  │  ├─ test_spines.py
   │     │  │  ├─ test_streamplot.py
   │     │  │  ├─ test_style.py
   │     │  │  ├─ test_subplots.py
   │     │  │  ├─ test_table.py
   │     │  │  ├─ test_testing.py
   │     │  │  ├─ test_texmanager.py
   │     │  │  ├─ test_text.py
   │     │  │  ├─ test_textpath.py
   │     │  │  ├─ test_ticker.py
   │     │  │  ├─ test_tightlayout.py
   │     │  │  ├─ test_transforms.py
   │     │  │  ├─ test_triangulation.py
   │     │  │  ├─ test_type1font.py
   │     │  │  ├─ test_units.py
   │     │  │  ├─ test_usetex.py
   │     │  │  ├─ test_widgets.py
   │     │  │  └─ __init__.py
   │     │  ├─ texmanager.py
   │     │  ├─ texmanager.pyi
   │     │  ├─ text.py
   │     │  ├─ text.pyi
   │     │  ├─ textpath.py
   │     │  ├─ textpath.pyi
   │     │  ├─ ticker.py
   │     │  ├─ ticker.pyi
   │     │  ├─ transforms.py
   │     │  ├─ transforms.pyi
   │     │  ├─ tri
   │     │  │  ├─ _triangulation.py
   │     │  │  ├─ _triangulation.pyi
   │     │  │  ├─ _tricontour.py
   │     │  │  ├─ _tricontour.pyi
   │     │  │  ├─ _trifinder.py
   │     │  │  ├─ _trifinder.pyi
   │     │  │  ├─ _triinterpolate.py
   │     │  │  ├─ _triinterpolate.pyi
   │     │  │  ├─ _tripcolor.py
   │     │  │  ├─ _tripcolor.pyi
   │     │  │  ├─ _triplot.py
   │     │  │  ├─ _triplot.pyi
   │     │  │  ├─ _trirefine.py
   │     │  │  ├─ _trirefine.pyi
   │     │  │  ├─ _tritools.py
   │     │  │  ├─ _tritools.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ typing.py
   │     │  ├─ units.py
   │     │  ├─ widgets.py
   │     │  ├─ widgets.pyi
   │     │  ├─ _afm.py
   │     │  ├─ _animation_data.py
   │     │  ├─ _api
   │     │  │  ├─ deprecation.py
   │     │  │  ├─ deprecation.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ _blocking_input.py
   │     │  ├─ _cm.py
   │     │  ├─ _cm_bivar.py
   │     │  ├─ _cm_listed.py
   │     │  ├─ _cm_multivar.py
   │     │  ├─ _color_data.py
   │     │  ├─ _color_data.pyi
   │     │  ├─ _constrained_layout.py
   │     │  ├─ _c_internal_utils.pyi
   │     │  ├─ _docstring.py
   │     │  ├─ _docstring.pyi
   │     │  ├─ _enums.py
   │     │  ├─ _enums.pyi
   │     │  ├─ _fontconfig_pattern.py
   │     │  ├─ _image.pyi
   │     │  ├─ _internal_utils.py
   │     │  ├─ _layoutgrid.py
   │     │  ├─ _mathtext.py
   │     │  ├─ _mathtext_data.py
   │     │  ├─ _path.pyi
   │     │  ├─ _pylab_helpers.py
   │     │  ├─ _pylab_helpers.pyi
   │     │  ├─ _qhull.pyi
   │     │  ├─ _text_helpers.py
   │     │  ├─ _tight_bbox.py
   │     │  ├─ _tight_layout.py
   │     │  ├─ _tri.pyi
   │     │  ├─ _type1font.py
   │     │  ├─ _version.py
   │     │  ├─ __init__.py
   │     │  └─ __init__.pyi
   │     ├─ matplotlib-3.10.9.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ mdurl
   │     │  ├─ py.typed
   │     │  ├─ _decode.py
   │     │  ├─ _encode.py
   │     │  ├─ _format.py
   │     │  ├─ _parse.py
   │     │  ├─ _url.py
   │     │  └─ __init__.py
   │     ├─ mdurl-0.1.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ ml_dtypes
   │     │  ├─ py.typed
   │     │  ├─ _finfo.py
   │     │  ├─ _iinfo.py
   │     │  └─ __init__.py
   │     ├─ ml_dtypes-0.6.0.dist-info
   │     │  ├─ DELVEWHEEL
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ LICENSE
   │     │  │  └─ LICENSE.eigen
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ ml_dtypes.libs
   │     │  └─ msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
   │     ├─ mpl_toolkits
   │     │  ├─ axes_grid1
   │     │  │  ├─ anchored_artists.py
   │     │  │  ├─ axes_divider.py
   │     │  │  ├─ axes_grid.py
   │     │  │  ├─ axes_rgb.py
   │     │  │  ├─ axes_size.py
   │     │  │  ├─ inset_locator.py
   │     │  │  ├─ mpl_axes.py
   │     │  │  ├─ parasite_axes.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ test_axes_grid1.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ axisartist
   │     │  │  ├─ angle_helper.py
   │     │  │  ├─ axes_divider.py
   │     │  │  ├─ axislines.py
   │     │  │  ├─ axisline_style.py
   │     │  │  ├─ axis_artist.py
   │     │  │  ├─ floating_axes.py
   │     │  │  ├─ grid_finder.py
   │     │  │  ├─ grid_helper_curvelinear.py
   │     │  │  ├─ parasite_axes.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ test_angle_helper.py
   │     │  │  │  ├─ test_axislines.py
   │     │  │  │  ├─ test_axis_artist.py
   │     │  │  │  ├─ test_floating_axes.py
   │     │  │  │  ├─ test_grid_finder.py
   │     │  │  │  ├─ test_grid_helper_curvelinear.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  └─ mplot3d
   │     │     ├─ art3d.py
   │     │     ├─ axes3d.py
   │     │     ├─ axis3d.py
   │     │     ├─ proj3d.py
   │     │     ├─ tests
   │     │     │  ├─ conftest.py
   │     │     │  ├─ test_art3d.py
   │     │     │  ├─ test_axes3d.py
   │     │     │  ├─ test_legend3d.py
   │     │     │  └─ __init__.py
   │     │     └─ __init__.py
   │     ├─ namex
   │     │  ├─ convert.py
   │     │  ├─ export.py
   │     │  ├─ generate.py
   │     │  └─ __init__.py
   │     ├─ namex-0.1.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ narwhals
   │     │  ├─ compliant.py
   │     │  ├─ dataframe.py
   │     │  ├─ dependencies.py
   │     │  ├─ dtypes.py
   │     │  ├─ exceptions.py
   │     │  ├─ expr.py
   │     │  ├─ expr_cat.py
   │     │  ├─ expr_dt.py
   │     │  ├─ expr_list.py
   │     │  ├─ expr_name.py
   │     │  ├─ expr_str.py
   │     │  ├─ expr_struct.py
   │     │  ├─ functions.py
   │     │  ├─ group_by.py
   │     │  ├─ plugins.py
   │     │  ├─ py.typed
   │     │  ├─ schema.py
   │     │  ├─ selectors.py
   │     │  ├─ series.py
   │     │  ├─ series_cat.py
   │     │  ├─ series_dt.py
   │     │  ├─ series_list.py
   │     │  ├─ series_str.py
   │     │  ├─ series_struct.py
   │     │  ├─ sql.py
   │     │  ├─ stable
   │     │  │  ├─ v1
   │     │  │  │  ├─ dependencies.py
   │     │  │  │  ├─ dtypes.py
   │     │  │  │  ├─ selectors.py
   │     │  │  │  ├─ typing.py
   │     │  │  │  ├─ _dtypes.py
   │     │  │  │  ├─ _namespace.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ v2
   │     │  │  │  ├─ dependencies.py
   │     │  │  │  ├─ dtypes.py
   │     │  │  │  ├─ selectors.py
   │     │  │  │  ├─ typing.py
   │     │  │  │  ├─ _namespace.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ testing
   │     │  │  ├─ asserts
   │     │  │  │  ├─ frame.py
   │     │  │  │  ├─ series.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ this.py
   │     │  ├─ translate.py
   │     │  ├─ typing.py
   │     │  ├─ utils.py
   │     │  ├─ _arrow
   │     │  │  ├─ dataframe.py
   │     │  │  ├─ expr.py
   │     │  │  ├─ group_by.py
   │     │  │  ├─ namespace.py
   │     │  │  ├─ selectors.py
   │     │  │  ├─ series.py
   │     │  │  ├─ series_cat.py
   │     │  │  ├─ series_dt.py
   │     │  │  ├─ series_list.py
   │     │  │  ├─ series_str.py
   │     │  │  ├─ series_struct.py
   │     │  │  ├─ typing.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ _compliant
   │     │  │  ├─ any_namespace.py
   │     │  │  ├─ column.py
   │     │  │  ├─ dataframe.py
   │     │  │  ├─ expr.py
   │     │  │  ├─ group_by.py
   │     │  │  ├─ namespace.py
   │     │  │  ├─ selectors.py
   │     │  │  ├─ series.py
   │     │  │  ├─ typing.py
   │     │  │  ├─ window.py
   │     │  │  └─ __init__.py
   │     │  ├─ _constants.py
   │     │  ├─ _dask
   │     │  │  ├─ dataframe.py
   │     │  │  ├─ expr.py
   │     │  │  ├─ expr_dt.py
   │     │  │  ├─ expr_str.py
   │     │  │  ├─ group_by.py
   │     │  │  ├─ namespace.py
   │     │  │  ├─ selectors.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ _duckdb
   │     │  │  ├─ dataframe.py
   │     │  │  ├─ expr.py
   │     │  │  ├─ expr_dt.py
   │     │  │  ├─ expr_list.py
   │     │  │  ├─ expr_str.py
   │     │  │  ├─ expr_struct.py
   │     │  │  ├─ group_by.py
   │     │  │  ├─ namespace.py
   │     │  │  ├─ selectors.py
   │     │  │  ├─ series.py
   │     │  │  ├─ typing.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ _duration.py
   │     │  ├─ _enum.py
   │     │  ├─ _exceptions.py
   │     │  ├─ _expression_parsing.py
   │     │  ├─ _ibis
   │     │  │  ├─ dataframe.py
   │     │  │  ├─ expr.py
   │     │  │  ├─ expr_dt.py
   │     │  │  ├─ expr_list.py
   │     │  │  ├─ expr_str.py
   │     │  │  ├─ expr_struct.py
   │     │  │  ├─ group_by.py
   │     │  │  ├─ namespace.py
   │     │  │  ├─ selectors.py
   │     │  │  ├─ series.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ _interchange
   │     │  │  ├─ dataframe.py
   │     │  │  ├─ series.py
   │     │  │  └─ __init__.py
   │     │  ├─ _namespace.py
   │     │  ├─ _native.py
   │     │  ├─ _pandas_like
   │     │  │  ├─ dataframe.py
   │     │  │  ├─ expr.py
   │     │  │  ├─ group_by.py
   │     │  │  ├─ namespace.py
   │     │  │  ├─ selectors.py
   │     │  │  ├─ series.py
   │     │  │  ├─ series_cat.py
   │     │  │  ├─ series_dt.py
   │     │  │  ├─ series_list.py
   │     │  │  ├─ series_str.py
   │     │  │  ├─ series_struct.py
   │     │  │  ├─ typing.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ _polars
   │     │  │  ├─ dataframe.py
   │     │  │  ├─ expr.py
   │     │  │  ├─ group_by.py
   │     │  │  ├─ namespace.py
   │     │  │  ├─ series.py
   │     │  │  ├─ typing.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ _spark_like
   │     │  │  ├─ dataframe.py
   │     │  │  ├─ expr.py
   │     │  │  ├─ expr_dt.py
   │     │  │  ├─ expr_list.py
   │     │  │  ├─ expr_str.py
   │     │  │  ├─ expr_struct.py
   │     │  │  ├─ group_by.py
   │     │  │  ├─ namespace.py
   │     │  │  ├─ selectors.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ _sql
   │     │  │  ├─ dataframe.py
   │     │  │  ├─ expr.py
   │     │  │  ├─ expr_dt.py
   │     │  │  ├─ expr_str.py
   │     │  │  ├─ group_by.py
   │     │  │  ├─ namespace.py
   │     │  │  ├─ typing.py
   │     │  │  └─ __init__.py
   │     │  ├─ _translate.py
   │     │  ├─ _typing.py
   │     │  ├─ _typing_compat.py
   │     │  ├─ _utils.py
   │     │  └─ __init__.py
   │     ├─ narwhals-2.25.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.md
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ numpy
   │     │  ├─ char
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ compat
   │     │  │  ├─ py3k.py
   │     │  │  ├─ tests
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ conftest.py
   │     │  ├─ core
   │     │  │  ├─ arrayprint.py
   │     │  │  ├─ defchararray.py
   │     │  │  ├─ einsumfunc.py
   │     │  │  ├─ fromnumeric.py
   │     │  │  ├─ function_base.py
   │     │  │  ├─ getlimits.py
   │     │  │  ├─ multiarray.py
   │     │  │  ├─ numeric.py
   │     │  │  ├─ numerictypes.py
   │     │  │  ├─ overrides.py
   │     │  │  ├─ overrides.pyi
   │     │  │  ├─ records.py
   │     │  │  ├─ shape_base.py
   │     │  │  ├─ umath.py
   │     │  │  ├─ _dtype.py
   │     │  │  ├─ _dtype.pyi
   │     │  │  ├─ _dtype_ctypes.py
   │     │  │  ├─ _dtype_ctypes.pyi
   │     │  │  ├─ _internal.py
   │     │  │  ├─ _multiarray_umath.py
   │     │  │  ├─ _utils.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ ctypeslib.py
   │     │  ├─ ctypeslib.pyi
   │     │  ├─ distutils
   │     │  │  ├─ armccompiler.py
   │     │  │  ├─ ccompiler.py
   │     │  │  ├─ ccompiler_opt.py
   │     │  │  ├─ checks
   │     │  │  │  ├─ cpu_asimd.c
   │     │  │  │  ├─ cpu_asimddp.c
   │     │  │  │  ├─ cpu_asimdfhm.c
   │     │  │  │  ├─ cpu_asimdhp.c
   │     │  │  │  ├─ cpu_avx.c
   │     │  │  │  ├─ cpu_avx2.c
   │     │  │  │  ├─ cpu_avx512cd.c
   │     │  │  │  ├─ cpu_avx512f.c
   │     │  │  │  ├─ cpu_avx512_clx.c
   │     │  │  │  ├─ cpu_avx512_cnl.c
   │     │  │  │  ├─ cpu_avx512_icl.c
   │     │  │  │  ├─ cpu_avx512_knl.c
   │     │  │  │  ├─ cpu_avx512_knm.c
   │     │  │  │  ├─ cpu_avx512_skx.c
   │     │  │  │  ├─ cpu_avx512_spr.c
   │     │  │  │  ├─ cpu_f16c.c
   │     │  │  │  ├─ cpu_fma3.c
   │     │  │  │  ├─ cpu_fma4.c
   │     │  │  │  ├─ cpu_neon.c
   │     │  │  │  ├─ cpu_neon_fp16.c
   │     │  │  │  ├─ cpu_neon_vfpv4.c
   │     │  │  │  ├─ cpu_popcnt.c
   │     │  │  │  ├─ cpu_rvv.c
   │     │  │  │  ├─ cpu_sse.c
   │     │  │  │  ├─ cpu_sse2.c
   │     │  │  │  ├─ cpu_sse3.c
   │     │  │  │  ├─ cpu_sse41.c
   │     │  │  │  ├─ cpu_sse42.c
   │     │  │  │  ├─ cpu_ssse3.c
   │     │  │  │  ├─ cpu_sve.c
   │     │  │  │  ├─ cpu_vsx.c
   │     │  │  │  ├─ cpu_vsx2.c
   │     │  │  │  ├─ cpu_vsx3.c
   │     │  │  │  ├─ cpu_vsx4.c
   │     │  │  │  ├─ cpu_vx.c
   │     │  │  │  ├─ cpu_vxe.c
   │     │  │  │  ├─ cpu_vxe2.c
   │     │  │  │  ├─ cpu_xop.c
   │     │  │  │  ├─ extra_avx512bw_mask.c
   │     │  │  │  ├─ extra_avx512dq_mask.c
   │     │  │  │  ├─ extra_avx512f_reduce.c
   │     │  │  │  ├─ extra_vsx3_half_double.c
   │     │  │  │  ├─ extra_vsx4_mma.c
   │     │  │  │  ├─ extra_vsx_asm.c
   │     │  │  │  └─ test_flags.c
   │     │  │  ├─ command
   │     │  │  │  ├─ autodist.py
   │     │  │  │  ├─ bdist_rpm.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ config_compiler.py
   │     │  │  │  ├─ develop.py
   │     │  │  │  ├─ egg_info.py
   │     │  │  │  ├─ install.py
   │     │  │  │  ├─ install_clib.py
   │     │  │  │  ├─ install_data.py
   │     │  │  │  ├─ install_headers.py
   │     │  │  │  ├─ sdist.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ conv_template.py
   │     │  │  ├─ core.py
   │     │  │  ├─ cpuinfo.py
   │     │  │  ├─ exec_command.py
   │     │  │  ├─ extension.py
   │     │  │  ├─ fcompiler
   │     │  │  │  ├─ absoft.py
   │     │  │  │  ├─ arm.py
   │     │  │  │  ├─ compaq.py
   │     │  │  │  ├─ environment.py
   │     │  │  │  ├─ fujitsu.py
   │     │  │  │  ├─ g95.py
   │     │  │  │  ├─ gnu.py
   │     │  │  │  ├─ hpux.py
   │     │  │  │  ├─ ibm.py
   │     │  │  │  ├─ intel.py
   │     │  │  │  ├─ lahey.py
   │     │  │  │  ├─ mips.py
   │     │  │  │  ├─ nag.py
   │     │  │  │  ├─ none.py
   │     │  │  │  ├─ nv.py
   │     │  │  │  ├─ pathf95.py
   │     │  │  │  ├─ pg.py
   │     │  │  │  ├─ sun.py
   │     │  │  │  ├─ vast.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ from_template.py
   │     │  │  ├─ fujitsuccompiler.py
   │     │  │  ├─ intelccompiler.py
   │     │  │  ├─ lib2def.py
   │     │  │  ├─ line_endings.py
   │     │  │  ├─ log.py
   │     │  │  ├─ mingw
   │     │  │  │  └─ gfortran_vs2003_hack.c
   │     │  │  ├─ mingw32ccompiler.py
   │     │  │  ├─ misc_util.py
   │     │  │  ├─ msvc9compiler.py
   │     │  │  ├─ msvccompiler.py
   │     │  │  ├─ npy_pkg_config.py
   │     │  │  ├─ numpy_distribution.py
   │     │  │  ├─ pathccompiler.py
   │     │  │  ├─ system_info.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_ccompiler_opt.py
   │     │  │  │  ├─ test_ccompiler_opt_conf.py
   │     │  │  │  ├─ test_exec_command.py
   │     │  │  │  ├─ test_fcompiler.py
   │     │  │  │  ├─ test_fcompiler_gnu.py
   │     │  │  │  ├─ test_fcompiler_intel.py
   │     │  │  │  ├─ test_fcompiler_nagfor.py
   │     │  │  │  ├─ test_from_template.py
   │     │  │  │  ├─ test_log.py
   │     │  │  │  ├─ test_mingw32ccompiler.py
   │     │  │  │  ├─ test_misc_util.py
   │     │  │  │  ├─ test_npy_pkg_config.py
   │     │  │  │  ├─ test_shell_utils.py
   │     │  │  │  ├─ test_system_info.py
   │     │  │  │  ├─ utilities.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ unixccompiler.py
   │     │  │  ├─ _shell_utils.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ doc
   │     │  │  └─ ufuncs.py
   │     │  ├─ dtypes.py
   │     │  ├─ dtypes.pyi
   │     │  ├─ exceptions.py
   │     │  ├─ exceptions.pyi
   │     │  ├─ f2py
   │     │  │  ├─ auxfuncs.py
   │     │  │  ├─ capi_maps.py
   │     │  │  ├─ cb_rules.py
   │     │  │  ├─ cfuncs.py
   │     │  │  ├─ common_rules.py
   │     │  │  ├─ crackfortran.py
   │     │  │  ├─ diagnose.py
   │     │  │  ├─ f2py2e.py
   │     │  │  ├─ f90mod_rules.py
   │     │  │  ├─ func2subr.py
   │     │  │  ├─ rules.py
   │     │  │  ├─ setup.cfg
   │     │  │  ├─ src
   │     │  │  │  ├─ fortranobject.c
   │     │  │  │  └─ fortranobject.h
   │     │  │  ├─ symbolic.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ src
   │     │  │  │  │  ├─ abstract_interface
   │     │  │  │  │  │  ├─ foo.f90
   │     │  │  │  │  │  └─ gh18403_mod.f90
   │     │  │  │  │  ├─ array_from_pyobj
   │     │  │  │  │  │  └─ wrapmodule.c
   │     │  │  │  │  ├─ assumed_shape
   │     │  │  │  │  │  ├─ .f2py_f2cmap
   │     │  │  │  │  │  ├─ foo_free.f90
   │     │  │  │  │  │  ├─ foo_mod.f90
   │     │  │  │  │  │  ├─ foo_use.f90
   │     │  │  │  │  │  └─ precision.f90
   │     │  │  │  │  ├─ block_docstring
   │     │  │  │  │  │  └─ foo.f
   │     │  │  │  │  ├─ callback
   │     │  │  │  │  │  ├─ foo.f
   │     │  │  │  │  │  ├─ gh17797.f90
   │     │  │  │  │  │  ├─ gh18335.f90
   │     │  │  │  │  │  ├─ gh25211.f
   │     │  │  │  │  │  ├─ gh25211.pyf
   │     │  │  │  │  │  └─ gh26681.f90
   │     │  │  │  │  ├─ cli
   │     │  │  │  │  │  ├─ gh_22819.pyf
   │     │  │  │  │  │  ├─ hi77.f
   │     │  │  │  │  │  └─ hiworld.f90
   │     │  │  │  │  ├─ common
   │     │  │  │  │  │  ├─ block.f
   │     │  │  │  │  │  └─ gh19161.f90
   │     │  │  │  │  ├─ crackfortran
   │     │  │  │  │  │  ├─ accesstype.f90
   │     │  │  │  │  │  ├─ common_with_division.f
   │     │  │  │  │  │  ├─ data_common.f
   │     │  │  │  │  │  ├─ data_multiplier.f
   │     │  │  │  │  │  ├─ data_stmts.f90
   │     │  │  │  │  │  ├─ data_with_comments.f
   │     │  │  │  │  │  ├─ foo_deps.f90
   │     │  │  │  │  │  ├─ gh15035.f
   │     │  │  │  │  │  ├─ gh17859.f
   │     │  │  │  │  │  ├─ gh22648.pyf
   │     │  │  │  │  │  ├─ gh23533.f
   │     │  │  │  │  │  ├─ gh23598.f90
   │     │  │  │  │  │  ├─ gh23598Warn.f90
   │     │  │  │  │  │  ├─ gh23879.f90
   │     │  │  │  │  │  ├─ gh27697.f90
   │     │  │  │  │  │  ├─ gh2848.f90
   │     │  │  │  │  │  ├─ operators.f90
   │     │  │  │  │  │  ├─ privatemod.f90
   │     │  │  │  │  │  ├─ publicmod.f90
   │     │  │  │  │  │  ├─ pubprivmod.f90
   │     │  │  │  │  │  └─ unicode_comment.f90
   │     │  │  │  │  ├─ f2cmap
   │     │  │  │  │  │  ├─ .f2py_f2cmap
   │     │  │  │  │  │  └─ isoFortranEnvMap.f90
   │     │  │  │  │  ├─ isocintrin
   │     │  │  │  │  │  └─ isoCtests.f90
   │     │  │  │  │  ├─ kind
   │     │  │  │  │  │  └─ foo.f90
   │     │  │  │  │  ├─ mixed
   │     │  │  │  │  │  ├─ foo.f
   │     │  │  │  │  │  ├─ foo_fixed.f90
   │     │  │  │  │  │  └─ foo_free.f90
   │     │  │  │  │  ├─ modules
   │     │  │  │  │  │  ├─ gh25337
   │     │  │  │  │  │  │  ├─ data.f90
   │     │  │  │  │  │  │  └─ use_data.f90
   │     │  │  │  │  │  ├─ gh26920
   │     │  │  │  │  │  │  ├─ two_mods_with_no_public_entities.f90
   │     │  │  │  │  │  │  └─ two_mods_with_one_public_routine.f90
   │     │  │  │  │  │  ├─ module_data_docstring.f90
   │     │  │  │  │  │  └─ use_modules.f90
   │     │  │  │  │  ├─ negative_bounds
   │     │  │  │  │  │  └─ issue_20853.f90
   │     │  │  │  │  ├─ parameter
   │     │  │  │  │  │  ├─ constant_array.f90
   │     │  │  │  │  │  ├─ constant_both.f90
   │     │  │  │  │  │  ├─ constant_compound.f90
   │     │  │  │  │  │  ├─ constant_integer.f90
   │     │  │  │  │  │  ├─ constant_non_compound.f90
   │     │  │  │  │  │  └─ constant_real.f90
   │     │  │  │  │  ├─ quoted_character
   │     │  │  │  │  │  └─ foo.f
   │     │  │  │  │  ├─ regression
   │     │  │  │  │  │  ├─ AB.inc
   │     │  │  │  │  │  ├─ assignOnlyModule.f90
   │     │  │  │  │  │  ├─ datonly.f90
   │     │  │  │  │  │  ├─ f77comments.f
   │     │  │  │  │  │  ├─ f77fixedform.f95
   │     │  │  │  │  │  ├─ f90continuation.f90
   │     │  │  │  │  │  ├─ incfile.f90
   │     │  │  │  │  │  ├─ inout.f90
   │     │  │  │  │  │  └─ lower_f2py_fortran.f90
   │     │  │  │  │  ├─ return_character
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_complex
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_integer
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_logical
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_real
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ routines
   │     │  │  │  │  │  ├─ funcfortranname.f
   │     │  │  │  │  │  ├─ funcfortranname.pyf
   │     │  │  │  │  │  ├─ subrout.f
   │     │  │  │  │  │  └─ subrout.pyf
   │     │  │  │  │  ├─ size
   │     │  │  │  │  │  └─ foo.f90
   │     │  │  │  │  ├─ string
   │     │  │  │  │  │  ├─ char.f90
   │     │  │  │  │  │  ├─ fixed_string.f90
   │     │  │  │  │  │  ├─ gh24008.f
   │     │  │  │  │  │  ├─ gh24662.f90
   │     │  │  │  │  │  ├─ gh25286.f90
   │     │  │  │  │  │  ├─ gh25286.pyf
   │     │  │  │  │  │  ├─ gh25286_bc.pyf
   │     │  │  │  │  │  ├─ scalar_string.f90
   │     │  │  │  │  │  └─ string.f
   │     │  │  │  │  └─ value_attrspec
   │     │  │  │  │     └─ gh21665.f90
   │     │  │  │  ├─ test_abstract_interface.py
   │     │  │  │  ├─ test_array_from_pyobj.py
   │     │  │  │  ├─ test_assumed_shape.py
   │     │  │  │  ├─ test_block_docstring.py
   │     │  │  │  ├─ test_callback.py
   │     │  │  │  ├─ test_character.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_crackfortran.py
   │     │  │  │  ├─ test_data.py
   │     │  │  │  ├─ test_docs.py
   │     │  │  │  ├─ test_f2cmap.py
   │     │  │  │  ├─ test_f2py2e.py
   │     │  │  │  ├─ test_isoc.py
   │     │  │  │  ├─ test_kind.py
   │     │  │  │  ├─ test_mixed.py
   │     │  │  │  ├─ test_modules.py
   │     │  │  │  ├─ test_parameter.py
   │     │  │  │  ├─ test_pyf_src.py
   │     │  │  │  ├─ test_quoted_character.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_return_character.py
   │     │  │  │  ├─ test_return_complex.py
   │     │  │  │  ├─ test_return_integer.py
   │     │  │  │  ├─ test_return_logical.py
   │     │  │  │  ├─ test_return_real.py
   │     │  │  │  ├─ test_routines.py
   │     │  │  │  ├─ test_semicolon_split.py
   │     │  │  │  ├─ test_size.py
   │     │  │  │  ├─ test_string.py
   │     │  │  │  ├─ test_symbolic.py
   │     │  │  │  ├─ test_value_attrspec.py
   │     │  │  │  ├─ util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ use_rules.py
   │     │  │  ├─ _backends
   │     │  │  │  ├─ _backend.py
   │     │  │  │  ├─ _distutils.py
   │     │  │  │  ├─ _meson.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _isocbind.py
   │     │  │  ├─ _src_pyf.py
   │     │  │  ├─ __init__.py
   │     │  │  ├─ __init__.pyi
   │     │  │  ├─ __main__.py
   │     │  │  └─ __version__.py
   │     │  ├─ fft
   │     │  │  ├─ helper.py
   │     │  │  ├─ helper.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_helper.py
   │     │  │  │  ├─ test_pocketfft.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _helper.py
   │     │  │  ├─ _helper.pyi
   │     │  │  ├─ _pocketfft.py
   │     │  │  ├─ _pocketfft.pyi
   │     │  │  ├─ _pocketfft_umath.cp310-win_amd64.lib
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ lib
   │     │  │  ├─ array_utils.py
   │     │  │  ├─ array_utils.pyi
   │     │  │  ├─ format.py
   │     │  │  ├─ format.pyi
   │     │  │  ├─ introspect.py
   │     │  │  ├─ introspect.pyi
   │     │  │  ├─ mixins.py
   │     │  │  ├─ mixins.pyi
   │     │  │  ├─ npyio.py
   │     │  │  ├─ npyio.pyi
   │     │  │  ├─ recfunctions.py
   │     │  │  ├─ recfunctions.pyi
   │     │  │  ├─ scimath.py
   │     │  │  ├─ scimath.pyi
   │     │  │  ├─ stride_tricks.py
   │     │  │  ├─ stride_tricks.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ py2-np0-objarr.npy
   │     │  │  │  │  ├─ py2-objarr.npy
   │     │  │  │  │  ├─ py2-objarr.npz
   │     │  │  │  │  ├─ py3-objarr.npy
   │     │  │  │  │  ├─ py3-objarr.npz
   │     │  │  │  │  ├─ python3.npy
   │     │  │  │  │  └─ win64python2.npy
   │     │  │  │  ├─ test_arraypad.py
   │     │  │  │  ├─ test_arraysetops.py
   │     │  │  │  ├─ test_arrayterator.py
   │     │  │  │  ├─ test_array_utils.py
   │     │  │  │  ├─ test_format.py
   │     │  │  │  ├─ test_function_base.py
   │     │  │  │  ├─ test_histograms.py
   │     │  │  │  ├─ test_index_tricks.py
   │     │  │  │  ├─ test_io.py
   │     │  │  │  ├─ test_loadtxt.py
   │     │  │  │  ├─ test_mixins.py
   │     │  │  │  ├─ test_nanfunctions.py
   │     │  │  │  ├─ test_packbits.py
   │     │  │  │  ├─ test_polynomial.py
   │     │  │  │  ├─ test_recfunctions.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_shape_base.py
   │     │  │  │  ├─ test_stride_tricks.py
   │     │  │  │  ├─ test_twodim_base.py
   │     │  │  │  ├─ test_type_check.py
   │     │  │  │  ├─ test_ufunclike.py
   │     │  │  │  ├─ test_utils.py
   │     │  │  │  ├─ test__datasource.py
   │     │  │  │  ├─ test__iotools.py
   │     │  │  │  ├─ test__version.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ user_array.py
   │     │  │  ├─ user_array.pyi
   │     │  │  ├─ _arraypad_impl.py
   │     │  │  ├─ _arraypad_impl.pyi
   │     │  │  ├─ _arraysetops_impl.py
   │     │  │  ├─ _arraysetops_impl.pyi
   │     │  │  ├─ _arrayterator_impl.py
   │     │  │  ├─ _arrayterator_impl.pyi
   │     │  │  ├─ _array_utils_impl.py
   │     │  │  ├─ _array_utils_impl.pyi
   │     │  │  ├─ _datasource.py
   │     │  │  ├─ _datasource.pyi
   │     │  │  ├─ _function_base_impl.py
   │     │  │  ├─ _function_base_impl.pyi
   │     │  │  ├─ _histograms_impl.py
   │     │  │  ├─ _histograms_impl.pyi
   │     │  │  ├─ _index_tricks_impl.py
   │     │  │  ├─ _index_tricks_impl.pyi
   │     │  │  ├─ _iotools.py
   │     │  │  ├─ _iotools.pyi
   │     │  │  ├─ _nanfunctions_impl.py
   │     │  │  ├─ _nanfunctions_impl.pyi
   │     │  │  ├─ _npyio_impl.py
   │     │  │  ├─ _npyio_impl.pyi
   │     │  │  ├─ _polynomial_impl.py
   │     │  │  ├─ _polynomial_impl.pyi
   │     │  │  ├─ _scimath_impl.py
   │     │  │  ├─ _scimath_impl.pyi
   │     │  │  ├─ _shape_base_impl.py
   │     │  │  ├─ _shape_base_impl.pyi
   │     │  │  ├─ _stride_tricks_impl.py
   │     │  │  ├─ _stride_tricks_impl.pyi
   │     │  │  ├─ _twodim_base_impl.py
   │     │  │  ├─ _twodim_base_impl.pyi
   │     │  │  ├─ _type_check_impl.py
   │     │  │  ├─ _type_check_impl.pyi
   │     │  │  ├─ _ufunclike_impl.py
   │     │  │  ├─ _ufunclike_impl.pyi
   │     │  │  ├─ _user_array_impl.py
   │     │  │  ├─ _user_array_impl.pyi
   │     │  │  ├─ _utils_impl.py
   │     │  │  ├─ _utils_impl.pyi
   │     │  │  ├─ _version.py
   │     │  │  ├─ _version.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ linalg
   │     │  │  ├─ lapack_lite.cp310-win_amd64.lib
   │     │  │  ├─ lapack_lite.pyi
   │     │  │  ├─ linalg.py
   │     │  │  ├─ linalg.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_deprecations.py
   │     │  │  │  ├─ test_linalg.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _linalg.py
   │     │  │  ├─ _linalg.pyi
   │     │  │  ├─ _umath_linalg.cp310-win_amd64.lib
   │     │  │  ├─ _umath_linalg.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ ma
   │     │  │  ├─ API_CHANGES.txt
   │     │  │  ├─ core.py
   │     │  │  ├─ core.pyi
   │     │  │  ├─ extras.py
   │     │  │  ├─ extras.pyi
   │     │  │  ├─ LICENSE
   │     │  │  ├─ mrecords.py
   │     │  │  ├─ mrecords.pyi
   │     │  │  ├─ README.rst
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_arrayobject.py
   │     │  │  │  ├─ test_core.py
   │     │  │  │  ├─ test_deprecations.py
   │     │  │  │  ├─ test_extras.py
   │     │  │  │  ├─ test_mrecords.py
   │     │  │  │  ├─ test_old_ma.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_subclassing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ testutils.py
   │     │  │  ├─ timer_comparison.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ matlib.py
   │     │  ├─ matlib.pyi
   │     │  ├─ matrixlib
   │     │  │  ├─ defmatrix.py
   │     │  │  ├─ defmatrix.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_defmatrix.py
   │     │  │  │  ├─ test_interaction.py
   │     │  │  │  ├─ test_masked_matrix.py
   │     │  │  │  ├─ test_matrix_linalg.py
   │     │  │  │  ├─ test_multiarray.py
   │     │  │  │  ├─ test_numeric.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ polynomial
   │     │  │  ├─ chebyshev.py
   │     │  │  ├─ chebyshev.pyi
   │     │  │  ├─ hermite.py
   │     │  │  ├─ hermite.pyi
   │     │  │  ├─ hermite_e.py
   │     │  │  ├─ hermite_e.pyi
   │     │  │  ├─ laguerre.py
   │     │  │  ├─ laguerre.pyi
   │     │  │  ├─ legendre.py
   │     │  │  ├─ legendre.pyi
   │     │  │  ├─ polynomial.py
   │     │  │  ├─ polynomial.pyi
   │     │  │  ├─ polyutils.py
   │     │  │  ├─ polyutils.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_chebyshev.py
   │     │  │  │  ├─ test_classes.py
   │     │  │  │  ├─ test_hermite.py
   │     │  │  │  ├─ test_hermite_e.py
   │     │  │  │  ├─ test_laguerre.py
   │     │  │  │  ├─ test_legendre.py
   │     │  │  │  ├─ test_polynomial.py
   │     │  │  │  ├─ test_polyutils.py
   │     │  │  │  ├─ test_printing.py
   │     │  │  │  ├─ test_symbol.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _polybase.py
   │     │  │  ├─ _polybase.pyi
   │     │  │  ├─ _polytypes.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ py.typed
   │     │  ├─ random
   │     │  │  ├─ bit_generator.cp310-win_amd64.lib
   │     │  │  ├─ bit_generator.pxd
   │     │  │  ├─ bit_generator.pyi
   │     │  │  ├─ c_distributions.pxd
   │     │  │  ├─ lib
   │     │  │  │  └─ npyrandom.lib
   │     │  │  ├─ LICENSE.md
   │     │  │  ├─ mtrand.cp310-win_amd64.lib
   │     │  │  ├─ mtrand.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ generator_pcg64_np121.pkl.gz
   │     │  │  │  │  ├─ generator_pcg64_np126.pkl.gz
   │     │  │  │  │  ├─ mt19937-testset-1.csv
   │     │  │  │  │  ├─ mt19937-testset-2.csv
   │     │  │  │  │  ├─ pcg64-testset-1.csv
   │     │  │  │  │  ├─ pcg64-testset-2.csv
   │     │  │  │  │  ├─ pcg64dxsm-testset-1.csv
   │     │  │  │  │  ├─ pcg64dxsm-testset-2.csv
   │     │  │  │  │  ├─ philox-testset-1.csv
   │     │  │  │  │  ├─ philox-testset-2.csv
   │     │  │  │  │  ├─ sfc64-testset-1.csv
   │     │  │  │  │  ├─ sfc64-testset-2.csv
   │     │  │  │  │  ├─ sfc64_np126.pkl.gz
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_direct.py
   │     │  │  │  ├─ test_extending.py
   │     │  │  │  ├─ test_generator_mt19937.py
   │     │  │  │  ├─ test_generator_mt19937_regressions.py
   │     │  │  │  ├─ test_random.py
   │     │  │  │  ├─ test_randomstate.py
   │     │  │  │  ├─ test_randomstate_regression.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_seed_sequence.py
   │     │  │  │  ├─ test_smoke.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _bounded_integers.cp310-win_amd64.lib
   │     │  │  ├─ _bounded_integers.pxd
   │     │  │  ├─ _common.cp310-win_amd64.lib
   │     │  │  ├─ _common.pxd
   │     │  │  ├─ _examples
   │     │  │  │  ├─ cffi
   │     │  │  │  │  ├─ extending.py
   │     │  │  │  │  └─ parse.py
   │     │  │  │  ├─ cython
   │     │  │  │  │  ├─ extending.pyx
   │     │  │  │  │  └─ extending_distributions.pyx
   │     │  │  │  └─ numba
   │     │  │  │     ├─ extending.py
   │     │  │  │     └─ extending_distributions.py
   │     │  │  ├─ _generator.cp310-win_amd64.lib
   │     │  │  ├─ _generator.pyi
   │     │  │  ├─ _mt19937.cp310-win_amd64.lib
   │     │  │  ├─ _mt19937.pyi
   │     │  │  ├─ _pcg64.cp310-win_amd64.lib
   │     │  │  ├─ _pcg64.pyi
   │     │  │  ├─ _philox.cp310-win_amd64.lib
   │     │  │  ├─ _philox.pyi
   │     │  │  ├─ _pickle.py
   │     │  │  ├─ _pickle.pyi
   │     │  │  ├─ _sfc64.cp310-win_amd64.lib
   │     │  │  ├─ _sfc64.pyi
   │     │  │  ├─ __init__.pxd
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ rec
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ strings
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ testing
   │     │  │  ├─ overrides.py
   │     │  │  ├─ overrides.pyi
   │     │  │  ├─ print_coercion_tables.py
   │     │  │  ├─ print_coercion_tables.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _private
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ utils.pyi
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __init__.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ tests
   │     │  │  ├─ test_configtool.py
   │     │  │  ├─ test_ctypeslib.py
   │     │  │  ├─ test_lazyloading.py
   │     │  │  ├─ test_matlib.py
   │     │  │  ├─ test_numpy_config.py
   │     │  │  ├─ test_numpy_version.py
   │     │  │  ├─ test_public_api.py
   │     │  │  ├─ test_reloading.py
   │     │  │  ├─ test_scripts.py
   │     │  │  ├─ test_warnings.py
   │     │  │  ├─ test__all__.py
   │     │  │  └─ __init__.py
   │     │  ├─ typing
   │     │  │  ├─ mypy_plugin.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ fail
   │     │  │  │  │  │  ├─ arithmetic.pyi
   │     │  │  │  │  │  ├─ arrayprint.pyi
   │     │  │  │  │  │  ├─ arrayterator.pyi
   │     │  │  │  │  │  ├─ array_constructors.pyi
   │     │  │  │  │  │  ├─ array_like.pyi
   │     │  │  │  │  │  ├─ array_pad.pyi
   │     │  │  │  │  │  ├─ bitwise_ops.pyi
   │     │  │  │  │  │  ├─ char.pyi
   │     │  │  │  │  │  ├─ chararray.pyi
   │     │  │  │  │  │  ├─ comparisons.pyi
   │     │  │  │  │  │  ├─ constants.pyi
   │     │  │  │  │  │  ├─ datasource.pyi
   │     │  │  │  │  │  ├─ dtype.pyi
   │     │  │  │  │  │  ├─ einsumfunc.pyi
   │     │  │  │  │  │  ├─ flatiter.pyi
   │     │  │  │  │  │  ├─ fromnumeric.pyi
   │     │  │  │  │  │  ├─ histograms.pyi
   │     │  │  │  │  │  ├─ index_tricks.pyi
   │     │  │  │  │  │  ├─ lib_function_base.pyi
   │     │  │  │  │  │  ├─ lib_polynomial.pyi
   │     │  │  │  │  │  ├─ lib_utils.pyi
   │     │  │  │  │  │  ├─ lib_version.pyi
   │     │  │  │  │  │  ├─ linalg.pyi
   │     │  │  │  │  │  ├─ memmap.pyi
   │     │  │  │  │  │  ├─ modules.pyi
   │     │  │  │  │  │  ├─ multiarray.pyi
   │     │  │  │  │  │  ├─ ndarray.pyi
   │     │  │  │  │  │  ├─ ndarray_misc.pyi
   │     │  │  │  │  │  ├─ nditer.pyi
   │     │  │  │  │  │  ├─ nested_sequence.pyi
   │     │  │  │  │  │  ├─ npyio.pyi
   │     │  │  │  │  │  ├─ numerictypes.pyi
   │     │  │  │  │  │  ├─ random.pyi
   │     │  │  │  │  │  ├─ rec.pyi
   │     │  │  │  │  │  ├─ scalars.pyi
   │     │  │  │  │  │  ├─ shape.pyi
   │     │  │  │  │  │  ├─ shape_base.pyi
   │     │  │  │  │  │  ├─ stride_tricks.pyi
   │     │  │  │  │  │  ├─ strings.pyi
   │     │  │  │  │  │  ├─ testing.pyi
   │     │  │  │  │  │  ├─ twodim_base.pyi
   │     │  │  │  │  │  ├─ type_check.pyi
   │     │  │  │  │  │  ├─ ufunclike.pyi
   │     │  │  │  │  │  ├─ ufuncs.pyi
   │     │  │  │  │  │  ├─ ufunc_config.pyi
   │     │  │  │  │  │  └─ warnings_and_errors.pyi
   │     │  │  │  │  ├─ misc
   │     │  │  │  │  │  └─ extended_precision.pyi
   │     │  │  │  │  ├─ mypy.ini
   │     │  │  │  │  ├─ pass
   │     │  │  │  │  │  ├─ arithmetic.py
   │     │  │  │  │  │  ├─ arrayprint.py
   │     │  │  │  │  │  ├─ arrayterator.py
   │     │  │  │  │  │  ├─ array_constructors.py
   │     │  │  │  │  │  ├─ array_like.py
   │     │  │  │  │  │  ├─ bitwise_ops.py
   │     │  │  │  │  │  ├─ comparisons.py
   │     │  │  │  │  │  ├─ dtype.py
   │     │  │  │  │  │  ├─ einsumfunc.py
   │     │  │  │  │  │  ├─ flatiter.py
   │     │  │  │  │  │  ├─ fromnumeric.py
   │     │  │  │  │  │  ├─ index_tricks.py
   │     │  │  │  │  │  ├─ lib_user_array.py
   │     │  │  │  │  │  ├─ lib_utils.py
   │     │  │  │  │  │  ├─ lib_version.py
   │     │  │  │  │  │  ├─ literal.py
   │     │  │  │  │  │  ├─ ma.py
   │     │  │  │  │  │  ├─ mod.py
   │     │  │  │  │  │  ├─ modules.py
   │     │  │  │  │  │  ├─ multiarray.py
   │     │  │  │  │  │  ├─ ndarray_conversion.py
   │     │  │  │  │  │  ├─ ndarray_misc.py
   │     │  │  │  │  │  ├─ ndarray_shape_manipulation.py
   │     │  │  │  │  │  ├─ nditer.py
   │     │  │  │  │  │  ├─ numeric.py
   │     │  │  │  │  │  ├─ numerictypes.py
   │     │  │  │  │  │  ├─ random.py
   │     │  │  │  │  │  ├─ recfunctions.py
   │     │  │  │  │  │  ├─ scalars.py
   │     │  │  │  │  │  ├─ shape.py
   │     │  │  │  │  │  ├─ simple.py
   │     │  │  │  │  │  ├─ simple_py3.py
   │     │  │  │  │  │  ├─ ufunclike.py
   │     │  │  │  │  │  ├─ ufuncs.py
   │     │  │  │  │  │  ├─ ufunc_config.py
   │     │  │  │  │  │  └─ warnings_and_errors.py
   │     │  │  │  │  └─ reveal
   │     │  │  │  │     ├─ arithmetic.pyi
   │     │  │  │  │     ├─ arraypad.pyi
   │     │  │  │  │     ├─ arrayprint.pyi
   │     │  │  │  │     ├─ arraysetops.pyi
   │     │  │  │  │     ├─ arrayterator.pyi
   │     │  │  │  │     ├─ array_api_info.pyi
   │     │  │  │  │     ├─ array_constructors.pyi
   │     │  │  │  │     ├─ bitwise_ops.pyi
   │     │  │  │  │     ├─ char.pyi
   │     │  │  │  │     ├─ chararray.pyi
   │     │  │  │  │     ├─ comparisons.pyi
   │     │  │  │  │     ├─ constants.pyi
   │     │  │  │  │     ├─ ctypeslib.pyi
   │     │  │  │  │     ├─ datasource.pyi
   │     │  │  │  │     ├─ dtype.pyi
   │     │  │  │  │     ├─ einsumfunc.pyi
   │     │  │  │  │     ├─ emath.pyi
   │     │  │  │  │     ├─ fft.pyi
   │     │  │  │  │     ├─ flatiter.pyi
   │     │  │  │  │     ├─ fromnumeric.pyi
   │     │  │  │  │     ├─ getlimits.pyi
   │     │  │  │  │     ├─ histograms.pyi
   │     │  │  │  │     ├─ index_tricks.pyi
   │     │  │  │  │     ├─ lib_function_base.pyi
   │     │  │  │  │     ├─ lib_polynomial.pyi
   │     │  │  │  │     ├─ lib_utils.pyi
   │     │  │  │  │     ├─ lib_version.pyi
   │     │  │  │  │     ├─ linalg.pyi
   │     │  │  │  │     ├─ matrix.pyi
   │     │  │  │  │     ├─ memmap.pyi
   │     │  │  │  │     ├─ mod.pyi
   │     │  │  │  │     ├─ modules.pyi
   │     │  │  │  │     ├─ multiarray.pyi
   │     │  │  │  │     ├─ nbit_base_example.pyi
   │     │  │  │  │     ├─ ndarray_assignability.pyi
   │     │  │  │  │     ├─ ndarray_conversion.pyi
   │     │  │  │  │     ├─ ndarray_misc.pyi
   │     │  │  │  │     ├─ ndarray_shape_manipulation.pyi
   │     │  │  │  │     ├─ nditer.pyi
   │     │  │  │  │     ├─ nested_sequence.pyi
   │     │  │  │  │     ├─ npyio.pyi
   │     │  │  │  │     ├─ numeric.pyi
   │     │  │  │  │     ├─ numerictypes.pyi
   │     │  │  │  │     ├─ polynomial_polybase.pyi
   │     │  │  │  │     ├─ polynomial_polyutils.pyi
   │     │  │  │  │     ├─ polynomial_series.pyi
   │     │  │  │  │     ├─ random.pyi
   │     │  │  │  │     ├─ rec.pyi
   │     │  │  │  │     ├─ scalars.pyi
   │     │  │  │  │     ├─ shape.pyi
   │     │  │  │  │     ├─ shape_base.pyi
   │     │  │  │  │     ├─ stride_tricks.pyi
   │     │  │  │  │     ├─ strings.pyi
   │     │  │  │  │     ├─ testing.pyi
   │     │  │  │  │     ├─ twodim_base.pyi
   │     │  │  │  │     ├─ type_check.pyi
   │     │  │  │  │     ├─ ufunclike.pyi
   │     │  │  │  │     ├─ ufuncs.pyi
   │     │  │  │  │     ├─ ufunc_config.pyi
   │     │  │  │  │     └─ warnings_and_errors.pyi
   │     │  │  │  ├─ test_isfile.py
   │     │  │  │  ├─ test_runtime.py
   │     │  │  │  ├─ test_typing.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ version.py
   │     │  ├─ version.pyi
   │     │  ├─ _array_api_info.py
   │     │  ├─ _array_api_info.pyi
   │     │  ├─ _configtool.py
   │     │  ├─ _configtool.pyi
   │     │  ├─ _core
   │     │  │  ├─ arrayprint.py
   │     │  │  ├─ arrayprint.pyi
   │     │  │  ├─ cversions.py
   │     │  │  ├─ defchararray.py
   │     │  │  ├─ defchararray.pyi
   │     │  │  ├─ einsumfunc.py
   │     │  │  ├─ einsumfunc.pyi
   │     │  │  ├─ fromnumeric.py
   │     │  │  ├─ fromnumeric.pyi
   │     │  │  ├─ function_base.py
   │     │  │  ├─ function_base.pyi
   │     │  │  ├─ getlimits.py
   │     │  │  ├─ getlimits.pyi
   │     │  │  ├─ include
   │     │  │  │  └─ numpy
   │     │  │  │     ├─ arrayobject.h
   │     │  │  │     ├─ arrayscalars.h
   │     │  │  │     ├─ dtype_api.h
   │     │  │  │     ├─ halffloat.h
   │     │  │  │     ├─ ndarrayobject.h
   │     │  │  │     ├─ ndarraytypes.h
   │     │  │  │     ├─ npy_1_7_deprecated_api.h
   │     │  │  │     ├─ npy_2_compat.h
   │     │  │  │     ├─ npy_2_complexcompat.h
   │     │  │  │     ├─ npy_3kcompat.h
   │     │  │  │     ├─ npy_common.h
   │     │  │  │     ├─ npy_cpu.h
   │     │  │  │     ├─ npy_endian.h
   │     │  │  │     ├─ npy_math.h
   │     │  │  │     ├─ npy_no_deprecated_api.h
   │     │  │  │     ├─ npy_os.h
   │     │  │  │     ├─ numpyconfig.h
   │     │  │  │     ├─ random
   │     │  │  │     │  ├─ bitgen.h
   │     │  │  │     │  ├─ distributions.h
   │     │  │  │     │  ├─ libdivide.h
   │     │  │  │     │  └─ LICENSE.txt
   │     │  │  │     ├─ ufuncobject.h
   │     │  │  │     ├─ utils.h
   │     │  │  │     ├─ _neighborhood_iterator_imp.h
   │     │  │  │     ├─ _numpyconfig.h
   │     │  │  │     ├─ _public_dtype_api_table.h
   │     │  │  │     ├─ __multiarray_api.c
   │     │  │  │     ├─ __multiarray_api.h
   │     │  │  │     ├─ __ufunc_api.c
   │     │  │  │     └─ __ufunc_api.h
   │     │  │  ├─ lib
   │     │  │  │  ├─ npy-pkg-config
   │     │  │  │  │  ├─ mlib.ini
   │     │  │  │  │  └─ npymath.ini
   │     │  │  │  ├─ npymath.lib
   │     │  │  │  └─ pkgconfig
   │     │  │  │     └─ numpy.pc
   │     │  │  ├─ memmap.py
   │     │  │  ├─ memmap.pyi
   │     │  │  ├─ multiarray.py
   │     │  │  ├─ multiarray.pyi
   │     │  │  ├─ numeric.py
   │     │  │  ├─ numeric.pyi
   │     │  │  ├─ numerictypes.py
   │     │  │  ├─ numerictypes.pyi
   │     │  │  ├─ overrides.py
   │     │  │  ├─ overrides.pyi
   │     │  │  ├─ printoptions.py
   │     │  │  ├─ printoptions.pyi
   │     │  │  ├─ records.py
   │     │  │  ├─ records.pyi
   │     │  │  ├─ shape_base.py
   │     │  │  ├─ shape_base.pyi
   │     │  │  ├─ strings.py
   │     │  │  ├─ strings.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ astype_copy.pkl
   │     │  │  │  │  ├─ generate_umath_validation_data.cpp
   │     │  │  │  │  ├─ recarray_from_file.fits
   │     │  │  │  │  ├─ umath-validation-set-arccos.csv
   │     │  │  │  │  ├─ umath-validation-set-arccosh.csv
   │     │  │  │  │  ├─ umath-validation-set-arcsin.csv
   │     │  │  │  │  ├─ umath-validation-set-arcsinh.csv
   │     │  │  │  │  ├─ umath-validation-set-arctan.csv
   │     │  │  │  │  ├─ umath-validation-set-arctanh.csv
   │     │  │  │  │  ├─ umath-validation-set-cbrt.csv
   │     │  │  │  │  ├─ umath-validation-set-cos.csv
   │     │  │  │  │  ├─ umath-validation-set-cosh.csv
   │     │  │  │  │  ├─ umath-validation-set-exp.csv
   │     │  │  │  │  ├─ umath-validation-set-exp2.csv
   │     │  │  │  │  ├─ umath-validation-set-expm1.csv
   │     │  │  │  │  ├─ umath-validation-set-log.csv
   │     │  │  │  │  ├─ umath-validation-set-log10.csv
   │     │  │  │  │  ├─ umath-validation-set-log1p.csv
   │     │  │  │  │  ├─ umath-validation-set-log2.csv
   │     │  │  │  │  ├─ umath-validation-set-README.txt
   │     │  │  │  │  ├─ umath-validation-set-sin.csv
   │     │  │  │  │  ├─ umath-validation-set-sinh.csv
   │     │  │  │  │  ├─ umath-validation-set-tan.csv
   │     │  │  │  │  └─ umath-validation-set-tanh.csv
   │     │  │  │  ├─ examples
   │     │  │  │  │  ├─ cython
   │     │  │  │  │  │  ├─ checks.pyx
   │     │  │  │  │  │  └─ setup.py
   │     │  │  │  │  └─ limited_api
   │     │  │  │  │     ├─ limited_api1.c
   │     │  │  │  │     ├─ limited_api2.pyx
   │     │  │  │  │     ├─ limited_api_latest.c
   │     │  │  │  │     └─ setup.py
   │     │  │  │  ├─ test_abc.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_argparse.py
   │     │  │  │  ├─ test_arraymethod.py
   │     │  │  │  ├─ test_arrayobject.py
   │     │  │  │  ├─ test_arrayprint.py
   │     │  │  │  ├─ test_array_api_info.py
   │     │  │  │  ├─ test_array_coercion.py
   │     │  │  │  ├─ test_array_interface.py
   │     │  │  │  ├─ test_casting_floatingpoint_errors.py
   │     │  │  │  ├─ test_casting_unittests.py
   │     │  │  │  ├─ test_conversion_utils.py
   │     │  │  │  ├─ test_cpu_dispatcher.py
   │     │  │  │  ├─ test_cpu_features.py
   │     │  │  │  ├─ test_custom_dtypes.py
   │     │  │  │  ├─ test_cython.py
   │     │  │  │  ├─ test_datetime.py
   │     │  │  │  ├─ test_defchararray.py
   │     │  │  │  ├─ test_deprecations.py
   │     │  │  │  ├─ test_dlpack.py
   │     │  │  │  ├─ test_dtype.py
   │     │  │  │  ├─ test_einsum.py
   │     │  │  │  ├─ test_errstate.py
   │     │  │  │  ├─ test_extint128.py
   │     │  │  │  ├─ test_function_base.py
   │     │  │  │  ├─ test_getlimits.py
   │     │  │  │  ├─ test_half.py
   │     │  │  │  ├─ test_hashtable.py
   │     │  │  │  ├─ test_indexerrors.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_item_selection.py
   │     │  │  │  ├─ test_limited_api.py
   │     │  │  │  ├─ test_longdouble.py
   │     │  │  │  ├─ test_machar.py
   │     │  │  │  ├─ test_memmap.py
   │     │  │  │  ├─ test_mem_overlap.py
   │     │  │  │  ├─ test_mem_policy.py
   │     │  │  │  ├─ test_multiarray.py
   │     │  │  │  ├─ test_multithreading.py
   │     │  │  │  ├─ test_nditer.py
   │     │  │  │  ├─ test_nep50_promotions.py
   │     │  │  │  ├─ test_numeric.py
   │     │  │  │  ├─ test_numerictypes.py
   │     │  │  │  ├─ test_overrides.py
   │     │  │  │  ├─ test_print.py
   │     │  │  │  ├─ test_protocols.py
   │     │  │  │  ├─ test_records.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_scalarbuffer.py
   │     │  │  │  ├─ test_scalarinherit.py
   │     │  │  │  ├─ test_scalarmath.py
   │     │  │  │  ├─ test_scalarprint.py
   │     │  │  │  ├─ test_scalar_ctors.py
   │     │  │  │  ├─ test_scalar_methods.py
   │     │  │  │  ├─ test_shape_base.py
   │     │  │  │  ├─ test_simd.py
   │     │  │  │  ├─ test_simd_module.py
   │     │  │  │  ├─ test_stringdtype.py
   │     │  │  │  ├─ test_strings.py
   │     │  │  │  ├─ test_ufunc.py
   │     │  │  │  ├─ test_umath.py
   │     │  │  │  ├─ test_umath_accuracy.py
   │     │  │  │  ├─ test_umath_complex.py
   │     │  │  │  ├─ test_unicode.py
   │     │  │  │  ├─ test__exceptions.py
   │     │  │  │  ├─ _locales.py
   │     │  │  │  └─ _natype.py
   │     │  │  ├─ umath.py
   │     │  │  ├─ umath.pyi
   │     │  │  ├─ _add_newdocs.py
   │     │  │  ├─ _add_newdocs.pyi
   │     │  │  ├─ _add_newdocs_scalars.py
   │     │  │  ├─ _add_newdocs_scalars.pyi
   │     │  │  ├─ _asarray.py
   │     │  │  ├─ _asarray.pyi
   │     │  │  ├─ _dtype.py
   │     │  │  ├─ _dtype.pyi
   │     │  │  ├─ _dtype_ctypes.py
   │     │  │  ├─ _dtype_ctypes.pyi
   │     │  │  ├─ _exceptions.py
   │     │  │  ├─ _exceptions.pyi
   │     │  │  ├─ _internal.py
   │     │  │  ├─ _internal.pyi
   │     │  │  ├─ _machar.py
   │     │  │  ├─ _machar.pyi
   │     │  │  ├─ _methods.py
   │     │  │  ├─ _methods.pyi
   │     │  │  ├─ _multiarray_tests.cp310-win_amd64.lib
   │     │  │  ├─ _multiarray_umath.cp310-win_amd64.lib
   │     │  │  ├─ _operand_flag_tests.cp310-win_amd64.lib
   │     │  │  ├─ _rational_tests.cp310-win_amd64.lib
   │     │  │  ├─ _simd.cp310-win_amd64.lib
   │     │  │  ├─ _simd.pyi
   │     │  │  ├─ _string_helpers.py
   │     │  │  ├─ _string_helpers.pyi
   │     │  │  ├─ _struct_ufunc_tests.cp310-win_amd64.lib
   │     │  │  ├─ _type_aliases.py
   │     │  │  ├─ _type_aliases.pyi
   │     │  │  ├─ _ufunc_config.py
   │     │  │  ├─ _ufunc_config.pyi
   │     │  │  ├─ _umath_tests.cp310-win_amd64.lib
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ _distributor_init.py
   │     │  ├─ _distributor_init.pyi
   │     │  ├─ _expired_attrs_2_0.py
   │     │  ├─ _expired_attrs_2_0.pyi
   │     │  ├─ _globals.py
   │     │  ├─ _globals.pyi
   │     │  ├─ _pyinstaller
   │     │  │  ├─ hook-numpy.py
   │     │  │  ├─ hook-numpy.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ pyinstaller-smoke.py
   │     │  │  │  ├─ test_pyinstaller.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ _pytesttester.py
   │     │  ├─ _pytesttester.pyi
   │     │  ├─ _typing
   │     │  │  ├─ _add_docstring.py
   │     │  │  ├─ _array_like.py
   │     │  │  ├─ _callable.pyi
   │     │  │  ├─ _char_codes.py
   │     │  │  ├─ _dtype_like.py
   │     │  │  ├─ _extended_precision.py
   │     │  │  ├─ _nbit.py
   │     │  │  ├─ _nbit_base.py
   │     │  │  ├─ _nested_sequence.py
   │     │  │  ├─ _scalars.py
   │     │  │  ├─ _shape.py
   │     │  │  ├─ _ufunc.py
   │     │  │  ├─ _ufunc.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ _utils
   │     │  │  ├─ _convertions.py
   │     │  │  ├─ _convertions.pyi
   │     │  │  ├─ _inspect.py
   │     │  │  ├─ _inspect.pyi
   │     │  │  ├─ _pep440.py
   │     │  │  ├─ _pep440.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ __config__.py
   │     │  ├─ __config__.pyi
   │     │  ├─ __init__.cython-30.pxd
   │     │  ├─ __init__.pxd
   │     │  ├─ __init__.py
   │     │  └─ __init__.pyi
   │     ├─ numpy-2.2.6-cp310-cp310-win_amd64.whl
   │     ├─ numpy-2.2.6.dist-info
   │     │  ├─ DELVEWHEEL
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ numpy.libs
   │     │  ├─ libscipy_openblas64_-13e2df515630b4a41f92893938845698.dll
   │     │  └─ msvcp140-263139962577ecda4cd9469ca360a746.dll
   │     ├─ optbinning
   │     │  ├─ binning
   │     │  │  ├─ auto_monotonic.py
   │     │  │  ├─ base.py
   │     │  │  ├─ binning.py
   │     │  │  ├─ binning_information.py
   │     │  │  ├─ binning_process.py
   │     │  │  ├─ binning_process_information.py
   │     │  │  ├─ binning_statistics.py
   │     │  │  ├─ continuous_binning.py
   │     │  │  ├─ continuous_cp.py
   │     │  │  ├─ cp.py
   │     │  │  ├─ distributed
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ binning_process_sketch.py
   │     │  │  │  ├─ binning_process_sketch_information.py
   │     │  │  │  ├─ binning_sketch.py
   │     │  │  │  ├─ bsketch.py
   │     │  │  │  ├─ bsketch_information.py
   │     │  │  │  ├─ gk.py
   │     │  │  │  ├─ plots.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ls.py
   │     │  │  ├─ mdlp.py
   │     │  │  ├─ metrics.py
   │     │  │  ├─ mip.py
   │     │  │  ├─ model_data.py
   │     │  │  ├─ multiclass_binning.py
   │     │  │  ├─ multiclass_cp.py
   │     │  │  ├─ multiclass_mip.py
   │     │  │  ├─ multidimensional
   │     │  │  │  ├─ binning_2d.py
   │     │  │  │  ├─ binning_statistics_2d.py
   │     │  │  │  ├─ continuous_binning_2d.py
   │     │  │  │  ├─ cp_2d.py
   │     │  │  │  ├─ mip_2d.py
   │     │  │  │  ├─ model_data_2d.py
   │     │  │  │  ├─ model_data_cart_2d.py
   │     │  │  │  ├─ preprocessing_2d.py
   │     │  │  │  ├─ transformations_2d.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ outlier.py
   │     │  │  ├─ piecewise
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ binning.py
   │     │  │  │  ├─ binning_information.py
   │     │  │  │  ├─ binning_statistics.py
   │     │  │  │  ├─ continuous_binning.py
   │     │  │  │  ├─ metrics.py
   │     │  │  │  ├─ transformations.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ prebinning.py
   │     │  │  ├─ preprocessing.py
   │     │  │  ├─ transformations.py
   │     │  │  ├─ uncertainty
   │     │  │  │  ├─ binning_scenarios.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ exceptions.py
   │     │  ├─ formatting.py
   │     │  ├─ information.py
   │     │  ├─ logging.py
   │     │  ├─ metrics
   │     │  │  ├─ classification.py
   │     │  │  ├─ regression.py
   │     │  │  └─ __init__.py
   │     │  ├─ options.py
   │     │  ├─ scorecard
   │     │  │  ├─ counterfactual
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ counterfactual.py
   │     │  │  │  ├─ counterfactual_information.py
   │     │  │  │  ├─ mip.py
   │     │  │  │  ├─ model_data.py
   │     │  │  │  ├─ multi_mip.py
   │     │  │  │  ├─ problem_data.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ monitoring.py
   │     │  │  ├─ monitoring_information.py
   │     │  │  ├─ plots.py
   │     │  │  ├─ rounding.py
   │     │  │  ├─ scorecard.py
   │     │  │  ├─ scorecard_information.py
   │     │  │  └─ __init__.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ optbinning-0.21.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ optree
   │     │  ├─ accessors.py
   │     │  ├─ dataclasses.py
   │     │  ├─ functools.py
   │     │  ├─ integrations
   │     │  │  ├─ attrs.py
   │     │  │  ├─ jax.py
   │     │  │  ├─ numpy.py
   │     │  │  ├─ torch.py
   │     │  │  └─ __init__.py
   │     │  ├─ ops.py
   │     │  ├─ py.typed
   │     │  ├─ pytree.py
   │     │  ├─ registry.py
   │     │  ├─ treespec.py
   │     │  ├─ typing.py
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ _C.pyi
   │     │  └─ __init__.py
   │     ├─ optree-0.20.0.dist-info
   │     │  ├─ DELVEWHEEL
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ optree.libs
   │     │  └─ msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
   │     ├─ opt_einsum
   │     │  ├─ backends
   │     │  │  ├─ cupy.py
   │     │  │  ├─ dispatch.py
   │     │  │  ├─ jax.py
   │     │  │  ├─ object_arrays.py
   │     │  │  ├─ tensorflow.py
   │     │  │  ├─ theano.py
   │     │  │  ├─ torch.py
   │     │  │  └─ __init__.py
   │     │  ├─ blas.py
   │     │  ├─ contract.py
   │     │  ├─ helpers.py
   │     │  ├─ parser.py
   │     │  ├─ paths.py
   │     │  ├─ path_random.py
   │     │  ├─ sharing.py
   │     │  ├─ testing.py
   │     │  ├─ tests
   │     │  │  ├─ test_backends.py
   │     │  │  ├─ test_blas.py
   │     │  │  ├─ test_contract.py
   │     │  │  ├─ test_edge_cases.py
   │     │  │  ├─ test_input.py
   │     │  │  ├─ test_parser.py
   │     │  │  ├─ test_paths.py
   │     │  │  ├─ test_sharing.py
   │     │  │  └─ __init__.py
   │     │  ├─ typing.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ opt_einsum-3.4.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ ortools
   │     │  ├─ algorithms
   │     │  │  ├─ python
   │     │  │  │  ├─ knapsack_solver.pyi
   │     │  │  │  ├─ set_cover.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ set_cover_pb2.py
   │     │  │  └─ __init__.py
   │     │  ├─ bop
   │     │  │  ├─ bop_parameters_pb2.py
   │     │  │  ├─ bop_parameters_pb2.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ constraint_solver
   │     │  │  ├─ assignment_pb2.py
   │     │  │  ├─ assignment_pb2.pyi
   │     │  │  ├─ pywrapcp.py
   │     │  │  ├─ pywrapcp.pyi
   │     │  │  ├─ routing_enums_pb2.py
   │     │  │  ├─ routing_enums_pb2.pyi
   │     │  │  ├─ routing_ils_pb2.py
   │     │  │  ├─ routing_ils_pb2.pyi
   │     │  │  ├─ routing_parameters_pb2.py
   │     │  │  ├─ routing_parameters_pb2.pyi
   │     │  │  ├─ search_limit_pb2.py
   │     │  │  ├─ search_limit_pb2.pyi
   │     │  │  ├─ search_stats_pb2.py
   │     │  │  ├─ search_stats_pb2.pyi
   │     │  │  ├─ solver_parameters_pb2.py
   │     │  │  ├─ solver_parameters_pb2.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ glop
   │     │  │  ├─ parameters_pb2.py
   │     │  │  ├─ parameters_pb2.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ graph
   │     │  │  ├─ flow_problem_pb2.py
   │     │  │  ├─ python
   │     │  │  │  ├─ linear_sum_assignment.pyi
   │     │  │  │  ├─ max_flow.pyi
   │     │  │  │  ├─ min_cost_flow.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ gscip
   │     │  │  ├─ gscip_pb2.py
   │     │  │  ├─ gscip_pb2.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ init
   │     │  │  ├─ python
   │     │  │  │  ├─ init.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ linear_solver
   │     │  │  ├─ linear_solver_pb2.py
   │     │  │  ├─ linear_solver_pb2.pyi
   │     │  │  ├─ python
   │     │  │  │  ├─ linear_solver_natural_api.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pywraplp.py
   │     │  │  ├─ pywraplp.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ math_opt
   │     │  │  ├─ callback_pb2.py
   │     │  │  ├─ callback_pb2.pyi
   │     │  │  ├─ core
   │     │  │  │  ├─ python
   │     │  │  │  │  ├─ solver.pyi
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ infeasible_subsystem_pb2.py
   │     │  │  ├─ infeasible_subsystem_pb2.pyi
   │     │  │  ├─ model_parameters_pb2.py
   │     │  │  ├─ model_parameters_pb2.pyi
   │     │  │  ├─ model_pb2.py
   │     │  │  ├─ model_pb2.pyi
   │     │  │  ├─ model_update_pb2.py
   │     │  │  ├─ model_update_pb2.pyi
   │     │  │  ├─ parameters_pb2.py
   │     │  │  ├─ parameters_pb2.pyi
   │     │  │  ├─ python
   │     │  │  │  ├─ callback.py
   │     │  │  │  ├─ compute_infeasible_subsystem_result.py
   │     │  │  │  ├─ errors.py
   │     │  │  │  ├─ expressions.py
   │     │  │  │  ├─ hash_model_storage.py
   │     │  │  │  ├─ ipc
   │     │  │  │  │  ├─ proto_converter.py
   │     │  │  │  │  ├─ remote_http_solve.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ mathopt.py
   │     │  │  │  ├─ message_callback.py
   │     │  │  │  ├─ model.py
   │     │  │  │  ├─ model_parameters.py
   │     │  │  │  ├─ model_storage.py
   │     │  │  │  ├─ normalize.py
   │     │  │  │  ├─ parameters.py
   │     │  │  │  ├─ result.py
   │     │  │  │  ├─ solution.py
   │     │  │  │  ├─ solve.py
   │     │  │  │  ├─ solver_resources.py
   │     │  │  │  ├─ sparse_containers.py
   │     │  │  │  ├─ statistics.py
   │     │  │  │  ├─ testing
   │     │  │  │  │  ├─ compare_proto.py
   │     │  │  │  │  ├─ proto_matcher.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ result_pb2.py
   │     │  │  ├─ result_pb2.pyi
   │     │  │  ├─ rpc_pb2.py
   │     │  │  ├─ rpc_pb2.pyi
   │     │  │  ├─ solution_pb2.py
   │     │  │  ├─ solution_pb2.pyi
   │     │  │  ├─ solvers
   │     │  │  │  ├─ glpk_pb2.py
   │     │  │  │  ├─ glpk_pb2.pyi
   │     │  │  │  ├─ gurobi_pb2.py
   │     │  │  │  ├─ gurobi_pb2.pyi
   │     │  │  │  ├─ highs_pb2.py
   │     │  │  │  ├─ highs_pb2.pyi
   │     │  │  │  ├─ osqp_pb2.py
   │     │  │  │  ├─ osqp_pb2.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sparse_containers_pb2.py
   │     │  │  ├─ sparse_containers_pb2.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ packing
   │     │  │  ├─ multiple_dimensions_bin_packing_pb2.py
   │     │  │  ├─ multiple_dimensions_bin_packing_pb2.pyi
   │     │  │  ├─ vector_bin_packing_pb2.py
   │     │  │  ├─ vector_bin_packing_pb2.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ pdlp
   │     │  │  ├─ python
   │     │  │  │  ├─ pdlp.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ solvers_pb2.py
   │     │  │  ├─ solvers_pb2.pyi
   │     │  │  ├─ solve_log_pb2.py
   │     │  │  ├─ solve_log_pb2.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ sat
   │     │  │  ├─ boolean_problem_pb2.py
   │     │  │  ├─ boolean_problem_pb2.pyi
   │     │  │  ├─ colab
   │     │  │  │  ├─ flags.py
   │     │  │  │  ├─ visualization.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cp_model_pb2.py
   │     │  │  ├─ cp_model_pb2.pyi
   │     │  │  ├─ cp_model_service_pb2.py
   │     │  │  ├─ cp_model_service_pb2.pyi
   │     │  │  ├─ python
   │     │  │  │  ├─ cp_model.py
   │     │  │  │  ├─ cp_model_helper.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ swig_helper.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sat_parameters_pb2.py
   │     │  │  ├─ sat_parameters_pb2.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ scheduling
   │     │  │  ├─ course_scheduling_pb2.py
   │     │  │  ├─ jobshop_scheduling_pb2.py
   │     │  │  ├─ python
   │     │  │  │  ├─ .tmpyrrh6s
   │     │  │  │  ├─ rcpsp.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ rcpsp_pb2.py
   │     │  │  └─ __init__.py
   │     │  ├─ service
   │     │  │  ├─ v1
   │     │  │  │  ├─ mathopt
   │     │  │  │  │  ├─ model_parameters_pb2.py
   │     │  │  │  │  ├─ model_parameters_pb2.pyi
   │     │  │  │  │  ├─ model_pb2.py
   │     │  │  │  │  ├─ model_pb2.pyi
   │     │  │  │  │  ├─ parameters_pb2.py
   │     │  │  │  │  ├─ parameters_pb2.pyi
   │     │  │  │  │  ├─ result_pb2.py
   │     │  │  │  │  ├─ result_pb2.pyi
   │     │  │  │  │  ├─ solution_pb2.py
   │     │  │  │  │  ├─ solution_pb2.pyi
   │     │  │  │  │  ├─ sparse_containers_pb2.py
   │     │  │  │  │  ├─ sparse_containers_pb2.pyi
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ optimization_pb2.py
   │     │  │  │  ├─ optimization_pb2.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ util
   │     │  │  ├─ int128_pb2.py
   │     │  │  ├─ optional_boolean_pb2.py
   │     │  │  ├─ python
   │     │  │  │  ├─ sorted_interval_list.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ ortools-9.11.4210.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ osqp
   │     │  ├─ builtin.py
   │     │  ├─ codegen
   │     │  │  ├─ codegen_src
   │     │  │  │  ├─ inc
   │     │  │  │  │  ├─ private
   │     │  │  │  │  │  ├─ algebra_impl.h
   │     │  │  │  │  │  ├─ algebra_matrix.h
   │     │  │  │  │  │  ├─ algebra_vector.h
   │     │  │  │  │  │  ├─ auxil.h
   │     │  │  │  │  │  ├─ csc_math.h
   │     │  │  │  │  │  ├─ csc_utils.h
   │     │  │  │  │  │  ├─ error.h
   │     │  │  │  │  │  ├─ glob_opts.h
   │     │  │  │  │  │  ├─ kkt.h
   │     │  │  │  │  │  ├─ lin_alg.h
   │     │  │  │  │  │  ├─ printing.h
   │     │  │  │  │  │  ├─ profilers.h
   │     │  │  │  │  │  ├─ qdldl.h
   │     │  │  │  │  │  ├─ qdldl_interface.h
   │     │  │  │  │  │  ├─ qdldl_types.h
   │     │  │  │  │  │  ├─ qdldl_version.h
   │     │  │  │  │  │  ├─ scaling.h
   │     │  │  │  │  │  ├─ timing.h
   │     │  │  │  │  │  ├─ types.h
   │     │  │  │  │  │  ├─ util.h
   │     │  │  │  │  │  └─ version.h
   │     │  │  │  │  └─ public
   │     │  │  │  │     ├─ osqp.h
   │     │  │  │  │     ├─ osqp_api_constants.h
   │     │  │  │  │     ├─ osqp_api_functions.h
   │     │  │  │  │     ├─ osqp_api_types.h
   │     │  │  │  │     └─ osqp_export_define.h
   │     │  │  │  ├─ Makefile
   │     │  │  │  └─ src
   │     │  │  │     ├─ algebra_libs.c
   │     │  │  │     ├─ auxil.c
   │     │  │  │     ├─ csc_math.c
   │     │  │  │     ├─ csc_utils.c
   │     │  │  │     ├─ error.c
   │     │  │  │     ├─ kkt.c
   │     │  │  │     ├─ matrix.c
   │     │  │  │     ├─ osqp_api.c
   │     │  │  │     ├─ qdldl.c
   │     │  │  │     ├─ qdldl_interface.c
   │     │  │  │     ├─ scaling.c
   │     │  │  │     ├─ util.c
   │     │  │  │     └─ vector.c
   │     │  │  ├─ pywrapper
   │     │  │  │  ├─ bindings.cpp.jinja
   │     │  │  │  ├─ CMakeLists.txt.jinja
   │     │  │  │  ├─ setup.py.jinja
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ cuda.py
   │     │  ├─ interface.py
   │     │  ├─ mkl.py
   │     │  ├─ nn
   │     │  │  ├─ torch.py
   │     │  │  └─ __init__.py
   │     │  ├─ tests
   │     │  │  ├─ basic_test.py
   │     │  │  ├─ codegen_matrices_test.py
   │     │  │  ├─ codegen_vectors_test.py
   │     │  │  ├─ conftest.py
   │     │  │  ├─ derivative_test.py
   │     │  │  ├─ dual_infeasibility_test.py
   │     │  │  ├─ feasibility_test.py
   │     │  │  ├─ multithread_test.py
   │     │  │  ├─ nn_test.py
   │     │  │  ├─ non_convex_test.py
   │     │  │  ├─ polishing_test.py
   │     │  │  ├─ primal_infeasibility_test.py
   │     │  │  ├─ solutions
   │     │  │  │  ├─ test_basic_QP.npz
   │     │  │  │  ├─ test_dual_infeasibility.npz
   │     │  │  │  ├─ test_feasibility_problem.npz
   │     │  │  │  ├─ test_polish_random.npz
   │     │  │  │  ├─ test_polish_simple.npz
   │     │  │  │  ├─ test_polish_unconstrained.npz
   │     │  │  │  ├─ test_primal_infeasibility.npz
   │     │  │  │  ├─ test_solve.npz
   │     │  │  │  ├─ test_unconstrained_problem.npz
   │     │  │  │  ├─ test_update_A.npz
   │     │  │  │  ├─ test_update_A_allind.npz
   │     │  │  │  ├─ test_update_bounds.npz
   │     │  │  │  ├─ test_update_l.npz
   │     │  │  │  ├─ test_update_P.npz
   │     │  │  │  ├─ test_update_P_allind.npz
   │     │  │  │  ├─ test_update_P_A_allind.npz
   │     │  │  │  ├─ test_update_P_A_indA.npz
   │     │  │  │  ├─ test_update_P_A_indP.npz
   │     │  │  │  ├─ test_update_P_A_indP_indA.npz
   │     │  │  │  ├─ test_update_q.npz
   │     │  │  │  ├─ test_update_u.npz
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ unconstrained_test.py
   │     │  │  ├─ update_matrices_test.py
   │     │  │  ├─ utils.py
   │     │  │  └─ warm_start_test.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ osqp-1.1.3.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ packaging
   │     │  ├─ dependency_groups.py
   │     │  ├─ direct_url.py
   │     │  ├─ errors.py
   │     │  ├─ licenses
   │     │  │  ├─ _spdx.py
   │     │  │  └─ __init__.py
   │     │  ├─ markers.py
   │     │  ├─ metadata.py
   │     │  ├─ py.typed
   │     │  ├─ pylock.py
   │     │  ├─ ranges.py
   │     │  ├─ requirements.py
   │     │  ├─ specifiers.py
   │     │  ├─ tags.py
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ _elffile.py
   │     │  ├─ _manylinux.py
   │     │  ├─ _musllinux.py
   │     │  ├─ _parser.py
   │     │  ├─ _ranges.py
   │     │  ├─ _structures.py
   │     │  ├─ _tokenizer.py
   │     │  └─ __init__.py
   │     ├─ packaging-26.3.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ LICENSE
   │     │  │  ├─ LICENSE.APACHE
   │     │  │  └─ LICENSE.BSD
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ pandas
   │     │  ├─ api
   │     │  │  ├─ extensions
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexers
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ interchange
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ types
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ typing
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ arrays
   │     │  │  └─ __init__.py
   │     │  ├─ compat
   │     │  │  ├─ compressors.py
   │     │  │  ├─ numpy
   │     │  │  │  ├─ function.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pickle_compat.py
   │     │  │  ├─ pyarrow.py
   │     │  │  ├─ _constants.py
   │     │  │  ├─ _optional.py
   │     │  │  └─ __init__.py
   │     │  ├─ conftest.py
   │     │  ├─ core
   │     │  │  ├─ accessor.py
   │     │  │  ├─ algorithms.py
   │     │  │  ├─ api.py
   │     │  │  ├─ apply.py
   │     │  │  ├─ arraylike.py
   │     │  │  ├─ arrays
   │     │  │  │  ├─ arrow
   │     │  │  │  │  ├─ accessors.py
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ extension_types.py
   │     │  │  │  │  ├─ _arrow_utils.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ boolean.py
   │     │  │  │  ├─ categorical.py
   │     │  │  │  ├─ datetimelike.py
   │     │  │  │  ├─ datetimes.py
   │     │  │  │  ├─ floating.py
   │     │  │  │  ├─ integer.py
   │     │  │  │  ├─ interval.py
   │     │  │  │  ├─ masked.py
   │     │  │  │  ├─ numeric.py
   │     │  │  │  ├─ numpy_.py
   │     │  │  │  ├─ period.py
   │     │  │  │  ├─ sparse
   │     │  │  │  │  ├─ accessor.py
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ scipy_sparse.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ string_.py
   │     │  │  │  ├─ string_arrow.py
   │     │  │  │  ├─ timedeltas.py
   │     │  │  │  ├─ _arrow_string_mixins.py
   │     │  │  │  ├─ _mixins.py
   │     │  │  │  ├─ _ranges.py
   │     │  │  │  ├─ _utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ array_algos
   │     │  │  │  ├─ datetimelike_accumulations.py
   │     │  │  │  ├─ masked_accumulations.py
   │     │  │  │  ├─ masked_reductions.py
   │     │  │  │  ├─ putmask.py
   │     │  │  │  ├─ quantile.py
   │     │  │  │  ├─ replace.py
   │     │  │  │  ├─ take.py
   │     │  │  │  ├─ transforms.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ base.py
   │     │  │  ├─ common.py
   │     │  │  ├─ computation
   │     │  │  │  ├─ align.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ engines.py
   │     │  │  │  ├─ eval.py
   │     │  │  │  ├─ expr.py
   │     │  │  │  ├─ expressions.py
   │     │  │  │  ├─ ops.py
   │     │  │  │  ├─ parsing.py
   │     │  │  │  ├─ pytables.py
   │     │  │  │  ├─ scope.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ config_init.py
   │     │  │  ├─ construction.py
   │     │  │  ├─ dtypes
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ astype.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ cast.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ concat.py
   │     │  │  │  ├─ dtypes.py
   │     │  │  │  ├─ generic.py
   │     │  │  │  ├─ inference.py
   │     │  │  │  ├─ missing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ flags.py
   │     │  │  ├─ frame.py
   │     │  │  ├─ generic.py
   │     │  │  ├─ groupby
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ categorical.py
   │     │  │  │  ├─ generic.py
   │     │  │  │  ├─ groupby.py
   │     │  │  │  ├─ grouper.py
   │     │  │  │  ├─ indexing.py
   │     │  │  │  ├─ numba_.py
   │     │  │  │  ├─ ops.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexers
   │     │  │  │  ├─ objects.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexes
   │     │  │  │  ├─ accessors.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ category.py
   │     │  │  │  ├─ datetimelike.py
   │     │  │  │  ├─ datetimes.py
   │     │  │  │  ├─ extension.py
   │     │  │  │  ├─ frozen.py
   │     │  │  │  ├─ interval.py
   │     │  │  │  ├─ multi.py
   │     │  │  │  ├─ period.py
   │     │  │  │  ├─ range.py
   │     │  │  │  ├─ timedeltas.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexing.py
   │     │  │  ├─ interchange
   │     │  │  │  ├─ buffer.py
   │     │  │  │  ├─ column.py
   │     │  │  │  ├─ dataframe.py
   │     │  │  │  ├─ dataframe_protocol.py
   │     │  │  │  ├─ from_dataframe.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ internals
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ array_manager.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ blocks.py
   │     │  │  │  ├─ concat.py
   │     │  │  │  ├─ construction.py
   │     │  │  │  ├─ managers.py
   │     │  │  │  ├─ ops.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ methods
   │     │  │  │  ├─ describe.py
   │     │  │  │  ├─ selectn.py
   │     │  │  │  ├─ to_dict.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ missing.py
   │     │  │  ├─ nanops.py
   │     │  │  ├─ ops
   │     │  │  │  ├─ array_ops.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ dispatch.py
   │     │  │  │  ├─ docstrings.py
   │     │  │  │  ├─ invalid.py
   │     │  │  │  ├─ mask_ops.py
   │     │  │  │  ├─ missing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ resample.py
   │     │  │  ├─ reshape
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ concat.py
   │     │  │  │  ├─ encoding.py
   │     │  │  │  ├─ melt.py
   │     │  │  │  ├─ merge.py
   │     │  │  │  ├─ pivot.py
   │     │  │  │  ├─ reshape.py
   │     │  │  │  ├─ tile.py
   │     │  │  │  ├─ util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ roperator.py
   │     │  │  ├─ sample.py
   │     │  │  ├─ series.py
   │     │  │  ├─ shared_docs.py
   │     │  │  ├─ sorting.py
   │     │  │  ├─ sparse
   │     │  │  │  ├─ api.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ strings
   │     │  │  │  ├─ accessor.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ object_array.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tools
   │     │  │  │  ├─ datetimes.py
   │     │  │  │  ├─ numeric.py
   │     │  │  │  ├─ timedeltas.py
   │     │  │  │  ├─ times.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ util
   │     │  │  │  ├─ hashing.py
   │     │  │  │  ├─ numba_.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ window
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ doc.py
   │     │  │  │  ├─ ewm.py
   │     │  │  │  ├─ expanding.py
   │     │  │  │  ├─ numba_.py
   │     │  │  │  ├─ online.py
   │     │  │  │  ├─ rolling.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _numba
   │     │  │  │  ├─ executor.py
   │     │  │  │  ├─ extensions.py
   │     │  │  │  ├─ kernels
   │     │  │  │  │  ├─ mean_.py
   │     │  │  │  │  ├─ min_max_.py
   │     │  │  │  │  ├─ shared.py
   │     │  │  │  │  ├─ sum_.py
   │     │  │  │  │  ├─ var_.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ errors
   │     │  │  └─ __init__.py
   │     │  ├─ io
   │     │  │  ├─ api.py
   │     │  │  ├─ clipboard
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ clipboards.py
   │     │  │  ├─ common.py
   │     │  │  ├─ excel
   │     │  │  │  ├─ _base.py
   │     │  │  │  ├─ _calamine.py
   │     │  │  │  ├─ _odfreader.py
   │     │  │  │  ├─ _odswriter.py
   │     │  │  │  ├─ _openpyxl.py
   │     │  │  │  ├─ _pyxlsb.py
   │     │  │  │  ├─ _util.py
   │     │  │  │  ├─ _xlrd.py
   │     │  │  │  ├─ _xlsxwriter.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ feather_format.py
   │     │  │  ├─ formats
   │     │  │  │  ├─ console.py
   │     │  │  │  ├─ css.py
   │     │  │  │  ├─ csvs.py
   │     │  │  │  ├─ excel.py
   │     │  │  │  ├─ format.py
   │     │  │  │  ├─ html.py
   │     │  │  │  ├─ info.py
   │     │  │  │  ├─ printing.py
   │     │  │  │  ├─ string.py
   │     │  │  │  ├─ style.py
   │     │  │  │  ├─ style_render.py
   │     │  │  │  ├─ templates
   │     │  │  │  │  ├─ html.tpl
   │     │  │  │  │  ├─ html_style.tpl
   │     │  │  │  │  ├─ html_table.tpl
   │     │  │  │  │  ├─ latex.tpl
   │     │  │  │  │  ├─ latex_longtable.tpl
   │     │  │  │  │  ├─ latex_table.tpl
   │     │  │  │  │  └─ string.tpl
   │     │  │  │  ├─ xml.py
   │     │  │  │  ├─ _color_data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ gbq.py
   │     │  │  ├─ html.py
   │     │  │  ├─ json
   │     │  │  │  ├─ _json.py
   │     │  │  │  ├─ _normalize.py
   │     │  │  │  ├─ _table_schema.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ orc.py
   │     │  │  ├─ parquet.py
   │     │  │  ├─ parsers
   │     │  │  │  ├─ arrow_parser_wrapper.py
   │     │  │  │  ├─ base_parser.py
   │     │  │  │  ├─ c_parser_wrapper.py
   │     │  │  │  ├─ python_parser.py
   │     │  │  │  ├─ readers.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pickle.py
   │     │  │  ├─ pytables.py
   │     │  │  ├─ sas
   │     │  │  │  ├─ sas7bdat.py
   │     │  │  │  ├─ sasreader.py
   │     │  │  │  ├─ sas_constants.py
   │     │  │  │  ├─ sas_xport.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ spss.py
   │     │  │  ├─ sql.py
   │     │  │  ├─ stata.py
   │     │  │  ├─ xml.py
   │     │  │  ├─ _util.py
   │     │  │  └─ __init__.py
   │     │  ├─ plotting
   │     │  │  ├─ _core.py
   │     │  │  ├─ _matplotlib
   │     │  │  │  ├─ boxplot.py
   │     │  │  │  ├─ converter.py
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ groupby.py
   │     │  │  │  ├─ hist.py
   │     │  │  │  ├─ misc.py
   │     │  │  │  ├─ style.py
   │     │  │  │  ├─ timeseries.py
   │     │  │  │  ├─ tools.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _misc.py
   │     │  │  └─ __init__.py
   │     │  ├─ pyproject.toml
   │     │  ├─ testing.py
   │     │  ├─ tests
   │     │  │  ├─ api
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_types.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ apply
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ test_frame_apply.py
   │     │  │  │  ├─ test_frame_apply_relabeling.py
   │     │  │  │  ├─ test_frame_transform.py
   │     │  │  │  ├─ test_invalid_arg.py
   │     │  │  │  ├─ test_numba.py
   │     │  │  │  ├─ test_series_apply.py
   │     │  │  │  ├─ test_series_apply_relabeling.py
   │     │  │  │  ├─ test_series_transform.py
   │     │  │  │  ├─ test_str.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ arithmetic
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ test_array_ops.py
   │     │  │  │  ├─ test_categorical.py
   │     │  │  │  ├─ test_datetime64.py
   │     │  │  │  ├─ test_interval.py
   │     │  │  │  ├─ test_numeric.py
   │     │  │  │  ├─ test_object.py
   │     │  │  │  ├─ test_period.py
   │     │  │  │  ├─ test_timedelta64.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ arrays
   │     │  │  │  ├─ boolean
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_comparison.py
   │     │  │  │  │  ├─ test_construction.py
   │     │  │  │  │  ├─ test_function.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_logical.py
   │     │  │  │  │  ├─ test_ops.py
   │     │  │  │  │  ├─ test_reduction.py
   │     │  │  │  │  ├─ test_repr.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ categorical
   │     │  │  │  │  ├─ .tmpDtTtAF
   │     │  │  │  │  ├─ test_algos.py
   │     │  │  │  │  ├─ test_analytics.py
   │     │  │  │  │  ├─ test_api.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_dtypes.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_map.py
   │     │  │  │  │  ├─ test_missing.py
   │     │  │  │  │  ├─ test_operators.py
   │     │  │  │  │  ├─ test_replace.py
   │     │  │  │  │  ├─ test_repr.py
   │     │  │  │  │  ├─ test_sorting.py
   │     │  │  │  │  ├─ test_subclass.py
   │     │  │  │  │  ├─ test_take.py
   │     │  │  │  │  ├─ test_warnings.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ datetimes
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_cumulative.py
   │     │  │  │  │  ├─ test_reductions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ floating
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_comparison.py
   │     │  │  │  │  ├─ test_concat.py
   │     │  │  │  │  ├─ test_construction.py
   │     │  │  │  │  ├─ test_contains.py
   │     │  │  │  │  ├─ test_function.py
   │     │  │  │  │  ├─ test_repr.py
   │     │  │  │  │  ├─ test_to_numpy.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ integer
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_comparison.py
   │     │  │  │  │  ├─ test_concat.py
   │     │  │  │  │  ├─ test_construction.py
   │     │  │  │  │  ├─ test_dtypes.py
   │     │  │  │  │  ├─ test_function.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_reduction.py
   │     │  │  │  │  ├─ test_repr.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ interval
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_interval.py
   │     │  │  │  │  ├─ test_interval_pyarrow.py
   │     │  │  │  │  ├─ test_overlaps.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ masked
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_arrow_compat.py
   │     │  │  │  │  ├─ test_function.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ masked_shared.py
   │     │  │  │  ├─ numpy_
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_numpy.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ period
   │     │  │  │  │  ├─ test_arrow_compat.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_reductions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sparse
   │     │  │  │  │  ├─ test_accessor.py
   │     │  │  │  │  ├─ test_arithmetics.py
   │     │  │  │  │  ├─ test_array.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_combine_concat.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_dtype.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_libsparse.py
   │     │  │  │  │  ├─ test_reductions.py
   │     │  │  │  │  ├─ test_unary.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ string_
   │     │  │  │  │  ├─ test_concat.py
   │     │  │  │  │  ├─ test_string.py
   │     │  │  │  │  ├─ test_string_arrow.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_array.py
   │     │  │  │  ├─ test_datetimelike.py
   │     │  │  │  ├─ test_datetimes.py
   │     │  │  │  ├─ test_ndarray_backed.py
   │     │  │  │  ├─ test_period.py
   │     │  │  │  ├─ test_timedeltas.py
   │     │  │  │  ├─ timedeltas
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_cumulative.py
   │     │  │  │  │  ├─ test_reductions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ base
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ test_constructors.py
   │     │  │  │  ├─ test_conversion.py
   │     │  │  │  ├─ test_fillna.py
   │     │  │  │  ├─ test_misc.py
   │     │  │  │  ├─ test_transpose.py
   │     │  │  │  ├─ test_unique.py
   │     │  │  │  ├─ test_value_counts.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ computation
   │     │  │  │  ├─ test_compat.py
   │     │  │  │  ├─ test_eval.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ config
   │     │  │  │  ├─ test_config.py
   │     │  │  │  ├─ test_localization.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ construction
   │     │  │  │  ├─ test_extract_array.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ copy_view
   │     │  │  │  ├─ index
   │     │  │  │  │  ├─ test_datetimeindex.py
   │     │  │  │  │  ├─ test_index.py
   │     │  │  │  │  ├─ test_periodindex.py
   │     │  │  │  │  ├─ test_timedeltaindex.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_array.py
   │     │  │  │  ├─ test_astype.py
   │     │  │  │  ├─ test_chained_assignment_deprecation.py
   │     │  │  │  ├─ test_clip.py
   │     │  │  │  ├─ test_constructors.py
   │     │  │  │  ├─ test_core_functionalities.py
   │     │  │  │  ├─ test_functions.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_internals.py
   │     │  │  │  ├─ test_interp_fillna.py
   │     │  │  │  ├─ test_methods.py
   │     │  │  │  ├─ test_replace.py
   │     │  │  │  ├─ test_setitem.py
   │     │  │  │  ├─ test_util.py
   │     │  │  │  ├─ util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ dtypes
   │     │  │  │  ├─ cast
   │     │  │  │  │  ├─ test_can_hold_element.py
   │     │  │  │  │  ├─ test_construct_from_scalar.py
   │     │  │  │  │  ├─ test_construct_ndarray.py
   │     │  │  │  │  ├─ test_construct_object_arr.py
   │     │  │  │  │  ├─ test_dict_compat.py
   │     │  │  │  │  ├─ test_downcast.py
   │     │  │  │  │  ├─ test_find_common_type.py
   │     │  │  │  │  ├─ test_infer_datetimelike.py
   │     │  │  │  │  ├─ test_infer_dtype.py
   │     │  │  │  │  ├─ test_maybe_box_native.py
   │     │  │  │  │  ├─ test_promote.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_concat.py
   │     │  │  │  ├─ test_dtypes.py
   │     │  │  │  ├─ test_generic.py
   │     │  │  │  ├─ test_inference.py
   │     │  │  │  ├─ test_missing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ extension
   │     │  │  │  ├─ array_with_attr
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ test_array_with_attr.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ base
   │     │  │  │  │  ├─ accumulate.py
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ casting.py
   │     │  │  │  │  ├─ constructors.py
   │     │  │  │  │  ├─ dim2.py
   │     │  │  │  │  ├─ dtype.py
   │     │  │  │  │  ├─ getitem.py
   │     │  │  │  │  ├─ groupby.py
   │     │  │  │  │  ├─ index.py
   │     │  │  │  │  ├─ interface.py
   │     │  │  │  │  ├─ io.py
   │     │  │  │  │  ├─ methods.py
   │     │  │  │  │  ├─ missing.py
   │     │  │  │  │  ├─ ops.py
   │     │  │  │  │  ├─ printing.py
   │     │  │  │  │  ├─ reduce.py
   │     │  │  │  │  ├─ reshaping.py
   │     │  │  │  │  ├─ setitem.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ date
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ decimal
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ test_decimal.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ json
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ test_json.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ list
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ test_list.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_arrow.py
   │     │  │  │  ├─ test_categorical.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_datetime.py
   │     │  │  │  ├─ test_extension.py
   │     │  │  │  ├─ test_interval.py
   │     │  │  │  ├─ test_masked.py
   │     │  │  │  ├─ test_numpy.py
   │     │  │  │  ├─ test_period.py
   │     │  │  │  ├─ test_sparse.py
   │     │  │  │  ├─ test_string.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ frame
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ constructors
   │     │  │  │  │  ├─ test_from_dict.py
   │     │  │  │  │  ├─ test_from_records.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ indexing
   │     │  │  │  │  ├─ test_coercion.py
   │     │  │  │  │  ├─ test_delitem.py
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  ├─ test_getitem.py
   │     │  │  │  │  ├─ test_get_value.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_insert.py
   │     │  │  │  │  ├─ test_mask.py
   │     │  │  │  │  ├─ test_setitem.py
   │     │  │  │  │  ├─ test_set_value.py
   │     │  │  │  │  ├─ test_take.py
   │     │  │  │  │  ├─ test_where.py
   │     │  │  │  │  ├─ test_xs.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ methods
   │     │  │  │  │  ├─ test_add_prefix_suffix.py
   │     │  │  │  │  ├─ test_align.py
   │     │  │  │  │  ├─ test_asfreq.py
   │     │  │  │  │  ├─ test_asof.py
   │     │  │  │  │  ├─ test_assign.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_at_time.py
   │     │  │  │  │  ├─ test_between_time.py
   │     │  │  │  │  ├─ test_clip.py
   │     │  │  │  │  ├─ test_combine.py
   │     │  │  │  │  ├─ test_combine_first.py
   │     │  │  │  │  ├─ test_compare.py
   │     │  │  │  │  ├─ test_convert_dtypes.py
   │     │  │  │  │  ├─ test_copy.py
   │     │  │  │  │  ├─ test_count.py
   │     │  │  │  │  ├─ test_cov_corr.py
   │     │  │  │  │  ├─ test_describe.py
   │     │  │  │  │  ├─ test_diff.py
   │     │  │  │  │  ├─ test_dot.py
   │     │  │  │  │  ├─ test_drop.py
   │     │  │  │  │  ├─ test_droplevel.py
   │     │  │  │  │  ├─ test_dropna.py
   │     │  │  │  │  ├─ test_drop_duplicates.py
   │     │  │  │  │  ├─ test_dtypes.py
   │     │  │  │  │  ├─ test_duplicated.py
   │     │  │  │  │  ├─ test_equals.py
   │     │  │  │  │  ├─ test_explode.py
   │     │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  ├─ test_filter.py
   │     │  │  │  │  ├─ test_first_and_last.py
   │     │  │  │  │  ├─ test_first_valid_index.py
   │     │  │  │  │  ├─ test_get_numeric_data.py
   │     │  │  │  │  ├─ test_head_tail.py
   │     │  │  │  │  ├─ test_infer_objects.py
   │     │  │  │  │  ├─ test_info.py
   │     │  │  │  │  ├─ test_interpolate.py
   │     │  │  │  │  ├─ test_isetitem.py
   │     │  │  │  │  ├─ test_isin.py
   │     │  │  │  │  ├─ test_is_homogeneous_dtype.py
   │     │  │  │  │  ├─ test_iterrows.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_map.py
   │     │  │  │  │  ├─ test_matmul.py
   │     │  │  │  │  ├─ test_nlargest.py
   │     │  │  │  │  ├─ test_pct_change.py
   │     │  │  │  │  ├─ test_pipe.py
   │     │  │  │  │  ├─ test_pop.py
   │     │  │  │  │  ├─ test_quantile.py
   │     │  │  │  │  ├─ test_rank.py
   │     │  │  │  │  ├─ test_reindex.py
   │     │  │  │  │  ├─ test_reindex_like.py
   │     │  │  │  │  ├─ test_rename.py
   │     │  │  │  │  ├─ test_rename_axis.py
   │     │  │  │  │  ├─ test_reorder_levels.py
   │     │  │  │  │  ├─ test_replace.py
   │     │  │  │  │  ├─ test_reset_index.py
   │     │  │  │  │  ├─ test_round.py
   │     │  │  │  │  ├─ test_sample.py
   │     │  │  │  │  ├─ test_select_dtypes.py
   │     │  │  │  │  ├─ test_set_axis.py
   │     │  │  │  │  ├─ test_set_index.py
   │     │  │  │  │  ├─ test_shift.py
   │     │  │  │  │  ├─ test_size.py
   │     │  │  │  │  ├─ test_sort_index.py
   │     │  │  │  │  ├─ test_sort_values.py
   │     │  │  │  │  ├─ test_swapaxes.py
   │     │  │  │  │  ├─ test_swaplevel.py
   │     │  │  │  │  ├─ test_to_csv.py
   │     │  │  │  │  ├─ test_to_dict.py
   │     │  │  │  │  ├─ test_to_dict_of_blocks.py
   │     │  │  │  │  ├─ test_to_numpy.py
   │     │  │  │  │  ├─ test_to_period.py
   │     │  │  │  │  ├─ test_to_records.py
   │     │  │  │  │  ├─ test_to_timestamp.py
   │     │  │  │  │  ├─ test_transpose.py
   │     │  │  │  │  ├─ test_truncate.py
   │     │  │  │  │  ├─ test_tz_convert.py
   │     │  │  │  │  ├─ test_tz_localize.py
   │     │  │  │  │  ├─ test_update.py
   │     │  │  │  │  ├─ test_values.py
   │     │  │  │  │  ├─ test_value_counts.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_alter_axes.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_arithmetic.py
   │     │  │  │  ├─ test_arrow_interface.py
   │     │  │  │  ├─ test_block_internals.py
   │     │  │  │  ├─ test_constructors.py
   │     │  │  │  ├─ test_cumulative.py
   │     │  │  │  ├─ test_iteration.py
   │     │  │  │  ├─ test_logical_ops.py
   │     │  │  │  ├─ test_nonunique_indexes.py
   │     │  │  │  ├─ test_npfuncs.py
   │     │  │  │  ├─ test_query_eval.py
   │     │  │  │  ├─ test_reductions.py
   │     │  │  │  ├─ test_repr.py
   │     │  │  │  ├─ test_stack_unstack.py
   │     │  │  │  ├─ test_subclass.py
   │     │  │  │  ├─ test_ufunc.py
   │     │  │  │  ├─ test_unary.py
   │     │  │  │  ├─ test_validate.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ generic
   │     │  │  │  ├─ test_duplicate_labels.py
   │     │  │  │  ├─ test_finalize.py
   │     │  │  │  ├─ test_frame.py
   │     │  │  │  ├─ test_generic.py
   │     │  │  │  ├─ test_label_or_level_utils.py
   │     │  │  │  ├─ test_series.py
   │     │  │  │  ├─ test_to_xarray.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ groupby
   │     │  │  │  ├─ aggregate
   │     │  │  │  │  ├─ test_aggregate.py
   │     │  │  │  │  ├─ test_cython.py
   │     │  │  │  │  ├─ test_numba.py
   │     │  │  │  │  ├─ test_other.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ methods
   │     │  │  │  │  ├─ test_corrwith.py
   │     │  │  │  │  ├─ test_describe.py
   │     │  │  │  │  ├─ test_groupby_shift_diff.py
   │     │  │  │  │  ├─ test_is_monotonic.py
   │     │  │  │  │  ├─ test_nlargest_nsmallest.py
   │     │  │  │  │  ├─ test_nth.py
   │     │  │  │  │  ├─ test_quantile.py
   │     │  │  │  │  ├─ test_rank.py
   │     │  │  │  │  ├─ test_sample.py
   │     │  │  │  │  ├─ test_size.py
   │     │  │  │  │  ├─ test_skew.py
   │     │  │  │  │  ├─ test_value_counts.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_all_methods.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_apply.py
   │     │  │  │  ├─ test_apply_mutate.py
   │     │  │  │  ├─ test_bin_groupby.py
   │     │  │  │  ├─ test_categorical.py
   │     │  │  │  ├─ test_counting.py
   │     │  │  │  ├─ test_cumulative.py
   │     │  │  │  ├─ test_filters.py
   │     │  │  │  ├─ test_groupby.py
   │     │  │  │  ├─ test_groupby_dropna.py
   │     │  │  │  ├─ test_groupby_subclass.py
   │     │  │  │  ├─ test_grouping.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_index_as_string.py
   │     │  │  │  ├─ test_libgroupby.py
   │     │  │  │  ├─ test_missing.py
   │     │  │  │  ├─ test_numba.py
   │     │  │  │  ├─ test_numeric_only.py
   │     │  │  │  ├─ test_pipe.py
   │     │  │  │  ├─ test_raises.py
   │     │  │  │  ├─ test_reductions.py
   │     │  │  │  ├─ test_timegrouper.py
   │     │  │  │  ├─ transform
   │     │  │  │  │  ├─ test_numba.py
   │     │  │  │  │  ├─ test_transform.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexes
   │     │  │  │  ├─ base_class
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_reshape.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  ├─ test_where.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ categorical
   │     │  │  │  │  ├─ test_append.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_category.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_equals.py
   │     │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_map.py
   │     │  │  │  │  ├─ test_reindex.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ datetimelike_
   │     │  │  │  │  ├─ test_drop_duplicates.py
   │     │  │  │  │  ├─ test_equals.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_is_monotonic.py
   │     │  │  │  │  ├─ test_nat.py
   │     │  │  │  │  ├─ test_sort_values.py
   │     │  │  │  │  ├─ test_value_counts.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ datetimes
   │     │  │  │  │  ├─ methods
   │     │  │  │  │  │  ├─ test_asof.py
   │     │  │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  │  ├─ test_delete.py
   │     │  │  │  │  │  ├─ test_factorize.py
   │     │  │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  │  ├─ test_insert.py
   │     │  │  │  │  │  ├─ test_isocalendar.py
   │     │  │  │  │  │  ├─ test_map.py
   │     │  │  │  │  │  ├─ test_normalize.py
   │     │  │  │  │  │  ├─ test_repeat.py
   │     │  │  │  │  │  ├─ test_resolution.py
   │     │  │  │  │  │  ├─ test_round.py
   │     │  │  │  │  │  ├─ test_shift.py
   │     │  │  │  │  │  ├─ test_snap.py
   │     │  │  │  │  │  ├─ test_to_frame.py
   │     │  │  │  │  │  ├─ test_to_julian_date.py
   │     │  │  │  │  │  ├─ test_to_period.py
   │     │  │  │  │  │  ├─ test_to_pydatetime.py
   │     │  │  │  │  │  ├─ test_to_series.py
   │     │  │  │  │  │  ├─ test_tz_convert.py
   │     │  │  │  │  │  ├─ test_tz_localize.py
   │     │  │  │  │  │  ├─ test_unique.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_datetime.py
   │     │  │  │  │  ├─ test_date_range.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_freq_attr.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_iter.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_npfuncs.py
   │     │  │  │  │  ├─ test_ops.py
   │     │  │  │  │  ├─ test_partial_slicing.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_reindex.py
   │     │  │  │  │  ├─ test_scalar_compat.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  ├─ test_timezones.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ interval
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_equals.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_interval.py
   │     │  │  │  │  ├─ test_interval_range.py
   │     │  │  │  │  ├─ test_interval_tree.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ multi
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_analytics.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_compat.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_conversion.py
   │     │  │  │  │  ├─ test_copy.py
   │     │  │  │  │  ├─ test_drop.py
   │     │  │  │  │  ├─ test_duplicates.py
   │     │  │  │  │  ├─ test_equivalence.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_get_level_values.py
   │     │  │  │  │  ├─ test_get_set.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_integrity.py
   │     │  │  │  │  ├─ test_isin.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_lexsort.py
   │     │  │  │  │  ├─ test_missing.py
   │     │  │  │  │  ├─ test_monotonic.py
   │     │  │  │  │  ├─ test_names.py
   │     │  │  │  │  ├─ test_partial_indexing.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_reindex.py
   │     │  │  │  │  ├─ test_reshape.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  ├─ test_sorting.py
   │     │  │  │  │  ├─ test_take.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ numeric
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_numeric.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ object
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ period
   │     │  │  │  │  ├─ methods
   │     │  │  │  │  │  ├─ test_asfreq.py
   │     │  │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  │  ├─ test_factorize.py
   │     │  │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  │  ├─ test_insert.py
   │     │  │  │  │  │  ├─ test_is_full.py
   │     │  │  │  │  │  ├─ test_repeat.py
   │     │  │  │  │  │  ├─ test_shift.py
   │     │  │  │  │  │  ├─ test_to_timestamp.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_freq_attr.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_monotonic.py
   │     │  │  │  │  ├─ test_partial_slicing.py
   │     │  │  │  │  ├─ test_period.py
   │     │  │  │  │  ├─ test_period_range.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_resolution.py
   │     │  │  │  │  ├─ test_scalar_compat.py
   │     │  │  │  │  ├─ test_searchsorted.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  ├─ test_tools.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ranges
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_range.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ string
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_any_index.py
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_datetimelike.py
   │     │  │  │  ├─ test_engines.py
   │     │  │  │  ├─ test_frozen.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_index_new.py
   │     │  │  │  ├─ test_numpy_compat.py
   │     │  │  │  ├─ test_old_base.py
   │     │  │  │  ├─ test_setops.py
   │     │  │  │  ├─ test_subclass.py
   │     │  │  │  ├─ timedeltas
   │     │  │  │  │  ├─ methods
   │     │  │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  │  ├─ test_factorize.py
   │     │  │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  │  ├─ test_insert.py
   │     │  │  │  │  │  ├─ test_repeat.py
   │     │  │  │  │  │  ├─ test_shift.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_delete.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_freq_attr.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_ops.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_scalar_compat.py
   │     │  │  │  │  ├─ test_searchsorted.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  ├─ test_timedelta.py
   │     │  │  │  │  ├─ test_timedelta_range.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexing
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ interval
   │     │  │  │  │  ├─ test_interval.py
   │     │  │  │  │  ├─ test_interval_new.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ multiindex
   │     │  │  │  │  ├─ test_chaining_and_caching.py
   │     │  │  │  │  ├─ test_datetime.py
   │     │  │  │  │  ├─ test_getitem.py
   │     │  │  │  │  ├─ test_iloc.py
   │     │  │  │  │  ├─ test_indexing_slow.py
   │     │  │  │  │  ├─ test_loc.py
   │     │  │  │  │  ├─ test_multiindex.py
   │     │  │  │  │  ├─ test_partial.py
   │     │  │  │  │  ├─ test_setitem.py
   │     │  │  │  │  ├─ test_slice.py
   │     │  │  │  │  ├─ test_sorted.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_at.py
   │     │  │  │  ├─ test_categorical.py
   │     │  │  │  ├─ test_chaining_and_caching.py
   │     │  │  │  ├─ test_check_indexer.py
   │     │  │  │  ├─ test_coercion.py
   │     │  │  │  ├─ test_datetime.py
   │     │  │  │  ├─ test_floats.py
   │     │  │  │  ├─ test_iat.py
   │     │  │  │  ├─ test_iloc.py
   │     │  │  │  ├─ test_indexers.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_loc.py
   │     │  │  │  ├─ test_na_indexing.py
   │     │  │  │  ├─ test_partial.py
   │     │  │  │  ├─ test_scalar.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ interchange
   │     │  │  │  ├─ test_impl.py
   │     │  │  │  ├─ test_spec_conformance.py
   │     │  │  │  ├─ test_utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ internals
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_internals.py
   │     │  │  │  ├─ test_managers.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ io
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ excel
   │     │  │  │  │  ├─ test_odf.py
   │     │  │  │  │  ├─ test_odswriter.py
   │     │  │  │  │  ├─ test_openpyxl.py
   │     │  │  │  │  ├─ test_readers.py
   │     │  │  │  │  ├─ test_style.py
   │     │  │  │  │  ├─ test_writers.py
   │     │  │  │  │  ├─ test_xlrd.py
   │     │  │  │  │  ├─ test_xlsxwriter.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ formats
   │     │  │  │  │  ├─ style
   │     │  │  │  │  │  ├─ test_bar.py
   │     │  │  │  │  │  ├─ test_exceptions.py
   │     │  │  │  │  │  ├─ test_format.py
   │     │  │  │  │  │  ├─ test_highlight.py
   │     │  │  │  │  │  ├─ test_html.py
   │     │  │  │  │  │  ├─ test_matplotlib.py
   │     │  │  │  │  │  ├─ test_non_unique.py
   │     │  │  │  │  │  ├─ test_style.py
   │     │  │  │  │  │  ├─ test_tooltip.py
   │     │  │  │  │  │  ├─ test_to_latex.py
   │     │  │  │  │  │  ├─ test_to_string.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_console.py
   │     │  │  │  │  ├─ test_css.py
   │     │  │  │  │  ├─ test_eng_formatting.py
   │     │  │  │  │  ├─ test_format.py
   │     │  │  │  │  ├─ test_ipython_compat.py
   │     │  │  │  │  ├─ test_printing.py
   │     │  │  │  │  ├─ test_to_csv.py
   │     │  │  │  │  ├─ test_to_excel.py
   │     │  │  │  │  ├─ test_to_html.py
   │     │  │  │  │  ├─ test_to_latex.py
   │     │  │  │  │  ├─ test_to_markdown.py
   │     │  │  │  │  ├─ test_to_string.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ generate_legacy_storage_files.py
   │     │  │  │  ├─ json
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_compression.py
   │     │  │  │  │  ├─ test_deprecated_kwargs.py
   │     │  │  │  │  ├─ test_json_table_schema.py
   │     │  │  │  │  ├─ test_json_table_schema_ext_dtype.py
   │     │  │  │  │  ├─ test_normalize.py
   │     │  │  │  │  ├─ test_pandas.py
   │     │  │  │  │  ├─ test_readlines.py
   │     │  │  │  │  ├─ test_ujson.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ parser
   │     │  │  │  │  ├─ common
   │     │  │  │  │  │  ├─ test_chunksize.py
   │     │  │  │  │  │  ├─ test_common_basic.py
   │     │  │  │  │  │  ├─ test_data_list.py
   │     │  │  │  │  │  ├─ test_decimal.py
   │     │  │  │  │  │  ├─ test_file_buffer_url.py
   │     │  │  │  │  │  ├─ test_float.py
   │     │  │  │  │  │  ├─ test_index.py
   │     │  │  │  │  │  ├─ test_inf.py
   │     │  │  │  │  │  ├─ test_ints.py
   │     │  │  │  │  │  ├─ test_iterator.py
   │     │  │  │  │  │  ├─ test_read_errors.py
   │     │  │  │  │  │  ├─ test_verbose.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ dtypes
   │     │  │  │  │  │  ├─ test_categorical.py
   │     │  │  │  │  │  ├─ test_dtypes_basic.py
   │     │  │  │  │  │  ├─ test_empty.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_comment.py
   │     │  │  │  │  ├─ test_compression.py
   │     │  │  │  │  ├─ test_concatenate_chunks.py
   │     │  │  │  │  ├─ test_converters.py
   │     │  │  │  │  ├─ test_c_parser_only.py
   │     │  │  │  │  ├─ test_dialect.py
   │     │  │  │  │  ├─ test_encoding.py
   │     │  │  │  │  ├─ test_header.py
   │     │  │  │  │  ├─ test_index_col.py
   │     │  │  │  │  ├─ test_mangle_dupes.py
   │     │  │  │  │  ├─ test_multi_thread.py
   │     │  │  │  │  ├─ test_na_values.py
   │     │  │  │  │  ├─ test_network.py
   │     │  │  │  │  ├─ test_parse_dates.py
   │     │  │  │  │  ├─ test_python_parser_only.py
   │     │  │  │  │  ├─ test_quoting.py
   │     │  │  │  │  ├─ test_read_fwf.py
   │     │  │  │  │  ├─ test_skiprows.py
   │     │  │  │  │  ├─ test_textreader.py
   │     │  │  │  │  ├─ test_unsupported.py
   │     │  │  │  │  ├─ test_upcast.py
   │     │  │  │  │  ├─ usecols
   │     │  │  │  │  │  ├─ test_parse_dates.py
   │     │  │  │  │  │  ├─ test_strings.py
   │     │  │  │  │  │  ├─ test_usecols_basic.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ pytables
   │     │  │  │  │  ├─ common.py
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_append.py
   │     │  │  │  │  ├─ test_categorical.py
   │     │  │  │  │  ├─ test_compat.py
   │     │  │  │  │  ├─ test_complex.py
   │     │  │  │  │  ├─ test_errors.py
   │     │  │  │  │  ├─ test_file_handling.py
   │     │  │  │  │  ├─ test_keys.py
   │     │  │  │  │  ├─ test_put.py
   │     │  │  │  │  ├─ test_pytables_missing.py
   │     │  │  │  │  ├─ test_read.py
   │     │  │  │  │  ├─ test_retain_attributes.py
   │     │  │  │  │  ├─ test_round_trip.py
   │     │  │  │  │  ├─ test_select.py
   │     │  │  │  │  ├─ test_store.py
   │     │  │  │  │  ├─ test_subclass.py
   │     │  │  │  │  ├─ test_timezones.py
   │     │  │  │  │  ├─ test_time_series.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sas
   │     │  │  │  │  ├─ test_byteswap.py
   │     │  │  │  │  ├─ test_sas.py
   │     │  │  │  │  ├─ test_sas7bdat.py
   │     │  │  │  │  ├─ test_xport.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_clipboard.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_compression.py
   │     │  │  │  ├─ test_feather.py
   │     │  │  │  ├─ test_fsspec.py
   │     │  │  │  ├─ test_gbq.py
   │     │  │  │  ├─ test_gcs.py
   │     │  │  │  ├─ test_html.py
   │     │  │  │  ├─ test_http_headers.py
   │     │  │  │  ├─ test_orc.py
   │     │  │  │  ├─ test_parquet.py
   │     │  │  │  ├─ test_pickle.py
   │     │  │  │  ├─ test_s3.py
   │     │  │  │  ├─ test_spss.py
   │     │  │  │  ├─ test_sql.py
   │     │  │  │  ├─ test_stata.py
   │     │  │  │  ├─ xml
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_to_xml.py
   │     │  │  │  │  ├─ test_xml.py
   │     │  │  │  │  ├─ test_xml_dtypes.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ libs
   │     │  │  │  ├─ test_hashtable.py
   │     │  │  │  ├─ test_join.py
   │     │  │  │  ├─ test_lib.py
   │     │  │  │  ├─ test_libalgos.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ plotting
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ frame
   │     │  │  │  │  ├─ test_frame.py
   │     │  │  │  │  ├─ test_frame_color.py
   │     │  │  │  │  ├─ test_frame_groupby.py
   │     │  │  │  │  ├─ test_frame_legend.py
   │     │  │  │  │  ├─ test_frame_subplots.py
   │     │  │  │  │  ├─ test_hist_box_by.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_backend.py
   │     │  │  │  ├─ test_boxplot_method.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_converter.py
   │     │  │  │  ├─ test_datetimelike.py
   │     │  │  │  ├─ test_groupby.py
   │     │  │  │  ├─ test_hist_method.py
   │     │  │  │  ├─ test_misc.py
   │     │  │  │  ├─ test_series.py
   │     │  │  │  ├─ test_style.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ reductions
   │     │  │  │  ├─ test_reductions.py
   │     │  │  │  ├─ test_stat_reductions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ resample
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_datetime_index.py
   │     │  │  │  ├─ test_period_index.py
   │     │  │  │  ├─ test_resampler_grouper.py
   │     │  │  │  ├─ test_resample_api.py
   │     │  │  │  ├─ test_timedelta.py
   │     │  │  │  ├─ test_time_grouper.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ reshape
   │     │  │  │  ├─ concat
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_append.py
   │     │  │  │  │  ├─ test_append_common.py
   │     │  │  │  │  ├─ test_categorical.py
   │     │  │  │  │  ├─ test_concat.py
   │     │  │  │  │  ├─ test_dataframe.py
   │     │  │  │  │  ├─ test_datetimes.py
   │     │  │  │  │  ├─ test_empty.py
   │     │  │  │  │  ├─ test_index.py
   │     │  │  │  │  ├─ test_invalid.py
   │     │  │  │  │  ├─ test_series.py
   │     │  │  │  │  ├─ test_sort.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ merge
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_merge.py
   │     │  │  │  │  ├─ test_merge_asof.py
   │     │  │  │  │  ├─ test_merge_cross.py
   │     │  │  │  │  ├─ test_merge_index_as_string.py
   │     │  │  │  │  ├─ test_merge_ordered.py
   │     │  │  │  │  ├─ test_multi.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_crosstab.py
   │     │  │  │  ├─ test_cut.py
   │     │  │  │  ├─ test_from_dummies.py
   │     │  │  │  ├─ test_get_dummies.py
   │     │  │  │  ├─ test_melt.py
   │     │  │  │  ├─ test_pivot.py
   │     │  │  │  ├─ test_pivot_multilevel.py
   │     │  │  │  ├─ test_qcut.py
   │     │  │  │  ├─ test_union_categoricals.py
   │     │  │  │  ├─ test_util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ scalar
   │     │  │  │  ├─ interval
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_contains.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_interval.py
   │     │  │  │  │  ├─ test_overlaps.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ period
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_asfreq.py
   │     │  │  │  │  ├─ test_period.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_nat.py
   │     │  │  │  ├─ test_na_scalar.py
   │     │  │  │  ├─ timedelta
   │     │  │  │  │  ├─ methods
   │     │  │  │  │  │  ├─ test_as_unit.py
   │     │  │  │  │  │  ├─ test_round.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_timedelta.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ timestamp
   │     │  │  │  │  ├─ methods
   │     │  │  │  │  │  ├─ test_as_unit.py
   │     │  │  │  │  │  ├─ test_normalize.py
   │     │  │  │  │  │  ├─ test_replace.py
   │     │  │  │  │  │  ├─ test_round.py
   │     │  │  │  │  │  ├─ test_timestamp_method.py
   │     │  │  │  │  │  ├─ test_to_julian_date.py
   │     │  │  │  │  │  ├─ test_to_pydatetime.py
   │     │  │  │  │  │  ├─ test_tz_convert.py
   │     │  │  │  │  │  ├─ test_tz_localize.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_comparisons.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_timestamp.py
   │     │  │  │  │  ├─ test_timezones.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ series
   │     │  │  │  ├─ accessors
   │     │  │  │  │  ├─ test_cat_accessor.py
   │     │  │  │  │  ├─ test_dt_accessor.py
   │     │  │  │  │  ├─ test_list_accessor.py
   │     │  │  │  │  ├─ test_sparse_accessor.py
   │     │  │  │  │  ├─ test_struct_accessor.py
   │     │  │  │  │  ├─ test_str_accessor.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ indexing
   │     │  │  │  │  ├─ test_datetime.py
   │     │  │  │  │  ├─ test_delitem.py
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  ├─ test_getitem.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_mask.py
   │     │  │  │  │  ├─ test_setitem.py
   │     │  │  │  │  ├─ test_set_value.py
   │     │  │  │  │  ├─ test_take.py
   │     │  │  │  │  ├─ test_where.py
   │     │  │  │  │  ├─ test_xs.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ methods
   │     │  │  │  │  ├─ test_add_prefix_suffix.py
   │     │  │  │  │  ├─ test_align.py
   │     │  │  │  │  ├─ test_argsort.py
   │     │  │  │  │  ├─ test_asof.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_autocorr.py
   │     │  │  │  │  ├─ test_between.py
   │     │  │  │  │  ├─ test_case_when.py
   │     │  │  │  │  ├─ test_clip.py
   │     │  │  │  │  ├─ test_combine.py
   │     │  │  │  │  ├─ test_combine_first.py
   │     │  │  │  │  ├─ test_compare.py
   │     │  │  │  │  ├─ test_convert_dtypes.py
   │     │  │  │  │  ├─ test_copy.py
   │     │  │  │  │  ├─ test_count.py
   │     │  │  │  │  ├─ test_cov_corr.py
   │     │  │  │  │  ├─ test_describe.py
   │     │  │  │  │  ├─ test_diff.py
   │     │  │  │  │  ├─ test_drop.py
   │     │  │  │  │  ├─ test_dropna.py
   │     │  │  │  │  ├─ test_drop_duplicates.py
   │     │  │  │  │  ├─ test_dtypes.py
   │     │  │  │  │  ├─ test_duplicated.py
   │     │  │  │  │  ├─ test_equals.py
   │     │  │  │  │  ├─ test_explode.py
   │     │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  ├─ test_get_numeric_data.py
   │     │  │  │  │  ├─ test_head_tail.py
   │     │  │  │  │  ├─ test_infer_objects.py
   │     │  │  │  │  ├─ test_info.py
   │     │  │  │  │  ├─ test_interpolate.py
   │     │  │  │  │  ├─ test_isin.py
   │     │  │  │  │  ├─ test_isna.py
   │     │  │  │  │  ├─ test_is_monotonic.py
   │     │  │  │  │  ├─ test_is_unique.py
   │     │  │  │  │  ├─ test_item.py
   │     │  │  │  │  ├─ test_map.py
   │     │  │  │  │  ├─ test_matmul.py
   │     │  │  │  │  ├─ test_nlargest.py
   │     │  │  │  │  ├─ test_nunique.py
   │     │  │  │  │  ├─ test_pct_change.py
   │     │  │  │  │  ├─ test_pop.py
   │     │  │  │  │  ├─ test_quantile.py
   │     │  │  │  │  ├─ test_rank.py
   │     │  │  │  │  ├─ test_reindex.py
   │     │  │  │  │  ├─ test_reindex_like.py
   │     │  │  │  │  ├─ test_rename.py
   │     │  │  │  │  ├─ test_rename_axis.py
   │     │  │  │  │  ├─ test_repeat.py
   │     │  │  │  │  ├─ test_replace.py
   │     │  │  │  │  ├─ test_reset_index.py
   │     │  │  │  │  ├─ test_round.py
   │     │  │  │  │  ├─ test_searchsorted.py
   │     │  │  │  │  ├─ test_set_name.py
   │     │  │  │  │  ├─ test_size.py
   │     │  │  │  │  ├─ test_sort_index.py
   │     │  │  │  │  ├─ test_sort_values.py
   │     │  │  │  │  ├─ test_tolist.py
   │     │  │  │  │  ├─ test_to_csv.py
   │     │  │  │  │  ├─ test_to_dict.py
   │     │  │  │  │  ├─ test_to_frame.py
   │     │  │  │  │  ├─ test_to_numpy.py
   │     │  │  │  │  ├─ test_truncate.py
   │     │  │  │  │  ├─ test_tz_localize.py
   │     │  │  │  │  ├─ test_unique.py
   │     │  │  │  │  ├─ test_unstack.py
   │     │  │  │  │  ├─ test_update.py
   │     │  │  │  │  ├─ test_values.py
   │     │  │  │  │  ├─ test_value_counts.py
   │     │  │  │  │  ├─ test_view.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_arithmetic.py
   │     │  │  │  ├─ test_constructors.py
   │     │  │  │  ├─ test_cumulative.py
   │     │  │  │  ├─ test_formats.py
   │     │  │  │  ├─ test_iteration.py
   │     │  │  │  ├─ test_logical_ops.py
   │     │  │  │  ├─ test_missing.py
   │     │  │  │  ├─ test_npfuncs.py
   │     │  │  │  ├─ test_reductions.py
   │     │  │  │  ├─ test_subclass.py
   │     │  │  │  ├─ test_ufunc.py
   │     │  │  │  ├─ test_unary.py
   │     │  │  │  ├─ test_validate.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ strings
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_case_justify.py
   │     │  │  │  ├─ test_cat.py
   │     │  │  │  ├─ test_extract.py
   │     │  │  │  ├─ test_find_replace.py
   │     │  │  │  ├─ test_get_dummies.py
   │     │  │  │  ├─ test_split_partition.py
   │     │  │  │  ├─ test_strings.py
   │     │  │  │  ├─ test_string_array.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ test_aggregation.py
   │     │  │  ├─ test_algos.py
   │     │  │  ├─ test_common.py
   │     │  │  ├─ test_downstream.py
   │     │  │  ├─ test_errors.py
   │     │  │  ├─ test_expressions.py
   │     │  │  ├─ test_flags.py
   │     │  │  ├─ test_multilevel.py
   │     │  │  ├─ test_nanops.py
   │     │  │  ├─ test_optional_dependency.py
   │     │  │  ├─ test_register_accessor.py
   │     │  │  ├─ test_sorting.py
   │     │  │  ├─ test_take.py
   │     │  │  ├─ tools
   │     │  │  │  ├─ test_to_datetime.py
   │     │  │  │  ├─ test_to_numeric.py
   │     │  │  │  ├─ test_to_time.py
   │     │  │  │  ├─ test_to_timedelta.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tseries
   │     │  │  │  ├─ frequencies
   │     │  │  │  │  ├─ test_frequencies.py
   │     │  │  │  │  ├─ test_freq_code.py
   │     │  │  │  │  ├─ test_inference.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ holiday
   │     │  │  │  │  ├─ test_calendar.py
   │     │  │  │  │  ├─ test_federal.py
   │     │  │  │  │  ├─ test_holiday.py
   │     │  │  │  │  ├─ test_observance.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ offsets
   │     │  │  │  │  ├─ common.py
   │     │  │  │  │  ├─ test_business_day.py
   │     │  │  │  │  ├─ test_business_hour.py
   │     │  │  │  │  ├─ test_business_month.py
   │     │  │  │  │  ├─ test_business_quarter.py
   │     │  │  │  │  ├─ test_business_year.py
   │     │  │  │  │  ├─ test_common.py
   │     │  │  │  │  ├─ test_custom_business_day.py
   │     │  │  │  │  ├─ test_custom_business_hour.py
   │     │  │  │  │  ├─ test_custom_business_month.py
   │     │  │  │  │  ├─ test_dst.py
   │     │  │  │  │  ├─ test_easter.py
   │     │  │  │  │  ├─ test_fiscal.py
   │     │  │  │  │  ├─ test_index.py
   │     │  │  │  │  ├─ test_month.py
   │     │  │  │  │  ├─ test_offsets.py
   │     │  │  │  │  ├─ test_offsets_properties.py
   │     │  │  │  │  ├─ test_quarter.py
   │     │  │  │  │  ├─ test_ticks.py
   │     │  │  │  │  ├─ test_week.py
   │     │  │  │  │  ├─ test_year.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tslibs
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_array_to_datetime.py
   │     │  │  │  ├─ test_ccalendar.py
   │     │  │  │  ├─ test_conversion.py
   │     │  │  │  ├─ test_fields.py
   │     │  │  │  ├─ test_libfrequencies.py
   │     │  │  │  ├─ test_liboffsets.py
   │     │  │  │  ├─ test_npy_units.py
   │     │  │  │  ├─ test_np_datetime.py
   │     │  │  │  ├─ test_parse_iso8601.py
   │     │  │  │  ├─ test_parsing.py
   │     │  │  │  ├─ test_period.py
   │     │  │  │  ├─ test_resolution.py
   │     │  │  │  ├─ test_strptime.py
   │     │  │  │  ├─ test_timedeltas.py
   │     │  │  │  ├─ test_timezones.py
   │     │  │  │  ├─ test_to_offset.py
   │     │  │  │  ├─ test_tzconversion.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ util
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ test_assert_almost_equal.py
   │     │  │  │  ├─ test_assert_attr_equal.py
   │     │  │  │  ├─ test_assert_categorical_equal.py
   │     │  │  │  ├─ test_assert_extension_array_equal.py
   │     │  │  │  ├─ test_assert_frame_equal.py
   │     │  │  │  ├─ test_assert_index_equal.py
   │     │  │  │  ├─ test_assert_interval_array_equal.py
   │     │  │  │  ├─ test_assert_numpy_array_equal.py
   │     │  │  │  ├─ test_assert_produces_warning.py
   │     │  │  │  ├─ test_assert_series_equal.py
   │     │  │  │  ├─ test_deprecate.py
   │     │  │  │  ├─ test_deprecate_kwarg.py
   │     │  │  │  ├─ test_deprecate_nonkeyword_arguments.py
   │     │  │  │  ├─ test_doc.py
   │     │  │  │  ├─ test_hashing.py
   │     │  │  │  ├─ test_numba.py
   │     │  │  │  ├─ test_rewrite_warning.py
   │     │  │  │  ├─ test_shares_memory.py
   │     │  │  │  ├─ test_show_versions.py
   │     │  │  │  ├─ test_util.py
   │     │  │  │  ├─ test_validate_args.py
   │     │  │  │  ├─ test_validate_args_and_kwargs.py
   │     │  │  │  ├─ test_validate_inclusive.py
   │     │  │  │  ├─ test_validate_kwargs.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ window
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ moments
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_moments_consistency_ewm.py
   │     │  │  │  │  ├─ test_moments_consistency_expanding.py
   │     │  │  │  │  ├─ test_moments_consistency_rolling.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_apply.py
   │     │  │  │  ├─ test_base_indexer.py
   │     │  │  │  ├─ test_cython_aggregations.py
   │     │  │  │  ├─ test_dtypes.py
   │     │  │  │  ├─ test_ewm.py
   │     │  │  │  ├─ test_expanding.py
   │     │  │  │  ├─ test_groupby.py
   │     │  │  │  ├─ test_numba.py
   │     │  │  │  ├─ test_online.py
   │     │  │  │  ├─ test_pairwise.py
   │     │  │  │  ├─ test_rolling.py
   │     │  │  │  ├─ test_rolling_functions.py
   │     │  │  │  ├─ test_rolling_quantile.py
   │     │  │  │  ├─ test_rolling_skew_kurt.py
   │     │  │  │  ├─ test_timeseries_window.py
   │     │  │  │  ├─ test_win_type.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ tseries
   │     │  │  ├─ api.py
   │     │  │  ├─ frequencies.py
   │     │  │  ├─ holiday.py
   │     │  │  ├─ offsets.py
   │     │  │  └─ __init__.py
   │     │  ├─ util
   │     │  │  ├─ version
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _decorators.py
   │     │  │  ├─ _doctools.py
   │     │  │  ├─ _exceptions.py
   │     │  │  ├─ _print_versions.py
   │     │  │  ├─ _tester.py
   │     │  │  ├─ _test_decorators.py
   │     │  │  ├─ _validators.py
   │     │  │  └─ __init__.py
   │     │  ├─ _config
   │     │  │  ├─ config.py
   │     │  │  ├─ dates.py
   │     │  │  ├─ display.py
   │     │  │  ├─ localization.py
   │     │  │  └─ __init__.py
   │     │  ├─ _libs
   │     │  │  ├─ algos.cp310-win_amd64.lib
   │     │  │  ├─ algos.pyi
   │     │  │  ├─ arrays.cp310-win_amd64.lib
   │     │  │  ├─ arrays.pyi
   │     │  │  ├─ byteswap.cp310-win_amd64.lib
   │     │  │  ├─ byteswap.pyi
   │     │  │  ├─ groupby.cp310-win_amd64.lib
   │     │  │  ├─ groupby.pyi
   │     │  │  ├─ hashing.cp310-win_amd64.lib
   │     │  │  ├─ hashing.pyi
   │     │  │  ├─ hashtable.cp310-win_amd64.lib
   │     │  │  ├─ hashtable.pyi
   │     │  │  ├─ index.cp310-win_amd64.lib
   │     │  │  ├─ index.pyi
   │     │  │  ├─ indexing.cp310-win_amd64.lib
   │     │  │  ├─ indexing.pyi
   │     │  │  ├─ internals.cp310-win_amd64.lib
   │     │  │  ├─ internals.pyi
   │     │  │  ├─ interval.cp310-win_amd64.lib
   │     │  │  ├─ interval.pyi
   │     │  │  ├─ join.cp310-win_amd64.lib
   │     │  │  ├─ join.pyi
   │     │  │  ├─ json.cp310-win_amd64.lib
   │     │  │  ├─ json.pyi
   │     │  │  ├─ lib.cp310-win_amd64.lib
   │     │  │  ├─ lib.pyi
   │     │  │  ├─ missing.cp310-win_amd64.lib
   │     │  │  ├─ missing.pyi
   │     │  │  ├─ ops.cp310-win_amd64.lib
   │     │  │  ├─ ops.pyi
   │     │  │  ├─ ops_dispatch.cp310-win_amd64.lib
   │     │  │  ├─ ops_dispatch.pyi
   │     │  │  ├─ pandas_datetime.cp310-win_amd64.lib
   │     │  │  ├─ pandas_parser.cp310-win_amd64.lib
   │     │  │  ├─ parsers.cp310-win_amd64.lib
   │     │  │  ├─ parsers.pyi
   │     │  │  ├─ properties.cp310-win_amd64.lib
   │     │  │  ├─ properties.pyi
   │     │  │  ├─ reshape.cp310-win_amd64.lib
   │     │  │  ├─ reshape.pyi
   │     │  │  ├─ sas.cp310-win_amd64.lib
   │     │  │  ├─ sas.pyi
   │     │  │  ├─ sparse.cp310-win_amd64.lib
   │     │  │  ├─ sparse.pyi
   │     │  │  ├─ testing.cp310-win_amd64.lib
   │     │  │  ├─ testing.pyi
   │     │  │  ├─ tslib.cp310-win_amd64.lib
   │     │  │  ├─ tslib.pyi
   │     │  │  ├─ tslibs
   │     │  │  │  ├─ base.cp310-win_amd64.lib
   │     │  │  │  ├─ ccalendar.cp310-win_amd64.lib
   │     │  │  │  ├─ ccalendar.pyi
   │     │  │  │  ├─ conversion.cp310-win_amd64.lib
   │     │  │  │  ├─ conversion.pyi
   │     │  │  │  ├─ dtypes.cp310-win_amd64.lib
   │     │  │  │  ├─ dtypes.pyi
   │     │  │  │  ├─ fields.cp310-win_amd64.lib
   │     │  │  │  ├─ fields.pyi
   │     │  │  │  ├─ nattype.cp310-win_amd64.lib
   │     │  │  │  ├─ nattype.pyi
   │     │  │  │  ├─ np_datetime.cp310-win_amd64.lib
   │     │  │  │  ├─ np_datetime.pyi
   │     │  │  │  ├─ offsets.cp310-win_amd64.lib
   │     │  │  │  ├─ offsets.pyi
   │     │  │  │  ├─ parsing.cp310-win_amd64.lib
   │     │  │  │  ├─ parsing.pyi
   │     │  │  │  ├─ period.cp310-win_amd64.lib
   │     │  │  │  ├─ period.pyi
   │     │  │  │  ├─ strptime.cp310-win_amd64.lib
   │     │  │  │  ├─ strptime.pyi
   │     │  │  │  ├─ timedeltas.cp310-win_amd64.lib
   │     │  │  │  ├─ timedeltas.pyi
   │     │  │  │  ├─ timestamps.cp310-win_amd64.lib
   │     │  │  │  ├─ timestamps.pyi
   │     │  │  │  ├─ timezones.cp310-win_amd64.lib
   │     │  │  │  ├─ timezones.pyi
   │     │  │  │  ├─ tzconversion.cp310-win_amd64.lib
   │     │  │  │  ├─ tzconversion.pyi
   │     │  │  │  ├─ vectorized.cp310-win_amd64.lib
   │     │  │  │  ├─ vectorized.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ window
   │     │  │  │  ├─ aggregations.cp310-win_amd64.lib
   │     │  │  │  ├─ aggregations.pyi
   │     │  │  │  ├─ indexers.cp310-win_amd64.lib
   │     │  │  │  ├─ indexers.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ writers.cp310-win_amd64.lib
   │     │  │  ├─ writers.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ _testing
   │     │  │  ├─ asserters.py
   │     │  │  ├─ compat.py
   │     │  │  ├─ contexts.py
   │     │  │  ├─ _hypothesis.py
   │     │  │  ├─ _io.py
   │     │  │  ├─ _warnings.py
   │     │  │  └─ __init__.py
   │     │  ├─ _typing.py
   │     │  ├─ _version.py
   │     │  ├─ _version_meson.py
   │     │  └─ __init__.py
   │     ├─ pandas-2.3.3.dist-info
   │     │  ├─ DELVEWHEEL
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ pandas.libs
   │     │  └─ msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
   │     ├─ pasta
   │     │  ├─ augment
   │     │  │  ├─ errors.py
   │     │  │  ├─ import_utils.py
   │     │  │  ├─ import_utils_test.py
   │     │  │  ├─ inline.py
   │     │  │  ├─ inline_test.py
   │     │  │  ├─ rename.py
   │     │  │  ├─ rename_test.py
   │     │  │  └─ __init__.py
   │     │  ├─ base
   │     │  │  ├─ annotate.py
   │     │  │  ├─ annotate_test.py
   │     │  │  ├─ ast_constants.py
   │     │  │  ├─ ast_utils.py
   │     │  │  ├─ ast_utils_test.py
   │     │  │  ├─ codegen.py
   │     │  │  ├─ codegen_test.py
   │     │  │  ├─ formatting.py
   │     │  │  ├─ fstring_utils.py
   │     │  │  ├─ scope.py
   │     │  │  ├─ scope_test.py
   │     │  │  ├─ test_utils.py
   │     │  │  ├─ test_utils_test.py
   │     │  │  ├─ token_generator.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ patsy
   │     │  ├─ builtins.py
   │     │  ├─ categorical.py
   │     │  ├─ compat.py
   │     │  ├─ compat_ordereddict.py
   │     │  ├─ constraint.py
   │     │  ├─ contrasts.py
   │     │  ├─ desc.py
   │     │  ├─ design_info.py
   │     │  ├─ eval.py
   │     │  ├─ highlevel.py
   │     │  ├─ infix_parser.py
   │     │  ├─ mgcv_cubic_splines.py
   │     │  ├─ missing.py
   │     │  ├─ origin.py
   │     │  ├─ parse_formula.py
   │     │  ├─ redundancy.py
   │     │  ├─ splines.py
   │     │  ├─ state.py
   │     │  ├─ test_highlevel.py
   │     │  ├─ test_regressions.py
   │     │  ├─ test_splines_bs_data.py
   │     │  ├─ test_splines_crs_data.py
   │     │  ├─ test_state.py
   │     │  ├─ tokens.py
   │     │  ├─ user_util.py
   │     │  ├─ util.py
   │     │  ├─ version.py
   │     │  └─ __init__.py
   │     ├─ patsy-1.0.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ pd_modules-0.1.0.dist-info
   │     │  ├─ direct_url.json
   │     │  ├─ INSTALLER
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  ├─ uv_cache.json
   │     │  └─ WHEEL
   │     ├─ PIL
   │     │  ├─ AvifImagePlugin.py
   │     │  ├─ BdfFontFile.py
   │     │  ├─ BlpImagePlugin.py
   │     │  ├─ BmpImagePlugin.py
   │     │  ├─ BufrStubImagePlugin.py
   │     │  ├─ ContainerIO.py
   │     │  ├─ CurImagePlugin.py
   │     │  ├─ DcxImagePlugin.py
   │     │  ├─ DdsImagePlugin.py
   │     │  ├─ EpsImagePlugin.py
   │     │  ├─ ExifTags.py
   │     │  ├─ features.py
   │     │  ├─ FitsImagePlugin.py
   │     │  ├─ FliImagePlugin.py
   │     │  ├─ FontFile.py
   │     │  ├─ FpxImagePlugin.py
   │     │  ├─ FtexImagePlugin.py
   │     │  ├─ GbrImagePlugin.py
   │     │  ├─ GdImageFile.py
   │     │  ├─ GifImagePlugin.py
   │     │  ├─ GimpGradientFile.py
   │     │  ├─ GimpPaletteFile.py
   │     │  ├─ GribStubImagePlugin.py
   │     │  ├─ Hdf5StubImagePlugin.py
   │     │  ├─ IcnsImagePlugin.py
   │     │  ├─ IcoImagePlugin.py
   │     │  ├─ Image.py
   │     │  ├─ ImageChops.py
   │     │  ├─ ImageCms.py
   │     │  ├─ ImageColor.py
   │     │  ├─ ImageDraw.py
   │     │  ├─ ImageDraw2.py
   │     │  ├─ ImageEnhance.py
   │     │  ├─ ImageFile.py
   │     │  ├─ ImageFilter.py
   │     │  ├─ ImageFont.py
   │     │  ├─ ImageGrab.py
   │     │  ├─ ImageMath.py
   │     │  ├─ ImageMode.py
   │     │  ├─ ImageMorph.py
   │     │  ├─ ImageOps.py
   │     │  ├─ ImagePalette.py
   │     │  ├─ ImagePath.py
   │     │  ├─ ImageQt.py
   │     │  ├─ ImageSequence.py
   │     │  ├─ ImageShow.py
   │     │  ├─ ImageStat.py
   │     │  ├─ ImageText.py
   │     │  ├─ ImageTk.py
   │     │  ├─ ImageTransform.py
   │     │  ├─ ImageWin.py
   │     │  ├─ ImImagePlugin.py
   │     │  ├─ ImtImagePlugin.py
   │     │  ├─ IptcImagePlugin.py
   │     │  ├─ Jpeg2KImagePlugin.py
   │     │  ├─ JpegImagePlugin.py
   │     │  ├─ JpegPresets.py
   │     │  ├─ McIdasImagePlugin.py
   │     │  ├─ MicImagePlugin.py
   │     │  ├─ MpegImagePlugin.py
   │     │  ├─ MpoImagePlugin.py
   │     │  ├─ MspImagePlugin.py
   │     │  ├─ PaletteFile.py
   │     │  ├─ PalmImagePlugin.py
   │     │  ├─ PcdImagePlugin.py
   │     │  ├─ PcfFontFile.py
   │     │  ├─ PcxImagePlugin.py
   │     │  ├─ PdfImagePlugin.py
   │     │  ├─ PdfParser.py
   │     │  ├─ PixarImagePlugin.py
   │     │  ├─ PngImagePlugin.py
   │     │  ├─ PpmImagePlugin.py
   │     │  ├─ PsdImagePlugin.py
   │     │  ├─ PSDraw.py
   │     │  ├─ py.typed
   │     │  ├─ QoiImagePlugin.py
   │     │  ├─ report.py
   │     │  ├─ SgiImagePlugin.py
   │     │  ├─ SpiderImagePlugin.py
   │     │  ├─ SunImagePlugin.py
   │     │  ├─ TarIO.py
   │     │  ├─ TgaImagePlugin.py
   │     │  ├─ TiffImagePlugin.py
   │     │  ├─ TiffTags.py
   │     │  ├─ WalImageFile.py
   │     │  ├─ WebPImagePlugin.py
   │     │  ├─ WmfImagePlugin.py
   │     │  ├─ XbmImagePlugin.py
   │     │  ├─ XpmImagePlugin.py
   │     │  ├─ XVThumbImagePlugin.py
   │     │  ├─ _avif.pyi
   │     │  ├─ _binary.py
   │     │  ├─ _deprecate.py
   │     │  ├─ _imaging.pyi
   │     │  ├─ _imagingcms.pyi
   │     │  ├─ _imagingft.pyi
   │     │  ├─ _imagingmath.pyi
   │     │  ├─ _imagingmorph.pyi
   │     │  ├─ _imagingtk.pyi
   │     │  ├─ _tkinter_finder.py
   │     │  ├─ _typing.py
   │     │  ├─ _util.py
   │     │  ├─ _version.py
   │     │  ├─ _webp.pyi
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ pillow-12.3.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ sboms
   │     │  │  └─ pillow-12.3.0.cdx.json
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ pip
   │     │  ├─ py.typed
   │     │  ├─ _internal
   │     │  │  ├─ cache.py
   │     │  │  ├─ cli
   │     │  │  │  ├─ autocompletion.py
   │     │  │  │  ├─ base_command.py
   │     │  │  │  ├─ cmdoptions.py
   │     │  │  │  ├─ command_context.py
   │     │  │  │  ├─ main.py
   │     │  │  │  ├─ main_parser.py
   │     │  │  │  ├─ parser.py
   │     │  │  │  ├─ progress_bars.py
   │     │  │  │  ├─ req_command.py
   │     │  │  │  ├─ spinners.py
   │     │  │  │  ├─ status_codes.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ commands
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ completion.py
   │     │  │  │  ├─ configuration.py
   │     │  │  │  ├─ debug.py
   │     │  │  │  ├─ download.py
   │     │  │  │  ├─ freeze.py
   │     │  │  │  ├─ hash.py
   │     │  │  │  ├─ help.py
   │     │  │  │  ├─ index.py
   │     │  │  │  ├─ inspect.py
   │     │  │  │  ├─ install.py
   │     │  │  │  ├─ list.py
   │     │  │  │  ├─ search.py
   │     │  │  │  ├─ show.py
   │     │  │  │  ├─ uninstall.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ configuration.py
   │     │  │  ├─ distributions
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ installed.py
   │     │  │  │  ├─ sdist.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ index
   │     │  │  │  ├─ collector.py
   │     │  │  │  ├─ package_finder.py
   │     │  │  │  ├─ sources.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ locations
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ _distutils.py
   │     │  │  │  ├─ _sysconfig.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ main.py
   │     │  │  ├─ metadata
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ importlib
   │     │  │  │  │  ├─ _compat.py
   │     │  │  │  │  ├─ _dists.py
   │     │  │  │  │  ├─ _envs.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ pkg_resources.py
   │     │  │  │  ├─ _json.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ models
   │     │  │  │  ├─ candidate.py
   │     │  │  │  ├─ direct_url.py
   │     │  │  │  ├─ format_control.py
   │     │  │  │  ├─ index.py
   │     │  │  │  ├─ installation_report.py
   │     │  │  │  ├─ link.py
   │     │  │  │  ├─ scheme.py
   │     │  │  │  ├─ search_scope.py
   │     │  │  │  ├─ selection_prefs.py
   │     │  │  │  ├─ target_python.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ network
   │     │  │  │  ├─ auth.py
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ download.py
   │     │  │  │  ├─ lazy_wheel.py
   │     │  │  │  ├─ session.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ xmlrpc.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ operations
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ freeze.py
   │     │  │  │  ├─ install
   │     │  │  │  │  ├─ editable_legacy.py
   │     │  │  │  │  ├─ legacy.py
   │     │  │  │  │  ├─ wheel.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ prepare.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pyproject.py
   │     │  │  ├─ req
   │     │  │  │  ├─ constructors.py
   │     │  │  │  ├─ req_file.py
   │     │  │  │  ├─ req_install.py
   │     │  │  │  ├─ req_set.py
   │     │  │  │  ├─ req_uninstall.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ resolution
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ legacy
   │     │  │  │  │  ├─ resolver.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ resolvelib
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ candidates.py
   │     │  │  │  │  ├─ factory.py
   │     │  │  │  │  ├─ found_candidates.py
   │     │  │  │  │  ├─ provider.py
   │     │  │  │  │  ├─ reporter.py
   │     │  │  │  │  ├─ requirements.py
   │     │  │  │  │  ├─ resolver.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ self_outdated_check.py
   │     │  │  ├─ utils
   │     │  │  │  ├─ appdirs.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ compatibility_tags.py
   │     │  │  │  ├─ datetime.py
   │     │  │  │  ├─ deprecation.py
   │     │  │  │  ├─ direct_url_helpers.py
   │     │  │  │  ├─ distutils_args.py
   │     │  │  │  ├─ egg_link.py
   │     │  │  │  ├─ encoding.py
   │     │  │  │  ├─ entrypoints.py
   │     │  │  │  ├─ filesystem.py
   │     │  │  │  ├─ filetypes.py
   │     │  │  │  ├─ glibc.py
   │     │  │  │  ├─ hashes.py
   │     │  │  │  ├─ inject_securetransport.py
   │     │  │  │  ├─ logging.py
   │     │  │  │  ├─ misc.py
   │     │  │  │  ├─ models.py
   │     │  │  │  ├─ packaging.py
   │     │  │  │  ├─ subprocess.py
   │     │  │  │  ├─ temp_dir.py
   │     │  │  │  ├─ unpacking.py
   │     │  │  │  ├─ urls.py
   │     │  │  │  ├─ virtualenv.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  ├─ _log.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vcs
   │     │  │  │  ├─ bazaar.py
   │     │  │  │  ├─ git.py
   │     │  │  │  ├─ mercurial.py
   │     │  │  │  ├─ subversion.py
   │     │  │  │  ├─ versioncontrol.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ _vendor
   │     │  │  ├─ cachecontrol
   │     │  │  │  ├─ adapter.py
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ caches
   │     │  │  │  │  ├─ file_cache.py
   │     │  │  │  │  ├─ redis_cache.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ controller.py
   │     │  │  │  ├─ filewrapper.py
   │     │  │  │  ├─ heuristics.py
   │     │  │  │  ├─ serialize.py
   │     │  │  │  ├─ wrapper.py
   │     │  │  │  ├─ _cmd.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ certifi
   │     │  │  │  ├─ cacert.pem
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ chardet
   │     │  │  │  ├─ big5freq.py
   │     │  │  │  ├─ big5prober.py
   │     │  │  │  ├─ chardistribution.py
   │     │  │  │  ├─ charsetgroupprober.py
   │     │  │  │  ├─ charsetprober.py
   │     │  │  │  ├─ cli
   │     │  │  │  │  ├─ chardetect.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ codingstatemachine.py
   │     │  │  │  ├─ cp949prober.py
   │     │  │  │  ├─ enums.py
   │     │  │  │  ├─ escprober.py
   │     │  │  │  ├─ escsm.py
   │     │  │  │  ├─ eucjpprober.py
   │     │  │  │  ├─ euckrfreq.py
   │     │  │  │  ├─ euckrprober.py
   │     │  │  │  ├─ euctwfreq.py
   │     │  │  │  ├─ euctwprober.py
   │     │  │  │  ├─ gb2312freq.py
   │     │  │  │  ├─ gb2312prober.py
   │     │  │  │  ├─ hebrewprober.py
   │     │  │  │  ├─ jisfreq.py
   │     │  │  │  ├─ johabfreq.py
   │     │  │  │  ├─ johabprober.py
   │     │  │  │  ├─ jpcntx.py
   │     │  │  │  ├─ langbulgarianmodel.py
   │     │  │  │  ├─ langgreekmodel.py
   │     │  │  │  ├─ langhebrewmodel.py
   │     │  │  │  ├─ langhungarianmodel.py
   │     │  │  │  ├─ langrussianmodel.py
   │     │  │  │  ├─ langthaimodel.py
   │     │  │  │  ├─ langturkishmodel.py
   │     │  │  │  ├─ latin1prober.py
   │     │  │  │  ├─ mbcharsetprober.py
   │     │  │  │  ├─ mbcsgroupprober.py
   │     │  │  │  ├─ mbcssm.py
   │     │  │  │  ├─ metadata
   │     │  │  │  │  ├─ languages.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sbcharsetprober.py
   │     │  │  │  ├─ sbcsgroupprober.py
   │     │  │  │  ├─ sjisprober.py
   │     │  │  │  ├─ universaldetector.py
   │     │  │  │  ├─ utf1632prober.py
   │     │  │  │  ├─ utf8prober.py
   │     │  │  │  ├─ version.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ colorama
   │     │  │  │  ├─ ansi.py
   │     │  │  │  ├─ ansitowin32.py
   │     │  │  │  ├─ initialise.py
   │     │  │  │  ├─ win32.py
   │     │  │  │  ├─ winterm.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ distlib
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ database.py
   │     │  │  │  ├─ index.py
   │     │  │  │  ├─ locators.py
   │     │  │  │  ├─ manifest.py
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ metadata.py
   │     │  │  │  ├─ resources.py
   │     │  │  │  ├─ scripts.py
   │     │  │  │  ├─ t32.exe
   │     │  │  │  ├─ t64-arm.exe
   │     │  │  │  ├─ t64.exe
   │     │  │  │  ├─ util.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ w32.exe
   │     │  │  │  ├─ w64-arm.exe
   │     │  │  │  ├─ w64.exe
   │     │  │  │  ├─ wheel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ distro
   │     │  │  │  ├─ distro.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ idna
   │     │  │  │  ├─ codec.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ idnadata.py
   │     │  │  │  ├─ intranges.py
   │     │  │  │  ├─ package_data.py
   │     │  │  │  ├─ uts46data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ msgpack
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ ext.py
   │     │  │  │  ├─ fallback.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ packaging
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ requirements.py
   │     │  │  │  ├─ specifiers.py
   │     │  │  │  ├─ tags.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ _manylinux.py
   │     │  │  │  ├─ _musllinux.py
   │     │  │  │  ├─ _structures.py
   │     │  │  │  ├─ __about__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pep517
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ colorlog.py
   │     │  │  │  ├─ dirtools.py
   │     │  │  │  ├─ in_process
   │     │  │  │  │  ├─ _in_process.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ meta.py
   │     │  │  │  ├─ wrappers.py
   │     │  │  │  ├─ _compat.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pkg_resources
   │     │  │  │  ├─ py31compat.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ platformdirs
   │     │  │  │  ├─ android.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ macos.py
   │     │  │  │  ├─ unix.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ windows.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ pygments
   │     │  │  │  ├─ cmdline.py
   │     │  │  │  ├─ console.py
   │     │  │  │  ├─ filter.py
   │     │  │  │  ├─ filters
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ formatter.py
   │     │  │  │  ├─ formatters
   │     │  │  │  │  ├─ bbcode.py
   │     │  │  │  │  ├─ groff.py
   │     │  │  │  │  ├─ html.py
   │     │  │  │  │  ├─ img.py
   │     │  │  │  │  ├─ irc.py
   │     │  │  │  │  ├─ latex.py
   │     │  │  │  │  ├─ other.py
   │     │  │  │  │  ├─ pangomarkup.py
   │     │  │  │  │  ├─ rtf.py
   │     │  │  │  │  ├─ svg.py
   │     │  │  │  │  ├─ terminal.py
   │     │  │  │  │  ├─ terminal256.py
   │     │  │  │  │  ├─ _mapping.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ lexer.py
   │     │  │  │  ├─ lexers
   │     │  │  │  │  ├─ python.py
   │     │  │  │  │  ├─ _mapping.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ modeline.py
   │     │  │  │  ├─ plugin.py
   │     │  │  │  ├─ regexopt.py
   │     │  │  │  ├─ scanner.py
   │     │  │  │  ├─ sphinxext.py
   │     │  │  │  ├─ style.py
   │     │  │  │  ├─ styles
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ token.py
   │     │  │  │  ├─ unistring.py
   │     │  │  │  ├─ util.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ pyparsing
   │     │  │  │  ├─ actions.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ diagram
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ helpers.py
   │     │  │  │  ├─ results.py
   │     │  │  │  ├─ testing.py
   │     │  │  │  ├─ unicode.py
   │     │  │  │  ├─ util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ requests
   │     │  │  │  ├─ adapters.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ auth.py
   │     │  │  │  ├─ certs.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ cookies.py
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ help.py
   │     │  │  │  ├─ hooks.py
   │     │  │  │  ├─ models.py
   │     │  │  │  ├─ packages.py
   │     │  │  │  ├─ sessions.py
   │     │  │  │  ├─ status_codes.py
   │     │  │  │  ├─ structures.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ _internal_utils.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __version__.py
   │     │  │  ├─ resolvelib
   │     │  │  │  ├─ compat
   │     │  │  │  │  ├─ collections_abc.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ providers.py
   │     │  │  │  ├─ reporters.py
   │     │  │  │  ├─ resolvers.py
   │     │  │  │  ├─ structs.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ rich
   │     │  │  │  ├─ abc.py
   │     │  │  │  ├─ align.py
   │     │  │  │  ├─ ansi.py
   │     │  │  │  ├─ bar.py
   │     │  │  │  ├─ box.py
   │     │  │  │  ├─ cells.py
   │     │  │  │  ├─ color.py
   │     │  │  │  ├─ color_triplet.py
   │     │  │  │  ├─ columns.py
   │     │  │  │  ├─ console.py
   │     │  │  │  ├─ constrain.py
   │     │  │  │  ├─ containers.py
   │     │  │  │  ├─ control.py
   │     │  │  │  ├─ default_styles.py
   │     │  │  │  ├─ diagnose.py
   │     │  │  │  ├─ emoji.py
   │     │  │  │  ├─ errors.py
   │     │  │  │  ├─ filesize.py
   │     │  │  │  ├─ file_proxy.py
   │     │  │  │  ├─ highlighter.py
   │     │  │  │  ├─ json.py
   │     │  │  │  ├─ jupyter.py
   │     │  │  │  ├─ layout.py
   │     │  │  │  ├─ live.py
   │     │  │  │  ├─ live_render.py
   │     │  │  │  ├─ logging.py
   │     │  │  │  ├─ markup.py
   │     │  │  │  ├─ measure.py
   │     │  │  │  ├─ padding.py
   │     │  │  │  ├─ pager.py
   │     │  │  │  ├─ palette.py
   │     │  │  │  ├─ panel.py
   │     │  │  │  ├─ pretty.py
   │     │  │  │  ├─ progress.py
   │     │  │  │  ├─ progress_bar.py
   │     │  │  │  ├─ prompt.py
   │     │  │  │  ├─ protocol.py
   │     │  │  │  ├─ region.py
   │     │  │  │  ├─ repr.py
   │     │  │  │  ├─ rule.py
   │     │  │  │  ├─ scope.py
   │     │  │  │  ├─ screen.py
   │     │  │  │  ├─ segment.py
   │     │  │  │  ├─ spinner.py
   │     │  │  │  ├─ status.py
   │     │  │  │  ├─ style.py
   │     │  │  │  ├─ styled.py
   │     │  │  │  ├─ syntax.py
   │     │  │  │  ├─ table.py
   │     │  │  │  ├─ terminal_theme.py
   │     │  │  │  ├─ text.py
   │     │  │  │  ├─ theme.py
   │     │  │  │  ├─ themes.py
   │     │  │  │  ├─ traceback.py
   │     │  │  │  ├─ tree.py
   │     │  │  │  ├─ _cell_widths.py
   │     │  │  │  ├─ _emoji_codes.py
   │     │  │  │  ├─ _emoji_replace.py
   │     │  │  │  ├─ _export_format.py
   │     │  │  │  ├─ _extension.py
   │     │  │  │  ├─ _inspect.py
   │     │  │  │  ├─ _log_render.py
   │     │  │  │  ├─ _loop.py
   │     │  │  │  ├─ _palettes.py
   │     │  │  │  ├─ _pick.py
   │     │  │  │  ├─ _ratio.py
   │     │  │  │  ├─ _spinners.py
   │     │  │  │  ├─ _stack.py
   │     │  │  │  ├─ _timer.py
   │     │  │  │  ├─ _win32_console.py
   │     │  │  │  ├─ _windows.py
   │     │  │  │  ├─ _windows_renderer.py
   │     │  │  │  ├─ _wrap.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ six.py
   │     │  │  ├─ tenacity
   │     │  │  │  ├─ after.py
   │     │  │  │  ├─ before.py
   │     │  │  │  ├─ before_sleep.py
   │     │  │  │  ├─ nap.py
   │     │  │  │  ├─ retry.py
   │     │  │  │  ├─ stop.py
   │     │  │  │  ├─ tornadoweb.py
   │     │  │  │  ├─ wait.py
   │     │  │  │  ├─ _asyncio.py
   │     │  │  │  ├─ _utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tomli
   │     │  │  │  ├─ _parser.py
   │     │  │  │  ├─ _re.py
   │     │  │  │  ├─ _types.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ typing_extensions.py
   │     │  │  ├─ urllib3
   │     │  │  │  ├─ connection.py
   │     │  │  │  ├─ connectionpool.py
   │     │  │  │  ├─ contrib
   │     │  │  │  │  ├─ appengine.py
   │     │  │  │  │  ├─ ntlmpool.py
   │     │  │  │  │  ├─ pyopenssl.py
   │     │  │  │  │  ├─ securetransport.py
   │     │  │  │  │  ├─ socks.py
   │     │  │  │  │  ├─ _appengine_environ.py
   │     │  │  │  │  ├─ _securetransport
   │     │  │  │  │  │  ├─ bindings.py
   │     │  │  │  │  │  ├─ low_level.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ fields.py
   │     │  │  │  ├─ filepost.py
   │     │  │  │  ├─ packages
   │     │  │  │  │  ├─ backports
   │     │  │  │  │  │  ├─ makefile.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ six.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ poolmanager.py
   │     │  │  │  ├─ request.py
   │     │  │  │  ├─ response.py
   │     │  │  │  ├─ util
   │     │  │  │  │  ├─ connection.py
   │     │  │  │  │  ├─ proxy.py
   │     │  │  │  │  ├─ queue.py
   │     │  │  │  │  ├─ request.py
   │     │  │  │  │  ├─ response.py
   │     │  │  │  │  ├─ retry.py
   │     │  │  │  │  ├─ ssltransport.py
   │     │  │  │  │  ├─ ssl_.py
   │     │  │  │  │  ├─ ssl_match_hostname.py
   │     │  │  │  │  ├─ timeout.py
   │     │  │  │  │  ├─ url.py
   │     │  │  │  │  ├─ wait.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _collections.py
   │     │  │  │  ├─ _version.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vendor.txt
   │     │  │  ├─ webencodings
   │     │  │  │  ├─ labels.py
   │     │  │  │  ├─ mklabels.py
   │     │  │  │  ├─ tests.py
   │     │  │  │  ├─ x_user_defined.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ __init__.py
   │     │  ├─ __main__.py
   │     │  └─ __pip-runner__.py
   │     ├─ pip-22.3.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ pluggy
   │     │  ├─ py.typed
   │     │  ├─ _callers.py
   │     │  ├─ _hooks.py
   │     │  ├─ _manager.py
   │     │  ├─ _result.py
   │     │  ├─ _tracing.py
   │     │  ├─ _version.py
   │     │  ├─ _warnings.py
   │     │  └─ __init__.py
   │     ├─ pluggy-1.6.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ protobuf-5.26.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ py.py
   │     ├─ pybind11_abseil
   │     │  ├─ status.pyi
   │     │  └─ __init__.py
   │     ├─ pycparser
   │     │  ├─ ast_transforms.py
   │     │  ├─ c_ast.py
   │     │  ├─ c_generator.py
   │     │  ├─ c_lexer.py
   │     │  ├─ c_parser.py
   │     │  ├─ _ast_gen.py
   │     │  ├─ _c_ast.cfg
   │     │  └─ __init__.py
   │     ├─ pycparser-3.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ pygments
   │     │  ├─ cmdline.py
   │     │  ├─ console.py
   │     │  ├─ filter.py
   │     │  ├─ filters
   │     │  │  └─ __init__.py
   │     │  ├─ formatter.py
   │     │  ├─ formatters
   │     │  │  ├─ bbcode.py
   │     │  │  ├─ groff.py
   │     │  │  ├─ html.py
   │     │  │  ├─ img.py
   │     │  │  ├─ irc.py
   │     │  │  ├─ latex.py
   │     │  │  ├─ other.py
   │     │  │  ├─ pangomarkup.py
   │     │  │  ├─ rtf.py
   │     │  │  ├─ svg.py
   │     │  │  ├─ terminal.py
   │     │  │  ├─ terminal256.py
   │     │  │  ├─ _mapping.py
   │     │  │  └─ __init__.py
   │     │  ├─ lexer.py
   │     │  ├─ lexers
   │     │  │  ├─ actionscript.py
   │     │  │  ├─ ada.py
   │     │  │  ├─ agile.py
   │     │  │  ├─ algebra.py
   │     │  │  ├─ ambient.py
   │     │  │  ├─ amdgpu.py
   │     │  │  ├─ ampl.py
   │     │  │  ├─ apdlexer.py
   │     │  │  ├─ apl.py
   │     │  │  ├─ archetype.py
   │     │  │  ├─ arrow.py
   │     │  │  ├─ arturo.py
   │     │  │  ├─ asc.py
   │     │  │  ├─ asm.py
   │     │  │  ├─ asn1.py
   │     │  │  ├─ automation.py
   │     │  │  ├─ bare.py
   │     │  │  ├─ basic.py
   │     │  │  ├─ bdd.py
   │     │  │  ├─ berry.py
   │     │  │  ├─ bibtex.py
   │     │  │  ├─ bitbake.py
   │     │  │  ├─ blueprint.py
   │     │  │  ├─ boa.py
   │     │  │  ├─ bqn.py
   │     │  │  ├─ business.py
   │     │  │  ├─ capnproto.py
   │     │  │  ├─ carbon.py
   │     │  │  ├─ cddl.py
   │     │  │  ├─ cel.py
   │     │  │  ├─ chapel.py
   │     │  │  ├─ clean.py
   │     │  │  ├─ codeql.py
   │     │  │  ├─ comal.py
   │     │  │  ├─ compiled.py
   │     │  │  ├─ configs.py
   │     │  │  ├─ console.py
   │     │  │  ├─ cplint.py
   │     │  │  ├─ crystal.py
   │     │  │  ├─ csound.py
   │     │  │  ├─ css.py
   │     │  │  ├─ c_cpp.py
   │     │  │  ├─ c_like.py
   │     │  │  ├─ d.py
   │     │  │  ├─ dalvik.py
   │     │  │  ├─ data.py
   │     │  │  ├─ dax.py
   │     │  │  ├─ devicetree.py
   │     │  │  ├─ diff.py
   │     │  │  ├─ dns.py
   │     │  │  ├─ dotnet.py
   │     │  │  ├─ dsls.py
   │     │  │  ├─ dylan.py
   │     │  │  ├─ ecl.py
   │     │  │  ├─ eiffel.py
   │     │  │  ├─ elm.py
   │     │  │  ├─ elpi.py
   │     │  │  ├─ email.py
   │     │  │  ├─ erlang.py
   │     │  │  ├─ esoteric.py
   │     │  │  ├─ ezhil.py
   │     │  │  ├─ factor.py
   │     │  │  ├─ fantom.py
   │     │  │  ├─ felix.py
   │     │  │  ├─ fift.py
   │     │  │  ├─ floscript.py
   │     │  │  ├─ forth.py
   │     │  │  ├─ fortran.py
   │     │  │  ├─ foxpro.py
   │     │  │  ├─ freefem.py
   │     │  │  ├─ func.py
   │     │  │  ├─ functional.py
   │     │  │  ├─ futhark.py
   │     │  │  ├─ gcodelexer.py
   │     │  │  ├─ gdscript.py
   │     │  │  ├─ gleam.py
   │     │  │  ├─ go.py
   │     │  │  ├─ grammar_notation.py
   │     │  │  ├─ graph.py
   │     │  │  ├─ graphics.py
   │     │  │  ├─ graphql.py
   │     │  │  ├─ graphviz.py
   │     │  │  ├─ gsql.py
   │     │  │  ├─ hare.py
   │     │  │  ├─ haskell.py
   │     │  │  ├─ haxe.py
   │     │  │  ├─ hdl.py
   │     │  │  ├─ hexdump.py
   │     │  │  ├─ html.py
   │     │  │  ├─ idl.py
   │     │  │  ├─ igor.py
   │     │  │  ├─ inferno.py
   │     │  │  ├─ installers.py
   │     │  │  ├─ int_fiction.py
   │     │  │  ├─ iolang.py
   │     │  │  ├─ j.py
   │     │  │  ├─ javascript.py
   │     │  │  ├─ jmespath.py
   │     │  │  ├─ jslt.py
   │     │  │  ├─ json5.py
   │     │  │  ├─ jsonnet.py
   │     │  │  ├─ jsx.py
   │     │  │  ├─ julia.py
   │     │  │  ├─ jvm.py
   │     │  │  ├─ kuin.py
   │     │  │  ├─ kusto.py
   │     │  │  ├─ ldap.py
   │     │  │  ├─ lean.py
   │     │  │  ├─ lilypond.py
   │     │  │  ├─ lisp.py
   │     │  │  ├─ macaulay2.py
   │     │  │  ├─ make.py
   │     │  │  ├─ maple.py
   │     │  │  ├─ markup.py
   │     │  │  ├─ math.py
   │     │  │  ├─ matlab.py
   │     │  │  ├─ maxima.py
   │     │  │  ├─ meson.py
   │     │  │  ├─ mime.py
   │     │  │  ├─ minecraft.py
   │     │  │  ├─ mips.py
   │     │  │  ├─ ml.py
   │     │  │  ├─ modeling.py
   │     │  │  ├─ modula2.py
   │     │  │  ├─ mojo.py
   │     │  │  ├─ monte.py
   │     │  │  ├─ mosel.py
   │     │  │  ├─ ncl.py
   │     │  │  ├─ nimrod.py
   │     │  │  ├─ nit.py
   │     │  │  ├─ nix.py
   │     │  │  ├─ numbair.py
   │     │  │  ├─ oberon.py
   │     │  │  ├─ objective.py
   │     │  │  ├─ ooc.py
   │     │  │  ├─ openscad.py
   │     │  │  ├─ other.py
   │     │  │  ├─ parasail.py
   │     │  │  ├─ parsers.py
   │     │  │  ├─ pascal.py
   │     │  │  ├─ pawn.py
   │     │  │  ├─ pddl.py
   │     │  │  ├─ perl.py
   │     │  │  ├─ phix.py
   │     │  │  ├─ php.py
   │     │  │  ├─ pointless.py
   │     │  │  ├─ pony.py
   │     │  │  ├─ praat.py
   │     │  │  ├─ procfile.py
   │     │  │  ├─ prolog.py
   │     │  │  ├─ promql.py
   │     │  │  ├─ prql.py
   │     │  │  ├─ ptx.py
   │     │  │  ├─ purescript.py
   │     │  │  ├─ python.py
   │     │  │  ├─ q.py
   │     │  │  ├─ qlik.py
   │     │  │  ├─ qvt.py
   │     │  │  ├─ r.py
   │     │  │  ├─ rdf.py
   │     │  │  ├─ rebol.py
   │     │  │  ├─ rego.py
   │     │  │  ├─ rell.py
   │     │  │  ├─ resource.py
   │     │  │  ├─ ride.py
   │     │  │  ├─ rita.py
   │     │  │  ├─ rnc.py
   │     │  │  ├─ roboconf.py
   │     │  │  ├─ robotframework.py
   │     │  │  ├─ ruby.py
   │     │  │  ├─ rust.py
   │     │  │  ├─ sas.py
   │     │  │  ├─ savi.py
   │     │  │  ├─ scdoc.py
   │     │  │  ├─ scripting.py
   │     │  │  ├─ sgf.py
   │     │  │  ├─ shell.py
   │     │  │  ├─ sieve.py
   │     │  │  ├─ slash.py
   │     │  │  ├─ smalltalk.py
   │     │  │  ├─ smithy.py
   │     │  │  ├─ smv.py
   │     │  │  ├─ snobol.py
   │     │  │  ├─ solidity.py
   │     │  │  ├─ soong.py
   │     │  │  ├─ sophia.py
   │     │  │  ├─ special.py
   │     │  │  ├─ spice.py
   │     │  │  ├─ sql.py
   │     │  │  ├─ srcinfo.py
   │     │  │  ├─ stata.py
   │     │  │  ├─ supercollider.py
   │     │  │  ├─ tablegen.py
   │     │  │  ├─ tact.py
   │     │  │  ├─ tal.py
   │     │  │  ├─ tcl.py
   │     │  │  ├─ teal.py
   │     │  │  ├─ templates.py
   │     │  │  ├─ teraterm.py
   │     │  │  ├─ testing.py
   │     │  │  ├─ text.py
   │     │  │  ├─ textedit.py
   │     │  │  ├─ textfmts.py
   │     │  │  ├─ theorem.py
   │     │  │  ├─ thingsdb.py
   │     │  │  ├─ tlb.py
   │     │  │  ├─ tls.py
   │     │  │  ├─ tnt.py
   │     │  │  ├─ trafficscript.py
   │     │  │  ├─ typoscript.py
   │     │  │  ├─ typst.py
   │     │  │  ├─ ul4.py
   │     │  │  ├─ unicon.py
   │     │  │  ├─ urbi.py
   │     │  │  ├─ usd.py
   │     │  │  ├─ varnish.py
   │     │  │  ├─ verification.py
   │     │  │  ├─ verifpal.py
   │     │  │  ├─ vip.py
   │     │  │  ├─ vyper.py
   │     │  │  ├─ web.py
   │     │  │  ├─ webassembly.py
   │     │  │  ├─ webidl.py
   │     │  │  ├─ webmisc.py
   │     │  │  ├─ wgsl.py
   │     │  │  ├─ whiley.py
   │     │  │  ├─ wowtoc.py
   │     │  │  ├─ wren.py
   │     │  │  ├─ x10.py
   │     │  │  ├─ xorg.py
   │     │  │  ├─ yang.py
   │     │  │  ├─ yara.py
   │     │  │  ├─ zig.py
   │     │  │  ├─ _ada_builtins.py
   │     │  │  ├─ _asy_builtins.py
   │     │  │  ├─ _cl_builtins.py
   │     │  │  ├─ _cocoa_builtins.py
   │     │  │  ├─ _csound_builtins.py
   │     │  │  ├─ _css_builtins.py
   │     │  │  ├─ _googlesql_builtins.py
   │     │  │  ├─ _julia_builtins.py
   │     │  │  ├─ _lasso_builtins.py
   │     │  │  ├─ _lilypond_builtins.py
   │     │  │  ├─ _luau_builtins.py
   │     │  │  ├─ _lua_builtins.py
   │     │  │  ├─ _mapping.py
   │     │  │  ├─ _mql_builtins.py
   │     │  │  ├─ _mysql_builtins.py
   │     │  │  ├─ _openedge_builtins.py
   │     │  │  ├─ _php_builtins.py
   │     │  │  ├─ _postgres_builtins.py
   │     │  │  ├─ _qlik_builtins.py
   │     │  │  ├─ _scheme_builtins.py
   │     │  │  ├─ _scilab_builtins.py
   │     │  │  ├─ _sourcemod_builtins.py
   │     │  │  ├─ _sql_builtins.py
   │     │  │  ├─ _stan_builtins.py
   │     │  │  ├─ _stata_builtins.py
   │     │  │  ├─ _tsql_builtins.py
   │     │  │  ├─ _usd_builtins.py
   │     │  │  ├─ _vbscript_builtins.py
   │     │  │  ├─ _vim_builtins.py
   │     │  │  └─ __init__.py
   │     │  ├─ modeline.py
   │     │  ├─ plugin.py
   │     │  ├─ regexopt.py
   │     │  ├─ scanner.py
   │     │  ├─ sphinxext.py
   │     │  ├─ style.py
   │     │  ├─ styles
   │     │  │  ├─ abap.py
   │     │  │  ├─ algol.py
   │     │  │  ├─ algol_nu.py
   │     │  │  ├─ arduino.py
   │     │  │  ├─ autumn.py
   │     │  │  ├─ borland.py
   │     │  │  ├─ bw.py
   │     │  │  ├─ coffee.py
   │     │  │  ├─ colorful.py
   │     │  │  ├─ default.py
   │     │  │  ├─ dracula.py
   │     │  │  ├─ emacs.py
   │     │  │  ├─ friendly.py
   │     │  │  ├─ friendly_grayscale.py
   │     │  │  ├─ fruity.py
   │     │  │  ├─ gh_dark.py
   │     │  │  ├─ gruvbox.py
   │     │  │  ├─ igor.py
   │     │  │  ├─ inkpot.py
   │     │  │  ├─ lightbulb.py
   │     │  │  ├─ lilypond.py
   │     │  │  ├─ lovelace.py
   │     │  │  ├─ manni.py
   │     │  │  ├─ material.py
   │     │  │  ├─ monokai.py
   │     │  │  ├─ murphy.py
   │     │  │  ├─ native.py
   │     │  │  ├─ night_owl.py
   │     │  │  ├─ nord.py
   │     │  │  ├─ onedark.py
   │     │  │  ├─ paraiso_dark.py
   │     │  │  ├─ paraiso_light.py
   │     │  │  ├─ pastie.py
   │     │  │  ├─ perldoc.py
   │     │  │  ├─ rainbow_dash.py
   │     │  │  ├─ rrt.py
   │     │  │  ├─ sas.py
   │     │  │  ├─ solarized.py
   │     │  │  ├─ staroffice.py
   │     │  │  ├─ stata_dark.py
   │     │  │  ├─ stata_light.py
   │     │  │  ├─ tango.py
   │     │  │  ├─ trac.py
   │     │  │  ├─ vim.py
   │     │  │  ├─ vs.py
   │     │  │  ├─ xcode.py
   │     │  │  ├─ zenburn.py
   │     │  │  ├─ _mapping.py
   │     │  │  └─ __init__.py
   │     │  ├─ token.py
   │     │  ├─ unistring.py
   │     │  ├─ util.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ pygments-2.21.0.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ AUTHORS
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ pylab.py
   │     ├─ pyparsing
   │     │  ├─ actions.py
   │     │  ├─ ai
   │     │  │  ├─ best_practices.md
   │     │  │  ├─ show_best_practices
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  └─ __init__.py
   │     │  ├─ common.py
   │     │  ├─ core.py
   │     │  ├─ diagram
   │     │  │  └─ __init__.py
   │     │  ├─ exceptions.py
   │     │  ├─ helpers.py
   │     │  ├─ py.typed
   │     │  ├─ results.py
   │     │  ├─ testing.py
   │     │  ├─ tools
   │     │  │  ├─ cvt_pyparsing_pep8_names.py
   │     │  │  └─ __init__.py
   │     │  ├─ unicode.py
   │     │  ├─ util.py
   │     │  ├─ warnings.py
   │     │  └─ __init__.py
   │     ├─ pyparsing-3.3.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ pytest
   │     │  ├─ py.typed
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ pytest-9.1.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ python_dateutil-2.9.0.post0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ pytz
   │     │  ├─ exceptions.py
   │     │  ├─ lazy.py
   │     │  ├─ reference.py
   │     │  ├─ tzfile.py
   │     │  ├─ tzinfo.py
   │     │  ├─ zoneinfo
   │     │  │  ├─ Africa
   │     │  │  │  ├─ Abidjan
   │     │  │  │  ├─ Accra
   │     │  │  │  ├─ Addis_Ababa
   │     │  │  │  ├─ Algiers
   │     │  │  │  ├─ Asmara
   │     │  │  │  ├─ Asmera
   │     │  │  │  ├─ Bamako
   │     │  │  │  ├─ Bangui
   │     │  │  │  ├─ Banjul
   │     │  │  │  ├─ Bissau
   │     │  │  │  ├─ Blantyre
   │     │  │  │  ├─ Brazzaville
   │     │  │  │  ├─ Bujumbura
   │     │  │  │  ├─ Cairo
   │     │  │  │  ├─ Casablanca
   │     │  │  │  ├─ Ceuta
   │     │  │  │  ├─ Conakry
   │     │  │  │  ├─ Dakar
   │     │  │  │  ├─ Dar_es_Salaam
   │     │  │  │  ├─ Djibouti
   │     │  │  │  ├─ Douala
   │     │  │  │  ├─ El_Aaiun
   │     │  │  │  ├─ Freetown
   │     │  │  │  ├─ Gaborone
   │     │  │  │  ├─ Harare
   │     │  │  │  ├─ Johannesburg
   │     │  │  │  ├─ Juba
   │     │  │  │  ├─ Kampala
   │     │  │  │  ├─ Khartoum
   │     │  │  │  ├─ Kigali
   │     │  │  │  ├─ Kinshasa
   │     │  │  │  ├─ Lagos
   │     │  │  │  ├─ Libreville
   │     │  │  │  ├─ Lome
   │     │  │  │  ├─ Luanda
   │     │  │  │  ├─ Lubumbashi
   │     │  │  │  ├─ Lusaka
   │     │  │  │  ├─ Malabo
   │     │  │  │  ├─ Maputo
   │     │  │  │  ├─ Maseru
   │     │  │  │  ├─ Mbabane
   │     │  │  │  ├─ Mogadishu
   │     │  │  │  ├─ Monrovia
   │     │  │  │  ├─ Nairobi
   │     │  │  │  ├─ Ndjamena
   │     │  │  │  ├─ Niamey
   │     │  │  │  ├─ Nouakchott
   │     │  │  │  ├─ Ouagadougou
   │     │  │  │  ├─ Porto-Novo
   │     │  │  │  ├─ Sao_Tome
   │     │  │  │  ├─ Timbuktu
   │     │  │  │  ├─ Tripoli
   │     │  │  │  ├─ Tunis
   │     │  │  │  └─ Windhoek
   │     │  │  ├─ America
   │     │  │  │  ├─ Adak
   │     │  │  │  ├─ Anchorage
   │     │  │  │  ├─ Anguilla
   │     │  │  │  ├─ Antigua
   │     │  │  │  ├─ Araguaina
   │     │  │  │  ├─ Argentina
   │     │  │  │  │  ├─ Buenos_Aires
   │     │  │  │  │  ├─ Catamarca
   │     │  │  │  │  ├─ ComodRivadavia
   │     │  │  │  │  ├─ Cordoba
   │     │  │  │  │  ├─ Jujuy
   │     │  │  │  │  ├─ La_Rioja
   │     │  │  │  │  ├─ Mendoza
   │     │  │  │  │  ├─ Rio_Gallegos
   │     │  │  │  │  ├─ Salta
   │     │  │  │  │  ├─ San_Juan
   │     │  │  │  │  ├─ San_Luis
   │     │  │  │  │  ├─ Tucuman
   │     │  │  │  │  └─ Ushuaia
   │     │  │  │  ├─ Aruba
   │     │  │  │  ├─ Asuncion
   │     │  │  │  ├─ Atikokan
   │     │  │  │  ├─ Atka
   │     │  │  │  ├─ Bahia
   │     │  │  │  ├─ Bahia_Banderas
   │     │  │  │  ├─ Barbados
   │     │  │  │  ├─ Belem
   │     │  │  │  ├─ Belize
   │     │  │  │  ├─ Blanc-Sablon
   │     │  │  │  ├─ Boa_Vista
   │     │  │  │  ├─ Bogota
   │     │  │  │  ├─ Boise
   │     │  │  │  ├─ Buenos_Aires
   │     │  │  │  ├─ Cambridge_Bay
   │     │  │  │  ├─ Campo_Grande
   │     │  │  │  ├─ Cancun
   │     │  │  │  ├─ Caracas
   │     │  │  │  ├─ Catamarca
   │     │  │  │  ├─ Cayenne
   │     │  │  │  ├─ Cayman
   │     │  │  │  ├─ Chicago
   │     │  │  │  ├─ Chihuahua
   │     │  │  │  ├─ Ciudad_Juarez
   │     │  │  │  ├─ Coral_Harbour
   │     │  │  │  ├─ Cordoba
   │     │  │  │  ├─ Costa_Rica
   │     │  │  │  ├─ Coyhaique
   │     │  │  │  ├─ Creston
   │     │  │  │  ├─ Cuiaba
   │     │  │  │  ├─ Curacao
   │     │  │  │  ├─ Danmarkshavn
   │     │  │  │  ├─ Dawson
   │     │  │  │  ├─ Dawson_Creek
   │     │  │  │  ├─ Denver
   │     │  │  │  ├─ Detroit
   │     │  │  │  ├─ Dominica
   │     │  │  │  ├─ Edmonton
   │     │  │  │  ├─ Eirunepe
   │     │  │  │  ├─ El_Salvador
   │     │  │  │  ├─ Ensenada
   │     │  │  │  ├─ Fortaleza
   │     │  │  │  ├─ Fort_Nelson
   │     │  │  │  ├─ Fort_Wayne
   │     │  │  │  ├─ Glace_Bay
   │     │  │  │  ├─ Godthab
   │     │  │  │  ├─ Goose_Bay
   │     │  │  │  ├─ Grand_Turk
   │     │  │  │  ├─ Grenada
   │     │  │  │  ├─ Guadeloupe
   │     │  │  │  ├─ Guatemala
   │     │  │  │  ├─ Guayaquil
   │     │  │  │  ├─ Guyana
   │     │  │  │  ├─ Halifax
   │     │  │  │  ├─ Havana
   │     │  │  │  ├─ Hermosillo
   │     │  │  │  ├─ Indiana
   │     │  │  │  │  ├─ Indianapolis
   │     │  │  │  │  ├─ Knox
   │     │  │  │  │  ├─ Marengo
   │     │  │  │  │  ├─ Petersburg
   │     │  │  │  │  ├─ Tell_City
   │     │  │  │  │  ├─ Vevay
   │     │  │  │  │  ├─ Vincennes
   │     │  │  │  │  └─ Winamac
   │     │  │  │  ├─ Indianapolis
   │     │  │  │  ├─ Inuvik
   │     │  │  │  ├─ Iqaluit
   │     │  │  │  ├─ Jamaica
   │     │  │  │  ├─ Jujuy
   │     │  │  │  ├─ Juneau
   │     │  │  │  ├─ Kentucky
   │     │  │  │  │  ├─ Louisville
   │     │  │  │  │  └─ Monticello
   │     │  │  │  ├─ Knox_IN
   │     │  │  │  ├─ Kralendijk
   │     │  │  │  ├─ La_Paz
   │     │  │  │  ├─ Lima
   │     │  │  │  ├─ Los_Angeles
   │     │  │  │  ├─ Louisville
   │     │  │  │  ├─ Lower_Princes
   │     │  │  │  ├─ Maceio
   │     │  │  │  ├─ Managua
   │     │  │  │  ├─ Manaus
   │     │  │  │  ├─ Marigot
   │     │  │  │  ├─ Martinique
   │     │  │  │  ├─ Matamoros
   │     │  │  │  ├─ Mazatlan
   │     │  │  │  ├─ Mendoza
   │     │  │  │  ├─ Menominee
   │     │  │  │  ├─ Merida
   │     │  │  │  ├─ Metlakatla
   │     │  │  │  ├─ Mexico_City
   │     │  │  │  ├─ Miquelon
   │     │  │  │  ├─ Moncton
   │     │  │  │  ├─ Monterrey
   │     │  │  │  ├─ Montevideo
   │     │  │  │  ├─ Montreal
   │     │  │  │  ├─ Montserrat
   │     │  │  │  ├─ Nassau
   │     │  │  │  ├─ New_York
   │     │  │  │  ├─ Nipigon
   │     │  │  │  ├─ Nome
   │     │  │  │  ├─ Noronha
   │     │  │  │  ├─ North_Dakota
   │     │  │  │  │  ├─ Beulah
   │     │  │  │  │  ├─ Center
   │     │  │  │  │  └─ New_Salem
   │     │  │  │  ├─ Nuuk
   │     │  │  │  ├─ Ojinaga
   │     │  │  │  ├─ Panama
   │     │  │  │  ├─ Pangnirtung
   │     │  │  │  ├─ Paramaribo
   │     │  │  │  ├─ Phoenix
   │     │  │  │  ├─ Port-au-Prince
   │     │  │  │  ├─ Porto_Acre
   │     │  │  │  ├─ Porto_Velho
   │     │  │  │  ├─ Port_of_Spain
   │     │  │  │  ├─ Puerto_Rico
   │     │  │  │  ├─ Punta_Arenas
   │     │  │  │  ├─ Rainy_River
   │     │  │  │  ├─ Rankin_Inlet
   │     │  │  │  ├─ Recife
   │     │  │  │  ├─ Regina
   │     │  │  │  ├─ Resolute
   │     │  │  │  ├─ Rio_Branco
   │     │  │  │  ├─ Rosario
   │     │  │  │  ├─ Santarem
   │     │  │  │  ├─ Santa_Isabel
   │     │  │  │  ├─ Santiago
   │     │  │  │  ├─ Santo_Domingo
   │     │  │  │  ├─ Sao_Paulo
   │     │  │  │  ├─ Scoresbysund
   │     │  │  │  ├─ Shiprock
   │     │  │  │  ├─ Sitka
   │     │  │  │  ├─ St_Barthelemy
   │     │  │  │  ├─ St_Johns
   │     │  │  │  ├─ St_Kitts
   │     │  │  │  ├─ St_Lucia
   │     │  │  │  ├─ St_Thomas
   │     │  │  │  ├─ St_Vincent
   │     │  │  │  ├─ Swift_Current
   │     │  │  │  ├─ Tegucigalpa
   │     │  │  │  ├─ Thule
   │     │  │  │  ├─ Thunder_Bay
   │     │  │  │  ├─ Tijuana
   │     │  │  │  ├─ Toronto
   │     │  │  │  ├─ Tortola
   │     │  │  │  ├─ Vancouver
   │     │  │  │  ├─ Virgin
   │     │  │  │  ├─ Whitehorse
   │     │  │  │  ├─ Winnipeg
   │     │  │  │  ├─ Yakutat
   │     │  │  │  └─ Yellowknife
   │     │  │  ├─ Antarctica
   │     │  │  │  ├─ Casey
   │     │  │  │  ├─ Davis
   │     │  │  │  ├─ DumontDUrville
   │     │  │  │  ├─ Macquarie
   │     │  │  │  ├─ Mawson
   │     │  │  │  ├─ McMurdo
   │     │  │  │  ├─ Palmer
   │     │  │  │  ├─ Rothera
   │     │  │  │  ├─ South_Pole
   │     │  │  │  ├─ Syowa
   │     │  │  │  ├─ Troll
   │     │  │  │  └─ Vostok
   │     │  │  ├─ Arctic
   │     │  │  │  └─ Longyearbyen
   │     │  │  ├─ Asia
   │     │  │  │  ├─ Aden
   │     │  │  │  ├─ Almaty
   │     │  │  │  ├─ Amman
   │     │  │  │  ├─ Anadyr
   │     │  │  │  ├─ Aqtau
   │     │  │  │  ├─ Aqtobe
   │     │  │  │  ├─ Ashgabat
   │     │  │  │  ├─ Ashkhabad
   │     │  │  │  ├─ Atyrau
   │     │  │  │  ├─ Baghdad
   │     │  │  │  ├─ Bahrain
   │     │  │  │  ├─ Baku
   │     │  │  │  ├─ Bangkok
   │     │  │  │  ├─ Barnaul
   │     │  │  │  ├─ Beirut
   │     │  │  │  ├─ Bishkek
   │     │  │  │  ├─ Brunei
   │     │  │  │  ├─ Calcutta
   │     │  │  │  ├─ Chita
   │     │  │  │  ├─ Choibalsan
   │     │  │  │  ├─ Chongqing
   │     │  │  │  ├─ Chungking
   │     │  │  │  ├─ Colombo
   │     │  │  │  ├─ Dacca
   │     │  │  │  ├─ Damascus
   │     │  │  │  ├─ Dhaka
   │     │  │  │  ├─ Dili
   │     │  │  │  ├─ Dubai
   │     │  │  │  ├─ Dushanbe
   │     │  │  │  ├─ Famagusta
   │     │  │  │  ├─ Gaza
   │     │  │  │  ├─ Harbin
   │     │  │  │  ├─ Hebron
   │     │  │  │  ├─ Hong_Kong
   │     │  │  │  ├─ Hovd
   │     │  │  │  ├─ Ho_Chi_Minh
   │     │  │  │  ├─ Irkutsk
   │     │  │  │  ├─ Istanbul
   │     │  │  │  ├─ Jakarta
   │     │  │  │  ├─ Jayapura
   │     │  │  │  ├─ Jerusalem
   │     │  │  │  ├─ Kabul
   │     │  │  │  ├─ Kamchatka
   │     │  │  │  ├─ Karachi
   │     │  │  │  ├─ Kashgar
   │     │  │  │  ├─ Kathmandu
   │     │  │  │  ├─ Katmandu
   │     │  │  │  ├─ Khandyga
   │     │  │  │  ├─ Kolkata
   │     │  │  │  ├─ Krasnoyarsk
   │     │  │  │  ├─ Kuala_Lumpur
   │     │  │  │  ├─ Kuching
   │     │  │  │  ├─ Kuwait
   │     │  │  │  ├─ Macao
   │     │  │  │  ├─ Macau
   │     │  │  │  ├─ Magadan
   │     │  │  │  ├─ Makassar
   │     │  │  │  ├─ Manila
   │     │  │  │  ├─ Muscat
   │     │  │  │  ├─ Nicosia
   │     │  │  │  ├─ Novokuznetsk
   │     │  │  │  ├─ Novosibirsk
   │     │  │  │  ├─ Omsk
   │     │  │  │  ├─ Oral
   │     │  │  │  ├─ Phnom_Penh
   │     │  │  │  ├─ Pontianak
   │     │  │  │  ├─ Pyongyang
   │     │  │  │  ├─ Qatar
   │     │  │  │  ├─ Qostanay
   │     │  │  │  ├─ Qyzylorda
   │     │  │  │  ├─ Rangoon
   │     │  │  │  ├─ Riyadh
   │     │  │  │  ├─ Saigon
   │     │  │  │  ├─ Sakhalin
   │     │  │  │  ├─ Samarkand
   │     │  │  │  ├─ Seoul
   │     │  │  │  ├─ Shanghai
   │     │  │  │  ├─ Singapore
   │     │  │  │  ├─ Srednekolymsk
   │     │  │  │  ├─ Taipei
   │     │  │  │  ├─ Tashkent
   │     │  │  │  ├─ Tbilisi
   │     │  │  │  ├─ Tehran
   │     │  │  │  ├─ Tel_Aviv
   │     │  │  │  ├─ Thimbu
   │     │  │  │  ├─ Thimphu
   │     │  │  │  ├─ Tokyo
   │     │  │  │  ├─ Tomsk
   │     │  │  │  ├─ Ujung_Pandang
   │     │  │  │  ├─ Ulaanbaatar
   │     │  │  │  ├─ Ulan_Bator
   │     │  │  │  ├─ Urumqi
   │     │  │  │  ├─ Ust-Nera
   │     │  │  │  ├─ Vientiane
   │     │  │  │  ├─ Vladivostok
   │     │  │  │  ├─ Yakutsk
   │     │  │  │  ├─ Yangon
   │     │  │  │  ├─ Yekaterinburg
   │     │  │  │  └─ Yerevan
   │     │  │  ├─ Atlantic
   │     │  │  │  ├─ Azores
   │     │  │  │  ├─ Bermuda
   │     │  │  │  ├─ Canary
   │     │  │  │  ├─ Cape_Verde
   │     │  │  │  ├─ Faeroe
   │     │  │  │  ├─ Faroe
   │     │  │  │  ├─ Jan_Mayen
   │     │  │  │  ├─ Madeira
   │     │  │  │  ├─ Reykjavik
   │     │  │  │  ├─ South_Georgia
   │     │  │  │  ├─ Stanley
   │     │  │  │  └─ St_Helena
   │     │  │  ├─ Australia
   │     │  │  │  ├─ .tmpHBU9kT
   │     │  │  │  ├─ ACT
   │     │  │  │  ├─ Adelaide
   │     │  │  │  ├─ Brisbane
   │     │  │  │  ├─ Broken_Hill
   │     │  │  │  ├─ Canberra
   │     │  │  │  ├─ Currie
   │     │  │  │  ├─ Darwin
   │     │  │  │  ├─ Eucla
   │     │  │  │  ├─ Hobart
   │     │  │  │  ├─ LHI
   │     │  │  │  ├─ Lindeman
   │     │  │  │  ├─ Lord_Howe
   │     │  │  │  ├─ Melbourne
   │     │  │  │  ├─ North
   │     │  │  │  ├─ NSW
   │     │  │  │  ├─ Perth
   │     │  │  │  ├─ Queensland
   │     │  │  │  ├─ South
   │     │  │  │  ├─ Sydney
   │     │  │  │  ├─ Tasmania
   │     │  │  │  ├─ Victoria
   │     │  │  │  ├─ West
   │     │  │  │  └─ Yancowinna
   │     │  │  ├─ Brazil
   │     │  │  │  ├─ Acre
   │     │  │  │  ├─ DeNoronha
   │     │  │  │  ├─ East
   │     │  │  │  └─ West
   │     │  │  ├─ Canada
   │     │  │  │  ├─ Atlantic
   │     │  │  │  ├─ Central
   │     │  │  │  ├─ Eastern
   │     │  │  │  ├─ Mountain
   │     │  │  │  ├─ Newfoundland
   │     │  │  │  ├─ Pacific
   │     │  │  │  ├─ Saskatchewan
   │     │  │  │  └─ Yukon
   │     │  │  ├─ CET
   │     │  │  ├─ Chile
   │     │  │  │  ├─ Continental
   │     │  │  │  └─ EasterIsland
   │     │  │  ├─ CST6CDT
   │     │  │  ├─ Cuba
   │     │  │  ├─ EET
   │     │  │  ├─ Egypt
   │     │  │  ├─ Eire
   │     │  │  ├─ EST
   │     │  │  ├─ EST5EDT
   │     │  │  ├─ Etc
   │     │  │  │  ├─ GMT
   │     │  │  │  ├─ GMT+0
   │     │  │  │  ├─ GMT+1
   │     │  │  │  ├─ GMT+10
   │     │  │  │  ├─ GMT+11
   │     │  │  │  ├─ GMT+12
   │     │  │  │  ├─ GMT+2
   │     │  │  │  ├─ GMT+3
   │     │  │  │  ├─ GMT+4
   │     │  │  │  ├─ GMT+5
   │     │  │  │  ├─ GMT+6
   │     │  │  │  ├─ GMT+7
   │     │  │  │  ├─ GMT+8
   │     │  │  │  ├─ GMT+9
   │     │  │  │  ├─ GMT-0
   │     │  │  │  ├─ GMT-1
   │     │  │  │  ├─ GMT-10
   │     │  │  │  ├─ GMT-11
   │     │  │  │  ├─ GMT-12
   │     │  │  │  ├─ GMT-13
   │     │  │  │  ├─ GMT-14
   │     │  │  │  ├─ GMT-2
   │     │  │  │  ├─ GMT-3
   │     │  │  │  ├─ GMT-4
   │     │  │  │  ├─ GMT-5
   │     │  │  │  ├─ GMT-6
   │     │  │  │  ├─ GMT-7
   │     │  │  │  ├─ GMT-8
   │     │  │  │  ├─ GMT-9
   │     │  │  │  ├─ GMT0
   │     │  │  │  ├─ Greenwich
   │     │  │  │  ├─ UCT
   │     │  │  │  ├─ Universal
   │     │  │  │  ├─ UTC
   │     │  │  │  └─ Zulu
   │     │  │  ├─ Europe
   │     │  │  │  ├─ Amsterdam
   │     │  │  │  ├─ Andorra
   │     │  │  │  ├─ Astrakhan
   │     │  │  │  ├─ Athens
   │     │  │  │  ├─ Belfast
   │     │  │  │  ├─ Belgrade
   │     │  │  │  ├─ Berlin
   │     │  │  │  ├─ Bratislava
   │     │  │  │  ├─ Brussels
   │     │  │  │  ├─ Bucharest
   │     │  │  │  ├─ Budapest
   │     │  │  │  ├─ Busingen
   │     │  │  │  ├─ Chisinau
   │     │  │  │  ├─ Copenhagen
   │     │  │  │  ├─ Dublin
   │     │  │  │  ├─ Gibraltar
   │     │  │  │  ├─ Guernsey
   │     │  │  │  ├─ Helsinki
   │     │  │  │  ├─ Isle_of_Man
   │     │  │  │  ├─ Istanbul
   │     │  │  │  ├─ Jersey
   │     │  │  │  ├─ Kaliningrad
   │     │  │  │  ├─ Kiev
   │     │  │  │  ├─ Kirov
   │     │  │  │  ├─ Kyiv
   │     │  │  │  ├─ Lisbon
   │     │  │  │  ├─ Ljubljana
   │     │  │  │  ├─ London
   │     │  │  │  ├─ Luxembourg
   │     │  │  │  ├─ Madrid
   │     │  │  │  ├─ Malta
   │     │  │  │  ├─ Mariehamn
   │     │  │  │  ├─ Minsk
   │     │  │  │  ├─ Monaco
   │     │  │  │  ├─ Moscow
   │     │  │  │  ├─ Nicosia
   │     │  │  │  ├─ Oslo
   │     │  │  │  ├─ Paris
   │     │  │  │  ├─ Podgorica
   │     │  │  │  ├─ Prague
   │     │  │  │  ├─ Riga
   │     │  │  │  ├─ Rome
   │     │  │  │  ├─ Samara
   │     │  │  │  ├─ San_Marino
   │     │  │  │  ├─ Sarajevo
   │     │  │  │  ├─ Saratov
   │     │  │  │  ├─ Simferopol
   │     │  │  │  ├─ Skopje
   │     │  │  │  ├─ Sofia
   │     │  │  │  ├─ Stockholm
   │     │  │  │  ├─ Tallinn
   │     │  │  │  ├─ Tirane
   │     │  │  │  ├─ Tiraspol
   │     │  │  │  ├─ Ulyanovsk
   │     │  │  │  ├─ Uzhgorod
   │     │  │  │  ├─ Vaduz
   │     │  │  │  ├─ Vatican
   │     │  │  │  ├─ Vienna
   │     │  │  │  ├─ Vilnius
   │     │  │  │  ├─ Volgograd
   │     │  │  │  ├─ Warsaw
   │     │  │  │  ├─ Zagreb
   │     │  │  │  ├─ Zaporozhye
   │     │  │  │  └─ Zurich
   │     │  │  ├─ Factory
   │     │  │  ├─ GB
   │     │  │  ├─ GB-Eire
   │     │  │  ├─ GMT
   │     │  │  ├─ GMT+0
   │     │  │  ├─ GMT-0
   │     │  │  ├─ GMT0
   │     │  │  ├─ Greenwich
   │     │  │  ├─ Hongkong
   │     │  │  ├─ HST
   │     │  │  ├─ Iceland
   │     │  │  ├─ Indian
   │     │  │  │  ├─ Antananarivo
   │     │  │  │  ├─ Chagos
   │     │  │  │  ├─ Christmas
   │     │  │  │  ├─ Cocos
   │     │  │  │  ├─ Comoro
   │     │  │  │  ├─ Kerguelen
   │     │  │  │  ├─ Mahe
   │     │  │  │  ├─ Maldives
   │     │  │  │  ├─ Mauritius
   │     │  │  │  ├─ Mayotte
   │     │  │  │  └─ Reunion
   │     │  │  ├─ Iran
   │     │  │  ├─ iso3166.tab
   │     │  │  ├─ Israel
   │     │  │  ├─ Jamaica
   │     │  │  ├─ Japan
   │     │  │  ├─ Kwajalein
   │     │  │  ├─ leapseconds
   │     │  │  ├─ Libya
   │     │  │  ├─ MET
   │     │  │  ├─ Mexico
   │     │  │  │  ├─ BajaNorte
   │     │  │  │  ├─ BajaSur
   │     │  │  │  └─ General
   │     │  │  ├─ MST
   │     │  │  ├─ MST7MDT
   │     │  │  ├─ Navajo
   │     │  │  ├─ NZ
   │     │  │  ├─ NZ-CHAT
   │     │  │  ├─ Pacific
   │     │  │  │  ├─ Apia
   │     │  │  │  ├─ Auckland
   │     │  │  │  ├─ Bougainville
   │     │  │  │  ├─ Chatham
   │     │  │  │  ├─ Chuuk
   │     │  │  │  ├─ Easter
   │     │  │  │  ├─ Efate
   │     │  │  │  ├─ Enderbury
   │     │  │  │  ├─ Fakaofo
   │     │  │  │  ├─ Fiji
   │     │  │  │  ├─ Funafuti
   │     │  │  │  ├─ Galapagos
   │     │  │  │  ├─ Gambier
   │     │  │  │  ├─ Guadalcanal
   │     │  │  │  ├─ Guam
   │     │  │  │  ├─ Honolulu
   │     │  │  │  ├─ Johnston
   │     │  │  │  ├─ Kanton
   │     │  │  │  ├─ Kiritimati
   │     │  │  │  ├─ Kosrae
   │     │  │  │  ├─ Kwajalein
   │     │  │  │  ├─ Majuro
   │     │  │  │  ├─ Marquesas
   │     │  │  │  ├─ Midway
   │     │  │  │  ├─ Nauru
   │     │  │  │  ├─ Niue
   │     │  │  │  ├─ Norfolk
   │     │  │  │  ├─ Noumea
   │     │  │  │  ├─ Pago_Pago
   │     │  │  │  ├─ Palau
   │     │  │  │  ├─ Pitcairn
   │     │  │  │  ├─ Pohnpei
   │     │  │  │  ├─ Ponape
   │     │  │  │  ├─ Port_Moresby
   │     │  │  │  ├─ Rarotonga
   │     │  │  │  ├─ Saipan
   │     │  │  │  ├─ Samoa
   │     │  │  │  ├─ Tahiti
   │     │  │  │  ├─ Tarawa
   │     │  │  │  ├─ Tongatapu
   │     │  │  │  ├─ Truk
   │     │  │  │  ├─ Wake
   │     │  │  │  ├─ Wallis
   │     │  │  │  └─ Yap
   │     │  │  ├─ Poland
   │     │  │  ├─ Portugal
   │     │  │  ├─ PRC
   │     │  │  ├─ PST8PDT
   │     │  │  ├─ ROC
   │     │  │  ├─ ROK
   │     │  │  ├─ Singapore
   │     │  │  ├─ Turkey
   │     │  │  ├─ tzdata.zi
   │     │  │  ├─ UCT
   │     │  │  ├─ Universal
   │     │  │  ├─ US
   │     │  │  │  ├─ Alaska
   │     │  │  │  ├─ Aleutian
   │     │  │  │  ├─ Arizona
   │     │  │  │  ├─ Central
   │     │  │  │  ├─ East-Indiana
   │     │  │  │  ├─ Eastern
   │     │  │  │  ├─ Hawaii
   │     │  │  │  ├─ Indiana-Starke
   │     │  │  │  ├─ Michigan
   │     │  │  │  ├─ Mountain
   │     │  │  │  ├─ Pacific
   │     │  │  │  └─ Samoa
   │     │  │  ├─ UTC
   │     │  │  ├─ W-SU
   │     │  │  ├─ WET
   │     │  │  ├─ zone.tab
   │     │  │  ├─ zone1970.tab
   │     │  │  ├─ zonenow.tab
   │     │  │  └─ Zulu
   │     │  └─ __init__.py
   │     ├─ pytz-2026.3.post1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ qdldl-0.1.9.post1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ requests
   │     │  ├─ adapters.py
   │     │  ├─ api.py
   │     │  ├─ auth.py
   │     │  ├─ certs.py
   │     │  ├─ compat.py
   │     │  ├─ cookies.py
   │     │  ├─ exceptions.py
   │     │  ├─ help.py
   │     │  ├─ hooks.py
   │     │  ├─ models.py
   │     │  ├─ packages.py
   │     │  ├─ py.typed
   │     │  ├─ sessions.py
   │     │  ├─ status_codes.py
   │     │  ├─ structures.py
   │     │  ├─ utils.py
   │     │  ├─ _internal_utils.py
   │     │  ├─ _types.py
   │     │  ├─ __init__.py
   │     │  └─ __version__.py
   │     ├─ requests-2.34.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ LICENSE
   │     │  │  └─ NOTICE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ rich
   │     │  ├─ abc.py
   │     │  ├─ align.py
   │     │  ├─ ansi.py
   │     │  ├─ bar.py
   │     │  ├─ box.py
   │     │  ├─ cells.py
   │     │  ├─ color.py
   │     │  ├─ color_triplet.py
   │     │  ├─ columns.py
   │     │  ├─ console.py
   │     │  ├─ constrain.py
   │     │  ├─ containers.py
   │     │  ├─ control.py
   │     │  ├─ default_styles.py
   │     │  ├─ diagnose.py
   │     │  ├─ emoji.py
   │     │  ├─ errors.py
   │     │  ├─ filesize.py
   │     │  ├─ file_proxy.py
   │     │  ├─ highlighter.py
   │     │  ├─ json.py
   │     │  ├─ jupyter.py
   │     │  ├─ layout.py
   │     │  ├─ live.py
   │     │  ├─ live_render.py
   │     │  ├─ logging.py
   │     │  ├─ markdown.py
   │     │  ├─ markup.py
   │     │  ├─ measure.py
   │     │  ├─ padding.py
   │     │  ├─ pager.py
   │     │  ├─ palette.py
   │     │  ├─ panel.py
   │     │  ├─ pretty.py
   │     │  ├─ progress.py
   │     │  ├─ progress_bar.py
   │     │  ├─ prompt.py
   │     │  ├─ protocol.py
   │     │  ├─ py.typed
   │     │  ├─ region.py
   │     │  ├─ repr.py
   │     │  ├─ rule.py
   │     │  ├─ scope.py
   │     │  ├─ screen.py
   │     │  ├─ segment.py
   │     │  ├─ spinner.py
   │     │  ├─ status.py
   │     │  ├─ style.py
   │     │  ├─ styled.py
   │     │  ├─ syntax.py
   │     │  ├─ table.py
   │     │  ├─ terminal_theme.py
   │     │  ├─ text.py
   │     │  ├─ theme.py
   │     │  ├─ themes.py
   │     │  ├─ traceback.py
   │     │  ├─ tree.py
   │     │  ├─ _emoji_codes.py
   │     │  ├─ _emoji_replace.py
   │     │  ├─ _export_format.py
   │     │  ├─ _extension.py
   │     │  ├─ _fileno.py
   │     │  ├─ _inspect.py
   │     │  ├─ _log_render.py
   │     │  ├─ _loop.py
   │     │  ├─ _null_file.py
   │     │  ├─ _palettes.py
   │     │  ├─ _pick.py
   │     │  ├─ _ratio.py
   │     │  ├─ _spinners.py
   │     │  ├─ _stack.py
   │     │  ├─ _timer.py
   │     │  ├─ _unicode_data
   │     │  │  ├─ unicode10-0-0.py
   │     │  │  ├─ unicode11-0-0.py
   │     │  │  ├─ unicode12-0-0.py
   │     │  │  ├─ unicode12-1-0.py
   │     │  │  ├─ unicode13-0-0.py
   │     │  │  ├─ unicode14-0-0.py
   │     │  │  ├─ unicode15-0-0.py
   │     │  │  ├─ unicode15-1-0.py
   │     │  │  ├─ unicode16-0-0.py
   │     │  │  ├─ unicode17-0-0.py
   │     │  │  ├─ unicode4-1-0.py
   │     │  │  ├─ unicode5-0-0.py
   │     │  │  ├─ unicode5-1-0.py
   │     │  │  ├─ unicode5-2-0.py
   │     │  │  ├─ unicode6-0-0.py
   │     │  │  ├─ unicode6-1-0.py
   │     │  │  ├─ unicode6-2-0.py
   │     │  │  ├─ unicode6-3-0.py
   │     │  │  ├─ unicode7-0-0.py
   │     │  │  ├─ unicode8-0-0.py
   │     │  │  ├─ unicode9-0-0.py
   │     │  │  ├─ _versions.py
   │     │  │  └─ __init__.py
   │     │  ├─ _win32_console.py
   │     │  ├─ _windows.py
   │     │  ├─ _windows_renderer.py
   │     │  ├─ _wrap.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ rich-15.0.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ ropwr
   │     │  ├─ base.py
   │     │  ├─ cvx.py
   │     │  ├─ cvx_qp.py
   │     │  ├─ cvx_socp.py
   │     │  ├─ direct.py
   │     │  ├─ matrices.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ ropwr-1.2.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ scikit_learn-1.7.2.dist-info
   │     │  ├─ licenses
   │     │  │  └─ COPYING
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ scipy
   │     │  ├─ cluster
   │     │  │  ├─ hierarchy.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ hierarchy_test_data.py
   │     │  │  │  ├─ test_disjoint_set.py
   │     │  │  │  ├─ test_hierarchy.py
   │     │  │  │  ├─ test_vq.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vq.py
   │     │  │  ├─ _hierarchy.cp310-win_amd64.dll.a
   │     │  │  ├─ _optimal_leaf_ordering.cp310-win_amd64.dll.a
   │     │  │  ├─ _vq.cp310-win_amd64.dll.a
   │     │  │  └─ __init__.py
   │     │  ├─ conftest.py
   │     │  ├─ constants
   │     │  │  ├─ codata.py
   │     │  │  ├─ constants.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_codata.py
   │     │  │  │  ├─ test_constants.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _codata.py
   │     │  │  ├─ _constants.py
   │     │  │  └─ __init__.py
   │     │  ├─ datasets
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _download_all.py
   │     │  │  ├─ _fetchers.py
   │     │  │  ├─ _registry.py
   │     │  │  ├─ _utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ differentiate
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_differentiate.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _differentiate.py
   │     │  │  └─ __init__.py
   │     │  ├─ fft
   │     │  │  ├─ tests
   │     │  │  │  ├─ mock_backend.py
   │     │  │  │  ├─ test_backend.py
   │     │  │  │  ├─ test_basic.py
   │     │  │  │  ├─ test_fftlog.py
   │     │  │  │  ├─ test_helper.py
   │     │  │  │  ├─ test_multithreading.py
   │     │  │  │  ├─ test_real_transforms.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _backend.py
   │     │  │  ├─ _basic.py
   │     │  │  ├─ _basic_backend.py
   │     │  │  ├─ _debug_backends.py
   │     │  │  ├─ _fftlog.py
   │     │  │  ├─ _fftlog_backend.py
   │     │  │  ├─ _helper.py
   │     │  │  ├─ _pocketfft
   │     │  │  │  ├─ basic.py
   │     │  │  │  ├─ helper.py
   │     │  │  │  ├─ LICENSE.md
   │     │  │  │  ├─ pypocketfft.cp310-win_amd64.dll.a
   │     │  │  │  ├─ realtransforms.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_basic.py
   │     │  │  │  │  ├─ test_real_transforms.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _realtransforms.py
   │     │  │  ├─ _realtransforms_backend.py
   │     │  │  └─ __init__.py
   │     │  ├─ fftpack
   │     │  │  ├─ basic.py
   │     │  │  ├─ convolve.cp310-win_amd64.dll.a
   │     │  │  ├─ helper.py
   │     │  │  ├─ pseudo_diffs.py
   │     │  │  ├─ realtransforms.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ fftw_double_ref.npz
   │     │  │  │  ├─ fftw_longdouble_ref.npz
   │     │  │  │  ├─ fftw_single_ref.npz
   │     │  │  │  ├─ test.npz
   │     │  │  │  ├─ test_basic.py
   │     │  │  │  ├─ test_helper.py
   │     │  │  │  ├─ test_import.py
   │     │  │  │  ├─ test_pseudo_diffs.py
   │     │  │  │  ├─ test_real_transforms.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _basic.py
   │     │  │  ├─ _helper.py
   │     │  │  ├─ _pseudo_diffs.py
   │     │  │  ├─ _realtransforms.py
   │     │  │  └─ __init__.py
   │     │  ├─ integrate
   │     │  │  ├─ dop.py
   │     │  │  ├─ lsoda.py
   │     │  │  ├─ odepack.py
   │     │  │  ├─ quadpack.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_banded_ode_solvers.py
   │     │  │  │  ├─ test_bvp.py
   │     │  │  │  ├─ test_cubature.py
   │     │  │  │  ├─ test_integrate.py
   │     │  │  │  ├─ test_odeint_jac.py
   │     │  │  │  ├─ test_quadpack.py
   │     │  │  │  ├─ test_quadrature.py
   │     │  │  │  ├─ test_tanhsinh.py
   │     │  │  │  ├─ test__quad_vec.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vode.py
   │     │  │  ├─ _bvp.py
   │     │  │  ├─ _cubature.py
   │     │  │  ├─ _dop.cp310-win_amd64.dll.a
   │     │  │  ├─ _ivp
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ bdf.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ dop853_coefficients.py
   │     │  │  │  ├─ ivp.py
   │     │  │  │  ├─ lsoda.py
   │     │  │  │  ├─ radau.py
   │     │  │  │  ├─ rk.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_ivp.py
   │     │  │  │  │  ├─ test_rk.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _lebedev.py
   │     │  │  ├─ _lsoda.cp310-win_amd64.dll.a
   │     │  │  ├─ _ode.py
   │     │  │  ├─ _odepack.cp310-win_amd64.dll.a
   │     │  │  ├─ _odepack_py.py
   │     │  │  ├─ _quadpack.cp310-win_amd64.dll.a
   │     │  │  ├─ _quadpack_py.py
   │     │  │  ├─ _quadrature.py
   │     │  │  ├─ _quad_vec.py
   │     │  │  ├─ _rules
   │     │  │  │  ├─ _base.py
   │     │  │  │  ├─ _gauss_kronrod.py
   │     │  │  │  ├─ _gauss_legendre.py
   │     │  │  │  ├─ _genz_malik.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _tanhsinh.py
   │     │  │  ├─ _test_multivariate.cp310-win_amd64.dll.a
   │     │  │  ├─ _test_odeint_banded.cp310-win_amd64.dll.a
   │     │  │  ├─ _vode.cp310-win_amd64.dll.a
   │     │  │  └─ __init__.py
   │     │  ├─ interpolate
   │     │  │  ├─ dfitpack.py
   │     │  │  ├─ fitpack.py
   │     │  │  ├─ fitpack2.py
   │     │  │  ├─ interpnd.py
   │     │  │  ├─ interpolate.py
   │     │  │  ├─ ndgriddata.py
   │     │  │  ├─ polyint.py
   │     │  │  ├─ rbf.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ bug-1310.npz
   │     │  │  │  │  ├─ estimate_gradients_hang.npy
   │     │  │  │  │  └─ gcvspl.npz
   │     │  │  │  ├─ test_bary_rational.py
   │     │  │  │  ├─ test_bsplines.py
   │     │  │  │  ├─ test_fitpack.py
   │     │  │  │  ├─ test_fitpack2.py
   │     │  │  │  ├─ test_gil.py
   │     │  │  │  ├─ test_interpnd.py
   │     │  │  │  ├─ test_interpolate.py
   │     │  │  │  ├─ test_ndgriddata.py
   │     │  │  │  ├─ test_pade.py
   │     │  │  │  ├─ test_polyint.py
   │     │  │  │  ├─ test_rbf.py
   │     │  │  │  ├─ test_rbfinterp.py
   │     │  │  │  ├─ test_rgi.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _bary_rational.py
   │     │  │  ├─ _bspl.cp310-win_amd64.dll.a
   │     │  │  ├─ _bsplines.py
   │     │  │  ├─ _cubic.py
   │     │  │  ├─ _dfitpack.cp310-win_amd64.dll.a
   │     │  │  ├─ _dierckx.cp310-win_amd64.dll.a
   │     │  │  ├─ _fitpack.cp310-win_amd64.dll.a
   │     │  │  ├─ _fitpack2.py
   │     │  │  ├─ _fitpack_impl.py
   │     │  │  ├─ _fitpack_py.py
   │     │  │  ├─ _fitpack_repro.py
   │     │  │  ├─ _interpnd.cp310-win_amd64.dll.a
   │     │  │  ├─ _interpolate.py
   │     │  │  ├─ _ndbspline.py
   │     │  │  ├─ _ndgriddata.py
   │     │  │  ├─ _pade.py
   │     │  │  ├─ _polyint.py
   │     │  │  ├─ _ppoly.cp310-win_amd64.dll.a
   │     │  │  ├─ _rbf.py
   │     │  │  ├─ _rbfinterp.py
   │     │  │  ├─ _rbfinterp_pythran.cp310-win_amd64.dll.a
   │     │  │  ├─ _rgi.py
   │     │  │  ├─ _rgi_cython.cp310-win_amd64.dll.a
   │     │  │  └─ __init__.py
   │     │  ├─ io
   │     │  │  ├─ arff
   │     │  │  │  ├─ arffread.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ data
   │     │  │  │  │  │  ├─ iris.arff
   │     │  │  │  │  │  ├─ missing.arff
   │     │  │  │  │  │  ├─ nodata.arff
   │     │  │  │  │  │  ├─ quoted_nominal.arff
   │     │  │  │  │  │  ├─ quoted_nominal_spaces.arff
   │     │  │  │  │  │  ├─ test1.arff
   │     │  │  │  │  │  ├─ test10.arff
   │     │  │  │  │  │  ├─ test11.arff
   │     │  │  │  │  │  ├─ test2.arff
   │     │  │  │  │  │  ├─ test3.arff
   │     │  │  │  │  │  ├─ test4.arff
   │     │  │  │  │  │  ├─ test5.arff
   │     │  │  │  │  │  ├─ test6.arff
   │     │  │  │  │  │  ├─ test7.arff
   │     │  │  │  │  │  ├─ test8.arff
   │     │  │  │  │  │  └─ test9.arff
   │     │  │  │  │  ├─ test_arffread.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _arffread.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ harwell_boeing.py
   │     │  │  ├─ idl.py
   │     │  │  ├─ matlab
   │     │  │  │  ├─ byteordercodes.py
   │     │  │  │  ├─ mio.py
   │     │  │  │  ├─ mio4.py
   │     │  │  │  ├─ mio5.py
   │     │  │  │  ├─ mio5_params.py
   │     │  │  │  ├─ mio5_utils.py
   │     │  │  │  ├─ miobase.py
   │     │  │  │  ├─ mio_utils.py
   │     │  │  │  ├─ streams.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ data
   │     │  │  │  │  │  ├─ .tmpfyINr0
   │     │  │  │  │  │  ├─ bad_miuint32.mat
   │     │  │  │  │  │  ├─ bad_miutf8_array_name.mat
   │     │  │  │  │  │  ├─ big_endian.mat
   │     │  │  │  │  │  ├─ broken_utf8.mat
   │     │  │  │  │  │  ├─ corrupted_zlib_checksum.mat
   │     │  │  │  │  │  ├─ corrupted_zlib_data.mat
   │     │  │  │  │  │  ├─ debigged_m4.mat
   │     │  │  │  │  │  ├─ japanese_utf8.txt
   │     │  │  │  │  │  ├─ little_endian.mat
   │     │  │  │  │  │  ├─ logical_sparse.mat
   │     │  │  │  │  │  ├─ malformed1.mat
   │     │  │  │  │  │  ├─ miuint32_for_miint32.mat
   │     │  │  │  │  │  ├─ miutf8_array_name.mat
   │     │  │  │  │  │  ├─ nasty_duplicate_fieldnames.mat
   │     │  │  │  │  │  ├─ one_by_zero_char.mat
   │     │  │  │  │  │  ├─ parabola.mat
   │     │  │  │  │  │  ├─ single_empty_string.mat
   │     │  │  │  │  │  ├─ some_functions.mat
   │     │  │  │  │  │  ├─ sqr.mat
   │     │  │  │  │  │  ├─ test3dmatrix_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ test3dmatrix_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ test3dmatrix_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ test3dmatrix_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testbool_8_WIN64.mat
   │     │  │  │  │  │  ├─ testcellnest_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testcellnest_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcellnest_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcellnest_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testcell_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testcell_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcell_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcell_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testcomplex_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testcomplex_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testcomplex_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcomplex_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcomplex_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testdouble_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testdouble_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testdouble_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testdouble_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testdouble_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testemptycell_5.3_SOL2.mat
   │     │  │  │  │  │  ├─ testemptycell_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testemptycell_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testemptycell_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testfunc_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testhdf5_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testmatrix_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testmatrix_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testmatrix_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testmatrix_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testmatrix_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testminus_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testminus_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testminus_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testminus_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testminus_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testmulti_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testmulti_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testmulti_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testobject_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testobject_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testobject_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testobject_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testonechar_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testonechar_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testonechar_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testonechar_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testonechar_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testscalarcell_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testsimplecell.mat
   │     │  │  │  │  │  ├─ testsparsecomplex_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testsparsecomplex_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testsparsecomplex_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparsecomplex_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparsecomplex_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparsefloat_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparse_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testsparse_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testsparse_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparse_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparse_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ teststringarray_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ teststringarray_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ teststringarray_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststringarray_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststringarray_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ teststring_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ teststring_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ teststring_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststring_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststring_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructarr_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ teststructarr_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructarr_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructarr_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructnest_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ teststructnest_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructnest_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructnest_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ teststruct_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ teststruct_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststruct_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststruct_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testunicode_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testunicode_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testvec_4_GLNX86.mat
   │     │  │  │  │  │  ├─ test_empty_struct.mat
   │     │  │  │  │  │  ├─ test_mat4_le_floats.mat
   │     │  │  │  │  │  └─ test_skip_variable.mat
   │     │  │  │  │  ├─ test_byteordercodes.py
   │     │  │  │  │  ├─ test_mio.py
   │     │  │  │  │  ├─ test_mio5_utils.py
   │     │  │  │  │  ├─ test_miobase.py
   │     │  │  │  │  ├─ test_mio_funcs.py
   │     │  │  │  │  ├─ test_mio_utils.py
   │     │  │  │  │  ├─ test_pathological.py
   │     │  │  │  │  ├─ test_streams.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _byteordercodes.py
   │     │  │  │  ├─ _mio.py
   │     │  │  │  ├─ _mio4.py
   │     │  │  │  ├─ _mio5.py
   │     │  │  │  ├─ _mio5_params.py
   │     │  │  │  ├─ _mio5_utils.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _miobase.py
   │     │  │  │  ├─ _mio_utils.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _streams.cp310-win_amd64.dll.a
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mmio.py
   │     │  │  ├─ netcdf.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ array_float32_1d.sav
   │     │  │  │  │  ├─ array_float32_2d.sav
   │     │  │  │  │  ├─ array_float32_3d.sav
   │     │  │  │  │  ├─ array_float32_4d.sav
   │     │  │  │  │  ├─ array_float32_5d.sav
   │     │  │  │  │  ├─ array_float32_6d.sav
   │     │  │  │  │  ├─ array_float32_7d.sav
   │     │  │  │  │  ├─ array_float32_8d.sav
   │     │  │  │  │  ├─ array_float32_pointer_1d.sav
   │     │  │  │  │  ├─ array_float32_pointer_2d.sav
   │     │  │  │  │  ├─ array_float32_pointer_3d.sav
   │     │  │  │  │  ├─ array_float32_pointer_4d.sav
   │     │  │  │  │  ├─ array_float32_pointer_5d.sav
   │     │  │  │  │  ├─ array_float32_pointer_6d.sav
   │     │  │  │  │  ├─ array_float32_pointer_7d.sav
   │     │  │  │  │  ├─ array_float32_pointer_8d.sav
   │     │  │  │  │  ├─ example_1.nc
   │     │  │  │  │  ├─ example_2.nc
   │     │  │  │  │  ├─ example_3_maskedvals.nc
   │     │  │  │  │  ├─ fortran-3x3d-2i.dat
   │     │  │  │  │  ├─ fortran-mixed.dat
   │     │  │  │  │  ├─ fortran-sf8-11x1x10.dat
   │     │  │  │  │  ├─ fortran-sf8-15x10x22.dat
   │     │  │  │  │  ├─ fortran-sf8-1x1x1.dat
   │     │  │  │  │  ├─ fortran-sf8-1x1x5.dat
   │     │  │  │  │  ├─ fortran-sf8-1x1x7.dat
   │     │  │  │  │  ├─ fortran-sf8-1x3x5.dat
   │     │  │  │  │  ├─ fortran-si4-11x1x10.dat
   │     │  │  │  │  ├─ fortran-si4-15x10x22.dat
   │     │  │  │  │  ├─ fortran-si4-1x1x1.dat
   │     │  │  │  │  ├─ fortran-si4-1x1x5.dat
   │     │  │  │  │  ├─ fortran-si4-1x1x7.dat
   │     │  │  │  │  ├─ fortran-si4-1x3x5.dat
   │     │  │  │  │  ├─ invalid_pointer.sav
   │     │  │  │  │  ├─ null_pointer.sav
   │     │  │  │  │  ├─ scalar_byte.sav
   │     │  │  │  │  ├─ scalar_byte_descr.sav
   │     │  │  │  │  ├─ scalar_complex32.sav
   │     │  │  │  │  ├─ scalar_complex64.sav
   │     │  │  │  │  ├─ scalar_float32.sav
   │     │  │  │  │  ├─ scalar_float64.sav
   │     │  │  │  │  ├─ scalar_heap_pointer.sav
   │     │  │  │  │  ├─ scalar_int16.sav
   │     │  │  │  │  ├─ scalar_int32.sav
   │     │  │  │  │  ├─ scalar_int64.sav
   │     │  │  │  │  ├─ scalar_string.sav
   │     │  │  │  │  ├─ scalar_uint16.sav
   │     │  │  │  │  ├─ scalar_uint32.sav
   │     │  │  │  │  ├─ scalar_uint64.sav
   │     │  │  │  │  ├─ struct_arrays.sav
   │     │  │  │  │  ├─ struct_arrays_byte_idl80.sav
   │     │  │  │  │  ├─ struct_arrays_replicated.sav
   │     │  │  │  │  ├─ struct_arrays_replicated_3d.sav
   │     │  │  │  │  ├─ struct_inherit.sav
   │     │  │  │  │  ├─ struct_pointers.sav
   │     │  │  │  │  ├─ struct_pointers_replicated.sav
   │     │  │  │  │  ├─ struct_pointers_replicated_3d.sav
   │     │  │  │  │  ├─ struct_pointer_arrays.sav
   │     │  │  │  │  ├─ struct_pointer_arrays_replicated.sav
   │     │  │  │  │  ├─ struct_pointer_arrays_replicated_3d.sav
   │     │  │  │  │  ├─ struct_scalars.sav
   │     │  │  │  │  ├─ struct_scalars_replicated.sav
   │     │  │  │  │  ├─ struct_scalars_replicated_3d.sav
   │     │  │  │  │  ├─ test-1234Hz-le-1ch-10S-20bit-extra.wav
   │     │  │  │  │  ├─ test-44100Hz-2ch-32bit-float-be.wav
   │     │  │  │  │  ├─ test-44100Hz-2ch-32bit-float-le.wav
   │     │  │  │  │  ├─ test-44100Hz-be-1ch-4bytes.wav
   │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-early-eof-no-data.wav
   │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-early-eof.wav
   │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-incomplete-chunk.wav
   │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-rf64.wav
   │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes.wav
   │     │  │  │  │  ├─ test-48000Hz-2ch-64bit-float-le-wavex.wav
   │     │  │  │  │  ├─ test-8000Hz-be-3ch-5S-24bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-1ch-1byte-ulaw.wav
   │     │  │  │  │  ├─ test-8000Hz-le-2ch-1byteu.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-24bit-inconsistent.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-24bit-rf64.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-24bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-36bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-45bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-53bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-64bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-4ch-9S-12bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-5ch-9S-5bit.wav
   │     │  │  │  │  ├─ Transparent Busy.ani
   │     │  │  │  │  └─ various_compressed.sav
   │     │  │  │  ├─ test_fortran.py
   │     │  │  │  ├─ test_idl.py
   │     │  │  │  ├─ test_mmio.py
   │     │  │  │  ├─ test_netcdf.py
   │     │  │  │  ├─ test_paths.py
   │     │  │  │  ├─ test_wavfile.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ wavfile.py
   │     │  │  ├─ _fast_matrix_market
   │     │  │  │  ├─ _fmm_core.cp310-win_amd64.dll.a
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _fortran.py
   │     │  │  ├─ _harwell_boeing
   │     │  │  │  ├─ hb.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_fortran_format.py
   │     │  │  │  │  ├─ test_hb.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _fortran_format_parser.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _idl.py
   │     │  │  ├─ _mmio.py
   │     │  │  ├─ _netcdf.py
   │     │  │  ├─ _test_fortran.cp310-win_amd64.dll.a
   │     │  │  └─ __init__.py
   │     │  ├─ linalg
   │     │  │  ├─ basic.py
   │     │  │  ├─ blas.py
   │     │  │  ├─ cython_blas.cp310-win_amd64.dll.a
   │     │  │  ├─ cython_blas.pxd
   │     │  │  ├─ cython_blas.pyx
   │     │  │  ├─ cython_lapack.cp310-win_amd64.dll.a
   │     │  │  ├─ cython_lapack.pxd
   │     │  │  ├─ cython_lapack.pyx
   │     │  │  ├─ decomp.py
   │     │  │  ├─ decomp_cholesky.py
   │     │  │  ├─ decomp_lu.py
   │     │  │  ├─ decomp_qr.py
   │     │  │  ├─ decomp_schur.py
   │     │  │  ├─ decomp_svd.py
   │     │  │  ├─ interpolative.py
   │     │  │  ├─ lapack.py
   │     │  │  ├─ matfuncs.py
   │     │  │  ├─ misc.py
   │     │  │  ├─ special_matrices.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ carex_15_data.npz
   │     │  │  │  │  ├─ carex_18_data.npz
   │     │  │  │  │  ├─ carex_19_data.npz
   │     │  │  │  │  ├─ carex_20_data.npz
   │     │  │  │  │  ├─ carex_6_data.npz
   │     │  │  │  │  └─ gendare_20170120_data.npz
   │     │  │  │  ├─ test_basic.py
   │     │  │  │  ├─ test_blas.py
   │     │  │  │  ├─ test_cythonized_array_utils.py
   │     │  │  │  ├─ test_cython_blas.py
   │     │  │  │  ├─ test_cython_lapack.py
   │     │  │  │  ├─ test_decomp.py
   │     │  │  │  ├─ test_decomp_cholesky.py
   │     │  │  │  ├─ test_decomp_cossin.py
   │     │  │  │  ├─ test_decomp_ldl.py
   │     │  │  │  ├─ test_decomp_lu.py
   │     │  │  │  ├─ test_decomp_polar.py
   │     │  │  │  ├─ test_decomp_update.py
   │     │  │  │  ├─ test_extending.py
   │     │  │  │  ├─ test_fblas.py
   │     │  │  │  ├─ test_interpolative.py
   │     │  │  │  ├─ test_lapack.py
   │     │  │  │  ├─ test_matfuncs.py
   │     │  │  │  ├─ test_matmul_toeplitz.py
   │     │  │  │  ├─ test_procrustes.py
   │     │  │  │  ├─ test_sketches.py
   │     │  │  │  ├─ test_solvers.py
   │     │  │  │  ├─ test_solve_toeplitz.py
   │     │  │  │  ├─ test_special_matrices.py
   │     │  │  │  ├─ _cython_examples
   │     │  │  │  │  └─ extending.pyx
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _basic.py
   │     │  │  ├─ _blas_subroutines.h
   │     │  │  ├─ _cythonized_array_utils.cp310-win_amd64.dll.a
   │     │  │  ├─ _cythonized_array_utils.pxd
   │     │  │  ├─ _cythonized_array_utils.pyi
   │     │  │  ├─ _decomp.py
   │     │  │  ├─ _decomp_cholesky.py
   │     │  │  ├─ _decomp_cossin.py
   │     │  │  ├─ _decomp_interpolative.cp310-win_amd64.dll.a
   │     │  │  ├─ _decomp_ldl.py
   │     │  │  ├─ _decomp_lu.py
   │     │  │  ├─ _decomp_lu_cython.cp310-win_amd64.dll.a
   │     │  │  ├─ _decomp_lu_cython.pyi
   │     │  │  ├─ _decomp_polar.py
   │     │  │  ├─ _decomp_qr.py
   │     │  │  ├─ _decomp_qz.py
   │     │  │  ├─ _decomp_schur.py
   │     │  │  ├─ _decomp_svd.py
   │     │  │  ├─ _decomp_update.cp310-win_amd64.dll.a
   │     │  │  ├─ _expm_frechet.py
   │     │  │  ├─ _fblas.cp310-win_amd64.dll.a
   │     │  │  ├─ _flapack.cp310-win_amd64.dll.a
   │     │  │  ├─ _lapack_subroutines.h
   │     │  │  ├─ _linalg_pythran.cp310-win_amd64.dll.a
   │     │  │  ├─ _matfuncs.py
   │     │  │  ├─ _matfuncs_expm.cp310-win_amd64.dll.a
   │     │  │  ├─ _matfuncs_expm.pyi
   │     │  │  ├─ _matfuncs_inv_ssq.py
   │     │  │  ├─ _matfuncs_sqrtm.py
   │     │  │  ├─ _matfuncs_sqrtm_triu.cp310-win_amd64.dll.a
   │     │  │  ├─ _misc.py
   │     │  │  ├─ _procrustes.py
   │     │  │  ├─ _sketches.py
   │     │  │  ├─ _solvers.py
   │     │  │  ├─ _solve_toeplitz.cp310-win_amd64.dll.a
   │     │  │  ├─ _special_matrices.py
   │     │  │  ├─ _testutils.py
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ misc
   │     │  │  ├─ common.py
   │     │  │  ├─ doccer.py
   │     │  │  └─ __init__.py
   │     │  ├─ ndimage
   │     │  │  ├─ filters.py
   │     │  │  ├─ fourier.py
   │     │  │  ├─ interpolation.py
   │     │  │  ├─ measurements.py
   │     │  │  ├─ morphology.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ label_inputs.txt
   │     │  │  │  │  ├─ label_results.txt
   │     │  │  │  │  └─ label_strels.txt
   │     │  │  │  ├─ dots.png
   │     │  │  │  ├─ test_c_api.py
   │     │  │  │  ├─ test_datatypes.py
   │     │  │  │  ├─ test_filters.py
   │     │  │  │  ├─ test_fourier.py
   │     │  │  │  ├─ test_interpolation.py
   │     │  │  │  ├─ test_measurements.py
   │     │  │  │  ├─ test_morphology.py
   │     │  │  │  ├─ test_ni_support.py
   │     │  │  │  ├─ test_splines.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _ctest.cp310-win_amd64.dll.a
   │     │  │  ├─ _cytest.cp310-win_amd64.dll.a
   │     │  │  ├─ _delegators.py
   │     │  │  ├─ _filters.py
   │     │  │  ├─ _fourier.py
   │     │  │  ├─ _interpolation.py
   │     │  │  ├─ _measurements.py
   │     │  │  ├─ _morphology.py
   │     │  │  ├─ _ndimage_api.py
   │     │  │  ├─ _nd_image.cp310-win_amd64.dll.a
   │     │  │  ├─ _ni_docstrings.py
   │     │  │  ├─ _ni_label.cp310-win_amd64.dll.a
   │     │  │  ├─ _ni_support.py
   │     │  │  ├─ _rank_filter_1d.cp310-win_amd64.dll.a
   │     │  │  ├─ _support_alternative_backends.py
   │     │  │  └─ __init__.py
   │     │  ├─ odr
   │     │  │  ├─ models.py
   │     │  │  ├─ odrpack.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_odr.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _add_newdocs.py
   │     │  │  ├─ _models.py
   │     │  │  ├─ _odrpack.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __odrpack.cp310-win_amd64.dll.a
   │     │  ├─ optimize
   │     │  │  ├─ cobyla.py
   │     │  │  ├─ cython_optimize
   │     │  │  │  ├─ c_zeros.pxd
   │     │  │  │  ├─ _zeros.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _zeros.pxd
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cython_optimize.pxd
   │     │  │  ├─ elementwise.py
   │     │  │  ├─ lbfgsb.py
   │     │  │  ├─ linesearch.py
   │     │  │  ├─ minpack.py
   │     │  │  ├─ minpack2.py
   │     │  │  ├─ moduleTNC.py
   │     │  │  ├─ nonlin.py
   │     │  │  ├─ optimize.py
   │     │  │  ├─ slsqp.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_bracket.py
   │     │  │  │  ├─ test_chandrupatla.py
   │     │  │  │  ├─ test_cobyla.py
   │     │  │  │  ├─ test_cobyqa.py
   │     │  │  │  ├─ test_constraints.py
   │     │  │  │  ├─ test_constraint_conversion.py
   │     │  │  │  ├─ test_cython_optimize.py
   │     │  │  │  ├─ test_differentiable_functions.py
   │     │  │  │  ├─ test_direct.py
   │     │  │  │  ├─ test_extending.py
   │     │  │  │  ├─ test_hessian_update_strategy.py
   │     │  │  │  ├─ test_isotonic_regression.py
   │     │  │  │  ├─ test_lbfgsb_hessinv.py
   │     │  │  │  ├─ test_lbfgsb_setulb.py
   │     │  │  │  ├─ test_least_squares.py
   │     │  │  │  ├─ test_linear_assignment.py
   │     │  │  │  ├─ test_linesearch.py
   │     │  │  │  ├─ test_linprog.py
   │     │  │  │  ├─ test_lsq_common.py
   │     │  │  │  ├─ test_lsq_linear.py
   │     │  │  │  ├─ test_milp.py
   │     │  │  │  ├─ test_minimize_constrained.py
   │     │  │  │  ├─ test_minpack.py
   │     │  │  │  ├─ test_nnls.py
   │     │  │  │  ├─ test_nonlin.py
   │     │  │  │  ├─ test_optimize.py
   │     │  │  │  ├─ test_quadratic_assignment.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_slsqp.py
   │     │  │  │  ├─ test_tnc.py
   │     │  │  │  ├─ test_trustregion.py
   │     │  │  │  ├─ test_trustregion_exact.py
   │     │  │  │  ├─ test_trustregion_krylov.py
   │     │  │  │  ├─ test_zeros.py
   │     │  │  │  ├─ test__basinhopping.py
   │     │  │  │  ├─ test__differential_evolution.py
   │     │  │  │  ├─ test__dual_annealing.py
   │     │  │  │  ├─ test__linprog_clean_inputs.py
   │     │  │  │  ├─ test__numdiff.py
   │     │  │  │  ├─ test__remove_redundancy.py
   │     │  │  │  ├─ test__root.py
   │     │  │  │  ├─ test__shgo.py
   │     │  │  │  ├─ test__spectral.py
   │     │  │  │  ├─ _cython_examples
   │     │  │  │  │  └─ extending.pyx
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tnc.py
   │     │  │  ├─ zeros.py
   │     │  │  ├─ _basinhopping.py
   │     │  │  ├─ _bglu_dense.cp310-win_amd64.dll.a
   │     │  │  ├─ _bracket.py
   │     │  │  ├─ _chandrupatla.py
   │     │  │  ├─ _cobyla.cp310-win_amd64.dll.a
   │     │  │  ├─ _cobyla_py.py
   │     │  │  ├─ _cobyqa_py.py
   │     │  │  ├─ _constraints.py
   │     │  │  ├─ _cython_nnls.cp310-win_amd64.dll.a
   │     │  │  ├─ _dcsrch.py
   │     │  │  ├─ _differentiable_functions.py
   │     │  │  ├─ _differentialevolution.py
   │     │  │  ├─ _direct.cp310-win_amd64.dll.a
   │     │  │  ├─ _direct_py.py
   │     │  │  ├─ _dual_annealing.py
   │     │  │  ├─ _elementwise.py
   │     │  │  ├─ _group_columns.cp310-win_amd64.dll.a
   │     │  │  ├─ _hessian_update_strategy.py
   │     │  │  ├─ _highspy
   │     │  │  │  ├─ _core.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _highs_options.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _highs_wrapper.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _isotonic.py
   │     │  │  ├─ _lbfgsb.cp310-win_amd64.dll.a
   │     │  │  ├─ _lbfgsb_py.py
   │     │  │  ├─ _linesearch.py
   │     │  │  ├─ _linprog.py
   │     │  │  ├─ _linprog_doc.py
   │     │  │  ├─ _linprog_highs.py
   │     │  │  ├─ _linprog_ip.py
   │     │  │  ├─ _linprog_rs.py
   │     │  │  ├─ _linprog_simplex.py
   │     │  │  ├─ _linprog_util.py
   │     │  │  ├─ _lsap.cp310-win_amd64.dll.a
   │     │  │  ├─ _lsq
   │     │  │  │  ├─ bvls.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ dogbox.py
   │     │  │  │  ├─ givens_elimination.cp310-win_amd64.dll.a
   │     │  │  │  ├─ least_squares.py
   │     │  │  │  ├─ lsq_linear.py
   │     │  │  │  ├─ trf.py
   │     │  │  │  ├─ trf_linear.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _milp.py
   │     │  │  ├─ _minimize.py
   │     │  │  ├─ _minpack.cp310-win_amd64.dll.a
   │     │  │  ├─ _minpack_py.py
   │     │  │  ├─ _moduleTNC.cp310-win_amd64.dll.a
   │     │  │  ├─ _nnls.py
   │     │  │  ├─ _nonlin.py
   │     │  │  ├─ _numdiff.py
   │     │  │  ├─ _optimize.py
   │     │  │  ├─ _pava_pybind.cp310-win_amd64.dll.a
   │     │  │  ├─ _qap.py
   │     │  │  ├─ _remove_redundancy.py
   │     │  │  ├─ _root.py
   │     │  │  ├─ _root_scalar.py
   │     │  │  ├─ _shgo.py
   │     │  │  ├─ _shgo_lib
   │     │  │  │  ├─ _complex.py
   │     │  │  │  ├─ _vertex.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _slsqp.cp310-win_amd64.dll.a
   │     │  │  ├─ _slsqp_py.py
   │     │  │  ├─ _spectral.py
   │     │  │  ├─ _tnc.py
   │     │  │  ├─ _trlib
   │     │  │  │  ├─ _trlib.cp310-win_amd64.dll.a
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _trustregion.py
   │     │  │  ├─ _trustregion_constr
   │     │  │  │  ├─ canonical_constraint.py
   │     │  │  │  ├─ equality_constrained_sqp.py
   │     │  │  │  ├─ minimize_trustregion_constr.py
   │     │  │  │  ├─ projections.py
   │     │  │  │  ├─ qp_subproblem.py
   │     │  │  │  ├─ report.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_canonical_constraint.py
   │     │  │  │  │  ├─ test_nested_minimize.py
   │     │  │  │  │  ├─ test_projections.py
   │     │  │  │  │  ├─ test_qp_subproblem.py
   │     │  │  │  │  ├─ test_report.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tr_interior_point.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _trustregion_dogleg.py
   │     │  │  ├─ _trustregion_exact.py
   │     │  │  ├─ _trustregion_krylov.py
   │     │  │  ├─ _trustregion_ncg.py
   │     │  │  ├─ _tstutils.py
   │     │  │  ├─ _zeros.cp310-win_amd64.dll.a
   │     │  │  ├─ _zeros_py.py
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ signal
   │     │  │  ├─ bsplines.py
   │     │  │  ├─ filter_design.py
   │     │  │  ├─ fir_filter_design.py
   │     │  │  ├─ ltisys.py
   │     │  │  ├─ lti_conversion.py
   │     │  │  ├─ signaltools.py
   │     │  │  ├─ spectral.py
   │     │  │  ├─ spline.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ mpsig.py
   │     │  │  │  ├─ test_array_tools.py
   │     │  │  │  ├─ test_bsplines.py
   │     │  │  │  ├─ test_cont2discrete.py
   │     │  │  │  ├─ test_czt.py
   │     │  │  │  ├─ test_dltisys.py
   │     │  │  │  ├─ test_filter_design.py
   │     │  │  │  ├─ test_fir_filter_design.py
   │     │  │  │  ├─ test_ltisys.py
   │     │  │  │  ├─ test_max_len_seq.py
   │     │  │  │  ├─ test_peak_finding.py
   │     │  │  │  ├─ test_result_type.py
   │     │  │  │  ├─ test_savitzky_golay.py
   │     │  │  │  ├─ test_short_time_fft.py
   │     │  │  │  ├─ test_signaltools.py
   │     │  │  │  ├─ test_spectral.py
   │     │  │  │  ├─ test_splines.py
   │     │  │  │  ├─ test_upfirdn.py
   │     │  │  │  ├─ test_waveforms.py
   │     │  │  │  ├─ test_wavelets.py
   │     │  │  │  ├─ test_windows.py
   │     │  │  │  ├─ _scipy_spectral_test_shim.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ waveforms.py
   │     │  │  ├─ wavelets.py
   │     │  │  ├─ windows
   │     │  │  │  ├─ windows.py
   │     │  │  │  ├─ _windows.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _arraytools.py
   │     │  │  ├─ _czt.py
   │     │  │  ├─ _filter_design.py
   │     │  │  ├─ _fir_filter_design.py
   │     │  │  ├─ _ltisys.py
   │     │  │  ├─ _lti_conversion.py
   │     │  │  ├─ _max_len_seq.py
   │     │  │  ├─ _max_len_seq_inner.cp310-win_amd64.dll.a
   │     │  │  ├─ _peak_finding.py
   │     │  │  ├─ _peak_finding_utils.cp310-win_amd64.dll.a
   │     │  │  ├─ _savitzky_golay.py
   │     │  │  ├─ _short_time_fft.py
   │     │  │  ├─ _signaltools.py
   │     │  │  ├─ _sigtools.cp310-win_amd64.dll.a
   │     │  │  ├─ _sosfilt.cp310-win_amd64.dll.a
   │     │  │  ├─ _spectral_py.py
   │     │  │  ├─ _spline.cp310-win_amd64.dll.a
   │     │  │  ├─ _spline.pyi
   │     │  │  ├─ _spline_filters.py
   │     │  │  ├─ _upfirdn.py
   │     │  │  ├─ _upfirdn_apply.cp310-win_amd64.dll.a
   │     │  │  ├─ _waveforms.py
   │     │  │  ├─ _wavelets.py
   │     │  │  └─ __init__.py
   │     │  ├─ sparse
   │     │  │  ├─ base.py
   │     │  │  ├─ bsr.py
   │     │  │  ├─ compressed.py
   │     │  │  ├─ construct.py
   │     │  │  ├─ coo.py
   │     │  │  ├─ csc.py
   │     │  │  ├─ csgraph
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_connected_components.py
   │     │  │  │  │  ├─ test_conversions.py
   │     │  │  │  │  ├─ test_flow.py
   │     │  │  │  │  ├─ test_graph_laplacian.py
   │     │  │  │  │  ├─ test_matching.py
   │     │  │  │  │  ├─ test_pydata_sparse.py
   │     │  │  │  │  ├─ test_reordering.py
   │     │  │  │  │  ├─ test_shortest_path.py
   │     │  │  │  │  ├─ test_spanning_tree.py
   │     │  │  │  │  ├─ test_traversal.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _flow.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _laplacian.py
   │     │  │  │  ├─ _matching.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _min_spanning_tree.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _reordering.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _shortest_path.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _tools.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _traversal.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _validation.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ csr.py
   │     │  │  ├─ data.py
   │     │  │  ├─ dia.py
   │     │  │  ├─ dok.py
   │     │  │  ├─ extract.py
   │     │  │  ├─ lil.py
   │     │  │  ├─ linalg
   │     │  │  │  ├─ dsolve.py
   │     │  │  │  ├─ eigen.py
   │     │  │  │  ├─ interface.py
   │     │  │  │  ├─ isolve.py
   │     │  │  │  ├─ matfuncs.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ propack_test_data.npz
   │     │  │  │  │  ├─ test_expm_multiply.py
   │     │  │  │  │  ├─ test_interface.py
   │     │  │  │  │  ├─ test_matfuncs.py
   │     │  │  │  │  ├─ test_norm.py
   │     │  │  │  │  ├─ test_onenormest.py
   │     │  │  │  │  ├─ test_propack.py
   │     │  │  │  │  ├─ test_pydata_sparse.py
   │     │  │  │  │  ├─ test_special_sparse_arrays.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _dsolve
   │     │  │  │  │  ├─ linsolve.py
   │     │  │  │  │  ├─ tests
   │     │  │  │  │  │  ├─ test_linsolve.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ _add_newdocs.py
   │     │  │  │  │  ├─ _superlu.cp310-win_amd64.dll.a
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _eigen
   │     │  │  │  │  ├─ arpack
   │     │  │  │  │  │  ├─ arpack.py
   │     │  │  │  │  │  ├─ COPYING
   │     │  │  │  │  │  ├─ tests
   │     │  │  │  │  │  │  ├─ test_arpack.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ _arpack.cp310-win_amd64.dll.a
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ lobpcg
   │     │  │  │  │  │  ├─ lobpcg.py
   │     │  │  │  │  │  ├─ tests
   │     │  │  │  │  │  │  ├─ test_lobpcg.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ tests
   │     │  │  │  │  │  ├─ test_svds.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ _svds.py
   │     │  │  │  │  ├─ _svds_doc.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _expm_multiply.py
   │     │  │  │  ├─ _interface.py
   │     │  │  │  ├─ _isolve
   │     │  │  │  │  ├─ iterative.py
   │     │  │  │  │  ├─ lgmres.py
   │     │  │  │  │  ├─ lsmr.py
   │     │  │  │  │  ├─ lsqr.py
   │     │  │  │  │  ├─ minres.py
   │     │  │  │  │  ├─ tests
   │     │  │  │  │  │  ├─ test_gcrotmk.py
   │     │  │  │  │  │  ├─ test_iterative.py
   │     │  │  │  │  │  ├─ test_lgmres.py
   │     │  │  │  │  │  ├─ test_lsmr.py
   │     │  │  │  │  │  ├─ test_lsqr.py
   │     │  │  │  │  │  ├─ test_minres.py
   │     │  │  │  │  │  ├─ test_utils.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ tfqmr.py
   │     │  │  │  │  ├─ utils.py
   │     │  │  │  │  ├─ _gcrotmk.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _matfuncs.py
   │     │  │  │  ├─ _norm.py
   │     │  │  │  ├─ _onenormest.py
   │     │  │  │  ├─ _propack
   │     │  │  │  │  ├─ _cpropack.cp310-win_amd64.dll.a
   │     │  │  │  │  ├─ _dpropack.cp310-win_amd64.dll.a
   │     │  │  │  │  ├─ _spropack.cp310-win_amd64.dll.a
   │     │  │  │  │  └─ _zpropack.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _special_sparse_arrays.py
   │     │  │  │  ├─ _svdp.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sparsetools.py
   │     │  │  ├─ spfuncs.py
   │     │  │  ├─ sputils.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ csc_py2.npz
   │     │  │  │  │  └─ csc_py3.npz
   │     │  │  │  ├─ test_arithmetic1d.py
   │     │  │  │  ├─ test_array_api.py
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_common1d.py
   │     │  │  │  ├─ test_construct.py
   │     │  │  │  ├─ test_coo.py
   │     │  │  │  ├─ test_csc.py
   │     │  │  │  ├─ test_csr.py
   │     │  │  │  ├─ test_dok.py
   │     │  │  │  ├─ test_extract.py
   │     │  │  │  ├─ test_indexing1d.py
   │     │  │  │  ├─ test_matrix_io.py
   │     │  │  │  ├─ test_minmax1d.py
   │     │  │  │  ├─ test_sparsetools.py
   │     │  │  │  ├─ test_spfuncs.py
   │     │  │  │  ├─ test_sputils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _bsr.py
   │     │  │  ├─ _compressed.py
   │     │  │  ├─ _construct.py
   │     │  │  ├─ _coo.py
   │     │  │  ├─ _csc.py
   │     │  │  ├─ _csparsetools.cp310-win_amd64.dll.a
   │     │  │  ├─ _csr.py
   │     │  │  ├─ _data.py
   │     │  │  ├─ _dia.py
   │     │  │  ├─ _dok.py
   │     │  │  ├─ _extract.py
   │     │  │  ├─ _index.py
   │     │  │  ├─ _lil.py
   │     │  │  ├─ _matrix.py
   │     │  │  ├─ _matrix_io.py
   │     │  │  ├─ _sparsetools.cp310-win_amd64.dll.a
   │     │  │  ├─ _spfuncs.py
   │     │  │  ├─ _sputils.py
   │     │  │  └─ __init__.py
   │     │  ├─ spatial
   │     │  │  ├─ ckdtree.py
   │     │  │  ├─ distance.py
   │     │  │  ├─ distance.pyi
   │     │  │  ├─ kdtree.py
   │     │  │  ├─ qhull.py
   │     │  │  ├─ qhull_src
   │     │  │  │  └─ COPYING.txt
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ cdist-X1.txt
   │     │  │  │  │  ├─ cdist-X2.txt
   │     │  │  │  │  ├─ degenerate_pointset.npz
   │     │  │  │  │  ├─ iris.txt
   │     │  │  │  │  ├─ pdist-boolean-inp.txt
   │     │  │  │  │  ├─ pdist-chebyshev-ml-iris.txt
   │     │  │  │  │  ├─ pdist-chebyshev-ml.txt
   │     │  │  │  │  ├─ pdist-cityblock-ml-iris.txt
   │     │  │  │  │  ├─ pdist-cityblock-ml.txt
   │     │  │  │  │  ├─ pdist-correlation-ml-iris.txt
   │     │  │  │  │  ├─ pdist-correlation-ml.txt
   │     │  │  │  │  ├─ pdist-cosine-ml-iris.txt
   │     │  │  │  │  ├─ pdist-cosine-ml.txt
   │     │  │  │  │  ├─ pdist-double-inp.txt
   │     │  │  │  │  ├─ pdist-euclidean-ml-iris.txt
   │     │  │  │  │  ├─ pdist-euclidean-ml.txt
   │     │  │  │  │  ├─ pdist-hamming-ml.txt
   │     │  │  │  │  ├─ pdist-jaccard-ml.txt
   │     │  │  │  │  ├─ pdist-jensenshannon-ml-iris.txt
   │     │  │  │  │  ├─ pdist-jensenshannon-ml.txt
   │     │  │  │  │  ├─ pdist-minkowski-3.2-ml-iris.txt
   │     │  │  │  │  ├─ pdist-minkowski-3.2-ml.txt
   │     │  │  │  │  ├─ pdist-minkowski-5.8-ml-iris.txt
   │     │  │  │  │  ├─ pdist-seuclidean-ml-iris.txt
   │     │  │  │  │  ├─ pdist-seuclidean-ml.txt
   │     │  │  │  │  ├─ pdist-spearman-ml.txt
   │     │  │  │  │  ├─ random-bool-data.txt
   │     │  │  │  │  ├─ random-double-data.txt
   │     │  │  │  │  ├─ random-int-data.txt
   │     │  │  │  │  ├─ random-uint-data.txt
   │     │  │  │  │  └─ selfdual-4d-polytope.txt
   │     │  │  │  ├─ test_distance.py
   │     │  │  │  ├─ test_hausdorff.py
   │     │  │  │  ├─ test_kdtree.py
   │     │  │  │  ├─ test_qhull.py
   │     │  │  │  ├─ test_slerp.py
   │     │  │  │  ├─ test_spherical_voronoi.py
   │     │  │  │  ├─ test__plotutils.py
   │     │  │  │  ├─ test__procrustes.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ transform
   │     │  │  │  ├─ rotation.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_rotation.py
   │     │  │  │  │  ├─ test_rotation_groups.py
   │     │  │  │  │  ├─ test_rotation_spline.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _rotation.cp310-win_amd64.dll.a
   │     │  │  │  ├─ _rotation_groups.py
   │     │  │  │  ├─ _rotation_spline.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _ckdtree.cp310-win_amd64.dll.a
   │     │  │  ├─ _distance_pybind.cp310-win_amd64.dll.a
   │     │  │  ├─ _distance_wrap.cp310-win_amd64.dll.a
   │     │  │  ├─ _geometric_slerp.py
   │     │  │  ├─ _hausdorff.cp310-win_amd64.dll.a
   │     │  │  ├─ _kdtree.py
   │     │  │  ├─ _plotutils.py
   │     │  │  ├─ _procrustes.py
   │     │  │  ├─ _qhull.cp310-win_amd64.dll.a
   │     │  │  ├─ _qhull.pyi
   │     │  │  ├─ _spherical_voronoi.py
   │     │  │  ├─ _voronoi.cp310-win_amd64.dll.a
   │     │  │  ├─ _voronoi.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ special
   │     │  │  ├─ add_newdocs.py
   │     │  │  ├─ basic.py
   │     │  │  ├─ cython_special.cp310-win_amd64.dll.a
   │     │  │  ├─ cython_special.pxd
   │     │  │  ├─ cython_special.pyi
   │     │  │  ├─ libsf_error_state.dll
   │     │  │  ├─ libsf_error_state.dll.a
   │     │  │  ├─ orthogonal.py
   │     │  │  ├─ sf_error.py
   │     │  │  ├─ specfun.py
   │     │  │  ├─ spfun_stats.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ boost.npz
   │     │  │  │  │  ├─ gsl.npz
   │     │  │  │  │  ├─ local.npz
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_basic.py
   │     │  │  │  ├─ test_bdtr.py
   │     │  │  │  ├─ test_boost_ufuncs.py
   │     │  │  │  ├─ test_boxcox.py
   │     │  │  │  ├─ test_cdflib.py
   │     │  │  │  ├─ test_cdft_asymptotic.py
   │     │  │  │  ├─ test_cephes_intp_cast.py
   │     │  │  │  ├─ test_cosine_distr.py
   │     │  │  │  ├─ test_cython_special.py
   │     │  │  │  ├─ test_data.py
   │     │  │  │  ├─ test_dd.py
   │     │  │  │  ├─ test_digamma.py
   │     │  │  │  ├─ test_ellip_harm.py
   │     │  │  │  ├─ test_erfinv.py
   │     │  │  │  ├─ test_exponential_integrals.py
   │     │  │  │  ├─ test_extending.py
   │     │  │  │  ├─ test_faddeeva.py
   │     │  │  │  ├─ test_gamma.py
   │     │  │  │  ├─ test_gammainc.py
   │     │  │  │  ├─ test_hyp2f1.py
   │     │  │  │  ├─ test_hypergeometric.py
   │     │  │  │  ├─ test_iv_ratio.py
   │     │  │  │  ├─ test_kolmogorov.py
   │     │  │  │  ├─ test_lambertw.py
   │     │  │  │  ├─ test_legendre.py
   │     │  │  │  ├─ test_loggamma.py
   │     │  │  │  ├─ test_logit.py
   │     │  │  │  ├─ test_logsumexp.py
   │     │  │  │  ├─ test_log_softmax.py
   │     │  │  │  ├─ test_mpmath.py
   │     │  │  │  ├─ test_nan_inputs.py
   │     │  │  │  ├─ test_ndtr.py
   │     │  │  │  ├─ test_ndtri_exp.py
   │     │  │  │  ├─ test_orthogonal.py
   │     │  │  │  ├─ test_orthogonal_eval.py
   │     │  │  │  ├─ test_owens_t.py
   │     │  │  │  ├─ test_pcf.py
   │     │  │  │  ├─ test_pdtr.py
   │     │  │  │  ├─ test_powm1.py
   │     │  │  │  ├─ test_precompute_expn_asy.py
   │     │  │  │  ├─ test_precompute_gammainc.py
   │     │  │  │  ├─ test_precompute_utils.py
   │     │  │  │  ├─ test_round.py
   │     │  │  │  ├─ test_sf_error.py
   │     │  │  │  ├─ test_sici.py
   │     │  │  │  ├─ test_specfun.py
   │     │  │  │  ├─ test_spence.py
   │     │  │  │  ├─ test_spfun_stats.py
   │     │  │  │  ├─ test_spherical_bessel.py
   │     │  │  │  ├─ test_sph_harm.py
   │     │  │  │  ├─ test_support_alternative_backends.py
   │     │  │  │  ├─ test_trig.py
   │     │  │  │  ├─ test_ufunc_signatures.py
   │     │  │  │  ├─ test_wrightomega.py
   │     │  │  │  ├─ test_wright_bessel.py
   │     │  │  │  ├─ test_xsf_cuda.py
   │     │  │  │  ├─ test_zeta.py
   │     │  │  │  ├─ _cython_examples
   │     │  │  │  │  └─ extending.pyx
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ xsf
   │     │  │  │  ├─ binom.h
   │     │  │  │  ├─ cdflib.h
   │     │  │  │  ├─ cephes
   │     │  │  │  │  ├─ airy.h
   │     │  │  │  │  ├─ besselpoly.h
   │     │  │  │  │  ├─ beta.h
   │     │  │  │  │  ├─ cbrt.h
   │     │  │  │  │  ├─ chbevl.h
   │     │  │  │  │  ├─ chdtr.h
   │     │  │  │  │  ├─ const.h
   │     │  │  │  │  ├─ ellie.h
   │     │  │  │  │  ├─ ellik.h
   │     │  │  │  │  ├─ ellpe.h
   │     │  │  │  │  ├─ ellpk.h
   │     │  │  │  │  ├─ expn.h
   │     │  │  │  │  ├─ gamma.h
   │     │  │  │  │  ├─ hyp2f1.h
   │     │  │  │  │  ├─ hyperg.h
   │     │  │  │  │  ├─ i0.h
   │     │  │  │  │  ├─ i1.h
   │     │  │  │  │  ├─ igam.h
   │     │  │  │  │  ├─ igami.h
   │     │  │  │  │  ├─ igam_asymp_coeff.h
   │     │  │  │  │  ├─ j0.h
   │     │  │  │  │  ├─ j1.h
   │     │  │  │  │  ├─ jv.h
   │     │  │  │  │  ├─ k0.h
   │     │  │  │  │  ├─ k1.h
   │     │  │  │  │  ├─ kn.h
   │     │  │  │  │  ├─ lanczos.h
   │     │  │  │  │  ├─ ndtr.h
   │     │  │  │  │  ├─ poch.h
   │     │  │  │  │  ├─ polevl.h
   │     │  │  │  │  ├─ psi.h
   │     │  │  │  │  ├─ rgamma.h
   │     │  │  │  │  ├─ scipy_iv.h
   │     │  │  │  │  ├─ shichi.h
   │     │  │  │  │  ├─ sici.h
   │     │  │  │  │  ├─ sindg.h
   │     │  │  │  │  ├─ tandg.h
   │     │  │  │  │  ├─ trig.h
   │     │  │  │  │  ├─ unity.h
   │     │  │  │  │  └─ zeta.h
   │     │  │  │  ├─ config.h
   │     │  │  │  ├─ digamma.h
   │     │  │  │  ├─ error.h
   │     │  │  │  ├─ evalpoly.h
   │     │  │  │  ├─ expint.h
   │     │  │  │  ├─ hyp2f1.h
   │     │  │  │  ├─ iv_ratio.h
   │     │  │  │  ├─ lambertw.h
   │     │  │  │  ├─ loggamma.h
   │     │  │  │  ├─ sici.h
   │     │  │  │  ├─ tools.h
   │     │  │  │  ├─ trig.h
   │     │  │  │  ├─ wright_bessel.h
   │     │  │  │  └─ zlog1.h
   │     │  │  ├─ _add_newdocs.py
   │     │  │  ├─ _basic.py
   │     │  │  ├─ _comb.cp310-win_amd64.dll.a
   │     │  │  ├─ _ellip_harm.py
   │     │  │  ├─ _ellip_harm_2.cp310-win_amd64.dll.a
   │     │  │  ├─ _gufuncs.cp310-win_amd64.dll.a
   │     │  │  ├─ _input_validation.py
   │     │  │  ├─ _lambertw.py
   │     │  │  ├─ _logsumexp.py
   │     │  │  ├─ _mptestutils.py
   │     │  │  ├─ _multiufuncs.py
   │     │  │  ├─ _orthogonal.py
   │     │  │  ├─ _orthogonal.pyi
   │     │  │  ├─ _precompute
   │     │  │  │  ├─ cosine_cdf.py
   │     │  │  │  ├─ expn_asy.py
   │     │  │  │  ├─ gammainc_asy.py
   │     │  │  │  ├─ gammainc_data.py
   │     │  │  │  ├─ hyp2f1_data.py
   │     │  │  │  ├─ lambertw.py
   │     │  │  │  ├─ loggamma.py
   │     │  │  │  ├─ struve_convergence.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ wrightomega.py
   │     │  │  │  ├─ wright_bessel.py
   │     │  │  │  ├─ wright_bessel_data.py
   │     │  │  │  ├─ zetac.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _sf_error.py
   │     │  │  ├─ _specfun.cp310-win_amd64.dll.a
   │     │  │  ├─ _special_ufuncs.cp310-win_amd64.dll.a
   │     │  │  ├─ _spfun_stats.py
   │     │  │  ├─ _spherical_bessel.py
   │     │  │  ├─ _support_alternative_backends.py
   │     │  │  ├─ _testutils.py
   │     │  │  ├─ _test_internal.cp310-win_amd64.dll.a
   │     │  │  ├─ _test_internal.pyi
   │     │  │  ├─ _ufuncs.cp310-win_amd64.dll.a
   │     │  │  ├─ _ufuncs.pyi
   │     │  │  ├─ _ufuncs.pyx
   │     │  │  ├─ _ufuncs_cxx.cp310-win_amd64.dll.a
   │     │  │  ├─ _ufuncs_cxx.pxd
   │     │  │  ├─ _ufuncs_cxx.pyx
   │     │  │  ├─ _ufuncs_cxx_defs.h
   │     │  │  ├─ _ufuncs_defs.h
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ stats
   │     │  │  ├─ biasedurn.py
   │     │  │  ├─ contingency.py
   │     │  │  ├─ distributions.py
   │     │  │  ├─ kde.py
   │     │  │  ├─ morestats.py
   │     │  │  ├─ mstats.py
   │     │  │  ├─ mstats_basic.py
   │     │  │  ├─ mstats_extras.py
   │     │  │  ├─ mvn.py
   │     │  │  ├─ qmc.py
   │     │  │  ├─ sampling.py
   │     │  │  ├─ stats.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ common_tests.py
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ fisher_exact_results_from_r.py
   │     │  │  │  │  ├─ jf_skew_t_gamlss_pdf_data.npy
   │     │  │  │  │  ├─ levy_stable
   │     │  │  │  │  │  ├─ stable-loc-scale-sample-data.npy
   │     │  │  │  │  │  ├─ stable-Z1-cdf-sample-data.npy
   │     │  │  │  │  │  └─ stable-Z1-pdf-sample-data.npy
   │     │  │  │  │  ├─ nist_anova
   │     │  │  │  │  │  ├─ AtmWtAg.dat
   │     │  │  │  │  │  ├─ SiRstv.dat
   │     │  │  │  │  │  ├─ SmLs01.dat
   │     │  │  │  │  │  ├─ SmLs02.dat
   │     │  │  │  │  │  ├─ SmLs03.dat
   │     │  │  │  │  │  ├─ SmLs04.dat
   │     │  │  │  │  │  ├─ SmLs05.dat
   │     │  │  │  │  │  ├─ SmLs06.dat
   │     │  │  │  │  │  ├─ SmLs07.dat
   │     │  │  │  │  │  ├─ SmLs08.dat
   │     │  │  │  │  │  └─ SmLs09.dat
   │     │  │  │  │  ├─ nist_linregress
   │     │  │  │  │  │  └─ Norris.dat
   │     │  │  │  │  ├─ rel_breitwigner_pdf_sample_data_ROOT.npy
   │     │  │  │  │  ├─ studentized_range_mpmath_ref.json
   │     │  │  │  │  └─ _mvt.py
   │     │  │  │  ├─ test_axis_nan_policy.py
   │     │  │  │  ├─ test_binned_statistic.py
   │     │  │  │  ├─ test_censored_data.py
   │     │  │  │  ├─ test_contingency.py
   │     │  │  │  ├─ test_continuous.py
   │     │  │  │  ├─ test_continuous_basic.py
   │     │  │  │  ├─ test_continuous_fit_censored.py
   │     │  │  │  ├─ test_correlation.py
   │     │  │  │  ├─ test_crosstab.py
   │     │  │  │  ├─ test_discrete_basic.py
   │     │  │  │  ├─ test_discrete_distns.py
   │     │  │  │  ├─ test_distributions.py
   │     │  │  │  ├─ test_entropy.py
   │     │  │  │  ├─ test_fast_gen_inversion.py
   │     │  │  │  ├─ test_fit.py
   │     │  │  │  ├─ test_hypotests.py
   │     │  │  │  ├─ test_kdeoth.py
   │     │  │  │  ├─ test_mgc.py
   │     │  │  │  ├─ test_morestats.py
   │     │  │  │  ├─ test_mstats_basic.py
   │     │  │  │  ├─ test_mstats_extras.py
   │     │  │  │  ├─ test_multicomp.py
   │     │  │  │  ├─ test_multivariate.py
   │     │  │  │  ├─ test_odds_ratio.py
   │     │  │  │  ├─ test_qmc.py
   │     │  │  │  ├─ test_rank.py
   │     │  │  │  ├─ test_relative_risk.py
   │     │  │  │  ├─ test_resampling.py
   │     │  │  │  ├─ test_sampling.py
   │     │  │  │  ├─ test_sensitivity_analysis.py
   │     │  │  │  ├─ test_stats.py
   │     │  │  │  ├─ test_survival.py
   │     │  │  │  ├─ test_tukeylambda_stats.py
   │     │  │  │  ├─ test_variation.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _ansari_swilk_statistics.cp310-win_amd64.dll.a
   │     │  │  ├─ _axis_nan_policy.py
   │     │  │  ├─ _biasedurn.cp310-win_amd64.dll.a
   │     │  │  ├─ _biasedurn.pxd
   │     │  │  ├─ _binned_statistic.py
   │     │  │  ├─ _binomtest.py
   │     │  │  ├─ _bws_test.py
   │     │  │  ├─ _censored_data.py
   │     │  │  ├─ _common.py
   │     │  │  ├─ _constants.py
   │     │  │  ├─ _continuous_distns.py
   │     │  │  ├─ _correlation.py
   │     │  │  ├─ _covariance.py
   │     │  │  ├─ _crosstab.py
   │     │  │  ├─ _discrete_distns.py
   │     │  │  ├─ _distn_infrastructure.py
   │     │  │  ├─ _distribution_infrastructure.py
   │     │  │  ├─ _distr_params.py
   │     │  │  ├─ _entropy.py
   │     │  │  ├─ _fit.py
   │     │  │  ├─ _hypotests.py
   │     │  │  ├─ _kde.py
   │     │  │  ├─ _ksstats.py
   │     │  │  ├─ _levy_stable
   │     │  │  │  ├─ levyst.cp310-win_amd64.dll.a
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _mannwhitneyu.py
   │     │  │  ├─ _mgc.py
   │     │  │  ├─ _morestats.py
   │     │  │  ├─ _mstats_basic.py
   │     │  │  ├─ _mstats_extras.py
   │     │  │  ├─ _multicomp.py
   │     │  │  ├─ _multivariate.py
   │     │  │  ├─ _mvn.cp310-win_amd64.dll.a
   │     │  │  ├─ _new_distributions.py
   │     │  │  ├─ _odds_ratio.py
   │     │  │  ├─ _page_trend_test.py
   │     │  │  ├─ _probability_distribution.py
   │     │  │  ├─ _qmc.py
   │     │  │  ├─ _qmc_cy.cp310-win_amd64.dll.a
   │     │  │  ├─ _qmc_cy.pyi
   │     │  │  ├─ _qmvnt.py
   │     │  │  ├─ _rcont
   │     │  │  │  ├─ rcont.cp310-win_amd64.dll.a
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _relative_risk.py
   │     │  │  ├─ _resampling.py
   │     │  │  ├─ _result_classes.py
   │     │  │  ├─ _sampling.py
   │     │  │  ├─ _sensitivity_analysis.py
   │     │  │  ├─ _sobol.cp310-win_amd64.dll.a
   │     │  │  ├─ _sobol.pyi
   │     │  │  ├─ _sobol_direction_numbers.npz
   │     │  │  ├─ _stats.cp310-win_amd64.dll.a
   │     │  │  ├─ _stats.pxd
   │     │  │  ├─ _stats_mstats_common.py
   │     │  │  ├─ _stats_py.py
   │     │  │  ├─ _stats_pythran.cp310-win_amd64.dll.a
   │     │  │  ├─ _survival.py
   │     │  │  ├─ _tukeylambda_stats.py
   │     │  │  ├─ _unuran
   │     │  │  │  ├─ unuran_wrapper.cp310-win_amd64.dll.a
   │     │  │  │  ├─ unuran_wrapper.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _variation.py
   │     │  │  ├─ _warnings_errors.py
   │     │  │  ├─ _wilcoxon.py
   │     │  │  └─ __init__.py
   │     │  ├─ version.py
   │     │  ├─ _distributor_init.py
   │     │  ├─ _lib
   │     │  │  ├─ array_api_compat
   │     │  │  │  ├─ common
   │     │  │  │  │  ├─ _aliases.py
   │     │  │  │  │  ├─ _fft.py
   │     │  │  │  │  ├─ _helpers.py
   │     │  │  │  │  ├─ _linalg.py
   │     │  │  │  │  ├─ _typing.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ cupy
   │     │  │  │  │  ├─ fft.py
   │     │  │  │  │  ├─ linalg.py
   │     │  │  │  │  ├─ _aliases.py
   │     │  │  │  │  ├─ _info.py
   │     │  │  │  │  ├─ _typing.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ dask
   │     │  │  │  │  ├─ array
   │     │  │  │  │  │  ├─ fft.py
   │     │  │  │  │  │  ├─ linalg.py
   │     │  │  │  │  │  ├─ _aliases.py
   │     │  │  │  │  │  ├─ _info.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ numpy
   │     │  │  │  │  ├─ fft.py
   │     │  │  │  │  ├─ linalg.py
   │     │  │  │  │  ├─ _aliases.py
   │     │  │  │  │  ├─ _info.py
   │     │  │  │  │  ├─ _typing.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ torch
   │     │  │  │  │  ├─ fft.py
   │     │  │  │  │  ├─ linalg.py
   │     │  │  │  │  ├─ _aliases.py
   │     │  │  │  │  ├─ _info.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _internal.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ array_api_extra
   │     │  │  │  ├─ _funcs.py
   │     │  │  │  ├─ _typing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cobyqa
   │     │  │  │  ├─ framework.py
   │     │  │  │  ├─ main.py
   │     │  │  │  ├─ models.py
   │     │  │  │  ├─ problem.py
   │     │  │  │  ├─ settings.py
   │     │  │  │  ├─ subsolvers
   │     │  │  │  │  ├─ geometry.py
   │     │  │  │  │  ├─ optim.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ utils
   │     │  │  │  │  ├─ exceptions.py
   │     │  │  │  │  ├─ math.py
   │     │  │  │  │  ├─ versions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ decorator.py
   │     │  │  ├─ deprecation.py
   │     │  │  ├─ doccer.py
   │     │  │  ├─ messagestream.cp310-win_amd64.dll.a
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_array_api.py
   │     │  │  │  ├─ test_bunch.py
   │     │  │  │  ├─ test_ccallback.py
   │     │  │  │  ├─ test_config.py
   │     │  │  │  ├─ test_deprecation.py
   │     │  │  │  ├─ test_doccer.py
   │     │  │  │  ├─ test_import_cycles.py
   │     │  │  │  ├─ test_public_api.py
   │     │  │  │  ├─ test_scipy_version.py
   │     │  │  │  ├─ test_tmpdirs.py
   │     │  │  │  ├─ test_warnings.py
   │     │  │  │  ├─ test__gcutils.py
   │     │  │  │  ├─ test__pep440.py
   │     │  │  │  ├─ test__testutils.py
   │     │  │  │  ├─ test__threadsafety.py
   │     │  │  │  ├─ test__util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ uarray.py
   │     │  │  ├─ _array_api.py
   │     │  │  ├─ _array_api_no_0d.py
   │     │  │  ├─ _bunch.py
   │     │  │  ├─ _ccallback.py
   │     │  │  ├─ _ccallback_c.cp310-win_amd64.dll.a
   │     │  │  ├─ _disjoint_set.py
   │     │  │  ├─ _docscrape.py
   │     │  │  ├─ _elementwise_iterative_method.py
   │     │  │  ├─ _finite_differences.py
   │     │  │  ├─ _fpumode.cp310-win_amd64.dll.a
   │     │  │  ├─ _gcutils.py
   │     │  │  ├─ _pep440.py
   │     │  │  ├─ _testutils.py
   │     │  │  ├─ _test_ccallback.cp310-win_amd64.dll.a
   │     │  │  ├─ _test_deprecation_call.cp310-win_amd64.dll.a
   │     │  │  ├─ _test_deprecation_def.cp310-win_amd64.dll.a
   │     │  │  ├─ _threadsafety.py
   │     │  │  ├─ _tmpdirs.py
   │     │  │  ├─ _uarray
   │     │  │  │  ├─ LICENSE
   │     │  │  │  ├─ _backend.py
   │     │  │  │  ├─ _uarray.cp310-win_amd64.dll.a
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _util.py
   │     │  │  └─ __init__.py
   │     │  ├─ __config__.py
   │     │  └─ __init__.py
   │     ├─ scipy-1.15.3-cp310-cp310-win_amd64.whl
   │     ├─ scipy-1.15.3.dist-info
   │     │  ├─ DELVEWHEEL
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ scipy.libs
   │     │  └─ libscipy_openblas-f07f5a5d207a3a47104dca54d6d0c86a.dll
   │     ├─ scs
   │     │  ├─ _scs_direct.cp310-win_amd64.dll.a
   │     │  ├─ _scs_indirect.cp310-win_amd64.dll.a
   │     │  └─ __init__.py
   │     ├─ scs-3.2.11.dist-info
   │     │  ├─ DELVEWHEEL
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ scs.libs
   │     │  └─ openblas-6202f9ff9919f0b9339ea4f477eb2411.dll
   │     ├─ setup
   │     │  ├─ extensions.py
   │     │  ├─ versioning.py
   │     │  └─ __init__.py
   │     ├─ setuptools
   │     │  ├─ archive_util.py
   │     │  ├─ cli-32.exe
   │     │  ├─ cli-64.exe
   │     │  ├─ cli-arm64.exe
   │     │  ├─ cli.exe
   │     │  ├─ command
   │     │  │  ├─ alias.py
   │     │  │  ├─ bdist_egg.py
   │     │  │  ├─ bdist_rpm.py
   │     │  │  ├─ bdist_wheel.py
   │     │  │  ├─ develop.py
   │     │  │  ├─ dist_info.py
   │     │  │  ├─ easy_install.py
   │     │  │  ├─ editable_wheel.py
   │     │  │  ├─ egg_info.py
   │     │  │  ├─ install.py
   │     │  │  ├─ install_egg_info.py
   │     │  │  ├─ install_lib.py
   │     │  │  ├─ install_scripts.py
   │     │  │  ├─ rotate.py
   │     │  │  ├─ saveopts.py
   │     │  │  ├─ sdist.py
   │     │  │  ├─ setopt.py
   │     │  │  ├─ test.py
   │     │  │  ├─ _requirestxt.py
   │     │  │  └─ __init__.py
   │     │  ├─ compat
   │     │  │  ├─ py310.py
   │     │  │  ├─ py311.py
   │     │  │  ├─ py312.py
   │     │  │  ├─ py39.py
   │     │  │  └─ __init__.py
   │     │  ├─ config
   │     │  │  ├─ distutils.schema.json
   │     │  │  ├─ expand.py
   │     │  │  ├─ NOTICE
   │     │  │  ├─ pyprojecttoml.py
   │     │  │  ├─ setupcfg.py
   │     │  │  ├─ setuptools.schema.json
   │     │  │  ├─ _apply_pyprojecttoml.py
   │     │  │  ├─ _validate_pyproject
   │     │  │  │  ├─ error_reporting.py
   │     │  │  │  ├─ extra_validations.py
   │     │  │  │  ├─ fastjsonschema_exceptions.py
   │     │  │  │  ├─ fastjsonschema_validations.py
   │     │  │  │  ├─ formats.py
   │     │  │  │  ├─ NOTICE
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ depends.py
   │     │  ├─ discovery.py
   │     │  ├─ dist.py
   │     │  ├─ errors.py
   │     │  ├─ extension.py
   │     │  ├─ glob.py
   │     │  ├─ gui-32.exe
   │     │  ├─ gui-64.exe
   │     │  ├─ gui-arm64.exe
   │     │  ├─ gui.exe
   │     │  ├─ installer.py
   │     │  ├─ launch.py
   │     │  ├─ launcher manifest.xml
   │     │  ├─ logging.py
   │     │  ├─ modified.py
   │     │  ├─ monkey.py
   │     │  ├─ msvc.py
   │     │  ├─ namespaces.py
   │     │  ├─ script (dev).tmpl
   │     │  ├─ script.tmpl
   │     │  ├─ unicode_utils.py
   │     │  ├─ version.py
   │     │  ├─ warnings.py
   │     │  ├─ wheel.py
   │     │  ├─ windows_support.py
   │     │  ├─ _core_metadata.py
   │     │  ├─ _discovery.py
   │     │  ├─ _distutils
   │     │  │  ├─ archive_util.py
   │     │  │  ├─ ccompiler.py
   │     │  │  ├─ cmd.py
   │     │  │  ├─ command
   │     │  │  │  ├─ bdist.py
   │     │  │  │  ├─ bdist_dumb.py
   │     │  │  │  ├─ bdist_rpm.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ clean.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ install.py
   │     │  │  │  ├─ install_data.py
   │     │  │  │  ├─ install_egg_info.py
   │     │  │  │  ├─ install_headers.py
   │     │  │  │  ├─ install_lib.py
   │     │  │  │  ├─ install_scripts.py
   │     │  │  │  ├─ sdist.py
   │     │  │  │  ├─ _framework_compat.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ compat
   │     │  │  │  ├─ numpy.py
   │     │  │  │  ├─ py310.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ compilers
   │     │  │  │  ├─ C
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ cygwin.py
   │     │  │  │  │  ├─ errors.py
   │     │  │  │  │  ├─ msvc.py
   │     │  │  │  │  ├─ py.typed
   │     │  │  │  │  ├─ unix.py
   │     │  │  │  │  └─ zos.py
   │     │  │  │  ├─ errors.py
   │     │  │  │  ├─ logging.py
   │     │  │  │  ├─ platform
   │     │  │  │  │  ├─ detect.py
   │     │  │  │  │  └─ macos.py
   │     │  │  │  ├─ _modified.py
   │     │  │  │  └─ _util.py
   │     │  │  ├─ core.py
   │     │  │  ├─ cygwinccompiler.py
   │     │  │  ├─ debug.py
   │     │  │  ├─ dep_util.py
   │     │  │  ├─ dir_util.py
   │     │  │  ├─ dist.py
   │     │  │  ├─ errors.py
   │     │  │  ├─ extension.py
   │     │  │  ├─ fancy_getopt.py
   │     │  │  ├─ filelist.py
   │     │  │  ├─ file_util.py
   │     │  │  ├─ log.py
   │     │  │  ├─ py.typed
   │     │  │  ├─ spawn.py
   │     │  │  ├─ sysconfig.py
   │     │  │  ├─ text_file.py
   │     │  │  ├─ unixccompiler.py
   │     │  │  ├─ util.py
   │     │  │  ├─ version.py
   │     │  │  ├─ versionpredicate.py
   │     │  │  ├─ zosccompiler.py
   │     │  │  ├─ _dataclass.py
   │     │  │  ├─ _log.py
   │     │  │  ├─ _macos_compat.py
   │     │  │  ├─ _modified.py
   │     │  │  ├─ _msvccompiler.py
   │     │  │  └─ __init__.py
   │     │  ├─ _entry_points.py
   │     │  ├─ _imp.py
   │     │  ├─ _importlib.py
   │     │  ├─ _itertools.py
   │     │  ├─ _normalization.py
   │     │  ├─ _path.py
   │     │  ├─ _reqs.py
   │     │  ├─ _scripts.py
   │     │  ├─ _shutil.py
   │     │  ├─ _static.py
   │     │  ├─ _vendor
   │     │  │  ├─ .lock
   │     │  │  ├─ autocommand
   │     │  │  │  ├─ autoasync.py
   │     │  │  │  ├─ autocommand.py
   │     │  │  │  ├─ automain.py
   │     │  │  │  ├─ autoparse.py
   │     │  │  │  ├─ errors.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ autocommand-2.2.2.dist-info
   │     │  │  │  ├─ INSTALLER
   │     │  │  │  ├─ LICENSE
   │     │  │  │  ├─ METADATA
   │     │  │  │  ├─ RECORD
   │     │  │  │  ├─ REQUESTED
   │     │  │  │  ├─ top_level.txt
   │     │  │  │  └─ WHEEL
   │     │  │  ├─ backports
   │     │  │  │  ├─ tarfile
   │     │  │  │  │  ├─ compat
   │     │  │  │  │  │  ├─ py38.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __main__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ backports.tarfile-1.2.0.dist-info
   │     │  │  │  ├─ INSTALLER
   │     │  │  │  ├─ LICENSE
   │     │  │  │  ├─ METADATA
   │     │  │  │  ├─ RECORD
   │     │  │  │  ├─ REQUESTED
   │     │  │  │  ├─ top_level.txt
   │     │  │  │  └─ WHEEL
   │     │  │  ├─ importlib_metadata
   │     │  │  │  ├─ compat
   │     │  │  │  │  ├─ py311.py
   │     │  │  │  │  ├─ py39.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ diagnose.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ _adapters.py
   │     │  │  │  ├─ _collections.py
   │     │  │  │  ├─ _compat.py
   │     │  │  │  ├─ _functools.py
   │     │  │  │  ├─ _itertools.py
   │     │  │  │  ├─ _meta.py
   │     │  │  │  ├─ _text.py
   │     │  │  │  ├─ _typing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ importlib_metadata-8.7.1.dist-info
   │     │  │  │  ├─ INSTALLER
   │     │  │  │  ├─ licenses
   │     │  │  │  │  └─ LICENSE
   │     │  │  │  ├─ METADATA
   │     │  │  │  ├─ RECORD
   │     │  │  │  ├─ REQUESTED
   │     │  │  │  ├─ top_level.txt
   │     │  │  │  └─ WHEEL
   │     │  │  ├─ jaraco
   │     │  │  │  ├─ context
   │     │  │  │  │  ├─ py.typed
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ functools
   │     │  │  │  │  ├─ py.typed
   │     │  │  │  │  ├─ __init__.py
   │     │  │  │  │  └─ __init__.pyi
   │     │  │  │  └─ text
   │     │  │  │     ├─ layouts.py
   │     │  │  │     ├─ Lorem ipsum.txt
   │     │  │  │     ├─ show-newlines.py
   │     │  │  │     ├─ strip-prefix.py
   │     │  │  │     ├─ to-dvorak.py
   │     │  │  │     ├─ to-qwerty.py
   │     │  │  │     └─ __init__.py
   │     │  │  ├─ jaraco.text-4.0.0.dist-info
   │     │  │  │  ├─ INSTALLER
   │     │  │  │  ├─ LICENSE
   │     │  │  │  ├─ METADATA
   │     │  │  │  ├─ RECORD
   │     │  │  │  ├─ REQUESTED
   │     │  │  │  ├─ top_level.txt
   │     │  │  │  └─ WHEEL
   │     │  │  ├─ jaraco_context-6.1.0.dist-info
   │     │  │  │  ├─ INSTALLER
   │     │  │  │  ├─ licenses
   │     │  │  │  │  └─ LICENSE
   │     │  │  │  ├─ METADATA
   │     │  │  │  ├─ RECORD
   │     │  │  │  ├─ REQUESTED
   │     │  │  │  ├─ top_level.txt
   │     │  │  │  └─ WHEEL
   │     │  │  ├─ jaraco_functools-4.4.0.dist-info
   │     │  │  │  ├─ INSTALLER
   │     │  │  │  ├─ licenses
   │     │  │  │  │  └─ LICENSE
   │     │  │  │  ├─ METADATA
   │     │  │  │  ├─ RECORD
   │     │  │  │  ├─ REQUESTED
   │     │  │  │  ├─ top_level.txt
   │     │  │  │  └─ WHEEL
   │     │  │  ├─ more_itertools
   │     │  │  │  ├─ more.py
   │     │  │  │  ├─ more.pyi
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ recipes.py
   │     │  │  │  ├─ recipes.pyi
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __init__.pyi
   │     │  │  ├─ more_itertools-10.8.0.dist-info
   │     │  │  │  ├─ INSTALLER
   │     │  │  │  ├─ licenses
   │     │  │  │  │  └─ LICENSE
   │     │  │  │  ├─ METADATA
   │     │  │  │  ├─ RECORD
   │     │  │  │  ├─ REQUESTED
   │     │  │  │  └─ WHEEL
   │     │  │  ├─ packaging
   │     │  │  │  ├─ licenses
   │     │  │  │  │  ├─ _spdx.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ metadata.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ pylock.py
   │     │  │  │  ├─ requirements.py
   │     │  │  │  ├─ specifiers.py
   │     │  │  │  ├─ tags.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ _elffile.py
   │     │  │  │  ├─ _manylinux.py
   │     │  │  │  ├─ _musllinux.py
   │     │  │  │  ├─ _parser.py
   │     │  │  │  ├─ _structures.py
   │     │  │  │  ├─ _tokenizer.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ packaging-26.0.dist-info
   │     │  │  │  ├─ INSTALLER
   │     │  │  │  ├─ licenses
   │     │  │  │  │  ├─ LICENSE
   │     │  │  │  │  ├─ LICENSE.APACHE
   │     │  │  │  │  └─ LICENSE.BSD
   │     │  │  │  ├─ METADATA
   │     │  │  │  ├─ RECORD
   │     │  │  │  ├─ REQUESTED
   │     │  │  │  └─ WHEEL
   │     │  │  ├─ platformdirs
   │     │  │  │  ├─ android.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ macos.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ unix.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ windows.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ platformdirs-4.4.0.dist-info
   │     │  │  │  ├─ INSTALLER
   │     │  │  │  ├─ licenses
   │     │  │  │  │  └─ LICENSE
   │     │  │  │  ├─ METADATA
   │     │  │  │  ├─ RECORD
   │     │  │  │  ├─ REQUESTED
   │     │  │  │  └─ WHEEL
   │     │  │  ├─ tomli
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ _parser.py
   │     │  │  │  ├─ _re.py
   │     │  │  │  ├─ _types.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tomli-2.4.0.dist-info
   │     │  │  │  ├─ INSTALLER
   │     │  │  │  ├─ licenses
   │     │  │  │  │  └─ LICENSE
   │     │  │  │  ├─ METADATA
   │     │  │  │  ├─ RECORD
   │     │  │  │  ├─ REQUESTED
   │     │  │  │  └─ WHEEL
   │     │  │  ├─ wheel
   │     │  │  │  ├─ bdist_wheel.py
   │     │  │  │  ├─ macosx_libfile.py
   │     │  │  │  ├─ metadata.py
   │     │  │  │  ├─ wheelfile.py
   │     │  │  │  ├─ _bdist_wheel.py
   │     │  │  │  ├─ _commands
   │     │  │  │  │  ├─ convert.py
   │     │  │  │  │  ├─ pack.py
   │     │  │  │  │  ├─ tags.py
   │     │  │  │  │  ├─ unpack.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _metadata.py
   │     │  │  │  ├─ _setuptools_logging.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ wheel-0.46.3.dist-info
   │     │  │  │  ├─ entry_points.txt
   │     │  │  │  ├─ INSTALLER
   │     │  │  │  ├─ licenses
   │     │  │  │  │  └─ LICENSE.txt
   │     │  │  │  ├─ METADATA
   │     │  │  │  ├─ RECORD
   │     │  │  │  ├─ REQUESTED
   │     │  │  │  └─ WHEEL
   │     │  │  ├─ zipp
   │     │  │  │  ├─ compat
   │     │  │  │  │  ├─ overlay.py
   │     │  │  │  │  ├─ py310.py
   │     │  │  │  │  ├─ py313.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ glob.py
   │     │  │  │  ├─ _functools.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ zipp-3.23.0.dist-info
   │     │  │     ├─ INSTALLER
   │     │  │     ├─ licenses
   │     │  │     │  └─ LICENSE
   │     │  │     ├─ METADATA
   │     │  │     ├─ RECORD
   │     │  │     ├─ REQUESTED
   │     │  │     ├─ top_level.txt
   │     │  │     └─ WHEEL
   │     │  └─ __init__.py
   │     ├─ setuptools-84.0.0.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ six-1.17.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ six.py
   │     ├─ sklearn
   │     │  ├─ .libs
   │     │  │  ├─ msvcp140.dll
   │     │  │  └─ vcomp140.dll
   │     │  ├─ base.py
   │     │  ├─ calibration.py
   │     │  ├─ cluster
   │     │  │  ├─ tests
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ test_affinity_propagation.py
   │     │  │  │  ├─ test_bicluster.py
   │     │  │  │  ├─ test_birch.py
   │     │  │  │  ├─ test_bisect_k_means.py
   │     │  │  │  ├─ test_dbscan.py
   │     │  │  │  ├─ test_feature_agglomeration.py
   │     │  │  │  ├─ test_hdbscan.py
   │     │  │  │  ├─ test_hierarchical.py
   │     │  │  │  ├─ test_k_means.py
   │     │  │  │  ├─ test_mean_shift.py
   │     │  │  │  ├─ test_optics.py
   │     │  │  │  ├─ test_spectral.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _affinity_propagation.py
   │     │  │  ├─ _agglomerative.py
   │     │  │  ├─ _bicluster.py
   │     │  │  ├─ _birch.py
   │     │  │  ├─ _bisect_k_means.py
   │     │  │  ├─ _dbscan.py
   │     │  │  ├─ _dbscan_inner.cp310-win_amd64.lib
   │     │  │  ├─ _dbscan_inner.pyx
   │     │  │  ├─ _feature_agglomeration.py
   │     │  │  ├─ _hdbscan
   │     │  │  │  ├─ hdbscan.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_reachibility.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _linkage.cp310-win_amd64.lib
   │     │  │  │  ├─ _linkage.pyx
   │     │  │  │  ├─ _reachability.cp310-win_amd64.lib
   │     │  │  │  ├─ _reachability.pyx
   │     │  │  │  ├─ _tree.cp310-win_amd64.lib
   │     │  │  │  ├─ _tree.pxd
   │     │  │  │  ├─ _tree.pyx
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _hierarchical_fast.cp310-win_amd64.lib
   │     │  │  ├─ _hierarchical_fast.pxd
   │     │  │  ├─ _hierarchical_fast.pyx
   │     │  │  ├─ _kmeans.py
   │     │  │  ├─ _k_means_common.cp310-win_amd64.lib
   │     │  │  ├─ _k_means_common.pxd
   │     │  │  ├─ _k_means_common.pyx
   │     │  │  ├─ _k_means_elkan.cp310-win_amd64.lib
   │     │  │  ├─ _k_means_elkan.pyx
   │     │  │  ├─ _k_means_lloyd.cp310-win_amd64.lib
   │     │  │  ├─ _k_means_lloyd.pyx
   │     │  │  ├─ _k_means_minibatch.cp310-win_amd64.lib
   │     │  │  ├─ _k_means_minibatch.pyx
   │     │  │  ├─ _mean_shift.py
   │     │  │  ├─ _optics.py
   │     │  │  ├─ _spectral.py
   │     │  │  └─ __init__.py
   │     │  ├─ compose
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_column_transformer.py
   │     │  │  │  ├─ test_target.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _column_transformer.py
   │     │  │  ├─ _target.py
   │     │  │  └─ __init__.py
   │     │  ├─ conftest.py
   │     │  ├─ covariance
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_covariance.py
   │     │  │  │  ├─ test_elliptic_envelope.py
   │     │  │  │  ├─ test_graphical_lasso.py
   │     │  │  │  ├─ test_robust_covariance.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _elliptic_envelope.py
   │     │  │  ├─ _empirical_covariance.py
   │     │  │  ├─ _graph_lasso.py
   │     │  │  ├─ _robust_covariance.py
   │     │  │  ├─ _shrunk_covariance.py
   │     │  │  └─ __init__.py
   │     │  ├─ cross_decomposition
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_pls.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _pls.py
   │     │  │  └─ __init__.py
   │     │  ├─ datasets
   │     │  │  ├─ data
   │     │  │  │  ├─ breast_cancer.csv
   │     │  │  │  ├─ diabetes_data_raw.csv.gz
   │     │  │  │  ├─ diabetes_target.csv.gz
   │     │  │  │  ├─ digits.csv.gz
   │     │  │  │  ├─ iris.csv
   │     │  │  │  ├─ linnerud_exercise.csv
   │     │  │  │  ├─ linnerud_physiological.csv
   │     │  │  │  ├─ wine_data.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ descr
   │     │  │  │  ├─ breast_cancer.rst
   │     │  │  │  ├─ california_housing.rst
   │     │  │  │  ├─ covtype.rst
   │     │  │  │  ├─ diabetes.rst
   │     │  │  │  ├─ digits.rst
   │     │  │  │  ├─ iris.rst
   │     │  │  │  ├─ kddcup99.rst
   │     │  │  │  ├─ lfw.rst
   │     │  │  │  ├─ linnerud.rst
   │     │  │  │  ├─ olivetti_faces.rst
   │     │  │  │  ├─ rcv1.rst
   │     │  │  │  ├─ species_distributions.rst
   │     │  │  │  ├─ twenty_newsgroups.rst
   │     │  │  │  ├─ wine_data.rst
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ images
   │     │  │  │  ├─ china.jpg
   │     │  │  │  ├─ flower.jpg
   │     │  │  │  ├─ README.txt
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ openml
   │     │  │  │  │  │  ├─ id_1
   │     │  │  │  │  │  │  ├─ api-v1-jd-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-1.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-1.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_1119
   │     │  │  │  │  │  │  ├─ api-v1-jd-1119.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-1119.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-adult-census-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-adult-census-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-1119.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-54002.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_1590
   │     │  │  │  │  │  │  ├─ api-v1-jd-1590.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-1590.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-1590.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-1595261.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_2
   │     │  │  │  │  │  │  ├─ api-v1-jd-2.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-2.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-anneal-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-anneal-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-2.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-1666876.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_292
   │     │  │  │  │  │  │  ├─ api-v1-jd-292.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jd-40981.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-292.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-40981.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-dv-1-s-dact.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-49822.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_3
   │     │  │  │  │  │  │  ├─ api-v1-jd-3.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-3.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-3.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-3.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_40589
   │     │  │  │  │  │  │  ├─ api-v1-jd-40589.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-40589.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-emotions-l-2-dv-3.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-emotions-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-40589.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-4644182.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_40675
   │     │  │  │  │  │  │  ├─ api-v1-jd-40675.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-40675.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-dv-1-s-dact.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-40675.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-4965250.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_40945
   │     │  │  │  │  │  │  ├─ api-v1-jd-40945.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-40945.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-40945.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-16826755.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_40966
   │     │  │  │  │  │  │  ├─ api-v1-jd-40966.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-40966.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-miceprotein-l-2-dv-4.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-miceprotein-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-40966.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-17928620.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_42074
   │     │  │  │  │  │  │  ├─ api-v1-jd-42074.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-42074.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-42074.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-21552912.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_42585
   │     │  │  │  │  │  │  ├─ api-v1-jd-42585.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-42585.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-42585.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-21854866.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_561
   │     │  │  │  │  │  │  ├─ api-v1-jd-561.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-561.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-cpu-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-cpu-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-561.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-52739.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_61
   │     │  │  │  │  │  │  ├─ api-v1-jd-61.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-61.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-iris-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-iris-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-61.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-61.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_62
   │     │  │  │  │  │  │  ├─ api-v1-jd-62.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-62.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-62.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-52352.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ svmlight_classification.txt
   │     │  │  │  │  ├─ svmlight_invalid.txt
   │     │  │  │  │  ├─ svmlight_invalid_order.txt
   │     │  │  │  │  ├─ svmlight_multilabel.txt
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_20news.py
   │     │  │  │  ├─ test_arff_parser.py
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_california_housing.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_covtype.py
   │     │  │  │  ├─ test_kddcup99.py
   │     │  │  │  ├─ test_lfw.py
   │     │  │  │  ├─ test_olivetti_faces.py
   │     │  │  │  ├─ test_openml.py
   │     │  │  │  ├─ test_rcv1.py
   │     │  │  │  ├─ test_samples_generator.py
   │     │  │  │  ├─ test_svmlight_format.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _arff_parser.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _california_housing.py
   │     │  │  ├─ _covtype.py
   │     │  │  ├─ _kddcup99.py
   │     │  │  ├─ _lfw.py
   │     │  │  ├─ _olivetti_faces.py
   │     │  │  ├─ _openml.py
   │     │  │  ├─ _rcv1.py
   │     │  │  ├─ _samples_generator.py
   │     │  │  ├─ _species_distributions.py
   │     │  │  ├─ _svmlight_format_fast.cp310-win_amd64.lib
   │     │  │  ├─ _svmlight_format_fast.pyx
   │     │  │  ├─ _svmlight_format_io.py
   │     │  │  ├─ _twenty_newsgroups.py
   │     │  │  └─ __init__.py
   │     │  ├─ decomposition
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_dict_learning.py
   │     │  │  │  ├─ test_factor_analysis.py
   │     │  │  │  ├─ test_fastica.py
   │     │  │  │  ├─ test_incremental_pca.py
   │     │  │  │  ├─ test_kernel_pca.py
   │     │  │  │  ├─ test_nmf.py
   │     │  │  │  ├─ test_online_lda.py
   │     │  │  │  ├─ test_pca.py
   │     │  │  │  ├─ test_sparse_pca.py
   │     │  │  │  ├─ test_truncated_svd.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _cdnmf_fast.cp310-win_amd64.lib
   │     │  │  ├─ _cdnmf_fast.pyx
   │     │  │  ├─ _dict_learning.py
   │     │  │  ├─ _factor_analysis.py
   │     │  │  ├─ _fastica.py
   │     │  │  ├─ _incremental_pca.py
   │     │  │  ├─ _kernel_pca.py
   │     │  │  ├─ _lda.py
   │     │  │  ├─ _nmf.py
   │     │  │  ├─ _online_lda_fast.cp310-win_amd64.lib
   │     │  │  ├─ _online_lda_fast.pyx
   │     │  │  ├─ _pca.py
   │     │  │  ├─ _sparse_pca.py
   │     │  │  ├─ _truncated_svd.py
   │     │  │  └─ __init__.py
   │     │  ├─ discriminant_analysis.py
   │     │  ├─ dummy.py
   │     │  └─ ensemble
   │     │     ├─ tests
   │     │     │  ├─ test_bagging.py
   │     │     │  ├─ test_base.py
   │     │     │  ├─ test_common.py
   │     │     │  ├─ test_forest.py
   │     │     │  ├─ test_gradient_boosting.py
   │     │     │  ├─ test_iforest.py
   │     │     │  ├─ test_stacking.py
   │     │     │  ├─ test_voting.py
   │     │     │  ├─ test_weight_boosting.py
   │     │     │  └─ __init__.py
   │     │     ├─ _bagging.py
   │     │     ├─ _base.py
   │     │     ├─ _forest.py
   │     │     ├─ _gb.py
   │     │     ├─ _gradient_boosting.cp310-win_amd64.lib
   │     │     ├─ _gradient_boosting.pyx
   │     │     └─ _hist_gradient_boosting
   │     │        ├─ .tmpp0Y88C
   │     │        ├─ binning.py
   │     │        ├─ common.cp310-win_amd64.lib
   │     │        ├─ common.pxd
   │     │        ├─ common.pyx
   │     │        ├─ gradient_boosting.py
   │     │        ├─ grower.py
   │     │        ├─ histogram.cp310-win_amd64.lib
   │     │        ├─ histogram.pyx
   │     │        └─ predictor.py
   │     ├─ sparsediffpy
   │     │  ├─ _bindings
   │     │  │  ├─ atoms
   │     │  │  │  ├─ add.h
   │     │  │  │  ├─ asinh.h
   │     │  │  │  ├─ atanh.h
   │     │  │  │  ├─ broadcast.h
   │     │  │  │  ├─ common.h
   │     │  │  │  ├─ convolve.h
   │     │  │  │  ├─ cos.h
   │     │  │  │  ├─ diag_mat.h
   │     │  │  │  ├─ diag_vec.h
   │     │  │  │  ├─ entr.h
   │     │  │  │  ├─ exp.h
   │     │  │  │  ├─ getters.h
   │     │  │  │  ├─ hstack.h
   │     │  │  │  ├─ index.h
   │     │  │  │  ├─ left_matmul.h
   │     │  │  │  ├─ linear.h
   │     │  │  │  ├─ log.h
   │     │  │  │  ├─ logistic.h
   │     │  │  │  ├─ matmul.h
   │     │  │  │  ├─ multiply.h
   │     │  │  │  ├─ neg.h
   │     │  │  │  ├─ normal_cdf.h
   │     │  │  │  ├─ parameter.h
   │     │  │  │  ├─ power.h
   │     │  │  │  ├─ prod.h
   │     │  │  │  ├─ prod_axis_one.h
   │     │  │  │  ├─ prod_axis_zero.h
   │     │  │  │  ├─ promote.h
   │     │  │  │  ├─ quad_form.h
   │     │  │  │  ├─ quad_over_lin.h
   │     │  │  │  ├─ rel_entr.h
   │     │  │  │  ├─ reshape.h
   │     │  │  │  ├─ right_matmul.h
   │     │  │  │  ├─ scalar_mult.h
   │     │  │  │  ├─ sin.h
   │     │  │  │  ├─ sinh.h
   │     │  │  │  ├─ sum.h
   │     │  │  │  ├─ tan.h
   │     │  │  │  ├─ tanh.h
   │     │  │  │  ├─ trace.h
   │     │  │  │  ├─ transpose.h
   │     │  │  │  ├─ upper_tri.h
   │     │  │  │  ├─ variable.h
   │     │  │  │  ├─ vector_mult.h
   │     │  │  │  ├─ vstack.h
   │     │  │  │  └─ xexp.h
   │     │  │  ├─ bindings.c
   │     │  │  └─ problem
   │     │  │     ├─ common.h
   │     │  │     ├─ constraint_forward.h
   │     │  │     ├─ gradient.h
   │     │  │     ├─ hessian.h
   │     │  │     ├─ init_derivatives.h
   │     │  │     ├─ init_hessian.h
   │     │  │     ├─ init_jacobian.h
   │     │  │     ├─ jacobian.h
   │     │  │     ├─ make_problem.h
   │     │  │     ├─ objective_forward.h
   │     │  │     ├─ register_params.h
   │     │  │     └─ update_params.h
   │     │  └─ __init__.py
   │     ├─ sparsediffpy-0.3.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ statsmodels
   │     │  ├─ api.py
   │     │  ├─ base
   │     │  │  ├─ covtype.py
   │     │  │  ├─ data.py
   │     │  │  ├─ distributed_estimation.py
   │     │  │  ├─ elastic_net.py
   │     │  │  ├─ l1_cvxopt.py
   │     │  │  ├─ l1_slsqp.py
   │     │  │  ├─ l1_solvers_common.py
   │     │  │  ├─ model.py
   │     │  │  ├─ optimizer.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_data.py
   │     │  │  │  ├─ test_distributed_estimation.py
   │     │  │  │  ├─ test_generic_methods.py
   │     │  │  │  ├─ test_optimize.py
   │     │  │  │  ├─ test_penalized.py
   │     │  │  │  ├─ test_penalties.py
   │     │  │  │  ├─ test_predict.py
   │     │  │  │  ├─ test_screening.py
   │     │  │  │  ├─ test_shrink_pickle.py
   │     │  │  │  ├─ test_transform.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ transform.py
   │     │  │  ├─ wrapper.py
   │     │  │  ├─ _constraints.py
   │     │  │  ├─ _parameter_inference.py
   │     │  │  ├─ _penalized.py
   │     │  │  ├─ _penalties.py
   │     │  │  ├─ _prediction_inference.py
   │     │  │  ├─ _screening.py
   │     │  │  └─ __init__.py
   │     │  ├─ compat
   │     │  │  ├─ numpy.py
   │     │  │  ├─ pandas.py
   │     │  │  ├─ patsy.py
   │     │  │  ├─ platform.py
   │     │  │  ├─ pytest.py
   │     │  │  ├─ python.py
   │     │  │  ├─ scipy.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_itercompat.py
   │     │  │  │  ├─ test_pandas.py
   │     │  │  │  ├─ test_scipy_compat.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _scipy_multivariate_t.py
   │     │  │  └─ __init__.py
   │     │  ├─ conftest.py
   │     │  ├─ datasets
   │     │  │  ├─ anes96
   │     │  │  │  ├─ anes96.csv
   │     │  │  │  ├─ data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cancer
   │     │  │  │  ├─ cancer.csv
   │     │  │  │  ├─ data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ccard
   │     │  │  │  ├─ ccard.csv
   │     │  │  │  ├─ data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ china_smoking
   │     │  │  │  ├─ china_smoking.csv
   │     │  │  │  ├─ data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ co2
   │     │  │  │  ├─ co2.csv
   │     │  │  │  ├─ data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ committee
   │     │  │  │  ├─ committee.csv
   │     │  │  │  ├─ data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ copper
   │     │  │  │  ├─ copper.csv
   │     │  │  │  ├─ data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cpunish
   │     │  │  │  ├─ cpunish.csv
   │     │  │  │  ├─ data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ danish_data
   │     │  │  │  ├─ data.csv
   │     │  │  │  ├─ data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ elec_equip
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ elec_equip.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ elnino
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ elnino.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ engel
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ engel.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ fair
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ fair.csv
   │     │  │  │  ├─ fair_pt.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ fertility
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ fertility.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ grunfeld
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ grunfeld.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ heart
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ heart.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ interest_inflation
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ E6.csv
   │     │  │  │  ├─ E6_jmulti.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ longley
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ longley.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ macrodata
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ macrodata.csv
   │     │  │  │  ├─ macrodata.dta
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ modechoice
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ modechoice.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ nile
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ nile.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ randhie
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ randhie.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ scotland
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ scotvote.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ spector
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ spector.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ stackloss
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ stackloss.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ star98
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ star98.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ statecrime
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ statecrime.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ strikes
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ strikes.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sunspots
   │     │  │  │  ├─ data.py
   │     │  │  │  ├─ sunspots.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ template_data.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_data.py
   │     │  │  │  ├─ test_utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ discrete
   │     │  │  ├─ conditional_models.py
   │     │  │  ├─ count_model.py
   │     │  │  ├─ diagnostic.py
   │     │  │  ├─ discrete_margins.py
   │     │  │  ├─ discrete_model.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ mnlogit_resid.csv
   │     │  │  │  │  ├─ mn_logit_summary.txt
   │     │  │  │  │  ├─ nbinom_resids.csv
   │     │  │  │  │  ├─ phat_mnlogit.csv
   │     │  │  │  │  ├─ poisson_resid.csv
   │     │  │  │  │  ├─ predict_prob_poisson.csv
   │     │  │  │  │  ├─ results_count_margins.py
   │     │  │  │  │  ├─ results_count_robust_cluster.py
   │     │  │  │  │  ├─ results_discrete.py
   │     │  │  │  │  ├─ results_glm_logit_constrained.py
   │     │  │  │  │  ├─ results_poisson_constrained.py
   │     │  │  │  │  ├─ results_predict.py
   │     │  │  │  │  ├─ results_truncated.py
   │     │  │  │  │  ├─ results_truncated_st.py
   │     │  │  │  │  ├─ ships.csv
   │     │  │  │  │  ├─ sm3533.csv
   │     │  │  │  │  ├─ yhat_mnlogit.csv
   │     │  │  │  │  ├─ yhat_poisson.csv
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_conditional.py
   │     │  │  │  ├─ test_constrained.py
   │     │  │  │  ├─ test_count_model.py
   │     │  │  │  ├─ test_diagnostic.py
   │     │  │  │  ├─ test_discrete.py
   │     │  │  │  ├─ test_margins.py
   │     │  │  │  ├─ test_predict.py
   │     │  │  │  ├─ test_sandwich_cov.py
   │     │  │  │  ├─ test_truncated_model.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ truncated_model.py
   │     │  │  ├─ _diagnostics_count.py
   │     │  │  └─ __init__.py
   │     │  ├─ distributions
   │     │  │  ├─ bernstein.py
   │     │  │  ├─ copula
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ archimedean.py
   │     │  │  │  ├─ copulas.py
   │     │  │  │  ├─ depfunc_ev.py
   │     │  │  │  ├─ elliptical.py
   │     │  │  │  ├─ extreme_value.py
   │     │  │  │  ├─ other_copulas.py
   │     │  │  │  ├─ transforms.py
   │     │  │  │  ├─ _special.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ discrete.py
   │     │  │  ├─ edgeworth.py
   │     │  │  ├─ empirical_distribution.py
   │     │  │  ├─ mixture_rvs.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_bernstein.py
   │     │  │  │  ├─ test_discrete.py
   │     │  │  │  ├─ test_ecdf.py
   │     │  │  │  ├─ test_edgeworth.py
   │     │  │  │  ├─ test_mixture.py
   │     │  │  │  ├─ test_tools.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tools.py
   │     │  │  └─ __init__.py
   │     │  ├─ duration
   │     │  │  ├─ api.py
   │     │  │  ├─ hazard_regression.py
   │     │  │  ├─ survfunc.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ bmt.csv
   │     │  │  │  │  ├─ bmt_results.csv
   │     │  │  │  │  ├─ phreg_gentests.py
   │     │  │  │  │  ├─ survival_data_1000_10.csv
   │     │  │  │  │  ├─ survival_data_100_5.csv
   │     │  │  │  │  ├─ survival_data_20_1.csv
   │     │  │  │  │  ├─ survival_data_50_1.csv
   │     │  │  │  │  ├─ survival_data_50_2.csv
   │     │  │  │  │  ├─ survival_enet_r_results.py
   │     │  │  │  │  ├─ survival_r_results.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_phreg.py
   │     │  │  │  ├─ test_survfunc.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _kernel_estimates.py
   │     │  │  └─ __init__.py
   │     │  ├─ emplike
   │     │  │  ├─ aft_el.py
   │     │  │  ├─ api.py
   │     │  │  ├─ descriptive.py
   │     │  │  ├─ elanova.py
   │     │  │  ├─ elregress.py
   │     │  │  ├─ originregress.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ el_results.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_aft.py
   │     │  │  │  ├─ test_anova.py
   │     │  │  │  ├─ test_descriptive.py
   │     │  │  │  ├─ test_origin.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ formula
   │     │  │  ├─ api.py
   │     │  │  ├─ formulatools.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_formula.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ gam
   │     │  │  ├─ api.py
   │     │  │  ├─ gam_cross_validation
   │     │  │  │  ├─ cross_validators.py
   │     │  │  │  ├─ gam_cross_validation.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ gam_penalties.py
   │     │  │  ├─ generalized_additive_model.py
   │     │  │  ├─ smooth_basis.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ autos.csv
   │     │  │  │  │  ├─ autos_exog.csv
   │     │  │  │  │  ├─ autos_predict.csv
   │     │  │  │  │  ├─ cubic_cyclic_splines_from_mgcv.csv
   │     │  │  │  │  ├─ gam_PIRLS_results.csv
   │     │  │  │  │  ├─ logit_gam_mgcv.csv
   │     │  │  │  │  ├─ motorcycle.csv
   │     │  │  │  │  ├─ prediction_from_mgcv.csv
   │     │  │  │  │  ├─ results_mpg_bs.py
   │     │  │  │  │  ├─ results_mpg_bs_poisson.py
   │     │  │  │  │  ├─ results_pls.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_gam.py
   │     │  │  │  ├─ test_penalized.py
   │     │  │  │  ├─ test_smooth_basis.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ genmod
   │     │  │  ├─ api.py
   │     │  │  ├─ bayes_mixed_glm.py
   │     │  │  ├─ cov_struct.py
   │     │  │  ├─ families
   │     │  │  │  ├─ family.py
   │     │  │  │  ├─ links.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_family.py
   │     │  │  │  │  ├─ test_link.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ varfuncs.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ generalized_estimating_equations.py
   │     │  │  ├─ generalized_linear_model.py
   │     │  │  ├─ qif.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ .tmpiy2xWs
   │     │  │  │  ├─ gee_categorical_simulation_check.py
   │     │  │  │  ├─ gee_gaussian_simulation_check.py
   │     │  │  │  ├─ gee_poisson_simulation_check.py
   │     │  │  │  ├─ gee_simulation_check.py
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ elastic_net_generate_tests.py
   │     │  │  │  │  ├─ enet_binomial.csv
   │     │  │  │  │  ├─ enet_poisson.csv
   │     │  │  │  │  ├─ epil.csv
   │     │  │  │  │  ├─ gee_generate_tests.py
   │     │  │  │  │  ├─ gee_linear_1.csv
   │     │  │  │  │  ├─ gee_logistic_1.csv
   │     │  │  │  │  ├─ gee_nested_linear_1.csv
   │     │  │  │  │  ├─ gee_nominal_1.csv
   │     │  │  │  │  ├─ gee_ordinal_1.csv
   │     │  │  │  │  ├─ gee_poisson_1.csv
   │     │  │  │  │  ├─ glmnet_r_results.py
   │     │  │  │  │  ├─ glm_test_resids.py
   │     │  │  │  │  ├─ igaussident_resids.csv
   │     │  │  │  │  ├─ inv_gaussian.csv
   │     │  │  │  │  ├─ iris.csv
   │     │  │  │  │  ├─ medparlogresids.csv
   │     │  │  │  │  ├─ results_glm.py
   │     │  │  │  │  ├─ results_glm_poisson_weights.py
   │     │  │  │  │  ├─ results_tweedie_aweights_nonrobust.csv
   │     │  │  │  │  ├─ res_R_var_weight.py
   │     │  │  │  │  ├─ stata_cancer_glm.csv
   │     │  │  │  │  ├─ stata_lbw_glm.csv
   │     │  │  │  │  ├─ stata_medpar1_glm.csv
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_bayes_mixed_glm.py
   │     │  │  │  ├─ test_constrained.py
   │     │  │  │  ├─ test_gee.py
   │     │  │  │  ├─ test_gee_glm.py
   │     │  │  │  ├─ test_glm.py
   │     │  │  │  ├─ test_glm_weights.py
   │     │  │  │  ├─ test_qif.py
   │     │  │  │  ├─ test_score_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _tweedie_compound_poisson.py
   │     │  │  └─ __init__.py
   │     │  ├─ graphics
   │     │  │  ├─ agreement.py
   │     │  │  ├─ api.py
   │     │  │  ├─ boxplots.py
   │     │  │  ├─ correlation.py
   │     │  │  ├─ dotplots.py
   │     │  │  ├─ factorplots.py
   │     │  │  ├─ functional.py
   │     │  │  ├─ gofplots.py
   │     │  │  ├─ mosaicplot.py
   │     │  │  ├─ plottools.py
   │     │  │  ├─ plot_grids.py
   │     │  │  ├─ regressionplots.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_agreement.py
   │     │  │  │  ├─ test_boxplots.py
   │     │  │  │  ├─ test_correlation.py
   │     │  │  │  ├─ test_dotplot.py
   │     │  │  │  ├─ test_factorplots.py
   │     │  │  │  ├─ test_functional.py
   │     │  │  │  ├─ test_gofplots.py
   │     │  │  │  ├─ test_mosaicplot.py
   │     │  │  │  ├─ test_regressionplots.py
   │     │  │  │  ├─ test_tsaplots.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tsaplots.py
   │     │  │  ├─ tukeyplot.py
   │     │  │  ├─ utils.py
   │     │  │  ├─ _regressionplots_doc.py
   │     │  │  └─ __init__.py
   │     │  ├─ imputation
   │     │  │  ├─ bayes_mi.py
   │     │  │  ├─ mice.py
   │     │  │  ├─ ros.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_bayes_mi.py
   │     │  │  │  ├─ test_mice.py
   │     │  │  │  ├─ test_ros.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ interface
   │     │  │  └─ __init__.py
   │     │  ├─ iolib
   │     │  │  ├─ api.py
   │     │  │  ├─ foreign.py
   │     │  │  ├─ openfile.py
   │     │  │  ├─ smpickle.py
   │     │  │  ├─ stata_summary_examples.py
   │     │  │  ├─ summary.py
   │     │  │  ├─ summary2.py
   │     │  │  ├─ table.py
   │     │  │  ├─ tableformatting.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ data_missing.dta
   │     │  │  │  │  ├─ macrodata.py
   │     │  │  │  │  ├─ time_series_examples.dta
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_pickle.py
   │     │  │  │  ├─ test_summary.py
   │     │  │  │  ├─ test_summary2.py
   │     │  │  │  ├─ test_summary_old.py
   │     │  │  │  ├─ test_table.py
   │     │  │  │  ├─ test_table_econpy.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ LICENSE.txt
   │     │  ├─ miscmodels
   │     │  │  ├─ api.py
   │     │  │  ├─ count.py
   │     │  │  ├─ nonlinls.py
   │     │  │  ├─ ordinal_model.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ ologit_ucla.csv
   │     │  │  │  │  ├─ results_ordinal_model.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ results_tmodel.py
   │     │  │  │  ├─ test_generic_mle.py
   │     │  │  │  ├─ test_ordinal_model.py
   │     │  │  │  ├─ test_poisson.py
   │     │  │  │  ├─ test_tmodel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tmodel.py
   │     │  │  ├─ try_mlecov.py
   │     │  │  └─ __init__.py
   │     │  ├─ multivariate
   │     │  │  ├─ api.py
   │     │  │  ├─ cancorr.py
   │     │  │  ├─ factor.py
   │     │  │  ├─ factor_rotation
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_rotation.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _analytic_rotation.py
   │     │  │  │  ├─ _gpa_rotation.py
   │     │  │  │  ├─ _wrappers.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ manova.py
   │     │  │  ├─ multivariate_ols.py
   │     │  │  ├─ pca.py
   │     │  │  ├─ plots.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ datamlw.py
   │     │  │  │  │  ├─ factors_stata.csv
   │     │  │  │  │  ├─ factor_data.csv
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_cancorr.py
   │     │  │  │  ├─ test_factor.py
   │     │  │  │  ├─ test_manova.py
   │     │  │  │  ├─ test_ml_factor.py
   │     │  │  │  ├─ test_multivariate_ols.py
   │     │  │  │  ├─ test_pca.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ nonparametric
   │     │  │  ├─ api.py
   │     │  │  ├─ bandwidths.py
   │     │  │  ├─ kde.py
   │     │  │  ├─ kdetools.py
   │     │  │  ├─ kernels.py
   │     │  │  ├─ kernels_asymmetric.py
   │     │  │  ├─ kernel_density.py
   │     │  │  ├─ kernel_regression.py
   │     │  │  ├─ smoothers_lowess.py
   │     │  │  ├─ smoothers_lowess_old.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ results_kcde.csv
   │     │  │  │  │  ├─ results_kde.csv
   │     │  │  │  │  ├─ results_kde_fft.csv
   │     │  │  │  │  ├─ results_kde_univ_weights.csv
   │     │  │  │  │  ├─ results_kde_weights.csv
   │     │  │  │  │  ├─ results_kernel_regression.csv
   │     │  │  │  │  ├─ test_lowess_delta.csv
   │     │  │  │  │  ├─ test_lowess_frac.csv
   │     │  │  │  │  ├─ test_lowess_iter.csv
   │     │  │  │  │  ├─ test_lowess_simple.csv
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_asymmetric.py
   │     │  │  │  ├─ test_bandwidths.py
   │     │  │  │  ├─ test_kde.py
   │     │  │  │  ├─ test_kernels.py
   │     │  │  │  ├─ test_kernel_density.py
   │     │  │  │  ├─ test_kernel_regression.py
   │     │  │  │  ├─ test_lowess.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _kernel_base.py
   │     │  │  └─ __init__.py
   │     │  ├─ othermod
   │     │  │  ├─ api.py
   │     │  │  ├─ betareg.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ foodexpenditure.csv
   │     │  │  │  │  ├─ methylation-test.csv
   │     │  │  │  │  ├─ resid_methylation.csv
   │     │  │  │  │  ├─ results_betareg.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_beta.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ regression
   │     │  │  ├─ dimred.py
   │     │  │  ├─ feasible_gls.py
   │     │  │  ├─ linear_model.py
   │     │  │  ├─ mixed_linear_model.py
   │     │  │  ├─ process_regression.py
   │     │  │  ├─ quantile_regression.py
   │     │  │  ├─ recursive_ls.py
   │     │  │  ├─ rolling.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ dietox.csv
   │     │  │  │  │  ├─ generate_lasso.py
   │     │  │  │  │  ├─ generate_lme.py
   │     │  │  │  │  ├─ glmnet_r_results.py
   │     │  │  │  │  ├─ lasso_data.csv
   │     │  │  │  │  ├─ leverage_influence_ols_nostars.txt
   │     │  │  │  │  ├─ lme00.csv
   │     │  │  │  │  ├─ lme01.csv
   │     │  │  │  │  ├─ lme02.csv
   │     │  │  │  │  ├─ lme03.csv
   │     │  │  │  │  ├─ lme04.csv
   │     │  │  │  │  ├─ lme05.csv
   │     │  │  │  │  ├─ lme06.csv
   │     │  │  │  │  ├─ lme07.csv
   │     │  │  │  │  ├─ lme08.csv
   │     │  │  │  │  ├─ lme09.csv
   │     │  │  │  │  ├─ lme10.csv
   │     │  │  │  │  ├─ lme11.csv
   │     │  │  │  │  ├─ lme_r_results.py
   │     │  │  │  │  ├─ macro_gr_corc_stata.py
   │     │  │  │  │  ├─ pastes.csv
   │     │  │  │  │  ├─ results_grunfeld_ols_robust_cluster.py
   │     │  │  │  │  ├─ results_macro_ols_robust.py
   │     │  │  │  │  ├─ results_quantile_regression.py
   │     │  │  │  │  ├─ results_regression.py
   │     │  │  │  │  ├─ results_rls_R.csv
   │     │  │  │  │  ├─ results_rls_stata.csv
   │     │  │  │  │  ├─ results_theil_textile.py
   │     │  │  │  │  ├─ theil_textile_predict.csv
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_cov.py
   │     │  │  │  ├─ test_dimred.py
   │     │  │  │  ├─ test_glsar_gretl.py
   │     │  │  │  ├─ test_glsar_stata.py
   │     │  │  │  ├─ test_lme.py
   │     │  │  │  ├─ test_predict.py
   │     │  │  │  ├─ test_processreg.py
   │     │  │  │  ├─ test_quantile_regression.py
   │     │  │  │  ├─ test_recursive_ls.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_robustcov.py
   │     │  │  │  ├─ test_rolling.py
   │     │  │  │  ├─ test_theil.py
   │     │  │  │  ├─ test_tools.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _prediction.py
   │     │  │  ├─ _tools.py
   │     │  │  └─ __init__.py
   │     │  ├─ robust
   │     │  │  ├─ norms.py
   │     │  │  ├─ robust_linear_model.py
   │     │  │  ├─ scale.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ results_norms.py
   │     │  │  │  │  ├─ results_rlm.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_mquantiles.py
   │     │  │  │  ├─ test_norms.py
   │     │  │  │  ├─ test_rlm.py
   │     │  │  │  ├─ test_scale.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ sandbox
   │     │  │  ├─ archive
   │     │  │  │  ├─ linalg_covmat.py
   │     │  │  │  ├─ linalg_decomp_1.py
   │     │  │  │  ├─ tsa.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ bspline.py
   │     │  │  ├─ datarich
   │     │  │  │  ├─ factormodels.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ descstats.py
   │     │  │  ├─ distributions
   │     │  │  │  ├─ estimators.py
   │     │  │  │  ├─ examples
   │     │  │  │  │  ├─ ex_extras.py
   │     │  │  │  │  ├─ ex_fitfr.py
   │     │  │  │  │  ├─ ex_gof.py
   │     │  │  │  │  ├─ ex_mvelliptical.py
   │     │  │  │  │  ├─ ex_transf2.py
   │     │  │  │  │  ├─ matchdist.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ extras.py
   │     │  │  │  ├─ genpareto.py
   │     │  │  │  ├─ gof_new.py
   │     │  │  │  ├─ multivariate.py
   │     │  │  │  ├─ mv_measures.py
   │     │  │  │  ├─ mv_normal.py
   │     │  │  │  ├─ otherdist.py
   │     │  │  │  ├─ quantize.py
   │     │  │  │  ├─ sppatch.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ check_moments.py
   │     │  │  │  │  ├─ distparams.py
   │     │  │  │  │  ├─ test_extras.py
   │     │  │  │  │  ├─ test_gof_new.py
   │     │  │  │  │  ├─ test_multivariate.py
   │     │  │  │  │  ├─ test_norm_expan.py
   │     │  │  │  │  ├─ test_transf.py
   │     │  │  │  │  ├─ _est_fit.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ transformed.py
   │     │  │  │  ├─ transform_functions.py
   │     │  │  │  ├─ try_max.py
   │     │  │  │  ├─ try_pot.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ gam.py
   │     │  │  ├─ infotheo.py
   │     │  │  ├─ mcevaluate
   │     │  │  │  ├─ arma.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mle.py
   │     │  │  ├─ multilinear.py
   │     │  │  ├─ nonparametric
   │     │  │  │  ├─ densityorthopoly.py
   │     │  │  │  ├─ dgp_examples.py
   │     │  │  │  ├─ kde2.py
   │     │  │  │  ├─ kdecovclass.py
   │     │  │  │  ├─ kernels.py
   │     │  │  │  ├─ kernel_extras.py
   │     │  │  │  ├─ smoothers.py
   │     │  │  │  ├─ testdata.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ ex_gam_am_new.py
   │     │  │  │  │  ├─ ex_gam_new.py
   │     │  │  │  │  ├─ ex_smoothers.py
   │     │  │  │  │  ├─ test_kernel_extras.py
   │     │  │  │  │  ├─ test_smoothers.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ panel
   │     │  │  │  ├─ correlation_structures.py
   │     │  │  │  ├─ mixed.py
   │     │  │  │  ├─ panelmod.py
   │     │  │  │  ├─ panel_short.py
   │     │  │  │  ├─ random_panel.py
   │     │  │  │  ├─ sandwich_covariance_generic.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_random_panel.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pca.py
   │     │  │  ├─ predict_functional.py
   │     │  │  ├─ regression
   │     │  │  │  ├─ anova_nistcertified.py
   │     │  │  │  ├─ ar_panel.py
   │     │  │  │  ├─ example_kernridge.py
   │     │  │  │  ├─ gmm.py
   │     │  │  │  ├─ kernridgeregress_class.py
   │     │  │  │  ├─ ols_anova_original.py
   │     │  │  │  ├─ onewaygls.py
   │     │  │  │  ├─ penalized.py
   │     │  │  │  ├─ predstd.py
   │     │  │  │  ├─ runmnl.py
   │     │  │  │  ├─ sympy_diff.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ griliches76.dta
   │     │  │  │  │  ├─ racd10data_with_transformed.csv
   │     │  │  │  │  ├─ results_gmm_griliches.py
   │     │  │  │  │  ├─ results_gmm_griliches_iter.py
   │     │  │  │  │  ├─ results_gmm_poisson.py
   │     │  │  │  │  ├─ results_ivreg2_griliches.py
   │     │  │  │  │  ├─ test_gmm.py
   │     │  │  │  │  ├─ test_gmm_poisson.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tools.py
   │     │  │  │  ├─ treewalkerclass.py
   │     │  │  │  ├─ try_catdata.py
   │     │  │  │  ├─ try_ols_anova.py
   │     │  │  │  ├─ try_treewalker.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ rls.py
   │     │  │  ├─ stats
   │     │  │  │  ├─ contrast_tools.py
   │     │  │  │  ├─ diagnostic.py
   │     │  │  │  ├─ ex_newtests.py
   │     │  │  │  ├─ multicomp.py
   │     │  │  │  ├─ runs.py
   │     │  │  │  ├─ stats_dhuard.py
   │     │  │  │  ├─ stats_mstats_short.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_multicomp.py
   │     │  │  │  │  ├─ test_runs.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sysreg.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ maketests_mlabwrap.py
   │     │  │  │  ├─ savervs.py
   │     │  │  │  ├─ test_gam.py
   │     │  │  │  ├─ test_pca.py
   │     │  │  │  ├─ test_predict_functional.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tools
   │     │  │  │  ├─ cross_val.py
   │     │  │  │  ├─ mctools.py
   │     │  │  │  ├─ tools_pca.py
   │     │  │  │  ├─ try_mctools.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tsa
   │     │  │  │  ├─ diffusion.py
   │     │  │  │  ├─ diffusion2.py
   │     │  │  │  ├─ example_arma.py
   │     │  │  │  ├─ fftarma.py
   │     │  │  │  ├─ movstat.py
   │     │  │  │  ├─ try_arma_more.py
   │     │  │  │  ├─ try_fi.py
   │     │  │  │  ├─ try_var_convolve.py
   │     │  │  │  ├─ varma.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ setup.cfg
   │     │  ├─ src
   │     │  │  └─ __init__.py
   │     │  ├─ stats
   │     │  │  ├─ anova.py
   │     │  │  ├─ api.py
   │     │  │  ├─ base.py
   │     │  │  ├─ contingency_tables.py
   │     │  │  ├─ contrast.py
   │     │  │  ├─ correlation_tools.py
   │     │  │  ├─ descriptivestats.py
   │     │  │  ├─ diagnostic.py
   │     │  │  ├─ diagnostic_gen.py
   │     │  │  ├─ dist_dependence_measures.py
   │     │  │  ├─ effect_size.py
   │     │  │  ├─ gof.py
   │     │  │  ├─ inter_rater.py
   │     │  │  ├─ knockoff_regeffects.py
   │     │  │  ├─ libqsturng
   │     │  │  │  ├─ CH.r
   │     │  │  │  ├─ LICENSE.txt
   │     │  │  │  ├─ make_tbls.py
   │     │  │  │  ├─ qsturng_.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ bootleg.dat
   │     │  │  │  │  ├─ test_qsturng.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mediation.py
   │     │  │  ├─ meta_analysis.py
   │     │  │  ├─ moment_helpers.py
   │     │  │  ├─ multicomp.py
   │     │  │  ├─ multitest.py
   │     │  │  ├─ multivariate.py
   │     │  │  ├─ multivariate_tools.py
   │     │  │  ├─ nonparametric.py
   │     │  │  ├─ oaxaca.py
   │     │  │  ├─ oneway.py
   │     │  │  ├─ outliers_influence.py
   │     │  │  ├─ power.py
   │     │  │  ├─ proportion.py
   │     │  │  ├─ rates.py
   │     │  │  ├─ regularized_covariance.py
   │     │  │  ├─ robust_compare.py
   │     │  │  ├─ sandwich_covariance.py
   │     │  │  ├─ stattools.py
   │     │  │  ├─ tabledist.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ binary_constrict.csv
   │     │  │  │  │  ├─ bootleg.csv
   │     │  │  │  │  ├─ contingency_table_r_results.csv
   │     │  │  │  │  ├─ data.dat
   │     │  │  │  │  ├─ framing.csv
   │     │  │  │  │  ├─ influence_lsdiag_R.json
   │     │  │  │  │  ├─ influence_measures_bool_R.csv
   │     │  │  │  │  ├─ influence_measures_R.csv
   │     │  │  │  │  ├─ lilliefors_critical_value_simulation.py
   │     │  │  │  │  ├─ results_influence_logit.csv
   │     │  │  │  │  ├─ results_meta.py
   │     │  │  │  │  ├─ results_multinomial_proportions.py
   │     │  │  │  │  ├─ results_panelrobust.py
   │     │  │  │  │  ├─ results_power.py
   │     │  │  │  │  ├─ results_proportion.py
   │     │  │  │  │  ├─ results_rates.py
   │     │  │  │  │  ├─ wspec1.csv
   │     │  │  │  │  ├─ wspec2.csv
   │     │  │  │  │  ├─ wspec3.csv
   │     │  │  │  │  ├─ wspec4.csv
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_anova.py
   │     │  │  │  ├─ test_anova_rm.py
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_contingency_tables.py
   │     │  │  │  ├─ test_contrast.py
   │     │  │  │  ├─ test_correlation.py
   │     │  │  │  ├─ test_corrpsd.py
   │     │  │  │  ├─ test_data.txt
   │     │  │  │  ├─ test_deltacov.py
   │     │  │  │  ├─ test_descriptivestats.py
   │     │  │  │  ├─ test_diagnostic.py
   │     │  │  │  ├─ test_diagnostic_other.py
   │     │  │  │  ├─ test_dist_dependant_measures.py
   │     │  │  │  ├─ test_effectsize.py
   │     │  │  │  ├─ test_gof.py
   │     │  │  │  ├─ test_groups_sw.py
   │     │  │  │  ├─ test_influence.py
   │     │  │  │  ├─ test_inter_rater.py
   │     │  │  │  ├─ test_knockoff.py
   │     │  │  │  ├─ test_lilliefors.py
   │     │  │  │  ├─ test_mediation.py
   │     │  │  │  ├─ test_meta.py
   │     │  │  │  ├─ test_moment_helpers.py
   │     │  │  │  ├─ test_multi.py
   │     │  │  │  ├─ test_multivariate.py
   │     │  │  │  ├─ test_nonparametric.py
   │     │  │  │  ├─ test_oaxaca.py
   │     │  │  │  ├─ test_oneway.py
   │     │  │  │  ├─ test_outliers_influence.py
   │     │  │  │  ├─ test_pairwise.py
   │     │  │  │  ├─ test_panel_robustcov.py
   │     │  │  │  ├─ test_power.py
   │     │  │  │  ├─ test_proportion.py
   │     │  │  │  ├─ test_qsturng.py
   │     │  │  │  ├─ test_rates_poisson.py
   │     │  │  │  ├─ test_regularized_covariance.py
   │     │  │  │  ├─ test_robust_compare.py
   │     │  │  │  ├─ test_sandwich.py
   │     │  │  │  ├─ test_statstools.py
   │     │  │  │  ├─ test_tabledist.py
   │     │  │  │  ├─ test_tost.py
   │     │  │  │  ├─ test_weightstats.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ weightstats.py
   │     │  │  ├─ _adnorm.py
   │     │  │  ├─ _delta_method.py
   │     │  │  ├─ _diagnostic_other.py
   │     │  │  ├─ _inference_tools.py
   │     │  │  ├─ _knockoff.py
   │     │  │  ├─ _lilliefors.py
   │     │  │  ├─ _lilliefors_critical_values.py
   │     │  │  └─ __init__.py
   │     │  ├─ tests
   │     │  │  ├─ test_package.py
   │     │  │  ├─ test_x13.py
   │     │  │  └─ __init__.py
   │     │  ├─ tools
   │     │  │  ├─ catadd.py
   │     │  │  ├─ data.py
   │     │  │  ├─ decorators.py
   │     │  │  ├─ docstring.py
   │     │  │  ├─ eval_measures.py
   │     │  │  ├─ grouputils.py
   │     │  │  ├─ linalg.py
   │     │  │  ├─ numdiff.py
   │     │  │  ├─ parallel.py
   │     │  │  ├─ print_version.py
   │     │  │  ├─ rng_qrng.py
   │     │  │  ├─ rootfinding.py
   │     │  │  ├─ sequences.py
   │     │  │  ├─ sm_exceptions.py
   │     │  │  ├─ testing.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_catadd.py
   │     │  │  │  ├─ test_data.py
   │     │  │  │  ├─ test_decorators.py
   │     │  │  │  ├─ test_docstring.py
   │     │  │  │  ├─ test_eval_measures.py
   │     │  │  │  ├─ test_grouputils.py
   │     │  │  │  ├─ test_linalg.py
   │     │  │  │  ├─ test_numdiff.py
   │     │  │  │  ├─ test_parallel.py
   │     │  │  │  ├─ test_rootfinding.py
   │     │  │  │  ├─ test_sequences.py
   │     │  │  │  ├─ test_testing.py
   │     │  │  │  ├─ test_tools.py
   │     │  │  │  ├─ test_transform_model.py
   │     │  │  │  ├─ test_web.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tools.py
   │     │  │  ├─ transform_model.py
   │     │  │  ├─ typing.py
   │     │  │  ├─ validation
   │     │  │  │  ├─ decorators.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_validation.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ validation.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ web.py
   │     │  │  ├─ _testing.py
   │     │  │  ├─ _test_runner.py
   │     │  │  └─ __init__.py
   │     │  ├─ treatment
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ cataneo2.csv
   │     │  │  │  │  ├─ results_teffects.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_teffects.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ treatment_effects.py
   │     │  │  └─ __init__.py
   │     │  ├─ tsa
   │     │  │  ├─ adfvalues.py
   │     │  │  ├─ api.py
   │     │  │  ├─ ardl
   │     │  │  │  ├─ model.py
   │     │  │  │  ├─ pss_critical_values.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_ardl.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _pss_critical_values
   │     │  │  │  │  ├─ pss-process.py
   │     │  │  │  │  ├─ pss.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ arima
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ datasets
   │     │  │  │  │  ├─ brockwell_davis_2002
   │     │  │  │  │  │  ├─ data
   │     │  │  │  │  │  │  ├─ dowj.py
   │     │  │  │  │  │  │  ├─ lake.py
   │     │  │  │  │  │  │  ├─ oshorts.py
   │     │  │  │  │  │  │  ├─ sbl.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ estimators
   │     │  │  │  │  ├─ burg.py
   │     │  │  │  │  ├─ durbin_levinson.py
   │     │  │  │  │  ├─ gls.py
   │     │  │  │  │  ├─ hannan_rissanen.py
   │     │  │  │  │  ├─ innovations.py
   │     │  │  │  │  ├─ statespace.py
   │     │  │  │  │  ├─ tests
   │     │  │  │  │  │  ├─ test_burg.py
   │     │  │  │  │  │  ├─ test_durbin_levinson.py
   │     │  │  │  │  │  ├─ test_gls.py
   │     │  │  │  │  │  ├─ test_hannan_rissanen.py
   │     │  │  │  │  │  ├─ test_innovations.py
   │     │  │  │  │  │  ├─ test_statespace.py
   │     │  │  │  │  │  ├─ test_yule_walker.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ yule_walker.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ model.py
   │     │  │  │  ├─ params.py
   │     │  │  │  ├─ specification.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_model.py
   │     │  │  │  │  ├─ test_params.py
   │     │  │  │  │  ├─ test_specification.py
   │     │  │  │  │  ├─ test_tools.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tools.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ arima_model.py
   │     │  │  ├─ arima_process.py
   │     │  │  ├─ arma_mle.py
   │     │  │  ├─ ar_model.py
   │     │  │  ├─ base
   │     │  │  │  ├─ datetools.py
   │     │  │  │  ├─ prediction.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_base.py
   │     │  │  │  │  ├─ test_datetools.py
   │     │  │  │  │  ├─ test_prediction.py
   │     │  │  │  │  ├─ test_tsa_indexes.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tsa_model.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ coint_tables.py
   │     │  │  ├─ descriptivestats.py
   │     │  │  ├─ deterministic.py
   │     │  │  ├─ exponential_smoothing
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ ets.py
   │     │  │  │  ├─ initialization.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ filters
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ bk_filter.py
   │     │  │  │  ├─ cf_filter.py
   │     │  │  │  ├─ filtertools.py
   │     │  │  │  ├─ hp_filter.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ results
   │     │  │  │  │  │  ├─ filter_results.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_filters.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ forecasting
   │     │  │  │  ├─ stl.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_stl.py
   │     │  │  │  │  ├─ test_theta.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ theta.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ holtwinters
   │     │  │  │  ├─ model.py
   │     │  │  │  ├─ results.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ results
   │     │  │  │  │  │  ├─ housing-data.csv
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_holtwinters.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _smoothers.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ innovations
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ arma_innovations.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_arma_innovations.py
   │     │  │  │  │  ├─ test_cython_arma_innovations_fast.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ interp
   │     │  │  │  ├─ denton.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_denton.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mlemodel.py
   │     │  │  ├─ regime_switching
   │     │  │  │  ├─ markov_autoregression.py
   │     │  │  │  ├─ markov_regression.py
   │     │  │  │  ├─ markov_switching.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ results
   │     │  │  │  │  │  ├─ mar_filardo.csv
   │     │  │  │  │  │  ├─ results_predict_fedfunds.csv
   │     │  │  │  │  │  ├─ results_predict_rgnp.csv
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_markov_autoregression.py
   │     │  │  │  │  ├─ test_markov_regression.py
   │     │  │  │  │  ├─ test_markov_switching.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ seasonal.py
   │     │  │  ├─ statespace
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ cfa_simulation_smoother.py
   │     │  │  │  ├─ dynamic_factor.py
   │     │  │  │  ├─ dynamic_factor_mq.py
   │     │  │  │  ├─ exponential_smoothing.py
   │     │  │  │  ├─ initialization.py
   │     │  │  │  ├─ kalman_filter.py
   │     │  │  │  ├─ kalman_smoother.py
   │     │  │  │  ├─ mlemodel.py
   │     │  │  │  ├─ news.py
   │     │  │  │  ├─ representation.py
   │     │  │  │  ├─ sarimax.py
   │     │  │  │  ├─ simulation_smoother.py
   │     │  │  │  ├─ structural.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ kfas_helpers.py
   │     │  │  │  │  ├─ results
   │     │  │  │  │  │  ├─ cfa_tvpvar_beta.csv
   │     │  │  │  │  │  ├─ cfa_tvpvar_invP.csv
   │     │  │  │  │  │  ├─ cfa_tvpvar_Omega_11.csv
   │     │  │  │  │  │  ├─ cfa_tvpvar_Omega_22.csv
   │     │  │  │  │  │  ├─ cfa_tvpvar_posterior_mean.csv
   │     │  │  │  │  │  ├─ cfa_tvpvar_S10.csv
   │     │  │  │  │  │  ├─ cfa_tvpvar_Si0.csv
   │     │  │  │  │  │  ├─ cfa_tvpvar_state_variates.csv
   │     │  │  │  │  │  ├─ cfa_tvpvar_v10.csv
   │     │  │  │  │  │  ├─ cfa_tvpvar_vi0.csv
   │     │  │  │  │  │  ├─ clark1989.csv
   │     │  │  │  │  │  ├─ exponential_smoothing_params.csv
   │     │  │  │  │  │  ├─ exponential_smoothing_predict.csv
   │     │  │  │  │  │  ├─ exponential_smoothing_states.csv
   │     │  │  │  │  │  ├─ frbny_nowcast
   │     │  │  │  │  │  │  ├─ Nowcasting
   │     │  │  │  │  │  │  │  ├─ data
   │     │  │  │  │  │  │  │  │  ├─ US
   │     │  │  │  │  │  │  │  │  │  ├─ 2016-06-29.csv
   │     │  │  │  │  │  │  │  │  │  ├─ 2016-07-29.csv
   │     │  │  │  │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  │  │  ├─ functions
   │     │  │  │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  │  ├─ test_dfm_111.mat
   │     │  │  │  │  │  │  ├─ test_dfm_112.mat
   │     │  │  │  │  │  │  ├─ test_dfm_11F.mat
   │     │  │  │  │  │  │  ├─ test_dfm_221.mat
   │     │  │  │  │  │  │  ├─ test_dfm_222.mat
   │     │  │  │  │  │  │  ├─ test_dfm_22F.mat
   │     │  │  │  │  │  │  ├─ test_dfm_blocks_111.mat
   │     │  │  │  │  │  │  ├─ test_dfm_blocks_112.mat
   │     │  │  │  │  │  │  ├─ test_dfm_blocks_221.mat
   │     │  │  │  │  │  │  ├─ test_dfm_blocks_222.mat
   │     │  │  │  │  │  │  ├─ test_news_112.mat
   │     │  │  │  │  │  │  ├─ test_news_222.mat
   │     │  │  │  │  │  │  ├─ test_news_blocks_112.mat
   │     │  │  │  │  │  │  ├─ test_news_blocks_222.mat
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ manufac.dta
   │     │  │  │  │  │  ├─ results_clark1989_R.csv
   │     │  │  │  │  │  ├─ results_dynamic_factor.py
   │     │  │  │  │  │  ├─ results_dynamic_factor_stata.csv
   │     │  │  │  │  │  ├─ results_exact_initial_common_level_R.csv
   │     │  │  │  │  │  ├─ results_exact_initial_common_level_restricted_R.csv
   │     │  │  │  │  │  ├─ results_exact_initial_dfm_R.csv
   │     │  │  │  │  │  ├─ results_exact_initial_local_level_R.csv
   │     │  │  │  │  │  ├─ results_exact_initial_local_linear_trend_missing_R.csv
   │     │  │  │  │  │  ├─ results_exact_initial_local_linear_trend_R.csv
   │     │  │  │  │  │  ├─ results_exact_initial_var1_measurement_error_R.csv
   │     │  │  │  │  │  ├─ results_exact_initial_var1_missing_R.csv
   │     │  │  │  │  │  ├─ results_exact_initial_var1_mixed_R.csv
   │     │  │  │  │  │  ├─ results_exact_initial_var1_R.csv
   │     │  │  │  │  │  ├─ results_intercepts_R.csv
   │     │  │  │  │  │  ├─ results_kalman_filter.py
   │     │  │  │  │  │  ├─ results_realgdpar_stata.csv
   │     │  │  │  │  │  ├─ results_sarimax.py
   │     │  │  │  │  │  ├─ results_sarimax_coverage.csv
   │     │  │  │  │  │  ├─ results_simulation_smoothing0.csv
   │     │  │  │  │  │  ├─ results_simulation_smoothing1.csv
   │     │  │  │  │  │  ├─ results_simulation_smoothing2.csv
   │     │  │  │  │  │  ├─ results_simulation_smoothing3.csv
   │     │  │  │  │  │  ├─ results_simulation_smoothing3_variates.csv
   │     │  │  │  │  │  ├─ results_simulation_smoothing4.csv
   │     │  │  │  │  │  ├─ results_simulation_smoothing5.csv
   │     │  │  │  │  │  ├─ results_simulation_smoothing6.csv
   │     │  │  │  │  │  ├─ results_smoothing2_R.csv
   │     │  │  │  │  │  ├─ results_smoothing3_R.csv
   │     │  │  │  │  │  ├─ results_smoothing_generalobscov_R.csv
   │     │  │  │  │  │  ├─ results_smoothing_R.csv
   │     │  │  │  │  │  ├─ results_structural.py
   │     │  │  │  │  │  ├─ results_varmax.py
   │     │  │  │  │  │  ├─ results_varmax_stata.csv
   │     │  │  │  │  │  ├─ results_var_misc.py
   │     │  │  │  │  │  ├─ results_var_R.py
   │     │  │  │  │  │  ├─ results_var_R_output.csv
   │     │  │  │  │  │  ├─ results_var_stata.csv
   │     │  │  │  │  │  ├─ results_wpi1_ar3_matlab_ssm.csv
   │     │  │  │  │  │  ├─ results_wpi1_ar3_stata.csv
   │     │  │  │  │  │  ├─ results_wpi1_missing_ar3_matlab_ssm.csv
   │     │  │  │  │  │  ├─ sm-0.9-sarimax.pkl
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_cfa_simulation_smoothing.py
   │     │  │  │  │  ├─ test_cfa_tvpvar.py
   │     │  │  │  │  ├─ test_chandrasekhar.py
   │     │  │  │  │  ├─ test_collapsed.py
   │     │  │  │  │  ├─ test_concentrated.py
   │     │  │  │  │  ├─ test_conserve_memory.py
   │     │  │  │  │  ├─ test_decompose.py
   │     │  │  │  │  ├─ test_dynamic_factor.py
   │     │  │  │  │  ├─ test_dynamic_factor_mq.py
   │     │  │  │  │  ├─ test_dynamic_factor_mq_frbny_nowcast.py
   │     │  │  │  │  ├─ test_dynamic_factor_mq_monte_carlo.py
   │     │  │  │  │  ├─ test_exact_diffuse_filtering.py
   │     │  │  │  │  ├─ test_exponential_smoothing.py
   │     │  │  │  │  ├─ test_fixed_params.py
   │     │  │  │  │  ├─ test_forecasting.py
   │     │  │  │  │  ├─ test_impulse_responses.py
   │     │  │  │  │  ├─ test_initialization.py
   │     │  │  │  │  ├─ test_kalman.py
   │     │  │  │  │  ├─ test_mlemodel.py
   │     │  │  │  │  ├─ test_models.py
   │     │  │  │  │  ├─ test_multivariate_switch_univariate.py
   │     │  │  │  │  ├─ test_news.py
   │     │  │  │  │  ├─ test_options.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_prediction.py
   │     │  │  │  │  ├─ test_representation.py
   │     │  │  │  │  ├─ test_sarimax.py
   │     │  │  │  │  ├─ test_save.py
   │     │  │  │  │  ├─ test_simulate.py
   │     │  │  │  │  ├─ test_simulation_smoothing.py
   │     │  │  │  │  ├─ test_smoothing.py
   │     │  │  │  │  ├─ test_structural.py
   │     │  │  │  │  ├─ test_tools.py
   │     │  │  │  │  ├─ test_univariate.py
   │     │  │  │  │  ├─ test_var.py
   │     │  │  │  │  ├─ test_varmax.py
   │     │  │  │  │  ├─ test_weights.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tools.py
   │     │  │  │  ├─ varmax.py
   │     │  │  │  ├─ _filters
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _pykalman_smoother.py
   │     │  │  │  ├─ _quarterly_ar1.py
   │     │  │  │  ├─ _smoothers
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ stattools.py
   │     │  │  ├─ stl
   │     │  │  │  ├─ mstl.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ results
   │     │  │  │  │  │  ├─ mstl_elec_vic.csv
   │     │  │  │  │  │  ├─ mstl_test_results.csv
   │     │  │  │  │  │  ├─ stl_co2.csv
   │     │  │  │  │  │  ├─ stl_test_results.csv
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_mstl.py
   │     │  │  │  │  ├─ test_stl.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ results
   │     │  │  │  │  ├─ arima111nc_css_results.py
   │     │  │  │  │  ├─ arima111nc_results.py
   │     │  │  │  │  ├─ arima111_css_results.py
   │     │  │  │  │  ├─ arima111_forecasts.csv
   │     │  │  │  │  ├─ arima111_results.py
   │     │  │  │  │  ├─ arima112nc_css_results.py
   │     │  │  │  │  ├─ arima112nc_results.py
   │     │  │  │  │  ├─ arima112_css_results.py
   │     │  │  │  │  ├─ arima112_results.py
   │     │  │  │  │  ├─ arima211nc_css_results.py
   │     │  │  │  │  ├─ arima211nc_results.py
   │     │  │  │  │  ├─ arima211_css_results.py
   │     │  │  │  │  ├─ arima211_results.py
   │     │  │  │  │  ├─ arima212_forecast.csv
   │     │  │  │  │  ├─ ARMLEConstantPredict.csv
   │     │  │  │  │  ├─ AROLSConstantPredict.csv
   │     │  │  │  │  ├─ AROLSNoConstantPredict.csv
   │     │  │  │  │  ├─ bds_data.csv
   │     │  │  │  │  ├─ bds_results.csv
   │     │  │  │  │  ├─ datamlw_tls.py
   │     │  │  │  │  ├─ fit_ets_results.json
   │     │  │  │  │  ├─ fit_ets_results_nonseasonal.json
   │     │  │  │  │  ├─ fit_ets_results_seasonal.json
   │     │  │  │  │  ├─ gnpdef.csv
   │     │  │  │  │  ├─ lutkepohl2.dta
   │     │  │  │  │  ├─ make_arma.py
   │     │  │  │  │  ├─ rand10000.csv
   │     │  │  │  │  ├─ resids_css_c.csv
   │     │  │  │  │  ├─ resids_css_nc.csv
   │     │  │  │  │  ├─ resids_exact_c.csv
   │     │  │  │  │  ├─ resids_exact_nc.csv
   │     │  │  │  │  ├─ results_ar.py
   │     │  │  │  │  ├─ results_arima.py
   │     │  │  │  │  ├─ results_arima_exog_forecasts_css.csv
   │     │  │  │  │  ├─ results_arima_exog_forecasts_mle.csv
   │     │  │  │  │  ├─ results_arima_forecasts.csv
   │     │  │  │  │  ├─ results_arima_forecasts_all_css.csv
   │     │  │  │  │  ├─ results_arima_forecasts_all_css_diff.csv
   │     │  │  │  │  ├─ results_arima_forecasts_all_mle.csv
   │     │  │  │  │  ├─ results_arima_forecasts_all_mle_diff.csv
   │     │  │  │  │  ├─ results_arma.py
   │     │  │  │  │  ├─ results_arma_acf.py
   │     │  │  │  │  ├─ results_arma_forecasts.csv
   │     │  │  │  │  ├─ results_ar_forecast_mle_dynamic.csv
   │     │  │  │  │  ├─ results_ccf.csv
   │     │  │  │  │  ├─ results_corrgram.csv
   │     │  │  │  │  ├─ results_process.py
   │     │  │  │  │  ├─ rgnp.csv
   │     │  │  │  │  ├─ rgnpq.csv
   │     │  │  │  │  ├─ savedrvs.py
   │     │  │  │  │  ├─ stkprc.csv
   │     │  │  │  │  ├─ yhat_css_c.csv
   │     │  │  │  │  ├─ yhat_css_nc.csv
   │     │  │  │  │  ├─ yhat_exact_c.csv
   │     │  │  │  │  ├─ yhat_exact_nc.csv
   │     │  │  │  │  ├─ y_arma_data.csv
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_adfuller_lag.py
   │     │  │  │  ├─ test_ar.py
   │     │  │  │  ├─ test_arima_process.py
   │     │  │  │  ├─ test_bds.py
   │     │  │  │  ├─ test_deterministic.py
   │     │  │  │  ├─ test_exponential_smoothing.py
   │     │  │  │  ├─ test_seasonal.py
   │     │  │  │  ├─ test_stattools.py
   │     │  │  │  ├─ test_tsa_tools.py
   │     │  │  │  ├─ test_x13.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tsatools.py
   │     │  │  ├─ varma_process.py
   │     │  │  ├─ vector_ar
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ hypothesis_test_results.py
   │     │  │  │  ├─ irf.py
   │     │  │  │  ├─ output.py
   │     │  │  │  ├─ plotting.py
   │     │  │  │  ├─ svar_model.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ example_svar.py
   │     │  │  │  │  ├─ JMulTi_results
   │     │  │  │  │  │  ├─ macrodata_jmulti_c.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst_diag.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst_fc5.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst_granger_causality_realcons.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst_granger_causality_realcons_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst_granger_causality_realcons_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst_granger_causality_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst_granger_causality_realgdp_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst_granger_causality_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst_ir.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst_lagorder.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cst_Sigmau.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs_diag.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs_fc5.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs_granger_causality_realcons.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs_granger_causality_realcons_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs_granger_causality_realcons_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs_granger_causality_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs_granger_causality_realgdp_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs_granger_causality_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs_ir.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs_lagorder.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_cs_Sigmau.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct_diag.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct_fc5.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct_granger_causality_realcons.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct_granger_causality_realcons_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct_granger_causality_realcons_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct_granger_causality_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct_granger_causality_realgdp_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct_granger_causality_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct_ir.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct_lagorder.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ct_Sigmau.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_c_diag.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_c_fc5.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_c_granger_causality_realcons.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_c_granger_causality_realcons_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_c_granger_causality_realcons_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_c_granger_causality_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_c_granger_causality_realgdp_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_c_granger_causality_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_c_ir.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_c_lagorder.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_c_Sigmau.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs_diag.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs_fc5.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs_granger_causality_realcons.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs_granger_causality_realcons_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs_granger_causality_realcons_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs_granger_causality_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs_granger_causality_realgdp_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs_granger_causality_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs_ir.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs_lagorder.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_ncs_Sigmau.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc_diag.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc_fc5.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc_granger_causality_realcons.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc_granger_causality_realcons_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc_granger_causality_realcons_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc_granger_causality_realgdp.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc_granger_causality_realgdp_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc_granger_causality_realinv.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc_ir.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc_lagorder.txt
   │     │  │  │  │  │  ├─ macrodata_jmulti_nc_Sigmau.txt
   │     │  │  │  │  │  ├─ parse_jmulti_var_output.py
   │     │  │  │  │  │  ├─ parse_jmulti_vecm_output.py
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ci.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cili.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cili_diag.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cili_fc5.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cili_granger_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cili_granger_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cili_inst_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cili_inst_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cili_ir.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cili_lagorder.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cili_Sigmau.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cis.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cisli.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cisli_diag.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cisli_fc5.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cisli_granger_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cisli_granger_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cisli_inst_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cisli_inst_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cisli_ir.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cisli_lagorder.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cisli_Sigmau.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cis_diag.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cis_fc5.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cis_granger_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cis_granger_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cis_inst_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cis_inst_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cis_ir.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cis_lagorder.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cis_Sigmau.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ci_diag.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ci_fc5.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ci_granger_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ci_granger_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ci_inst_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ci_inst_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ci_ir.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ci_lagorder.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ci_Sigmau.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_co.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_colo.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_colo_diag.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_colo_fc5.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_colo_granger_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_colo_granger_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_colo_inst_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_colo_inst_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_colo_ir.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_colo_lagorder.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_colo_Sigmau.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cos.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_coslo.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_coslo_diag.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_coslo_fc5.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_coslo_granger_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_coslo_granger_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_coslo_inst_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_coslo_inst_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_coslo_ir.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_coslo_lagorder.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_coslo_Sigmau.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cos_diag.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cos_fc5.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cos_granger_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cos_granger_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cos_inst_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cos_inst_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cos_ir.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cos_lagorder.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_cos_Sigmau.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_co_diag.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_co_fc5.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_co_granger_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_co_granger_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_co_inst_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_co_inst_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_co_ir.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_co_lagorder.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_co_Sigmau.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_nc.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ncs.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ncs_diag.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ncs_fc5.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ncs_granger_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ncs_granger_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ncs_inst_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ncs_inst_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ncs_ir.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ncs_lagorder.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_ncs_Sigmau.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_nc_diag.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_nc_fc5.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_nc_granger_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_nc_granger_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_nc_inst_causality_dp_r.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_nc_inst_causality_r_dp.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_nc_ir.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_nc_lagorder.txt
   │     │  │  │  │  │  ├─ vecm_e6_jmulti_nc_Sigmau.txt
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ Matlab_results
   │     │  │  │  │  │  ├─ test_coint.csv
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ results
   │     │  │  │  │  │  ├─ e1.dat
   │     │  │  │  │  │  ├─ e2.dat
   │     │  │  │  │  │  ├─ e3.dat
   │     │  │  │  │  │  ├─ e4.dat
   │     │  │  │  │  │  ├─ e5.dat
   │     │  │  │  │  │  ├─ e6.dat
   │     │  │  │  │  │  ├─ results_svar.py
   │     │  │  │  │  │  ├─ results_svar_st.py
   │     │  │  │  │  │  ├─ results_var.py
   │     │  │  │  │  │  ├─ results_var_data.py
   │     │  │  │  │  │  ├─ vars_results.npz
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_coint.py
   │     │  │  │  │  ├─ test_svar.py
   │     │  │  │  │  ├─ test_var.py
   │     │  │  │  │  ├─ test_var_jmulti.py
   │     │  │  │  │  ├─ test_vecm.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ util.py
   │     │  │  │  ├─ var_model.py
   │     │  │  │  ├─ vecm.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ x13.py
   │     │  │  ├─ _bds.py
   │     │  │  └─ __init__.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ statsmodels-0.14.6.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ tensorflow
   │     │  ├─ compiler
   │     │  │  ├─ jit
   │     │  │  │  ├─ ops
   │     │  │  │  │  ├─ xla_ops.py
   │     │  │  │  │  ├─ xla_ops_grad.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mlir
   │     │  │  │  ├─ lite
   │     │  │  │  │  ├─ converter_flags_pb2.py
   │     │  │  │  │  ├─ debug
   │     │  │  │  │  │  ├─ debug_options_pb2.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ metrics
   │     │  │  │  │  │  ├─ converter_error_data_pb2.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ model_flags_pb2.py
   │     │  │  │  │  ├─ python
   │     │  │  │  │  │  ├─ wrap_converter.py
   │     │  │  │  │  │  ├─ _pywrap_converter_api.pyi
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ types_pb2.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ quantization
   │     │  │  │  │  ├─ stablehlo
   │     │  │  │  │  │  ├─ quantization_config_pb2.py
   │     │  │  │  │  │  ├─ quantization_options_pb2.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ tensorflow
   │     │  │  │  │  │  ├─ calibrator
   │     │  │  │  │  │  │  ├─ calibration_algorithm.py
   │     │  │  │  │  │  │  ├─ calibration_statistics_pb2.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ exported_model_pb2.py
   │     │  │  │  │  │  ├─ python
   │     │  │  │  │  │  │  ├─ pywrap_function_lib.pyi
   │     │  │  │  │  │  │  ├─ pywrap_quantize_model.pyi
   │     │  │  │  │  │  │  ├─ py_function_lib.py
   │     │  │  │  │  │  │  ├─ quantize_model.py
   │     │  │  │  │  │  │  ├─ representative_dataset.py
   │     │  │  │  │  │  │  ├─ save_model.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ quantization_options_pb2.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ stablehlo
   │     │  │  │  │  ├─ stablehlo.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tensorflow
   │     │  │  │  │  ├─ gen_mlir_passthrough_op.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tensorflow_to_stablehlo
   │     │  │  │  │  └─ python
   │     │  │  │  │     └─ pywrap_tensorflow_to_stablehlo.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tf2tensorrt
   │     │  │  │  ├─ ops
   │     │  │  │  │  ├─ gen_trt_ops.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _pywrap_py_utils.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tf2xla
   │     │  │  │  ├─ ops
   │     │  │  │  │  ├─ gen_xla_ops.py
   │     │  │  │  │  ├─ _xla_ops.so
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ python
   │     │  │  │  │  ├─ xla.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tf2xla_pb2.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ xla
   │     │  │  │  ├─ service
   │     │  │  │  │  ├─ hlo_pb2.py
   │     │  │  │  │  ├─ metrics_pb2.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tsl
   │     │  │  │  │  ├─ protobuf
   │     │  │  │  │  │  ├─ bfc_memory_map_pb2.py
   │     │  │  │  │  │  ├─ coordination_config_pb2.py
   │     │  │  │  │  │  ├─ distributed_runtime_payloads_pb2.py
   │     │  │  │  │  │  ├─ error_codes_pb2.py
   │     │  │  │  │  │  ├─ histogram_pb2.py
   │     │  │  │  │  │  ├─ rpc_options_pb2.py
   │     │  │  │  │  │  ├─ status_pb2.py
   │     │  │  │  │  │  ├─ test_log_pb2.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ xla_data_pb2.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ core
   │     │  │  ├─ config
   │     │  │  │  ├─ flags.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ debug
   │     │  │  │  ├─ debugger_event_metadata_pb2.py
   │     │  │  │  ├─ debug_service_pb2.py
   │     │  │  │  ├─ debug_service_pb2_grpc.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ distributed_runtime
   │     │  │  │  ├─ preemption
   │     │  │  │  │  ├─ gen_check_preemption_op.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ example
   │     │  │  │  ├─ example_parser_configuration_pb2.py
   │     │  │  │  ├─ example_pb2.py
   │     │  │  │  ├─ feature_pb2.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ framework
   │     │  │  │  ├─ allocation_description_pb2.py
   │     │  │  │  ├─ api_def_pb2.py
   │     │  │  │  ├─ attr_value_pb2.py
   │     │  │  │  ├─ cost_graph_pb2.py
   │     │  │  │  ├─ cpp_shape_inference_pb2.py
   │     │  │  │  ├─ dataset_metadata_pb2.py
   │     │  │  │  ├─ dataset_options_pb2.py
   │     │  │  │  ├─ dataset_pb2.py
   │     │  │  │  ├─ device_attributes_pb2.py
   │     │  │  │  ├─ full_type_pb2.py
   │     │  │  │  ├─ function_pb2.py
   │     │  │  │  ├─ graph_debug_info_pb2.py
   │     │  │  │  ├─ graph_pb2.py
   │     │  │  │  ├─ graph_transfer_info_pb2.py
   │     │  │  │  ├─ kernel_def_pb2.py
   │     │  │  │  ├─ log_memory_pb2.py
   │     │  │  │  ├─ model_pb2.py
   │     │  │  │  ├─ node_def_pb2.py
   │     │  │  │  ├─ optimized_function_graph_pb2.py
   │     │  │  │  ├─ op_def_pb2.py
   │     │  │  │  ├─ reader_base_pb2.py
   │     │  │  │  ├─ resource_handle_pb2.py
   │     │  │  │  ├─ step_stats_pb2.py
   │     │  │  │  ├─ summary_pb2.py
   │     │  │  │  ├─ tensor_description_pb2.py
   │     │  │  │  ├─ tensor_pb2.py
   │     │  │  │  ├─ tensor_shape_pb2.py
   │     │  │  │  ├─ tensor_slice_pb2.py
   │     │  │  │  ├─ types_pb2.py
   │     │  │  │  ├─ variable_pb2.py
   │     │  │  │  ├─ versions_pb2.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ function
   │     │  │  │  ├─ capture
   │     │  │  │  │  ├─ capture_container.py
   │     │  │  │  │  ├─ restore_captures.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ polymorphism
   │     │  │  │  │  ├─ function_cache.py
   │     │  │  │  │  ├─ function_type.py
   │     │  │  │  │  ├─ function_type_pb2.py
   │     │  │  │  │  ├─ type_dispatch.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ trace_type
   │     │  │  │  │  ├─ custom_nest_trace_type.py
   │     │  │  │  │  ├─ default_types.py
   │     │  │  │  │  ├─ default_types_pb2.py
   │     │  │  │  │  ├─ serialization.py
   │     │  │  │  │  ├─ serialization_pb2.py
   │     │  │  │  │  ├─ serialization_test_pb2.py
   │     │  │  │  │  ├─ util.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ grappler
   │     │  │  │  ├─ costs
   │     │  │  │  │  ├─ op_performance_data_pb2.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ lib
   │     │  │  │  ├─ core
   │     │  │  │  │  ├─ error_codes_pb2.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ profiler
   │     │  │  │  ├─ profiler_options_pb2.py
   │     │  │  │  ├─ profile_pb2.py
   │     │  │  │  ├─ tfprof_log_pb2.py
   │     │  │  │  ├─ tfprof_options_pb2.py
   │     │  │  │  ├─ tfprof_output_pb2.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ protobuf
   │     │  │  │  ├─ bfc_memory_map_pb2.py
   │     │  │  │  ├─ cluster_pb2.py
   │     │  │  │  ├─ composite_tensor_variant_pb2.py
   │     │  │  │  ├─ config_pb2.py
   │     │  │  │  ├─ control_flow_pb2.py
   │     │  │  │  ├─ core_platform_payloads_pb2.py
   │     │  │  │  ├─ data_service_pb2.py
   │     │  │  │  ├─ debug_event_pb2.py
   │     │  │  │  ├─ debug_pb2.py
   │     │  │  │  ├─ device_filters_pb2.py
   │     │  │  │  ├─ device_properties_pb2.py
   │     │  │  │  ├─ error_codes_pb2.py
   │     │  │  │  ├─ fingerprint_pb2.py
   │     │  │  │  ├─ meta_graph_pb2.py
   │     │  │  │  ├─ named_tensor_pb2.py
   │     │  │  │  ├─ queue_runner_pb2.py
   │     │  │  │  ├─ remote_tensor_handle_pb2.py
   │     │  │  │  ├─ rewriter_config_pb2.py
   │     │  │  │  ├─ rpc_options_pb2.py
   │     │  │  │  ├─ saved_model_pb2.py
   │     │  │  │  ├─ saved_object_graph_pb2.py
   │     │  │  │  ├─ saver_pb2.py
   │     │  │  │  ├─ service_config_pb2.py
   │     │  │  │  ├─ snapshot_pb2.py
   │     │  │  │  ├─ status_pb2.py
   │     │  │  │  ├─ struct_pb2.py
   │     │  │  │  ├─ tensorflow_server_pb2.py
   │     │  │  │  ├─ tensor_bundle_pb2.py
   │     │  │  │  ├─ tpu
   │     │  │  │  │  ├─ compilation_result_pb2.py
   │     │  │  │  │  ├─ dynamic_padding_pb2.py
   │     │  │  │  │  ├─ optimization_parameters_pb2.py
   │     │  │  │  │  ├─ topology_pb2.py
   │     │  │  │  │  ├─ tpu_embedding_configuration_pb2.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ trackable_object_graph_pb2.py
   │     │  │  │  ├─ transport_options_pb2.py
   │     │  │  │  ├─ verifier_config_pb2.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tpu
   │     │  │  │  ├─ kernels
   │     │  │  │  │  ├─ sparse_core_layout_pb2.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ util
   │     │  │  │  ├─ event_pb2.py
   │     │  │  │  ├─ memmapped_file_system_pb2.py
   │     │  │  │  ├─ quantization
   │     │  │  │  │  ├─ uniform_quant_ops_attr_pb2.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ saved_tensor_slice_pb2.py
   │     │  │  │  ├─ test_log_pb2.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ distribute
   │     │  │  ├─ experimental
   │     │  │  │  ├─ rpc
   │     │  │  │  │  ├─ kernels
   │     │  │  │  │  │  ├─ gen_rpc_ops.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ proto
   │     │  │  │  │  │  ├─ tf_rpc_service_pb2.py
   │     │  │  │  │  │  ├─ tf_rpc_service_pb2_grpc.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ dtensor
   │     │  │  ├─ proto
   │     │  │  │  ├─ layout_pb2.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ python
   │     │  │  │  ├─ accelerator_util.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ dtensor_device.py
   │     │  │  │  ├─ d_checkpoint.py
   │     │  │  │  ├─ d_variable.py
   │     │  │  │  ├─ gen_dtensor_ops.py
   │     │  │  │  ├─ input_util.py
   │     │  │  │  ├─ layout.py
   │     │  │  │  ├─ mesh_util.py
   │     │  │  │  ├─ numpy_util.py
   │     │  │  │  ├─ save_restore.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ multi_client_test_util.py
   │     │  │  │  │  ├─ test_backend_name.py
   │     │  │  │  │  ├─ test_backend_util.py
   │     │  │  │  │  ├─ test_util.py
   │     │  │  │  │  ├─ test_util_ops.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tpu_util.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  └─ include
   │     │     ├─ absl
   │     │     │  ├─ algorithm
   │     │     │  │  ├─ algorithm.h
   │     │     │  │  └─ container.h
   │     │     │  ├─ base
   │     │     │  │  ├─ attributes.h
   │     │     │  │  ├─ call_once.h
   │     │     │  │  ├─ casts.h
   │     │     │  │  ├─ config.h
   │     │     │  │  ├─ const_init.h
   │     │     │  │  ├─ dynamic_annotations.h
   │     │     │  │  ├─ fast_type_id.h
   │     │     │  │  ├─ internal
   │     │     │  │  │  ├─ atomic_hook.h
   │     │     │  │  │  ├─ cycleclock.h
   │     │     │  │  │  ├─ cycleclock_config.h
   │     │     │  │  │  ├─ direct_mmap.h
   │     │     │  │  │  ├─ dynamic_annotations.h
   │     │     │  │  │  ├─ endian.h
   │     │     │  │  │  ├─ errno_saver.h
   │     │     │  │  │  ├─ hide_ptr.h
   │     │     │  │  │  ├─ identity.h
   │     │     │  │  │  ├─ iterator_traits.h
   │     │     │  │  │  ├─ low_level_alloc.h
   │     │     │  │  │  ├─ low_level_scheduling.h
   │     │     │  │  │  ├─ per_thread_tls.h
   │     │     │  │  │  ├─ raw_logging.h
   │     │     │  │  │  ├─ scheduling_mode.h
   │     │     │  │  │  ├─ spinlock.h
   │     │     │  │  │  ├─ spinlock_akaros.inc
   │     │     │  │  │  ├─ spinlock_linux.inc
   │     │     │  │  │  ├─ spinlock_posix.inc
   │     │     │  │  │  ├─ spinlock_wait.h
   │     │     │  │  │  ├─ spinlock_win32.inc
   │     │     │  │  │  ├─ strerror.h
   │     │     │  │  │  ├─ sysinfo.h
   │     │     │  │  │  ├─ thread_identity.h
   │     │     │  │  │  ├─ throw_delegate.h
   │     │     │  │  │  ├─ tracing.h
   │     │     │  │  │  ├─ tsan_mutex_interface.h
   │     │     │  │  │  ├─ unaligned_access.h
   │     │     │  │  │  ├─ unscaledcycleclock.h
   │     │     │  │  │  └─ unscaledcycleclock_config.h
   │     │     │  │  ├─ log_severity.h
   │     │     │  │  ├─ macros.h
   │     │     │  │  ├─ no_destructor.h
   │     │     │  │  ├─ nullability.h
   │     │     │  │  ├─ optimization.h
   │     │     │  │  ├─ options.h
   │     │     │  │  ├─ policy_checks.h
   │     │     │  │  ├─ port.h
   │     │     │  │  ├─ prefetch.h
   │     │     │  │  └─ thread_annotations.h
   │     │     │  ├─ cleanup
   │     │     │  │  ├─ cleanup.h
   │     │     │  │  └─ internal
   │     │     │  │     └─ cleanup.h
   │     │     │  ├─ container
   │     │     │  │  ├─ btree_map.h
   │     │     │  │  ├─ btree_set.h
   │     │     │  │  ├─ fixed_array.h
   │     │     │  │  ├─ flat_hash_map.h
   │     │     │  │  ├─ flat_hash_set.h
   │     │     │  │  ├─ hash_container_defaults.h
   │     │     │  │  ├─ inlined_vector.h
   │     │     │  │  ├─ internal
   │     │     │  │  │  ├─ btree.h
   │     │     │  │  │  ├─ btree_container.h
   │     │     │  │  │  ├─ common.h
   │     │     │  │  │  ├─ common_policy_traits.h
   │     │     │  │  │  ├─ compressed_tuple.h
   │     │     │  │  │  ├─ container_memory.h
   │     │     │  │  │  ├─ hashtablez_sampler.h
   │     │     │  │  │  ├─ hashtable_control_bytes.h
   │     │     │  │  │  ├─ hashtable_debug_hooks.h
   │     │     │  │  │  ├─ hash_function_defaults.h
   │     │     │  │  │  ├─ hash_policy_traits.h
   │     │     │  │  │  ├─ inlined_vector.h
   │     │     │  │  │  ├─ layout.h
   │     │     │  │  │  ├─ node_slot_policy.h
   │     │     │  │  │  ├─ raw_hash_map.h
   │     │     │  │  │  ├─ raw_hash_set.h
   │     │     │  │  │  └─ raw_hash_set_resize_impl.h
   │     │     │  │  ├─ node_hash_map.h
   │     │     │  │  └─ node_hash_set.h
   │     │     │  ├─ crc
   │     │     │  │  ├─ crc32c.h
   │     │     │  │  └─ internal
   │     │     │  │     ├─ cpu_detect.h
   │     │     │  │     ├─ crc.h
   │     │     │  │     ├─ crc32c.h
   │     │     │  │     ├─ crc32c_inline.h
   │     │     │  │     ├─ crc32_x86_arm_combined_simd.h
   │     │     │  │     ├─ crc_cord_state.h
   │     │     │  │     ├─ crc_internal.h
   │     │     │  │     ├─ crc_memcpy.h
   │     │     │  │     ├─ non_temporal_arm_intrinsics.h
   │     │     │  │     └─ non_temporal_memcpy.h
   │     │     │  ├─ debugging
   │     │     │  │  ├─ internal
   │     │     │  │  │  ├─ addresses.h
   │     │     │  │  │  ├─ address_is_readable.h
   │     │     │  │  │  ├─ bounded_utf8_length_sequence.h
   │     │     │  │  │  ├─ decode_rust_punycode.h
   │     │     │  │  │  ├─ demangle.h
   │     │     │  │  │  ├─ demangle_rust.h
   │     │     │  │  │  ├─ elf_mem_image.h
   │     │     │  │  │  ├─ examine_stack.h
   │     │     │  │  │  ├─ stacktrace_aarch64-inl.inc
   │     │     │  │  │  ├─ stacktrace_arm-inl.inc
   │     │     │  │  │  ├─ stacktrace_config.h
   │     │     │  │  │  ├─ stacktrace_emscripten-inl.inc
   │     │     │  │  │  ├─ stacktrace_generic-inl.inc
   │     │     │  │  │  ├─ stacktrace_powerpc-inl.inc
   │     │     │  │  │  ├─ stacktrace_riscv-inl.inc
   │     │     │  │  │  ├─ stacktrace_unimplemented-inl.inc
   │     │     │  │  │  ├─ stacktrace_win32-inl.inc
   │     │     │  │  │  ├─ stacktrace_x86-inl.inc
   │     │     │  │  │  ├─ symbolize.h
   │     │     │  │  │  ├─ utf8_for_code_point.h
   │     │     │  │  │  └─ vdso_support.h
   │     │     │  │  ├─ leak_check.h
   │     │     │  │  ├─ stacktrace.h
   │     │     │  │  ├─ symbolize.h
   │     │     │  │  ├─ symbolize_darwin.inc
   │     │     │  │  ├─ symbolize_elf.inc
   │     │     │  │  ├─ symbolize_emscripten.inc
   │     │     │  │  ├─ symbolize_unimplemented.inc
   │     │     │  │  └─ symbolize_win32.inc
   │     │     │  ├─ flags
   │     │     │  │  ├─ commandlineflag.h
   │     │     │  │  ├─ config.h
   │     │     │  │  ├─ declare.h
   │     │     │  │  ├─ flag.h
   │     │     │  │  ├─ internal
   │     │     │  │  │  ├─ commandlineflag.h
   │     │     │  │  │  ├─ flag.h
   │     │     │  │  │  ├─ path_util.h
   │     │     │  │  │  ├─ private_handle_accessor.h
   │     │     │  │  │  ├─ program_name.h
   │     │     │  │  │  ├─ registry.h
   │     │     │  │  │  └─ sequence_lock.h
   │     │     │  │  ├─ marshalling.h
   │     │     │  │  ├─ reflection.h
   │     │     │  │  └─ usage_config.h
   │     │     │  ├─ functional
   │     │     │  │  ├─ any_invocable.h
   │     │     │  │  ├─ bind_front.h
   │     │     │  │  ├─ function_ref.h
   │     │     │  │  ├─ internal
   │     │     │  │  │  ├─ any_invocable.h
   │     │     │  │  │  ├─ front_binder.h
   │     │     │  │  │  └─ function_ref.h
   │     │     │  │  └─ overload.h
   │     │     │  ├─ hash
   │     │     │  │  ├─ hash.h
   │     │     │  │  └─ internal
   │     │     │  │     ├─ city.h
   │     │     │  │     ├─ hash.h
   │     │     │  │     └─ weakly_mixed_integer.h
   │     │     │  ├─ log
   │     │     │  │  ├─ absl_check.h
   │     │     │  │  ├─ absl_log.h
   │     │     │  │  ├─ absl_vlog_is_on.h
   │     │     │  │  ├─ check.h
   │     │     │  │  ├─ die_if_null.h
   │     │     │  │  ├─ globals.h
   │     │     │  │  ├─ internal
   │     │     │  │  │  ├─ append_truncated.h
   │     │     │  │  │  ├─ check_impl.h
   │     │     │  │  │  ├─ check_op.h
   │     │     │  │  │  ├─ conditions.h
   │     │     │  │  │  ├─ config.h
   │     │     │  │  │  ├─ fnmatch.h
   │     │     │  │  │  ├─ globals.h
   │     │     │  │  │  ├─ log_format.h
   │     │     │  │  │  ├─ log_impl.h
   │     │     │  │  │  ├─ log_message.h
   │     │     │  │  │  ├─ log_sink_set.h
   │     │     │  │  │  ├─ nullguard.h
   │     │     │  │  │  ├─ nullstream.h
   │     │     │  │  │  ├─ proto.h
   │     │     │  │  │  ├─ strip.h
   │     │     │  │  │  ├─ structured_proto.h
   │     │     │  │  │  ├─ vlog_config.h
   │     │     │  │  │  └─ voidify.h
   │     │     │  │  ├─ log.h
   │     │     │  │  ├─ log_entry.h
   │     │     │  │  ├─ log_sink.h
   │     │     │  │  ├─ log_sink_registry.h
   │     │     │  │  └─ vlog_is_on.h
   │     │     │  ├─ memory
   │     │     │  │  └─ memory.h
   │     │     │  ├─ meta
   │     │     │  │  └─ type_traits.h
   │     │     │  ├─ numeric
   │     │     │  │  ├─ bits.h
   │     │     │  │  ├─ int128.h
   │     │     │  │  ├─ int128_have_intrinsic.inc
   │     │     │  │  ├─ int128_no_intrinsic.inc
   │     │     │  │  └─ internal
   │     │     │  │     ├─ bits.h
   │     │     │  │     └─ representation.h
   │     │     │  ├─ profiling
   │     │     │  │  └─ internal
   │     │     │  │     ├─ exponential_biased.h
   │     │     │  │     └─ sample_recorder.h
   │     │     │  ├─ random
   │     │     │  │  ├─ bernoulli_distribution.h
   │     │     │  │  ├─ beta_distribution.h
   │     │     │  │  ├─ bit_gen_ref.h
   │     │     │  │  ├─ discrete_distribution.h
   │     │     │  │  ├─ distributions.h
   │     │     │  │  ├─ exponential_distribution.h
   │     │     │  │  ├─ gaussian_distribution.h
   │     │     │  │  ├─ internal
   │     │     │  │  │  ├─ distribution_caller.h
   │     │     │  │  │  ├─ entropy_pool.h
   │     │     │  │  │  ├─ fastmath.h
   │     │     │  │  │  ├─ fast_uniform_bits.h
   │     │     │  │  │  ├─ generate_real.h
   │     │     │  │  │  ├─ iostream_state_saver.h
   │     │     │  │  │  ├─ nonsecure_base.h
   │     │     │  │  │  ├─ pcg_engine.h
   │     │     │  │  │  ├─ platform.h
   │     │     │  │  │  ├─ randen.h
   │     │     │  │  │  ├─ randen_detect.h
   │     │     │  │  │  ├─ randen_engine.h
   │     │     │  │  │  ├─ randen_hwaes.h
   │     │     │  │  │  ├─ randen_slow.h
   │     │     │  │  │  ├─ randen_traits.h
   │     │     │  │  │  ├─ salted_seed_seq.h
   │     │     │  │  │  ├─ seed_material.h
   │     │     │  │  │  ├─ traits.h
   │     │     │  │  │  ├─ uniform_helper.h
   │     │     │  │  │  └─ wide_multiply.h
   │     │     │  │  ├─ log_uniform_int_distribution.h
   │     │     │  │  ├─ poisson_distribution.h
   │     │     │  │  ├─ random.h
   │     │     │  │  ├─ seed_gen_exception.h
   │     │     │  │  ├─ seed_sequences.h
   │     │     │  │  ├─ uniform_int_distribution.h
   │     │     │  │  ├─ uniform_real_distribution.h
   │     │     │  │  └─ zipf_distribution.h
   │     │     │  ├─ status
   │     │     │  │  ├─ internal
   │     │     │  │  │  ├─ statusor_internal.h
   │     │     │  │  │  └─ status_internal.h
   │     │     │  │  ├─ status.h
   │     │     │  │  ├─ statusor.h
   │     │     │  │  └─ status_payload_printer.h
   │     │     │  ├─ strings
   │     │     │  │  ├─ ascii.h
   │     │     │  │  ├─ charconv.h
   │     │     │  │  ├─ charset.h
   │     │     │  │  ├─ cord.h
   │     │     │  │  ├─ cord_analysis.h
   │     │     │  │  ├─ cord_buffer.h
   │     │     │  │  ├─ escaping.h
   │     │     │  │  ├─ has_absl_stringify.h
   │     │     │  │  ├─ has_ostream_operator.h
   │     │     │  │  ├─ internal
   │     │     │  │  │  ├─ charconv_bigint.h
   │     │     │  │  │  ├─ charconv_parse.h
   │     │     │  │  │  ├─ cordz_functions.h
   │     │     │  │  │  ├─ cordz_handle.h
   │     │     │  │  │  ├─ cordz_info.h
   │     │     │  │  │  ├─ cordz_statistics.h
   │     │     │  │  │  ├─ cordz_update_scope.h
   │     │     │  │  │  ├─ cordz_update_tracker.h
   │     │     │  │  │  ├─ cord_data_edge.h
   │     │     │  │  │  ├─ cord_internal.h
   │     │     │  │  │  ├─ cord_rep_btree.h
   │     │     │  │  │  ├─ cord_rep_btree_navigator.h
   │     │     │  │  │  ├─ cord_rep_btree_reader.h
   │     │     │  │  │  ├─ cord_rep_consume.h
   │     │     │  │  │  ├─ cord_rep_crc.h
   │     │     │  │  │  ├─ cord_rep_flat.h
   │     │     │  │  │  ├─ damerau_levenshtein_distance.h
   │     │     │  │  │  ├─ escaping.h
   │     │     │  │  │  ├─ memutil.h
   │     │     │  │  │  ├─ ostringstream.h
   │     │     │  │  │  ├─ resize_uninitialized.h
   │     │     │  │  │  ├─ stl_type_traits.h
   │     │     │  │  │  ├─ stringify_sink.h
   │     │     │  │  │  ├─ string_constant.h
   │     │     │  │  │  ├─ str_format
   │     │     │  │  │  │  ├─ arg.h
   │     │     │  │  │  │  ├─ bind.h
   │     │     │  │  │  │  ├─ checker.h
   │     │     │  │  │  │  ├─ constexpr_parser.h
   │     │     │  │  │  │  ├─ extension.h
   │     │     │  │  │  │  ├─ float_conversion.h
   │     │     │  │  │  │  ├─ output.h
   │     │     │  │  │  │  └─ parser.h
   │     │     │  │  │  ├─ str_join_internal.h
   │     │     │  │  │  ├─ str_split_internal.h
   │     │     │  │  │  └─ utf8.h
   │     │     │  │  ├─ match.h
   │     │     │  │  ├─ numbers.h
   │     │     │  │  ├─ string_view.h
   │     │     │  │  ├─ strip.h
   │     │     │  │  ├─ str_cat.h
   │     │     │  │  ├─ str_format.h
   │     │     │  │  ├─ str_join.h
   │     │     │  │  ├─ str_replace.h
   │     │     │  │  ├─ str_split.h
   │     │     │  │  └─ substitute.h
   │     │     │  ├─ synchronization
   │     │     │  │  ├─ barrier.h
   │     │     │  │  ├─ blocking_counter.h
   │     │     │  │  ├─ internal
   │     │     │  │  │  ├─ create_thread_identity.h
   │     │     │  │  │  ├─ futex.h
   │     │     │  │  │  ├─ futex_waiter.h
   │     │     │  │  │  ├─ graphcycles.h
   │     │     │  │  │  ├─ kernel_timeout.h
   │     │     │  │  │  ├─ per_thread_sem.h
   │     │     │  │  │  ├─ pthread_waiter.h
   │     │     │  │  │  ├─ sem_waiter.h
   │     │     │  │  │  ├─ stdcpp_waiter.h
   │     │     │  │  │  ├─ waiter.h
   │     │     │  │  │  ├─ waiter_base.h
   │     │     │  │  │  └─ win32_waiter.h
   │     │     │  │  ├─ mutex.h
   │     │     │  │  └─ notification.h
   │     │     │  ├─ time
   │     │     │  │  ├─ civil_time.h
   │     │     │  │  ├─ clock.h
   │     │     │  │  ├─ internal
   │     │     │  │  │  ├─ cctz
   │     │     │  │  │  │  ├─ include
   │     │     │  │  │  │  │  └─ cctz
   │     │     │  │  │  │  │     ├─ civil_time.h
   │     │     │  │  │  │  │     ├─ civil_time_detail.h
   │     │     │  │  │  │  │     ├─ time_zone.h
   │     │     │  │  │  │  │     └─ zone_info_source.h
   │     │     │  │  │  │  └─ src
   │     │     │  │  │  │     ├─ time_zone_fixed.h
   │     │     │  │  │  │     ├─ time_zone_if.h
   │     │     │  │  │  │     ├─ time_zone_impl.h
   │     │     │  │  │  │     ├─ time_zone_info.h
   │     │     │  │  │  │     ├─ time_zone_libc.h
   │     │     │  │  │  │     ├─ time_zone_posix.h
   │     │     │  │  │  │     └─ tzfile.h
   │     │     │  │  │  ├─ get_current_time_chrono.inc
   │     │     │  │  │  └─ get_current_time_posix.inc
   │     │     │  │  └─ time.h
   │     │     │  ├─ types
   │     │     │  │  ├─ compare.h
   │     │     │  │  ├─ internal
   │     │     │  │  │  └─ span.h
   │     │     │  │  ├─ optional.h
   │     │     │  │  ├─ span.h
   │     │     │  │  └─ variant.h
   │     │     │  └─ utility
   │     │     │     └─ utility.h
   │     │     ├─ ducc
   │     │     │  └─ google
   │     │     │     ├─ ducc0_custom_lowlevel_threading.h
   │     │     │     ├─ fft.h
   │     │     │     └─ threading.h
   │     │     ├─ Eigen
   │     │     │  ├─ AccelerateSupport
   │     │     │  ├─ Cholesky
   │     │     │  ├─ CholmodSupport
   │     │     │  ├─ Core
   │     │     │  ├─ Dense
   │     │     │  ├─ Eigen
   │     │     │  ├─ Eigenvalues
   │     │     │  ├─ Geometry
   │     │     │  ├─ Householder
   │     │     │  ├─ IterativeLinearSolvers
   │     │     │  ├─ Jacobi
   │     │     │  ├─ KLUSupport
   │     │     │  ├─ LU
   │     │     │  ├─ MetisSupport
   │     │     │  ├─ OrderingMethods
   │     │     │  ├─ PardisoSupport
   │     │     │  ├─ PaStiXSupport
   │     │     │  ├─ QR
   │     │     │  ├─ QtAlignedMalloc
   │     │     │  ├─ Sparse
   │     │     │  ├─ SparseCholesky
   │     │     │  ├─ SparseCore
   │     │     │  ├─ SparseLU
   │     │     │  ├─ SparseQR
   │     │     │  ├─ SPQRSupport
   │     │     │  ├─ src
   │     │     │  │  ├─ AccelerateSupport
   │     │     │  │  │  ├─ AccelerateSupport.h
   │     │     │  │  │  └─ InternalHeaderCheck.h
   │     │     │  │  ├─ Cholesky
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ LDLT.h
   │     │     │  │  │  ├─ LLT.h
   │     │     │  │  │  └─ LLT_LAPACKE.h
   │     │     │  │  ├─ CholmodSupport
   │     │     │  │  │  ├─ CholmodSupport.h
   │     │     │  │  │  └─ InternalHeaderCheck.h
   │     │     │  │  ├─ Core
   │     │     │  │  │  ├─ arch
   │     │     │  │  │  │  ├─ AltiVec
   │     │     │  │  │  │  │  ├─ Complex.h
   │     │     │  │  │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  │  │  ├─ MatrixProduct.h
   │     │     │  │  │  │  │  ├─ MatrixProductCommon.h
   │     │     │  │  │  │  │  ├─ MatrixProductMMA.h
   │     │     │  │  │  │  │  ├─ MatrixProductMMAbfloat16.h
   │     │     │  │  │  │  │  ├─ MatrixVectorProduct.inc
   │     │     │  │  │  │  │  ├─ PacketMath.h
   │     │     │  │  │  │  │  └─ TypeCasting.h
   │     │     │  │  │  │  ├─ AVX
   │     │     │  │  │  │  │  ├─ Complex.h
   │     │     │  │  │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  │  │  ├─ PacketMath.h
   │     │     │  │  │  │  │  ├─ Reductions.h
   │     │     │  │  │  │  │  └─ TypeCasting.h
   │     │     │  │  │  │  ├─ AVX512
   │     │     │  │  │  │  │  ├─ Complex.h
   │     │     │  │  │  │  │  ├─ GemmKernel.h
   │     │     │  │  │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  │  │  ├─ MathFunctionsFP16.h
   │     │     │  │  │  │  │  ├─ PacketMath.h
   │     │     │  │  │  │  │  ├─ PacketMathFP16.h
   │     │     │  │  │  │  │  ├─ Reductions.h
   │     │     │  │  │  │  │  ├─ TrsmKernel.h
   │     │     │  │  │  │  │  ├─ TrsmUnrolls.inc
   │     │     │  │  │  │  │  ├─ TypeCasting.h
   │     │     │  │  │  │  │  └─ TypeCastingFP16.h
   │     │     │  │  │  │  ├─ clang
   │     │     │  │  │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  │  │  ├─ PacketMath.h
   │     │     │  │  │  │  │  ├─ Reductions.h
   │     │     │  │  │  │  │  └─ TypeCasting.h
   │     │     │  │  │  │  ├─ Default
   │     │     │  │  │  │  │  ├─ BFloat16.h
   │     │     │  │  │  │  │  ├─ ConjHelper.h
   │     │     │  │  │  │  │  ├─ GenericPacketMathFunctions.h
   │     │     │  │  │  │  │  ├─ GenericPacketMathFunctionsFwd.h
   │     │     │  │  │  │  │  ├─ Half.h
   │     │     │  │  │  │  │  └─ Settings.h
   │     │     │  │  │  │  ├─ GPU
   │     │     │  │  │  │  │  ├─ Complex.h
   │     │     │  │  │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  │  │  ├─ PacketMath.h
   │     │     │  │  │  │  │  ├─ Tuple.h
   │     │     │  │  │  │  │  └─ TypeCasting.h
   │     │     │  │  │  │  ├─ HIP
   │     │     │  │  │  │  │  └─ hcc
   │     │     │  │  │  │  │     └─ math_constants.h
   │     │     │  │  │  │  ├─ HVX
   │     │     │  │  │  │  │  └─ PacketMath.h
   │     │     │  │  │  │  ├─ LSX
   │     │     │  │  │  │  │  ├─ Complex.h
   │     │     │  │  │  │  │  ├─ GeneralBlockPanelKernel.h
   │     │     │  │  │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  │  │  ├─ PacketMath.h
   │     │     │  │  │  │  │  └─ TypeCasting.h
   │     │     │  │  │  │  ├─ MSA
   │     │     │  │  │  │  │  ├─ Complex.h
   │     │     │  │  │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  │  │  └─ PacketMath.h
   │     │     │  │  │  │  ├─ NEON
   │     │     │  │  │  │  │  ├─ Complex.h
   │     │     │  │  │  │  │  ├─ GeneralBlockPanelKernel.h
   │     │     │  │  │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  │  │  ├─ PacketMath.h
   │     │     │  │  │  │  │  ├─ TypeCasting.h
   │     │     │  │  │  │  │  └─ UnaryFunctors.h
   │     │     │  │  │  │  ├─ SSE
   │     │     │  │  │  │  │  ├─ Complex.h
   │     │     │  │  │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  │  │  ├─ PacketMath.h
   │     │     │  │  │  │  │  ├─ Reductions.h
   │     │     │  │  │  │  │  └─ TypeCasting.h
   │     │     │  │  │  │  ├─ SVE
   │     │     │  │  │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  │  │  ├─ PacketMath.h
   │     │     │  │  │  │  │  └─ TypeCasting.h
   │     │     │  │  │  │  ├─ SYCL
   │     │     │  │  │  │  │  ├─ InteropHeaders.h
   │     │     │  │  │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  │  │  ├─ PacketMath.h
   │     │     │  │  │  │  │  └─ TypeCasting.h
   │     │     │  │  │  │  └─ ZVector
   │     │     │  │  │  │     ├─ Complex.h
   │     │     │  │  │  │     ├─ MathFunctions.h
   │     │     │  │  │  │     └─ PacketMath.h
   │     │     │  │  │  ├─ ArithmeticSequence.h
   │     │     │  │  │  ├─ Array.h
   │     │     │  │  │  ├─ ArrayBase.h
   │     │     │  │  │  ├─ ArrayWrapper.h
   │     │     │  │  │  ├─ Assign.h
   │     │     │  │  │  ├─ AssignEvaluator.h
   │     │     │  │  │  ├─ Assign_MKL.h
   │     │     │  │  │  ├─ BandMatrix.h
   │     │     │  │  │  ├─ Block.h
   │     │     │  │  │  ├─ CommaInitializer.h
   │     │     │  │  │  ├─ ConditionEstimator.h
   │     │     │  │  │  ├─ CoreEvaluators.h
   │     │     │  │  │  ├─ CoreIterators.h
   │     │     │  │  │  ├─ CwiseBinaryOp.h
   │     │     │  │  │  ├─ CwiseNullaryOp.h
   │     │     │  │  │  ├─ CwiseTernaryOp.h
   │     │     │  │  │  ├─ CwiseUnaryOp.h
   │     │     │  │  │  ├─ CwiseUnaryView.h
   │     │     │  │  │  ├─ DenseBase.h
   │     │     │  │  │  ├─ DenseCoeffsBase.h
   │     │     │  │  │  ├─ DenseStorage.h
   │     │     │  │  │  ├─ DeviceWrapper.h
   │     │     │  │  │  ├─ Diagonal.h
   │     │     │  │  │  ├─ DiagonalMatrix.h
   │     │     │  │  │  ├─ DiagonalProduct.h
   │     │     │  │  │  ├─ Dot.h
   │     │     │  │  │  ├─ EigenBase.h
   │     │     │  │  │  ├─ Fill.h
   │     │     │  │  │  ├─ FindCoeff.h
   │     │     │  │  │  ├─ ForceAlignedAccess.h
   │     │     │  │  │  ├─ functors
   │     │     │  │  │  │  ├─ AssignmentFunctors.h
   │     │     │  │  │  │  ├─ BinaryFunctors.h
   │     │     │  │  │  │  ├─ NullaryFunctors.h
   │     │     │  │  │  │  ├─ StlFunctors.h
   │     │     │  │  │  │  ├─ TernaryFunctors.h
   │     │     │  │  │  │  └─ UnaryFunctors.h
   │     │     │  │  │  ├─ Fuzzy.h
   │     │     │  │  │  ├─ GeneralProduct.h
   │     │     │  │  │  ├─ GenericPacketMath.h
   │     │     │  │  │  ├─ GlobalFunctions.h
   │     │     │  │  │  ├─ IndexedView.h
   │     │     │  │  │  ├─ InnerProduct.h
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ Inverse.h
   │     │     │  │  │  ├─ IO.h
   │     │     │  │  │  ├─ Map.h
   │     │     │  │  │  ├─ MapBase.h
   │     │     │  │  │  ├─ MathFunctions.h
   │     │     │  │  │  ├─ MathFunctionsImpl.h
   │     │     │  │  │  ├─ Matrix.h
   │     │     │  │  │  ├─ MatrixBase.h
   │     │     │  │  │  ├─ NestByValue.h
   │     │     │  │  │  ├─ NoAlias.h
   │     │     │  │  │  ├─ NumTraits.h
   │     │     │  │  │  ├─ PartialReduxEvaluator.h
   │     │     │  │  │  ├─ PermutationMatrix.h
   │     │     │  │  │  ├─ PlainObjectBase.h
   │     │     │  │  │  ├─ Product.h
   │     │     │  │  │  ├─ ProductEvaluators.h
   │     │     │  │  │  ├─ products
   │     │     │  │  │  │  ├─ GeneralBlockPanelKernel.h
   │     │     │  │  │  │  ├─ GeneralMatrixMatrix.h
   │     │     │  │  │  │  ├─ GeneralMatrixMatrixTriangular.h
   │     │     │  │  │  │  ├─ GeneralMatrixMatrixTriangular_BLAS.h
   │     │     │  │  │  │  ├─ GeneralMatrixMatrix_BLAS.h
   │     │     │  │  │  │  ├─ GeneralMatrixVector.h
   │     │     │  │  │  │  ├─ GeneralMatrixVector_BLAS.h
   │     │     │  │  │  │  ├─ Parallelizer.h
   │     │     │  │  │  │  ├─ SelfadjointMatrixMatrix.h
   │     │     │  │  │  │  ├─ SelfadjointMatrixMatrix_BLAS.h
   │     │     │  │  │  │  ├─ SelfadjointMatrixVector.h
   │     │     │  │  │  │  ├─ SelfadjointMatrixVector_BLAS.h
   │     │     │  │  │  │  ├─ SelfadjointProduct.h
   │     │     │  │  │  │  ├─ SelfadjointRank2Update.h
   │     │     │  │  │  │  ├─ TriangularMatrixMatrix.h
   │     │     │  │  │  │  ├─ TriangularMatrixMatrix_BLAS.h
   │     │     │  │  │  │  ├─ TriangularMatrixVector.h
   │     │     │  │  │  │  ├─ TriangularMatrixVector_BLAS.h
   │     │     │  │  │  │  ├─ TriangularSolverMatrix.h
   │     │     │  │  │  │  ├─ TriangularSolverMatrix_BLAS.h
   │     │     │  │  │  │  └─ TriangularSolverVector.h
   │     │     │  │  │  ├─ Random.h
   │     │     │  │  │  ├─ RandomImpl.h
   │     │     │  │  │  ├─ RealView.h
   │     │     │  │  │  ├─ Redux.h
   │     │     │  │  │  ├─ Ref.h
   │     │     │  │  │  ├─ Replicate.h
   │     │     │  │  │  ├─ Reshaped.h
   │     │     │  │  │  ├─ ReturnByValue.h
   │     │     │  │  │  ├─ Reverse.h
   │     │     │  │  │  ├─ Select.h
   │     │     │  │  │  ├─ SelfAdjointView.h
   │     │     │  │  │  ├─ SelfCwiseBinaryOp.h
   │     │     │  │  │  ├─ SkewSymmetricMatrix3.h
   │     │     │  │  │  ├─ Solve.h
   │     │     │  │  │  ├─ SolverBase.h
   │     │     │  │  │  ├─ SolveTriangular.h
   │     │     │  │  │  ├─ StableNorm.h
   │     │     │  │  │  ├─ StlIterators.h
   │     │     │  │  │  ├─ Stride.h
   │     │     │  │  │  ├─ Swap.h
   │     │     │  │  │  ├─ Transpose.h
   │     │     │  │  │  ├─ Transpositions.h
   │     │     │  │  │  ├─ TriangularMatrix.h
   │     │     │  │  │  ├─ util
   │     │     │  │  │  │  ├─ Assert.h
   │     │     │  │  │  │  ├─ BlasUtil.h
   │     │     │  │  │  │  ├─ ConfigureVectorization.h
   │     │     │  │  │  │  ├─ Constants.h
   │     │     │  │  │  │  ├─ DisableStupidWarnings.h
   │     │     │  │  │  │  ├─ EmulateArray.h
   │     │     │  │  │  │  ├─ ForwardDeclarations.h
   │     │     │  │  │  │  ├─ GpuHipCudaDefines.inc
   │     │     │  │  │  │  ├─ GpuHipCudaUndefines.inc
   │     │     │  │  │  │  ├─ IndexedViewHelper.h
   │     │     │  │  │  │  ├─ IntegralConstant.h
   │     │     │  │  │  │  ├─ Macros.h
   │     │     │  │  │  │  ├─ MaxSizeVector.h
   │     │     │  │  │  │  ├─ Memory.h
   │     │     │  │  │  │  ├─ Meta.h
   │     │     │  │  │  │  ├─ MKL_support.h
   │     │     │  │  │  │  ├─ MoreMeta.h
   │     │     │  │  │  │  ├─ ReenableStupidWarnings.h
   │     │     │  │  │  │  ├─ ReshapedHelper.h
   │     │     │  │  │  │  ├─ Serializer.h
   │     │     │  │  │  │  ├─ StaticAssert.h
   │     │     │  │  │  │  ├─ SymbolicIndex.h
   │     │     │  │  │  │  └─ XprHelper.h
   │     │     │  │  │  ├─ VectorBlock.h
   │     │     │  │  │  ├─ VectorwiseOp.h
   │     │     │  │  │  └─ Visitor.h
   │     │     │  │  ├─ Eigenvalues
   │     │     │  │  │  ├─ ComplexEigenSolver.h
   │     │     │  │  │  ├─ ComplexQZ.h
   │     │     │  │  │  ├─ ComplexSchur.h
   │     │     │  │  │  ├─ ComplexSchur_LAPACKE.h
   │     │     │  │  │  ├─ EigenSolver.h
   │     │     │  │  │  ├─ GeneralizedEigenSolver.h
   │     │     │  │  │  ├─ GeneralizedSelfAdjointEigenSolver.h
   │     │     │  │  │  ├─ HessenbergDecomposition.h
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ MatrixBaseEigenvalues.h
   │     │     │  │  │  ├─ RealQZ.h
   │     │     │  │  │  ├─ RealSchur.h
   │     │     │  │  │  ├─ RealSchur_LAPACKE.h
   │     │     │  │  │  ├─ SelfAdjointEigenSolver.h
   │     │     │  │  │  ├─ SelfAdjointEigenSolver_LAPACKE.h
   │     │     │  │  │  └─ Tridiagonalization.h
   │     │     │  │  ├─ Geometry
   │     │     │  │  │  ├─ AlignedBox.h
   │     │     │  │  │  ├─ AngleAxis.h
   │     │     │  │  │  ├─ arch
   │     │     │  │  │  │  └─ Geometry_SIMD.h
   │     │     │  │  │  ├─ EulerAngles.h
   │     │     │  │  │  ├─ Homogeneous.h
   │     │     │  │  │  ├─ Hyperplane.h
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ OrthoMethods.h
   │     │     │  │  │  ├─ ParametrizedLine.h
   │     │     │  │  │  ├─ Quaternion.h
   │     │     │  │  │  ├─ Rotation2D.h
   │     │     │  │  │  ├─ RotationBase.h
   │     │     │  │  │  ├─ Scaling.h
   │     │     │  │  │  ├─ Transform.h
   │     │     │  │  │  ├─ Translation.h
   │     │     │  │  │  └─ Umeyama.h
   │     │     │  │  ├─ Householder
   │     │     │  │  │  ├─ BlockHouseholder.h
   │     │     │  │  │  ├─ Householder.h
   │     │     │  │  │  ├─ HouseholderSequence.h
   │     │     │  │  │  └─ InternalHeaderCheck.h
   │     │     │  │  ├─ IterativeLinearSolvers
   │     │     │  │  │  ├─ BasicPreconditioners.h
   │     │     │  │  │  ├─ BiCGSTAB.h
   │     │     │  │  │  ├─ ConjugateGradient.h
   │     │     │  │  │  ├─ IncompleteCholesky.h
   │     │     │  │  │  ├─ IncompleteLUT.h
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ IterativeSolverBase.h
   │     │     │  │  │  ├─ LeastSquareConjugateGradient.h
   │     │     │  │  │  └─ SolveWithGuess.h
   │     │     │  │  ├─ Jacobi
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  └─ Jacobi.h
   │     │     │  │  ├─ KLUSupport
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  └─ KLUSupport.h
   │     │     │  │  ├─ LU
   │     │     │  │  │  ├─ arch
   │     │     │  │  │  │  └─ InverseSize4.h
   │     │     │  │  │  ├─ Determinant.h
   │     │     │  │  │  ├─ FullPivLU.h
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ InverseImpl.h
   │     │     │  │  │  ├─ PartialPivLU.h
   │     │     │  │  │  └─ PartialPivLU_LAPACKE.h
   │     │     │  │  ├─ MetisSupport
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  └─ MetisSupport.h
   │     │     │  │  ├─ misc
   │     │     │  │  │  ├─ blas.h
   │     │     │  │  │  ├─ Image.h
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ Kernel.h
   │     │     │  │  │  ├─ lapacke.h
   │     │     │  │  │  ├─ lapacke_helpers.h
   │     │     │  │  │  └─ lapacke_mangling.h
   │     │     │  │  ├─ OrderingMethods
   │     │     │  │  │  ├─ Amd.h
   │     │     │  │  │  ├─ Eigen_Colamd.h
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  └─ Ordering.h
   │     │     │  │  ├─ PardisoSupport
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  └─ PardisoSupport.h
   │     │     │  │  ├─ PaStiXSupport
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  └─ PaStiXSupport.h
   │     │     │  │  ├─ plugins
   │     │     │  │  │  ├─ ArrayCwiseBinaryOps.inc
   │     │     │  │  │  ├─ ArrayCwiseUnaryOps.inc
   │     │     │  │  │  ├─ BlockMethods.inc
   │     │     │  │  │  ├─ CommonCwiseBinaryOps.inc
   │     │     │  │  │  ├─ CommonCwiseUnaryOps.inc
   │     │     │  │  │  ├─ IndexedViewMethods.inc
   │     │     │  │  │  ├─ InternalHeaderCheck.inc
   │     │     │  │  │  ├─ MatrixCwiseBinaryOps.inc
   │     │     │  │  │  ├─ MatrixCwiseUnaryOps.inc
   │     │     │  │  │  └─ ReshapedMethods.inc
   │     │     │  │  ├─ QR
   │     │     │  │  │  ├─ ColPivHouseholderQR.h
   │     │     │  │  │  ├─ ColPivHouseholderQR_LAPACKE.h
   │     │     │  │  │  ├─ CompleteOrthogonalDecomposition.h
   │     │     │  │  │  ├─ FullPivHouseholderQR.h
   │     │     │  │  │  ├─ HouseholderQR.h
   │     │     │  │  │  ├─ HouseholderQR_LAPACKE.h
   │     │     │  │  │  └─ InternalHeaderCheck.h
   │     │     │  │  ├─ SparseCholesky
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ SimplicialCholesky.h
   │     │     │  │  │  └─ SimplicialCholesky_impl.h
   │     │     │  │  ├─ SparseCore
   │     │     │  │  │  ├─ AmbiVector.h
   │     │     │  │  │  ├─ CompressedStorage.h
   │     │     │  │  │  ├─ ConservativeSparseSparseProduct.h
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ SparseAssign.h
   │     │     │  │  │  ├─ SparseBlock.h
   │     │     │  │  │  ├─ SparseColEtree.h
   │     │     │  │  │  ├─ SparseCompressedBase.h
   │     │     │  │  │  ├─ SparseCwiseBinaryOp.h
   │     │     │  │  │  ├─ SparseCwiseUnaryOp.h
   │     │     │  │  │  ├─ SparseDenseProduct.h
   │     │     │  │  │  ├─ SparseDiagonalProduct.h
   │     │     │  │  │  ├─ SparseDot.h
   │     │     │  │  │  ├─ SparseFuzzy.h
   │     │     │  │  │  ├─ SparseMap.h
   │     │     │  │  │  ├─ SparseMatrix.h
   │     │     │  │  │  ├─ SparseMatrixBase.h
   │     │     │  │  │  ├─ SparsePermutation.h
   │     │     │  │  │  ├─ SparseProduct.h
   │     │     │  │  │  ├─ SparseRedux.h
   │     │     │  │  │  ├─ SparseRef.h
   │     │     │  │  │  ├─ SparseSelfAdjointView.h
   │     │     │  │  │  ├─ SparseSolverBase.h
   │     │     │  │  │  ├─ SparseSparseProductWithPruning.h
   │     │     │  │  │  ├─ SparseTranspose.h
   │     │     │  │  │  ├─ SparseTriangularView.h
   │     │     │  │  │  ├─ SparseUtil.h
   │     │     │  │  │  ├─ SparseVector.h
   │     │     │  │  │  ├─ SparseView.h
   │     │     │  │  │  └─ TriangularSolver.h
   │     │     │  │  ├─ SparseLU
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ SparseLU.h
   │     │     │  │  │  ├─ SparseLUImpl.h
   │     │     │  │  │  ├─ SparseLU_column_bmod.h
   │     │     │  │  │  ├─ SparseLU_column_dfs.h
   │     │     │  │  │  ├─ SparseLU_copy_to_ucol.h
   │     │     │  │  │  ├─ SparseLU_heap_relax_snode.h
   │     │     │  │  │  ├─ SparseLU_kernel_bmod.h
   │     │     │  │  │  ├─ SparseLU_Memory.h
   │     │     │  │  │  ├─ SparseLU_panel_bmod.h
   │     │     │  │  │  ├─ SparseLU_panel_dfs.h
   │     │     │  │  │  ├─ SparseLU_pivotL.h
   │     │     │  │  │  ├─ SparseLU_pruneL.h
   │     │     │  │  │  ├─ SparseLU_relax_snode.h
   │     │     │  │  │  ├─ SparseLU_Structs.h
   │     │     │  │  │  ├─ SparseLU_SupernodalMatrix.h
   │     │     │  │  │  └─ SparseLU_Utils.h
   │     │     │  │  ├─ SparseQR
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  └─ SparseQR.h
   │     │     │  │  ├─ SPQRSupport
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  └─ SuiteSparseQRSupport.h
   │     │     │  │  ├─ StlSupport
   │     │     │  │  │  ├─ details.h
   │     │     │  │  │  ├─ StdDeque.h
   │     │     │  │  │  ├─ StdList.h
   │     │     │  │  │  └─ StdVector.h
   │     │     │  │  ├─ SuperLUSupport
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  └─ SuperLUSupport.h
   │     │     │  │  ├─ SVD
   │     │     │  │  │  ├─ BDCSVD.h
   │     │     │  │  │  ├─ BDCSVD_LAPACKE.h
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ JacobiSVD.h
   │     │     │  │  │  ├─ JacobiSVD_LAPACKE.h
   │     │     │  │  │  ├─ SVDBase.h
   │     │     │  │  │  └─ UpperBidiagonalization.h
   │     │     │  │  ├─ ThreadPool
   │     │     │  │  │  ├─ Barrier.h
   │     │     │  │  │  ├─ CoreThreadPoolDevice.h
   │     │     │  │  │  ├─ EventCount.h
   │     │     │  │  │  ├─ ForkJoin.h
   │     │     │  │  │  ├─ InternalHeaderCheck.h
   │     │     │  │  │  ├─ NonBlockingThreadPool.h
   │     │     │  │  │  ├─ RunQueue.h
   │     │     │  │  │  ├─ ThreadCancel.h
   │     │     │  │  │  ├─ ThreadEnvironment.h
   │     │     │  │  │  ├─ ThreadLocal.h
   │     │     │  │  │  ├─ ThreadPoolInterface.h
   │     │     │  │  │  └─ ThreadYield.h
   │     │     │  │  └─ UmfPackSupport
   │     │     │  │     ├─ InternalHeaderCheck.h
   │     │     │  │     └─ UmfPackSupport.h
   │     │     │  ├─ StdDeque
   │     │     │  ├─ StdList
   │     │     │  ├─ StdVector
   │     │     │  ├─ SuperLUSupport
   │     │     │  ├─ SVD
   │     │     │  ├─ ThreadPool
   │     │     │  ├─ UmfPackSupport
   │     │     │  └─ Version
   │     │     └─ external
   │     │        ├─ absl_py
   │     │        │  └─ LICENSE
   │     │        ├─ boringssl
   │     │        │  └─ src
   │     │        │     ├─ crypto
   │     │        │     │  ├─ asn1
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ bio
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ bytestring
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ chacha
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ cipher_extra
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ conf
   │     │        │     │  │  ├─ conf_def.h
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ cpu_arm_linux.h
   │     │        │     │  ├─ curve25519
   │     │        │     │  │  ├─ curve25519_tables.h
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ des
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ dsa
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ ec_extra
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ err
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ evp
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ fipsmodule
   │     │        │     │  │  ├─ aes
   │     │        │     │  │  │  ├─ aes.c
   │     │        │     │  │  │  ├─ aes_nohw.c
   │     │        │     │  │  │  ├─ internal.h
   │     │        │     │  │  │  ├─ key_wrap.c
   │     │        │     │  │  │  └─ mode_wrappers.c
   │     │        │     │  │  ├─ bn
   │     │        │     │  │  │  ├─ add.c
   │     │        │     │  │  │  ├─ asm
   │     │        │     │  │  │  │  └─ x86_64-gcc.c
   │     │        │     │  │  │  ├─ bn.c
   │     │        │     │  │  │  ├─ bytes.c
   │     │        │     │  │  │  ├─ cmp.c
   │     │        │     │  │  │  ├─ ctx.c
   │     │        │     │  │  │  ├─ div.c
   │     │        │     │  │  │  ├─ div_extra.c
   │     │        │     │  │  │  ├─ exponentiation.c
   │     │        │     │  │  │  ├─ gcd.c
   │     │        │     │  │  │  ├─ gcd_extra.c
   │     │        │     │  │  │  ├─ generic.c
   │     │        │     │  │  │  ├─ internal.h
   │     │        │     │  │  │  ├─ jacobi.c
   │     │        │     │  │  │  ├─ montgomery.c
   │     │        │     │  │  │  ├─ montgomery_inv.c
   │     │        │     │  │  │  ├─ mul.c
   │     │        │     │  │  │  ├─ prime.c
   │     │        │     │  │  │  ├─ random.c
   │     │        │     │  │  │  ├─ rsaz_exp.c
   │     │        │     │  │  │  ├─ rsaz_exp.h
   │     │        │     │  │  │  ├─ shift.c
   │     │        │     │  │  │  └─ sqrt.c
   │     │        │     │  │  ├─ cipher
   │     │        │     │  │  │  ├─ aead.c
   │     │        │     │  │  │  ├─ cipher.c
   │     │        │     │  │  │  ├─ e_aes.c
   │     │        │     │  │  │  ├─ e_aesccm.c
   │     │        │     │  │  │  └─ internal.h
   │     │        │     │  │  ├─ cmac
   │     │        │     │  │  │  └─ cmac.c
   │     │        │     │  │  ├─ delocate.h
   │     │        │     │  │  ├─ dh
   │     │        │     │  │  │  ├─ check.c
   │     │        │     │  │  │  ├─ dh.c
   │     │        │     │  │  │  └─ internal.h
   │     │        │     │  │  ├─ digest
   │     │        │     │  │  │  ├─ digest.c
   │     │        │     │  │  │  ├─ digests.c
   │     │        │     │  │  │  ├─ internal.h
   │     │        │     │  │  │  └─ md32_common.h
   │     │        │     │  │  ├─ digestsign
   │     │        │     │  │  │  └─ digestsign.c
   │     │        │     │  │  ├─ ec
   │     │        │     │  │  │  ├─ ec.c
   │     │        │     │  │  │  ├─ ec_key.c
   │     │        │     │  │  │  ├─ ec_montgomery.c
   │     │        │     │  │  │  ├─ felem.c
   │     │        │     │  │  │  ├─ internal.h
   │     │        │     │  │  │  ├─ oct.c
   │     │        │     │  │  │  ├─ p224-64.c
   │     │        │     │  │  │  ├─ p256-nistz-table.h
   │     │        │     │  │  │  ├─ p256-nistz.c
   │     │        │     │  │  │  ├─ p256-nistz.h
   │     │        │     │  │  │  ├─ p256.c
   │     │        │     │  │  │  ├─ p256_table.h
   │     │        │     │  │  │  ├─ scalar.c
   │     │        │     │  │  │  ├─ simple.c
   │     │        │     │  │  │  ├─ simple_mul.c
   │     │        │     │  │  │  ├─ util.c
   │     │        │     │  │  │  └─ wnaf.c
   │     │        │     │  │  ├─ ecdh
   │     │        │     │  │  │  └─ ecdh.c
   │     │        │     │  │  ├─ ecdsa
   │     │        │     │  │  │  ├─ ecdsa.c
   │     │        │     │  │  │  └─ internal.h
   │     │        │     │  │  ├─ hmac
   │     │        │     │  │  │  └─ hmac.c
   │     │        │     │  │  ├─ md4
   │     │        │     │  │  │  └─ md4.c
   │     │        │     │  │  ├─ md5
   │     │        │     │  │  │  ├─ internal.h
   │     │        │     │  │  │  └─ md5.c
   │     │        │     │  │  ├─ modes
   │     │        │     │  │  │  ├─ cbc.c
   │     │        │     │  │  │  ├─ cfb.c
   │     │        │     │  │  │  ├─ ctr.c
   │     │        │     │  │  │  ├─ gcm.c
   │     │        │     │  │  │  ├─ gcm_nohw.c
   │     │        │     │  │  │  ├─ internal.h
   │     │        │     │  │  │  ├─ ofb.c
   │     │        │     │  │  │  └─ polyval.c
   │     │        │     │  │  ├─ rand
   │     │        │     │  │  │  ├─ ctrdrbg.c
   │     │        │     │  │  │  ├─ fork_detect.c
   │     │        │     │  │  │  ├─ fork_detect.h
   │     │        │     │  │  │  ├─ getrandom_fillin.h
   │     │        │     │  │  │  ├─ internal.h
   │     │        │     │  │  │  ├─ rand.c
   │     │        │     │  │  │  └─ urandom.c
   │     │        │     │  │  ├─ rsa
   │     │        │     │  │  │  ├─ blinding.c
   │     │        │     │  │  │  ├─ internal.h
   │     │        │     │  │  │  ├─ padding.c
   │     │        │     │  │  │  ├─ rsa.c
   │     │        │     │  │  │  └─ rsa_impl.c
   │     │        │     │  │  ├─ self_check
   │     │        │     │  │  │  ├─ fips.c
   │     │        │     │  │  │  └─ self_check.c
   │     │        │     │  │  ├─ service_indicator
   │     │        │     │  │  │  ├─ internal.h
   │     │        │     │  │  │  └─ service_indicator.c
   │     │        │     │  │  ├─ sha
   │     │        │     │  │  │  ├─ internal.h
   │     │        │     │  │  │  ├─ sha1.c
   │     │        │     │  │  │  ├─ sha256.c
   │     │        │     │  │  │  └─ sha512.c
   │     │        │     │  │  └─ tls
   │     │        │     │  │     ├─ internal.h
   │     │        │     │  │     └─ kdf.c
   │     │        │     │  ├─ hrss
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ internal.h
   │     │        │     │  ├─ lhash
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ obj
   │     │        │     │  │  └─ obj_dat.h
   │     │        │     │  ├─ pkcs7
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ pkcs8
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ poly1305
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ pool
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ trust_token
   │     │        │     │  │  └─ internal.h
   │     │        │     │  ├─ x509
   │     │        │     │  │  └─ internal.h
   │     │        │     │  └─ x509v3
   │     │        │     │     ├─ ext_dat.h
   │     │        │     │     └─ internal.h
   │     │        │     ├─ include
   │     │        │     │  └─ openssl
   │     │        │     │     ├─ aead.h
   │     │        │     │     ├─ aes.h
   │     │        │     │     ├─ arm_arch.h
   │     │        │     │     ├─ asn1.h
   │     │        │     │     ├─ asn1t.h
   │     │        │     │     ├─ asn1_mac.h
   │     │        │     │     ├─ base.h
   │     │        │     │     ├─ base64.h
   │     │        │     │     ├─ bio.h
   │     │        │     │     ├─ blake2.h
   │     │        │     │     ├─ blowfish.h
   │     │        │     │     ├─ bn.h
   │     │        │     │     ├─ buf.h
   │     │        │     │     ├─ buffer.h
   │     │        │     │     ├─ bytestring.h
   │     │        │     │     ├─ cast.h
   │     │        │     │     ├─ chacha.h
   │     │        │     │     ├─ cipher.h
   │     │        │     │     ├─ cmac.h
   │     │        │     │     ├─ conf.h
   │     │        │     │     ├─ cpu.h
   │     │        │     │     ├─ crypto.h
   │     │        │     │     ├─ ctrdrbg.h
   │     │        │     │     ├─ curve25519.h
   │     │        │     │     ├─ des.h
   │     │        │     │     ├─ dh.h
   │     │        │     │     ├─ digest.h
   │     │        │     │     ├─ dsa.h
   │     │        │     │     ├─ dtls1.h
   │     │        │     │     ├─ ec.h
   │     │        │     │     ├─ ecdh.h
   │     │        │     │     ├─ ecdsa.h
   │     │        │     │     ├─ ec_key.h
   │     │        │     │     ├─ engine.h
   │     │        │     │     ├─ err.h
   │     │        │     │     ├─ evp.h
   │     │        │     │     ├─ evp_errors.h
   │     │        │     │     ├─ ex_data.h
   │     │        │     │     ├─ e_os2.h
   │     │        │     │     ├─ hkdf.h
   │     │        │     │     ├─ hmac.h
   │     │        │     │     ├─ hpke.h
   │     │        │     │     ├─ hrss.h
   │     │        │     │     ├─ is_boringssl.h
   │     │        │     │     ├─ kdf.h
   │     │        │     │     ├─ lhash.h
   │     │        │     │     ├─ md4.h
   │     │        │     │     ├─ md5.h
   │     │        │     │     ├─ mem.h
   │     │        │     │     ├─ nid.h
   │     │        │     │     ├─ obj.h
   │     │        │     │     ├─ objects.h
   │     │        │     │     ├─ obj_mac.h
   │     │        │     │     ├─ opensslconf.h
   │     │        │     │     ├─ opensslv.h
   │     │        │     │     ├─ ossl_typ.h
   │     │        │     │     ├─ pem.h
   │     │        │     │     ├─ pkcs12.h
   │     │        │     │     ├─ pkcs7.h
   │     │        │     │     ├─ pkcs8.h
   │     │        │     │     ├─ poly1305.h
   │     │        │     │     ├─ pool.h
   │     │        │     │     ├─ rand.h
   │     │        │     │     ├─ rc4.h
   │     │        │     │     ├─ ripemd.h
   │     │        │     │     ├─ rsa.h
   │     │        │     │     ├─ safestack.h
   │     │        │     │     ├─ service_indicator.h
   │     │        │     │     ├─ sha.h
   │     │        │     │     ├─ siphash.h
   │     │        │     │     ├─ span.h
   │     │        │     │     ├─ srtp.h
   │     │        │     │     ├─ ssl.h
   │     │        │     │     ├─ ssl3.h
   │     │        │     │     ├─ stack.h
   │     │        │     │     ├─ thread.h
   │     │        │     │     ├─ time.h
   │     │        │     │     ├─ tls1.h
   │     │        │     │     ├─ trust_token.h
   │     │        │     │     ├─ type_check.h
   │     │        │     │     ├─ x509.h
   │     │        │     │     ├─ x509v3.h
   │     │        │     │     └─ x509_vfy.h
   │     │        │     ├─ ssl
   │     │        │     │  └─ internal.h
   │     │        │     └─ third_party
   │     │        │        └─ fiat
   │     │        │           ├─ curve25519_32.h
   │     │        │           ├─ curve25519_64.h
   │     │        │           ├─ p256_32.h
   │     │        │           └─ p256_64.h
   │     │        ├─ com_envoyproxy_protoc_gen_validate
   │     │        │  └─ validate
   │     │        │     ├─ validate.upb.h
   │     │        │     ├─ validate.upbdefs.h
   │     │        │     └─ validate.upb_minitable.h
   │     │        ├─ com_github_cncf_xds
   │     │        │  ├─ udpa
   │     │        │  │  └─ annotations
   │     │        │  │     ├─ migrate.upb.h
   │     │        │  │     ├─ migrate.upbdefs.h
   │     │        │  │     ├─ migrate.upb_minitable.h
   │     │        │  │     ├─ security.upb.h
   │     │        │  │     ├─ security.upbdefs.h
   │     │        │  │     ├─ security.upb_minitable.h
   │     │        │  │     ├─ sensitive.upb.h
   │     │        │  │     ├─ sensitive.upbdefs.h
   │     │        │  │     ├─ sensitive.upb_minitable.h
   │     │        │  │     ├─ status.upb.h
   │     │        │  │     ├─ status.upbdefs.h
   │     │        │  │     ├─ status.upb_minitable.h
   │     │        │  │     ├─ versioning.upb.h
   │     │        │  │     ├─ versioning.upbdefs.h
   │     │        │  │     └─ versioning.upb_minitable.h
   │     │        │  └─ xds
   │     │        │     ├─ annotations
   │     │        │     │  └─ v3
   │     │        │     │     ├─ migrate.upb.h
   │     │        │     │     ├─ migrate.upbdefs.h
   │     │        │     │     ├─ migrate.upb_minitable.h
   │     │        │     │     ├─ security.upb.h
   │     │        │     │     ├─ security.upbdefs.h
   │     │        │     │     ├─ security.upb_minitable.h
   │     │        │     │     ├─ sensitive.upb.h
   │     │        │     │     ├─ sensitive.upbdefs.h
   │     │        │     │     ├─ sensitive.upb_minitable.h
   │     │        │     │     ├─ status.upb.h
   │     │        │     │     ├─ status.upbdefs.h
   │     │        │     │     ├─ status.upb_minitable.h
   │     │        │     │     ├─ versioning.upb.h
   │     │        │     │     ├─ versioning.upbdefs.h
   │     │        │     │     └─ versioning.upb_minitable.h
   │     │        │     ├─ core
   │     │        │     │  └─ v3
   │     │        │     │     ├─ authority.upb.h
   │     │        │     │     ├─ authority.upbdefs.h
   │     │        │     │     ├─ authority.upb_minitable.h
   │     │        │     │     ├─ cidr.upb.h
   │     │        │     │     ├─ cidr.upbdefs.h
   │     │        │     │     ├─ cidr.upb_minitable.h
   │     │        │     │     ├─ collection_entry.upb.h
   │     │        │     │     ├─ collection_entry.upbdefs.h
   │     │        │     │     ├─ collection_entry.upb_minitable.h
   │     │        │     │     ├─ context_params.upb.h
   │     │        │     │     ├─ context_params.upbdefs.h
   │     │        │     │     ├─ context_params.upb_minitable.h
   │     │        │     │     ├─ extension.upb.h
   │     │        │     │     ├─ extension.upbdefs.h
   │     │        │     │     ├─ extension.upb_minitable.h
   │     │        │     │     ├─ resource.upb.h
   │     │        │     │     ├─ resource.upbdefs.h
   │     │        │     │     ├─ resource.upb_minitable.h
   │     │        │     │     ├─ resource_locator.upb.h
   │     │        │     │     ├─ resource_locator.upbdefs.h
   │     │        │     │     ├─ resource_locator.upb_minitable.h
   │     │        │     │     ├─ resource_name.upb.h
   │     │        │     │     ├─ resource_name.upbdefs.h
   │     │        │     │     └─ resource_name.upb_minitable.h
   │     │        │     ├─ data
   │     │        │     │  └─ orca
   │     │        │     │     └─ v3
   │     │        │     │        ├─ orca_load_report.upb.h
   │     │        │     │        └─ orca_load_report.upb_minitable.h
   │     │        │     ├─ service
   │     │        │     │  └─ orca
   │     │        │     │     └─ v3
   │     │        │     │        ├─ orca.upb.h
   │     │        │     │        └─ orca.upb_minitable.h
   │     │        │     └─ type
   │     │        │        ├─ matcher
   │     │        │        │  └─ v3
   │     │        │        │     ├─ cel.upb.h
   │     │        │        │     ├─ cel.upbdefs.h
   │     │        │        │     ├─ cel.upb_minitable.h
   │     │        │        │     ├─ domain.upb.h
   │     │        │        │     ├─ domain.upbdefs.h
   │     │        │        │     ├─ domain.upb_minitable.h
   │     │        │        │     ├─ http_inputs.upb.h
   │     │        │        │     ├─ http_inputs.upbdefs.h
   │     │        │        │     ├─ http_inputs.upb_minitable.h
   │     │        │        │     ├─ ip.upb.h
   │     │        │        │     ├─ ip.upbdefs.h
   │     │        │        │     ├─ ip.upb_minitable.h
   │     │        │        │     ├─ matcher.upb.h
   │     │        │        │     ├─ matcher.upbdefs.h
   │     │        │        │     ├─ matcher.upb_minitable.h
   │     │        │        │     ├─ range.upb.h
   │     │        │        │     ├─ range.upbdefs.h
   │     │        │        │     ├─ range.upb_minitable.h
   │     │        │        │     ├─ regex.upb.h
   │     │        │        │     ├─ regex.upbdefs.h
   │     │        │        │     ├─ regex.upb_minitable.h
   │     │        │        │     ├─ string.upb.h
   │     │        │        │     ├─ string.upbdefs.h
   │     │        │        │     └─ string.upb_minitable.h
   │     │        │        └─ v3
   │     │        │           ├─ cel.upb.h
   │     │        │           ├─ cel.upbdefs.h
   │     │        │           ├─ cel.upb_minitable.h
   │     │        │           ├─ range.upb.h
   │     │        │           ├─ range.upbdefs.h
   │     │        │           ├─ range.upb_minitable.h
   │     │        │           ├─ typed_struct.upb.h
   │     │        │           ├─ typed_struct.upbdefs.h
   │     │        │           └─ typed_struct.upb_minitable.h
   │     │        └─ com_github_grpc_grpc
   │     │           ├─ include
   │     │           │  ├─ grpc
   │     │           │  │  ├─ byte_buffer.h
   │     │           │  │  ├─ byte_buffer_reader.h
   │     │           │  │  ├─ census.h
   │     │           │  │  ├─ compression.h
   │     │           │  │  ├─ create_channel_from_endpoint.h
   │     │           │  │  ├─ credentials.h
   │     │           │  │  ├─ event_engine
   │     │           │  │  │  ├─ endpoint_config.h
   │     │           │  │  │  ├─ event_engine.h
   │     │           │  │  │  ├─ extensible.h
   │     │           │  │  │  ├─ internal
   │     │           │  │  │  │  ├─ memory_allocator_impl.h
   │     │           │  │  │  │  ├─ slice_cast.h
   │     │           │  │  │  │  └─ write_event.h
   │     │           │  │  │  ├─ memory_allocator.h
   │     │           │  │  │  ├─ memory_request.h
   │     │           │  │  │  ├─ port.h
   │     │           │  │  │  ├─ slice.h
   │     │           │  │  │  └─ slice_buffer.h
   │     │           │  │  ├─ fork.h
   │     │           │  │  ├─ grpc.h
   │     │           │  │  ├─ grpc_audit_logging.h
   │     │           │  │  ├─ grpc_crl_provider.h
   │     │           │  │  ├─ grpc_posix.h
   │     │           │  │  ├─ grpc_security.h
   │     │           │  │  ├─ grpc_security_constants.h
   │     │           │  │  ├─ impl
   │     │           │  │  │  ├─ call.h
   │     │           │  │  │  ├─ channel_arg_names.h
   │     │           │  │  │  ├─ codegen
   │     │           │  │  │  │  ├─ atm.h
   │     │           │  │  │  │  ├─ atm_gcc_atomic.h
   │     │           │  │  │  │  ├─ atm_gcc_sync.h
   │     │           │  │  │  │  ├─ atm_windows.h
   │     │           │  │  │  │  ├─ byte_buffer.h
   │     │           │  │  │  │  ├─ byte_buffer_reader.h
   │     │           │  │  │  │  ├─ compression_types.h
   │     │           │  │  │  │  ├─ connectivity_state.h
   │     │           │  │  │  │  ├─ fork.h
   │     │           │  │  │  │  ├─ gpr_types.h
   │     │           │  │  │  │  ├─ grpc_types.h
   │     │           │  │  │  │  ├─ log.h
   │     │           │  │  │  │  ├─ port_platform.h
   │     │           │  │  │  │  ├─ propagation_bits.h
   │     │           │  │  │  │  ├─ slice.h
   │     │           │  │  │  │  ├─ status.h
   │     │           │  │  │  │  ├─ sync.h
   │     │           │  │  │  │  ├─ sync_abseil.h
   │     │           │  │  │  │  ├─ sync_custom.h
   │     │           │  │  │  │  ├─ sync_generic.h
   │     │           │  │  │  │  ├─ sync_posix.h
   │     │           │  │  │  │  └─ sync_windows.h
   │     │           │  │  │  ├─ compression_types.h
   │     │           │  │  │  ├─ connectivity_state.h
   │     │           │  │  │  ├─ grpc_types.h
   │     │           │  │  │  ├─ propagation_bits.h
   │     │           │  │  │  └─ slice_type.h
   │     │           │  │  ├─ load_reporting.h
   │     │           │  │  ├─ passive_listener.h
   │     │           │  │  ├─ slice.h
   │     │           │  │  ├─ slice_buffer.h
   │     │           │  │  ├─ status.h
   │     │           │  │  └─ support
   │     │           │  │     ├─ alloc.h
   │     │           │  │     ├─ atm.h
   │     │           │  │     ├─ atm_gcc_atomic.h
   │     │           │  │     ├─ atm_gcc_sync.h
   │     │           │  │     ├─ atm_windows.h
   │     │           │  │     ├─ cpu.h
   │     │           │  │     ├─ json.h
   │     │           │  │     ├─ log.h
   │     │           │  │     ├─ log_windows.h
   │     │           │  │     ├─ metrics.h
   │     │           │  │     ├─ port_platform.h
   │     │           │  │     ├─ string_util.h
   │     │           │  │     ├─ sync.h
   │     │           │  │     ├─ sync_abseil.h
   │     │           │  │     ├─ sync_custom.h
   │     │           │  │     ├─ sync_generic.h
   │     │           │  │     ├─ sync_posix.h
   │     │           │  │     ├─ sync_windows.h
   │     │           │  │     ├─ thd_id.h
   │     │           │  │     ├─ time.h
   │     │           │  │     └─ workaround_list.h
   │     │           │  ├─ grpc++
   │     │           │  │  ├─ alarm.h
   │     │           │  │  ├─ channel.h
   │     │           │  │  ├─ client_context.h
   │     │           │  │  ├─ completion_queue.h
   │     │           │  │  ├─ create_channel.h
   │     │           │  │  ├─ create_channel_posix.h
   │     │           │  │  ├─ ext
   │     │           │  │  ├─ generic
   │     │           │  │  │  ├─ async_generic_service.h
   │     │           │  │  │  └─ generic_stub.h
   │     │           │  │  ├─ grpc++.h
   │     │           │  │  ├─ health_check_service_interface.h
   │     │           │  │  ├─ impl
   │     │           │  │  │  ├─ call.h
   │     │           │  │  │  ├─ channel_argument_option.h
   │     │           │  │  │  ├─ client_unary_call.h
   │     │           │  │  │  ├─ codegen
   │     │           │  │  │  │  ├─ async_stream.h
   │     │           │  │  │  │  ├─ async_unary_call.h
   │     │           │  │  │  │  ├─ byte_buffer.h
   │     │           │  │  │  │  ├─ call.h
   │     │           │  │  │  │  ├─ call_hook.h
   │     │           │  │  │  │  ├─ channel_interface.h
   │     │           │  │  │  │  ├─ client_context.h
   │     │           │  │  │  │  ├─ client_unary_call.h
   │     │           │  │  │  │  ├─ completion_queue.h
   │     │           │  │  │  │  ├─ completion_queue_tag.h
   │     │           │  │  │  │  ├─ config.h
   │     │           │  │  │  │  ├─ config_protobuf.h
   │     │           │  │  │  │  ├─ create_auth_context.h
   │     │           │  │  │  │  ├─ metadata_map.h
   │     │           │  │  │  │  ├─ method_handler_impl.h
   │     │           │  │  │  │  ├─ proto_utils.h
   │     │           │  │  │  │  ├─ rpc_method.h
   │     │           │  │  │  │  ├─ rpc_service_method.h
   │     │           │  │  │  │  ├─ security
   │     │           │  │  │  │  │  └─ auth_context.h
   │     │           │  │  │  │  ├─ serialization_traits.h
   │     │           │  │  │  │  ├─ server_context.h
   │     │           │  │  │  │  ├─ server_interface.h
   │     │           │  │  │  │  ├─ service_type.h
   │     │           │  │  │  │  ├─ slice.h
   │     │           │  │  │  │  ├─ status.h
   │     │           │  │  │  │  ├─ status_code_enum.h
   │     │           │  │  │  │  ├─ string_ref.h
   │     │           │  │  │  │  ├─ stub_options.h
   │     │           │  │  │  │  ├─ sync_stream.h
   │     │           │  │  │  │  └─ time.h
   │     │           │  │  │  ├─ grpc_library.h
   │     │           │  │  │  ├─ method_handler_impl.h
   │     │           │  │  │  ├─ rpc_method.h
   │     │           │  │  │  ├─ rpc_service_method.h
   │     │           │  │  │  ├─ serialization_traits.h
   │     │           │  │  │  ├─ server_initializer.h
   │     │           │  │  │  └─ service_type.h
   │     │           │  │  ├─ resource_quota.h
   │     │           │  │  ├─ security
   │     │           │  │  │  ├─ auth_context.h
   │     │           │  │  │  ├─ auth_metadata_processor.h
   │     │           │  │  │  ├─ credentials.h
   │     │           │  │  │  └─ server_credentials.h
   │     │           │  │  ├─ server.h
   │     │           │  │  ├─ server_context.h
   │     │           │  │  ├─ server_posix.h
   │     │           │  │  └─ support
   │     │           │  │     ├─ async_stream.h
   │     │           │  │     ├─ async_unary_call.h
   │     │           │  │     ├─ byte_buffer.h
   │     │           │  │     ├─ channel_arguments.h
   │     │           │  │     ├─ config.h
   │     │           │  │     ├─ slice.h
   │     │           │  │     ├─ status.h
   │     │           │  │     ├─ status_code_enum.h
   │     │           │  │     ├─ string_ref.h
   │     │           │  │     ├─ stub_options.h
   │     │           │  │     ├─ sync_stream.h
   │     │           │  │     └─ time.h
   │     │           │  └─ grpcpp
   │     │           │     ├─ alarm.h
   │     │           │     ├─ channel.h
   │     │           │     ├─ client_context.h
   │     │           │     ├─ completion_queue.h
   │     │           │     ├─ create_channel.h
   │     │           │     ├─ create_channel_posix.h
   │     │           │     ├─ ext
   │     │           │     │  ├─ call_metric_recorder.h
   │     │           │     │  └─ server_metric_recorder.h
   │     │           │     ├─ generic
   │     │           │     │  ├─ async_generic_service.h
   │     │           │     │  ├─ callback_generic_service.h
   │     │           │     │  ├─ generic_stub.h
   │     │           │     │  └─ generic_stub_callback.h
   │     │           │     ├─ grpcpp.h
   │     │           │     ├─ health_check_service_interface.h
   │     │           │     ├─ impl
   │     │           │     │  ├─ call.h
   │     │           │     │  ├─ call_hook.h
   │     │           │     │  ├─ call_op_set.h
   │     │           │     │  ├─ call_op_set_interface.h
   │     │           │     │  ├─ channel_argument_option.h
   │     │           │     │  ├─ channel_interface.h
   │     │           │     │  ├─ client_unary_call.h
   │     │           │     │  ├─ codegen
   │     │           │     │  │  ├─ async_generic_service.h
   │     │           │     │  │  ├─ async_stream.h
   │     │           │     │  │  ├─ async_unary_call.h
   │     │           │     │  │  ├─ byte_buffer.h
   │     │           │     │  │  ├─ call.h
   │     │           │     │  │  ├─ callback_common.h
   │     │           │     │  │  ├─ call_hook.h
   │     │           │     │  │  ├─ call_op_set.h
   │     │           │     │  │  ├─ call_op_set_interface.h
   │     │           │     │  │  ├─ channel_interface.h
   │     │           │     │  │  ├─ client_callback.h
   │     │           │     │  │  ├─ client_context.h
   │     │           │     │  │  ├─ client_interceptor.h
   │     │           │     │  │  ├─ client_unary_call.h
   │     │           │     │  │  ├─ completion_queue.h
   │     │           │     │  │  ├─ completion_queue_tag.h
   │     │           │     │  │  ├─ config.h
   │     │           │     │  │  ├─ config_protobuf.h
   │     │           │     │  │  ├─ create_auth_context.h
   │     │           │     │  │  ├─ delegating_channel.h
   │     │           │     │  │  ├─ intercepted_channel.h
   │     │           │     │  │  ├─ interceptor.h
   │     │           │     │  │  ├─ interceptor_common.h
   │     │           │     │  │  ├─ message_allocator.h
   │     │           │     │  │  ├─ metadata_map.h
   │     │           │     │  │  ├─ method_handler.h
   │     │           │     │  │  ├─ method_handler_impl.h
   │     │           │     │  │  ├─ proto_buffer_reader.h
   │     │           │     │  │  ├─ proto_buffer_writer.h
   │     │           │     │  │  ├─ proto_utils.h
   │     │           │     │  │  ├─ rpc_method.h
   │     │           │     │  │  ├─ rpc_service_method.h
   │     │           │     │  │  ├─ security
   │     │           │     │  │  │  └─ auth_context.h
   │     │           │     │  │  ├─ serialization_traits.h
   │     │           │     │  │  ├─ server_callback.h
   │     │           │     │  │  ├─ server_callback_handlers.h
   │     │           │     │  │  ├─ server_context.h
   │     │           │     │  │  ├─ server_interceptor.h
   │     │           │     │  │  ├─ server_interface.h
   │     │           │     │  │  ├─ service_type.h
   │     │           │     │  │  ├─ slice.h
   │     │           │     │  │  ├─ status.h
   │     │           │     │  │  ├─ status_code_enum.h
   │     │           │     │  │  ├─ string_ref.h
   │     │           │     │  │  ├─ stub_options.h
   │     │           │     │  │  ├─ sync.h
   │     │           │     │  │  ├─ sync_stream.h
   │     │           │     │  │  └─ time.h
   │     │           │     │  ├─ completion_queue_tag.h
   │     │           │     │  ├─ create_auth_context.h
   │     │           │     │  ├─ delegating_channel.h
   │     │           │     │  ├─ generic_serialize.h
   │     │           │     │  ├─ generic_stub_internal.h
   │     │           │     │  ├─ grpc_library.h
   │     │           │     │  ├─ intercepted_channel.h
   │     │           │     │  ├─ interceptor_common.h
   │     │           │     │  ├─ metadata_map.h
   │     │           │     │  ├─ method_handler_impl.h
   │     │           │     │  ├─ proto_utils.h
   │     │           │     │  ├─ rpc_method.h
   │     │           │     │  ├─ rpc_service_method.h
   │     │           │     │  ├─ serialization_traits.h
   │     │           │     │  ├─ server_callback_handlers.h
   │     │           │     │  ├─ server_initializer.h
   │     │           │     │  ├─ service_type.h
   │     │           │     │  ├─ status.h
   │     │           │     │  └─ sync.h
   │     │           │     ├─ passive_listener.h
   │     │           │     ├─ ports_def.inc
   │     │           │     ├─ ports_undef.inc
   │     │           │     ├─ resource_quota.h
   │     │           │     ├─ security
   │     │           │     │  ├─ audit_logging.h
   │     │           │     │  ├─ authorization_policy_provider.h
   │     │           │     │  ├─ auth_context.h
   │     │           │     │  ├─ auth_metadata_processor.h
   │     │           │     │  ├─ credentials.h
   │     │           │     │  ├─ server_credentials.h
   │     │           │     │  ├─ tls_certificate_provider.h
   │     │           │     │  ├─ tls_certificate_verifier.h
   │     │           │     │  ├─ tls_credentials_options.h
   │     │           │     │  └─ tls_crl_provider.h
   │     │           │     ├─ server.h
   │     │           │     ├─ server_context.h
   │     │           │     ├─ server_interface.h
   │     │           │     ├─ server_posix.h
   │     │           │     ├─ support
   │     │           │     │  ├─ async_stream.h
   │     │           │     │  ├─ async_unary_call.h
   │     │           │     │  ├─ byte_buffer.h
   │     │           │     │  ├─ callback_common.h
   │     │           │     │  ├─ channel_arguments.h
   │     │           │     │  ├─ client_callback.h
   │     │           │     │  ├─ client_interceptor.h
   │     │           │     │  ├─ config.h
   │     │           │     │  ├─ global_callback_hook.h
   │     │           │     │  ├─ interceptor.h
   │     │           │     │  ├─ message_allocator.h
   │     │           │     │  ├─ method_handler.h
   │     │           │     │  ├─ proto_buffer_reader.h
   │     │           │     │  ├─ proto_buffer_writer.h
   │     │           │     │  ├─ server_callback.h
   │     │           │     │  ├─ server_interceptor.h
   │     │           │     │  ├─ slice.h
   │     │           │     │  ├─ status.h
   │     │           │     │  ├─ status_code_enum.h
   │     │           │     │  ├─ string_ref.h
   │     │           │     │  ├─ stub_options.h
   │     │           │     │  ├─ sync_stream.h
   │     │           │     │  ├─ time.h
   │     │           │     │  └─ validate_service_config.h
   │     │           │     └─ version_info.h
   │     │           └─ src
   │     │              └─ core
   │     │                 ├─ call
   │     │                 │  ├─ call_arena_allocator.h
   │     │                 │  ├─ call_destination.h
   │     │                 │  ├─ call_filters.h
   │     │                 │  ├─ call_finalization.h
   │     │                 │  ├─ call_spine.h
   │     │                 │  ├─ call_state.h
   │     │                 │  ├─ client_call.h
   │     │                 │  ├─ custom_metadata.h
   │     │                 │  ├─ interception_chain.h
   │     │                 │  ├─ message.h
   │     │                 │  ├─ metadata.h
   │     │                 │  ├─ metadata_batch.h
   │     │                 │  ├─ metadata_compression_traits.h
   │     │                 │  ├─ metadata_info.h
   │     │                 │  ├─ parsed_metadata.h
   │     │                 │  ├─ request_buffer.h
   │     │                 │  ├─ security_context.h
   │     │                 │  ├─ server_call.h
   │     │                 │  ├─ simple_slice_based_metadata.h
   │     │                 │  └─ status_util.h
   │     │                 ├─ channelz
   │     │                 │  ├─ channelz.h
   │     │                 │  ├─ channelz_registry.h
   │     │                 │  ├─ channel_trace.h
   │     │                 │  ├─ property_list.h
   │     │                 │  └─ ztrace_collector.h
   │     │                 ├─ client_channel
   │     │                 │  ├─ backup_poller.h
   │     │                 │  ├─ client_channel.h
   │     │                 │  ├─ client_channel_args.h
   │     │                 │  ├─ client_channel_factory.h
   │     │                 │  ├─ client_channel_filter.h
   │     │                 │  ├─ client_channel_internal.h
   │     │                 │  ├─ client_channel_service_config.h
   │     │                 │  ├─ config_selector.h
   │     │                 │  ├─ connector.h
   │     │                 │  ├─ direct_channel.h
   │     │                 │  ├─ dynamic_filters.h
   │     │                 │  ├─ global_subchannel_pool.h
   │     │                 │  ├─ lb_metadata.h
   │     │                 │  ├─ load_balanced_call_destination.h
   │     │                 │  ├─ local_subchannel_pool.h
   │     │                 │  ├─ retry_filter.h
   │     │                 │  ├─ retry_filter_legacy_call_data.h
   │     │                 │  ├─ retry_interceptor.h
   │     │                 │  ├─ retry_service_config.h
   │     │                 │  ├─ retry_throttle.h
   │     │                 │  ├─ subchannel.h
   │     │                 │  ├─ subchannel_interface_internal.h
   │     │                 │  ├─ subchannel_pool_interface.h
   │     │                 │  └─ subchannel_stream_client.h
   │     │                 ├─ config
   │     │                 │  ├─ config_vars.h
   │     │                 │  ├─ core_configuration.h
   │     │                 │  └─ load_config.h
   │     │                 ├─ credentials
   │     │                 │  ├─ call
   │     │                 │  │  ├─ call_credentials.h
   │     │                 │  │  ├─ call_creds_registry.h
   │     │                 │  │  ├─ call_creds_util.h
   │     │                 │  │  ├─ composite
   │     │                 │  │  │  └─ composite_call_credentials.h
   │     │                 │  │  ├─ external
   │     │                 │  │  │  ├─ aws_external_account_credentials.h
   │     │                 │  │  │  ├─ aws_request_signer.h
   │     │                 │  │  │  ├─ external_account_credentials.h
   │     │                 │  │  │  ├─ file_external_account_credentials.h
   │     │                 │  │  │  └─ url_external_account_credentials.h
   │     │                 │  │  ├─ gcp_service_account_identity
   │     │                 │  │  │  └─ gcp_service_account_identity_credentials.h
   │     │                 │  │  ├─ iam
   │     │                 │  │  │  └─ iam_credentials.h
   │     │                 │  │  ├─ json_util.h
   │     │                 │  │  ├─ jwt
   │     │                 │  │  │  ├─ json_token.h
   │     │                 │  │  │  ├─ jwt_credentials.h
   │     │                 │  │  │  └─ jwt_verifier.h
   │     │                 │  │  ├─ jwt_token_file
   │     │                 │  │  │  └─ jwt_token_file_call_credentials.h
   │     │                 │  │  ├─ jwt_util.h
   │     │                 │  │  ├─ oauth2
   │     │                 │  │  │  └─ oauth2_credentials.h
   │     │                 │  │  ├─ plugin
   │     │                 │  │  │  └─ plugin_credentials.h
   │     │                 │  │  └─ token_fetcher
   │     │                 │  │     └─ token_fetcher_credentials.h
   │     │                 │  └─ transport
   │     │                 │     ├─ alts
   │     │                 │     │  ├─ alts_credentials.h
   │     │                 │     │  ├─ alts_security_connector.h
   │     │                 │     │  ├─ check_gcp_environment.h
   │     │                 │     │  └─ grpc_alts_credentials_options.h
   │     │                 │     ├─ channel_creds_registry.h
   │     │                 │     ├─ composite
   │     │                 │     │  └─ composite_channel_credentials.h
   │     │                 │     ├─ fake
   │     │                 │     │  ├─ fake_credentials.h
   │     │                 │     │  └─ fake_security_connector.h
   │     │                 │     ├─ google_default
   │     │                 │     │  └─ google_default_credentials.h
   │     │                 │     ├─ insecure
   │     │                 │     │  ├─ insecure_credentials.h
   │     │                 │     │  └─ insecure_security_connector.h
   │     │                 │     ├─ local
   │     │                 │     │  ├─ local_credentials.h
   │     │                 │     │  └─ local_security_connector.h
   │     │                 │     ├─ security_connector.h
   │     │                 │     ├─ ssl
   │     │                 │     │  ├─ ssl_credentials.h
   │     │                 │     │  └─ ssl_security_connector.h
   │     │                 │     ├─ tls
   │     │                 │     │  ├─ certificate_provider_factory.h
   │     │                 │     │  ├─ certificate_provider_registry.h
   │     │                 │     │  ├─ grpc_tls_certificate_distributor.h
   │     │                 │     │  ├─ grpc_tls_certificate_provider.h
   │     │                 │     │  ├─ grpc_tls_certificate_verifier.h
   │     │                 │     │  ├─ grpc_tls_credentials_options.h
   │     │                 │     │  ├─ grpc_tls_crl_provider.h
   │     │                 │     │  ├─ load_system_roots.h
   │     │                 │     │  ├─ load_system_roots_supported.h
   │     │                 │     │  ├─ ssl_utils.h
   │     │                 │     │  ├─ tls_credentials.h
   │     │                 │     │  ├─ tls_security_connector.h
   │     │                 │     │  └─ tls_utils.h
   │     │                 │     ├─ transport_credentials.h
   │     │                 │     └─ xds
   │     │                 │        └─ xds_credentials.h
   │     │                 ├─ ext
   │     │                 │  ├─ filters
   │     │                 │  │  ├─ backend_metrics
   │     │                 │  │  │  ├─ backend_metric_filter.h
   │     │                 │  │  │  └─ backend_metric_provider.h
   │     │                 │  │  ├─ channel_idle
   │     │                 │  │  │  ├─ idle_filter_state.h
   │     │                 │  │  │  └─ legacy_channel_idle_filter.h
   │     │                 │  │  ├─ fault_injection
   │     │                 │  │  │  ├─ fault_injection_filter.h
   │     │                 │  │  │  └─ fault_injection_service_config_parser.h
   │     │                 │  │  ├─ gcp_authentication
   │     │                 │  │  │  ├─ gcp_authentication_filter.h
   │     │                 │  │  │  └─ gcp_authentication_service_config_parser.h
   │     │                 │  │  ├─ http
   │     │                 │  │  │  ├─ client
   │     │                 │  │  │  │  └─ http_client_filter.h
   │     │                 │  │  │  ├─ client_authority_filter.h
   │     │                 │  │  │  ├─ message_compress
   │     │                 │  │  │  │  └─ compression_filter.h
   │     │                 │  │  │  └─ server
   │     │                 │  │  │     └─ http_server_filter.h
   │     │                 │  │  ├─ message_size
   │     │                 │  │  │  └─ message_size_filter.h
   │     │                 │  │  ├─ rbac
   │     │                 │  │  │  ├─ rbac_filter.h
   │     │                 │  │  │  └─ rbac_service_config_parser.h
   │     │                 │  │  └─ stateful_session
   │     │                 │  │     ├─ stateful_session_filter.h
   │     │                 │  │     └─ stateful_session_service_config_parser.h
   │     │                 │  └─ transport
   │     │                 │     ├─ chttp2
   │     │                 │     │  ├─ alpn
   │     │                 │     │  │  └─ alpn.h
   │     │                 │     │  ├─ client
   │     │                 │     │  │  └─ chttp2_connector.h
   │     │                 │     │  ├─ server
   │     │                 │     │  │  └─ chttp2_server.h
   │     │                 │     │  └─ transport
   │     │                 │     │     ├─ bin_decoder.h
   │     │                 │     │     ├─ bin_encoder.h
   │     │                 │     │     ├─ call_tracer_wrapper.h
   │     │                 │     │     ├─ chttp2_transport.h
   │     │                 │     │     ├─ decode_huff.h
   │     │                 │     │     ├─ flow_control.h
   │     │                 │     │     ├─ frame.h
   │     │                 │     │     ├─ frame_data.h
   │     │                 │     │     ├─ frame_goaway.h
   │     │                 │     │     ├─ frame_ping.h
   │     │                 │     │     ├─ frame_rst_stream.h
   │     │                 │     │     ├─ frame_security.h
   │     │                 │     │     ├─ frame_settings.h
   │     │                 │     │     ├─ frame_window_update.h
   │     │                 │     │     ├─ header_assembler.h
   │     │                 │     │     ├─ hpack_constants.h
   │     │                 │     │     ├─ hpack_encoder.h
   │     │                 │     │     ├─ hpack_encoder_table.h
   │     │                 │     │     ├─ hpack_parser.h
   │     │                 │     │     ├─ hpack_parser_table.h
   │     │                 │     │     ├─ hpack_parse_result.h
   │     │                 │     │     ├─ http2_client_transport.h
   │     │                 │     │     ├─ http2_settings.h
   │     │                 │     │     ├─ http2_stats_collector.h
   │     │                 │     │     ├─ http2_status.h
   │     │                 │     │     ├─ http2_transport.h
   │     │                 │     │     ├─ http2_ztrace_collector.h
   │     │                 │     │     ├─ huffsyms.h
   │     │                 │     │     ├─ internal.h
   │     │                 │     │     ├─ internal_channel_arg_names.h
   │     │                 │     │     ├─ keepalive.h
   │     │                 │     │     ├─ legacy_frame.h
   │     │                 │     │     ├─ message_assembler.h
   │     │                 │     │     ├─ ping_abuse_policy.h
   │     │                 │     │     ├─ ping_callbacks.h
   │     │                 │     │     ├─ ping_promise.h
   │     │                 │     │     ├─ ping_rate_policy.h
   │     │                 │     │     ├─ stream_lists.h
   │     │                 │     │     ├─ transport_common.h
   │     │                 │     │     ├─ varint.h
   │     │                 │     │     └─ write_size_policy.h
   │     │                 │     └─ inproc
   │     │                 │        ├─ inproc_transport.h
   │     │                 │        └─ legacy_inproc_transport.h
   │     │                 ├─ filter
   │     │                 │  ├─ auth
   │     │                 │  │  └─ auth_filters.h
   │     │                 │  ├─ blackboard.h
   │     │                 │  └─ filter_args.h
   │     │                 ├─ handshaker
   │     │                 │  ├─ endpoint_info
   │     │                 │  │  └─ endpoint_info_handshaker.h
   │     │                 │  ├─ handshaker.h
   │     │                 │  ├─ handshaker_factory.h
   │     │                 │  ├─ handshaker_registry.h
   │     │                 │  ├─ http_connect
   │     │                 │  │  ├─ http_connect_handshaker.h
   │     │                 │  │  ├─ http_proxy_mapper.h
   │     │                 │  │  └─ xds_http_proxy_mapper.h
   │     │                 │  ├─ proxy_mapper.h
   │     │                 │  ├─ proxy_mapper_registry.h
   │     │                 │  ├─ security
   │     │                 │  │  ├─ secure_endpoint.h
   │     │                 │  │  └─ security_handshaker.h
   │     │                 │  └─ tcp_connect
   │     │                 │     └─ tcp_connect_handshaker.h
   │     │                 └─ lib
   │     │                    ├─ address_utils
   │     │                    │  ├─ parse_address.h
   │     │                    │  └─ sockaddr_utils.h
   │     │                    ├─ channel
   │     │                    │  ├─ channel_args.h
   │     │                    │  ├─ channel_args_preconditioning.h
   │     │                    │  ├─ channel_fwd.h
   │     │                    │  ├─ channel_stack.h
   │     │                    │  ├─ connected_channel.h
   │     │                    │  └─ promise_based_filter.h
   │     │                    ├─ compression
   │     │                    │  ├─ compression_internal.h
   │     │                    │  └─ message_compress.h
   │     │                    ├─ debug
   │     │                    │  ├─ trace.h
   │     │                    │  ├─ trace_flags.h
   │     │                    │  └─ trace_impl.h
   │     │                    ├─ event_engine
   │     │                    │  ├─ ares_resolver.h
   │     │                    │  ├─ channel_args_endpoint_config.h
   │     │                    │  ├─ common_closures.h
   │     │                    │  ├─ default_event_engine.h
   │     │                    │  ├─ default_event_engine_factory.h
   │     │                    │  ├─ endpoint_channel_arg_wrapper.h
   │     │                    │  ├─ event_engine_context.h
   │     │                    │  ├─ extensions
   │     │                    │  │  ├─ blocking_dns.h
   │     │                    │  │  ├─ can_track_errors.h
   │     │                    │  │  ├─ channelz.h
   │     │                    │  │  ├─ chaotic_good_extension.h
   │     │                    │  │  ├─ iomgr_compatible.h
   │     │                    │  │  ├─ supports_fd.h
   │     │                    │  │  ├─ supports_win_sockets.h
   │     │                    │  │  └─ tcp_trace.h
   │     │                    │  ├─ grpc_polled_fd.h
   │     │                    │  ├─ handle_containers.h
   │     │                    │  ├─ memory_allocator_factory.h
   │     │                    │  ├─ nameser.h
   │     │                    │  ├─ poller.h
   │     │                    │  ├─ posix.h
   │     │                    │  ├─ posix_engine
   │     │                    │  │  ├─ event_poller.h
   │     │                    │  │  ├─ file_descriptor_collection.h
   │     │                    │  │  ├─ grpc_polled_fd_posix.h
   │     │                    │  │  ├─ internal_errqueue.h
   │     │                    │  │  ├─ posix_endpoint.h
   │     │                    │  │  ├─ posix_engine_closure.h
   │     │                    │  │  ├─ posix_interface.h
   │     │                    │  │  ├─ posix_write_event_sink.h
   │     │                    │  │  ├─ tcp_socket_utils.h
   │     │                    │  │  ├─ timer.h
   │     │                    │  │  ├─ timer_heap.h
   │     │                    │  │  ├─ timer_manager.h
   │     │                    │  │  └─ traced_buffer_list.h
   │     │                    │  ├─ query_extensions.h
   │     │                    │  ├─ ref_counted_dns_resolver_interface.h
   │     │                    │  ├─ resolved_address_internal.h
   │     │                    │  ├─ shim.h
   │     │                    │  ├─ tcp_socket_utils.h
   │     │                    │  ├─ thready_event_engine
   │     │                    │  │  └─ thready_event_engine.h
   │     │                    │  ├─ thread_local.h
   │     │                    │  ├─ thread_pool
   │     │                    │  │  ├─ thread_count.h
   │     │                    │  │  ├─ thread_pool.h
   │     │                    │  │  └─ work_stealing_thread_pool.h
   │     │                    │  ├─ time_util.h
   │     │                    │  ├─ utils.h
   │     │                    │  ├─ windows
   │     │                    │  │  ├─ grpc_polled_fd_windows.h
   │     │                    │  │  ├─ iocp.h
   │     │                    │  │  ├─ native_windows_dns_resolver.h
   │     │                    │  │  ├─ windows_endpoint.h
   │     │                    │  │  ├─ windows_engine.h
   │     │                    │  │  ├─ windows_listener.h
   │     │                    │  │  └─ win_socket.h
   │     │                    │  └─ work_queue
   │     │                    │     ├─ basic_work_queue.h
   │     │                    │     └─ work_queue.h
   │     │                    ├─ experiments
   │     │                    │  ├─ config.h
   │     │                    │  └─ experiments.h
   │     │                    ├─ iomgr
   │     │                    │  ├─ block_annotate.h
   │     │                    │  ├─ buffer_list.h
   │     │                    │  ├─ call_combiner.h
   │     │                    │  ├─ cfstream_handle.h
   │     │                    │  ├─ closure.h
   │     │                    │  ├─ combiner.h
   │     │                    │  ├─ dynamic_annotations.h
   │     │                    │  ├─ endpoint.h
   │     │                    │  ├─ endpoint_cfstream.h
   │     │                    │  ├─ endpoint_pair.h
   │     │                    │  ├─ error.h
   │     │                    │  ├─ error_cfstream.h
   │     │                    │  ├─ event_engine_shims
   │     │                    │  │  ├─ closure.h
   │     │                    │  │  ├─ endpoint.h
   │     │                    │  │  └─ tcp_client.h
   │     │                    │  ├─ ev_apple.h
   │     │                    │  ├─ ev_epoll1_linux.h
   │     │                    │  ├─ ev_poll_posix.h
   │     │                    │  ├─ ev_posix.h
   │     │                    │  ├─ exec_ctx.h
   │     │                    │  ├─ internal_errqueue.h
   │     │                    │  ├─ iocp_windows.h
   │     │                    │  ├─ iomgr.h
   │     │                    │  ├─ iomgr_fwd.h
   │     │                    │  ├─ iomgr_internal.h
   │     │                    │  ├─ lockfree_event.h
   │     │                    │  ├─ nameser.h
   │     │                    │  ├─ polling_entity.h
   │     │                    │  ├─ pollset.h
   │     │                    │  ├─ pollset_set.h
   │     │                    │  ├─ pollset_set_windows.h
   │     │                    │  ├─ pollset_windows.h
   │     │                    │  ├─ port.h
   │     │                    │  ├─ resolved_address.h
   │     │                    │  ├─ resolve_address.h
   │     │                    │  ├─ resolve_address_impl.h
   │     │                    │  ├─ resolve_address_posix.h
   │     │                    │  ├─ resolve_address_windows.h
   │     │                    │  ├─ sockaddr.h
   │     │                    │  ├─ sockaddr_posix.h
   │     │                    │  ├─ sockaddr_windows.h
   │     │                    │  ├─ socket_factory_posix.h
   │     │                    │  ├─ socket_mutator.h
   │     │                    │  ├─ socket_utils.h
   │     │                    │  ├─ socket_utils_posix.h
   │     │                    │  ├─ socket_windows.h
   │     │                    │  ├─ systemd_utils.h
   │     │                    │  ├─ tcp_client.h
   │     │                    │  ├─ tcp_client_posix.h
   │     │                    │  ├─ tcp_posix.h
   │     │                    │  ├─ tcp_server.h
   │     │                    │  ├─ tcp_server_utils_posix.h
   │     │                    │  ├─ tcp_windows.h
   │     │                    │  ├─ timer.h
   │     │                    │  ├─ timer_generic.h
   │     │                    │  ├─ timer_heap.h
   │     │                    │  ├─ timer_manager.h
   │     │                    │  ├─ unix_sockets_posix.h
   │     │                    │  ├─ vsock.h
   │     │                    │  ├─ wakeup_fd_pipe.h
   │     │                    │  └─ wakeup_fd_posix.h
   │     │                    ├─ promise
   │     │                    │  ├─ activity.h
   │     │                    │  ├─ all_ok.h
   │     │                    │  ├─ arena_promise.h
   │     │                    │  ├─ cancel_callback.h
   │     │                    │  ├─ context.h
   │     │                    │  ├─ detail
   │     │                    │  │  ├─ basic_seq.h
   │     │                    │  │  ├─ join_state.h
   │     │                    │  │  ├─ promise_factory.h
   │     │                    │  │  ├─ promise_like.h
   │     │                    │  │  ├─ promise_variant.h
   │     │                    │  │  ├─ seq_state.h
   │     │                    │  │  └─ status.h
   │     │                    │  ├─ exec_ctx_wakeup_scheduler.h
   │     │                    │  ├─ for_each.h
   │     │                    │  ├─ if.h
   │     │                    │  ├─ interceptor_list.h
   │     │                    │  ├─ inter_activity_latch.h
   │     │                    │  ├─ inter_activity_mutex.h
   │     │                    │  ├─ latch.h
   │     │                    │  ├─ loop.h
   │     │                    │  ├─ map.h
   │     │                    │  ├─ match_promise.h
   │     │                    │  ├─ mpsc.h
   │     │                    │  ├─ observable.h
   │     │                    │  ├─ party.h
   │     │                    │  ├─ pipe.h
   │     │                    │  ├─ poll.h
   │     │                    │  ├─ prioritized_race.h
   │     │                    │  ├─ promise.h
   │     │                    │  ├─ race.h
   │     │                    │  ├─ seq.h
   │     │                    │  ├─ sleep.h
   │     │                    │  ├─ status_flag.h
   │     │                    │  ├─ try_join.h
   │     │                    │  ├─ try_seq.h
   │     │                    │  └─ wait_set.h
   │     │                    ├─ resource_quota
   │     │                    │  ├─ api.h
   │     │                    │  ├─ arena.h
   │     │                    │  ├─ connection_quota.h
   │     │                    │  ├─ memory_quota.h
   │     │                    │  ├─ periodic_update.h
   │     │                    │  ├─ resource_quota.h
   │     │                    │  └─ thread_quota.h
   │     │                    ├─ security
   │     │                    │  └─ authorization
   │     │                    │     ├─ audit_logging.h
   │     │                    │     ├─ authorization_engine.h
   │     │                    │     ├─ authorization_policy_provider.h
   │     │                    │     ├─ evaluate_args.h
   │     │                    │     ├─ grpc_authorization_engine.h
   │     │                    │     ├─ grpc_server_authz_filter.h
   │     │                    │     ├─ matchers.h
   │     │                    │     ├─ rbac_policy.h
   │     │                    │     └─ stdout_logger.h
   │     │                    ├─ slice
   │     │                    │  ├─ percent_encoding.h
   │     │                    │  ├─ slice.h
   │     │                    │  ├─ slice_buffer.h
   │     │                    │  ├─ slice_internal.h
   │     │                    │  ├─ slice_refcount.h
   │     │                    │  └─ slice_string_helpers.h
   │     │                    └─ surface
   │     │                       ├─ .tmp3tHVKU
   │     │                       ├─ call.h
   │     │                       ├─ call_test_only.h
   │     │                       ├─ call_utils.h
   │     │                       ├─ channel.h
   │     │                       ├─ channel_create.h
   │     │                       ├─ channel_init.h
   │     │                       ├─ channel_stack_type.h
   │     │                       ├─ completion_queue.h
   │     │                       ├─ completion_queue_factory.h
   │     │                       ├─ connection_context.h
   │     │                       └─ event_string.h
   │     ├─ termcolor
   │     │  ├─ py.typed
   │     │  ├─ termcolor.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ termcolor-3.3.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ COPYING.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ threadpoolctl-3.6.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ threadpoolctl.py
   │     ├─ tomli
   │     │  ├─ py.typed
   │     │  ├─ _parser.py
   │     │  ├─ _re.py
   │     │  ├─ _types.py
   │     │  └─ __init__.py
   │     ├─ tomli-2.4.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ tqdm
   │     │  ├─ asyncio.py
   │     │  ├─ auto.py
   │     │  ├─ autonotebook.py
   │     │  ├─ cli.py
   │     │  ├─ completion.sh
   │     │  ├─ contrib
   │     │  │  ├─ bells.py
   │     │  │  ├─ concurrent.py
   │     │  │  ├─ discord.py
   │     │  │  ├─ itertools.py
   │     │  │  ├─ logging.py
   │     │  │  ├─ slack.py
   │     │  │  ├─ telegram.py
   │     │  │  ├─ utils_worker.py
   │     │  │  └─ __init__.py
   │     │  ├─ dask.py
   │     │  ├─ gui.py
   │     │  ├─ keras.py
   │     │  ├─ notebook.py
   │     │  ├─ rich.py
   │     │  ├─ std.py
   │     │  ├─ tk.py
   │     │  ├─ tqdm.1
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ _main.py
   │     │  ├─ _monitor.py
   │     │  ├─ _tqdm.py
   │     │  ├─ _tqdm_gui.py
   │     │  ├─ _tqdm_notebook.py
   │     │  ├─ _tqdm_pandas.py
   │     │  ├─ _utils.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ tqdm-4.70.0.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENCE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ typing_extensions-4.16.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ typing_extensions.py
   │     ├─ tzdata
   │     │  ├─ zoneinfo
   │     │  │  ├─ Africa
   │     │  │  │  ├─ Abidjan
   │     │  │  │  ├─ Accra
   │     │  │  │  ├─ Addis_Ababa
   │     │  │  │  ├─ Algiers
   │     │  │  │  ├─ Asmara
   │     │  │  │  ├─ Asmera
   │     │  │  │  ├─ Bamako
   │     │  │  │  ├─ Bangui
   │     │  │  │  ├─ Banjul
   │     │  │  │  ├─ Bissau
   │     │  │  │  ├─ Blantyre
   │     │  │  │  ├─ Brazzaville
   │     │  │  │  ├─ Bujumbura
   │     │  │  │  ├─ Cairo
   │     │  │  │  ├─ Casablanca
   │     │  │  │  ├─ Ceuta
   │     │  │  │  ├─ Conakry
   │     │  │  │  ├─ Dakar
   │     │  │  │  ├─ Dar_es_Salaam
   │     │  │  │  ├─ Djibouti
   │     │  │  │  ├─ Douala
   │     │  │  │  ├─ El_Aaiun
   │     │  │  │  ├─ Freetown
   │     │  │  │  ├─ Gaborone
   │     │  │  │  ├─ Harare
   │     │  │  │  ├─ Johannesburg
   │     │  │  │  ├─ Juba
   │     │  │  │  ├─ Kampala
   │     │  │  │  ├─ Khartoum
   │     │  │  │  ├─ Kigali
   │     │  │  │  ├─ Kinshasa
   │     │  │  │  ├─ Lagos
   │     │  │  │  ├─ Libreville
   │     │  │  │  ├─ Lome
   │     │  │  │  ├─ Luanda
   │     │  │  │  ├─ Lubumbashi
   │     │  │  │  ├─ Lusaka
   │     │  │  │  ├─ Malabo
   │     │  │  │  ├─ Maputo
   │     │  │  │  ├─ Maseru
   │     │  │  │  ├─ Mbabane
   │     │  │  │  ├─ Mogadishu
   │     │  │  │  ├─ Monrovia
   │     │  │  │  ├─ Nairobi
   │     │  │  │  ├─ Ndjamena
   │     │  │  │  ├─ Niamey
   │     │  │  │  ├─ Nouakchott
   │     │  │  │  ├─ Ouagadougou
   │     │  │  │  ├─ Porto-Novo
   │     │  │  │  ├─ Sao_Tome
   │     │  │  │  ├─ Timbuktu
   │     │  │  │  ├─ Tripoli
   │     │  │  │  ├─ Tunis
   │     │  │  │  ├─ Windhoek
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ America
   │     │  │  │  ├─ Adak
   │     │  │  │  ├─ Anchorage
   │     │  │  │  ├─ Anguilla
   │     │  │  │  ├─ Antigua
   │     │  │  │  ├─ Araguaina
   │     │  │  │  ├─ Argentina
   │     │  │  │  │  ├─ Buenos_Aires
   │     │  │  │  │  ├─ Catamarca
   │     │  │  │  │  ├─ ComodRivadavia
   │     │  │  │  │  ├─ Cordoba
   │     │  │  │  │  ├─ Jujuy
   │     │  │  │  │  ├─ La_Rioja
   │     │  │  │  │  ├─ Mendoza
   │     │  │  │  │  ├─ Rio_Gallegos
   │     │  │  │  │  ├─ Salta
   │     │  │  │  │  ├─ San_Juan
   │     │  │  │  │  ├─ San_Luis
   │     │  │  │  │  ├─ Tucuman
   │     │  │  │  │  ├─ Ushuaia
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ Aruba
   │     │  │  │  ├─ Asuncion
   │     │  │  │  ├─ Atikokan
   │     │  │  │  ├─ Atka
   │     │  │  │  ├─ Bahia
   │     │  │  │  ├─ Bahia_Banderas
   │     │  │  │  ├─ Barbados
   │     │  │  │  ├─ Belem
   │     │  │  │  ├─ Belize
   │     │  │  │  ├─ Blanc-Sablon
   │     │  │  │  ├─ Boa_Vista
   │     │  │  │  ├─ Bogota
   │     │  │  │  ├─ Boise
   │     │  │  │  ├─ Buenos_Aires
   │     │  │  │  ├─ Cambridge_Bay
   │     │  │  │  ├─ Campo_Grande
   │     │  │  │  ├─ Cancun
   │     │  │  │  ├─ Caracas
   │     │  │  │  ├─ Catamarca
   │     │  │  │  ├─ Cayenne
   │     │  │  │  ├─ Cayman
   │     │  │  │  ├─ Chicago
   │     │  │  │  ├─ Chihuahua
   │     │  │  │  ├─ Ciudad_Juarez
   │     │  │  │  ├─ Coral_Harbour
   │     │  │  │  ├─ Cordoba
   │     │  │  │  ├─ Costa_Rica
   │     │  │  │  ├─ Coyhaique
   │     │  │  │  ├─ Creston
   │     │  │  │  ├─ Cuiaba
   │     │  │  │  ├─ Curacao
   │     │  │  │  ├─ Danmarkshavn
   │     │  │  │  ├─ Dawson
   │     │  │  │  ├─ Dawson_Creek
   │     │  │  │  ├─ Denver
   │     │  │  │  ├─ Detroit
   │     │  │  │  ├─ Dominica
   │     │  │  │  ├─ Edmonton
   │     │  │  │  ├─ Eirunepe
   │     │  │  │  ├─ El_Salvador
   │     │  │  │  ├─ Ensenada
   │     │  │  │  ├─ Fortaleza
   │     │  │  │  ├─ Fort_Nelson
   │     │  │  │  ├─ Fort_Wayne
   │     │  │  │  ├─ Glace_Bay
   │     │  │  │  ├─ Godthab
   │     │  │  │  ├─ Goose_Bay
   │     │  │  │  ├─ Grand_Turk
   │     │  │  │  ├─ Grenada
   │     │  │  │  ├─ Guadeloupe
   │     │  │  │  ├─ Guatemala
   │     │  │  │  ├─ Guayaquil
   │     │  │  │  ├─ Guyana
   │     │  │  │  ├─ Halifax
   │     │  │  │  ├─ Havana
   │     │  │  │  ├─ Hermosillo
   │     │  │  │  ├─ Indiana
   │     │  │  │  │  ├─ Indianapolis
   │     │  │  │  │  ├─ Knox
   │     │  │  │  │  ├─ Marengo
   │     │  │  │  │  ├─ Petersburg
   │     │  │  │  │  ├─ Tell_City
   │     │  │  │  │  ├─ Vevay
   │     │  │  │  │  ├─ Vincennes
   │     │  │  │  │  ├─ Winamac
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ Indianapolis
   │     │  │  │  ├─ Inuvik
   │     │  │  │  ├─ Iqaluit
   │     │  │  │  ├─ Jamaica
   │     │  │  │  ├─ Jujuy
   │     │  │  │  ├─ Juneau
   │     │  │  │  ├─ Kentucky
   │     │  │  │  │  ├─ Louisville
   │     │  │  │  │  ├─ Monticello
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ Knox_IN
   │     │  │  │  ├─ Kralendijk
   │     │  │  │  ├─ La_Paz
   │     │  │  │  ├─ Lima
   │     │  │  │  ├─ Los_Angeles
   │     │  │  │  ├─ Louisville
   │     │  │  │  ├─ Lower_Princes
   │     │  │  │  ├─ Maceio
   │     │  │  │  ├─ Managua
   │     │  │  │  ├─ Manaus
   │     │  │  │  ├─ Marigot
   │     │  │  │  ├─ Martinique
   │     │  │  │  ├─ Matamoros
   │     │  │  │  ├─ Mazatlan
   │     │  │  │  ├─ Mendoza
   │     │  │  │  ├─ Menominee
   │     │  │  │  ├─ Merida
   │     │  │  │  ├─ Metlakatla
   │     │  │  │  ├─ Mexico_City
   │     │  │  │  ├─ Miquelon
   │     │  │  │  ├─ Moncton
   │     │  │  │  ├─ Monterrey
   │     │  │  │  ├─ Montevideo
   │     │  │  │  ├─ Montreal
   │     │  │  │  ├─ Montserrat
   │     │  │  │  ├─ Nassau
   │     │  │  │  ├─ New_York
   │     │  │  │  ├─ Nipigon
   │     │  │  │  ├─ Nome
   │     │  │  │  ├─ Noronha
   │     │  │  │  ├─ North_Dakota
   │     │  │  │  │  ├─ Beulah
   │     │  │  │  │  ├─ Center
   │     │  │  │  │  ├─ New_Salem
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ Nuuk
   │     │  │  │  ├─ Ojinaga
   │     │  │  │  ├─ Panama
   │     │  │  │  ├─ Pangnirtung
   │     │  │  │  ├─ Paramaribo
   │     │  │  │  ├─ Phoenix
   │     │  │  │  ├─ Port-au-Prince
   │     │  │  │  ├─ Porto_Acre
   │     │  │  │  ├─ Porto_Velho
   │     │  │  │  ├─ Port_of_Spain
   │     │  │  │  ├─ Puerto_Rico
   │     │  │  │  ├─ Punta_Arenas
   │     │  │  │  ├─ Rainy_River
   │     │  │  │  ├─ Rankin_Inlet
   │     │  │  │  ├─ Recife
   │     │  │  │  ├─ Regina
   │     │  │  │  ├─ Resolute
   │     │  │  │  ├─ Rio_Branco
   │     │  │  │  ├─ Rosario
   │     │  │  │  ├─ Santarem
   │     │  │  │  ├─ Santa_Isabel
   │     │  │  │  ├─ Santiago
   │     │  │  │  ├─ Santo_Domingo
   │     │  │  │  ├─ Sao_Paulo
   │     │  │  │  ├─ Scoresbysund
   │     │  │  │  ├─ Shiprock
   │     │  │  │  ├─ Sitka
   │     │  │  │  ├─ St_Barthelemy
   │     │  │  │  ├─ St_Johns
   │     │  │  │  ├─ St_Kitts
   │     │  │  │  ├─ St_Lucia
   │     │  │  │  ├─ St_Thomas
   │     │  │  │  ├─ St_Vincent
   │     │  │  │  ├─ Swift_Current
   │     │  │  │  ├─ Tegucigalpa
   │     │  │  │  ├─ Thule
   │     │  │  │  ├─ Thunder_Bay
   │     │  │  │  ├─ Tijuana
   │     │  │  │  ├─ Toronto
   │     │  │  │  ├─ Tortola
   │     │  │  │  ├─ Vancouver
   │     │  │  │  ├─ Virgin
   │     │  │  │  ├─ Whitehorse
   │     │  │  │  ├─ Winnipeg
   │     │  │  │  ├─ Yakutat
   │     │  │  │  ├─ Yellowknife
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Antarctica
   │     │  │  │  ├─ Casey
   │     │  │  │  ├─ Davis
   │     │  │  │  ├─ DumontDUrville
   │     │  │  │  ├─ Macquarie
   │     │  │  │  ├─ Mawson
   │     │  │  │  ├─ McMurdo
   │     │  │  │  ├─ Palmer
   │     │  │  │  ├─ Rothera
   │     │  │  │  ├─ South_Pole
   │     │  │  │  ├─ Syowa
   │     │  │  │  ├─ Troll
   │     │  │  │  ├─ Vostok
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Arctic
   │     │  │  │  ├─ Longyearbyen
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Asia
   │     │  │  │  ├─ Aden
   │     │  │  │  ├─ Almaty
   │     │  │  │  ├─ Amman
   │     │  │  │  ├─ Anadyr
   │     │  │  │  ├─ Aqtau
   │     │  │  │  ├─ Aqtobe
   │     │  │  │  ├─ Ashgabat
   │     │  │  │  ├─ Ashkhabad
   │     │  │  │  ├─ Atyrau
   │     │  │  │  ├─ Baghdad
   │     │  │  │  ├─ Bahrain
   │     │  │  │  ├─ Baku
   │     │  │  │  ├─ Bangkok
   │     │  │  │  ├─ Barnaul
   │     │  │  │  ├─ Beirut
   │     │  │  │  ├─ Bishkek
   │     │  │  │  ├─ Brunei
   │     │  │  │  ├─ Calcutta
   │     │  │  │  ├─ Chita
   │     │  │  │  ├─ Choibalsan
   │     │  │  │  ├─ Chongqing
   │     │  │  │  ├─ Chungking
   │     │  │  │  ├─ Colombo
   │     │  │  │  ├─ Dacca
   │     │  │  │  ├─ Damascus
   │     │  │  │  ├─ Dhaka
   │     │  │  │  ├─ Dili
   │     │  │  │  ├─ Dubai
   │     │  │  │  ├─ Dushanbe
   │     │  │  │  ├─ Famagusta
   │     │  │  │  ├─ Gaza
   │     │  │  │  ├─ Harbin
   │     │  │  │  ├─ Hebron
   │     │  │  │  ├─ Hong_Kong
   │     │  │  │  ├─ Hovd
   │     │  │  │  ├─ Ho_Chi_Minh
   │     │  │  │  ├─ Irkutsk
   │     │  │  │  ├─ Istanbul
   │     │  │  │  ├─ Jakarta
   │     │  │  │  ├─ Jayapura
   │     │  │  │  ├─ Jerusalem
   │     │  │  │  ├─ Kabul
   │     │  │  │  ├─ Kamchatka
   │     │  │  │  ├─ Karachi
   │     │  │  │  ├─ Kashgar
   │     │  │  │  ├─ Kathmandu
   │     │  │  │  ├─ Katmandu
   │     │  │  │  ├─ Khandyga
   │     │  │  │  ├─ Kolkata
   │     │  │  │  ├─ Krasnoyarsk
   │     │  │  │  ├─ Kuala_Lumpur
   │     │  │  │  ├─ Kuching
   │     │  │  │  ├─ Kuwait
   │     │  │  │  ├─ Macao
   │     │  │  │  ├─ Macau
   │     │  │  │  ├─ Magadan
   │     │  │  │  ├─ Makassar
   │     │  │  │  ├─ Manila
   │     │  │  │  ├─ Muscat
   │     │  │  │  ├─ Nicosia
   │     │  │  │  ├─ Novokuznetsk
   │     │  │  │  ├─ Novosibirsk
   │     │  │  │  ├─ Omsk
   │     │  │  │  ├─ Oral
   │     │  │  │  ├─ Phnom_Penh
   │     │  │  │  ├─ Pontianak
   │     │  │  │  ├─ Pyongyang
   │     │  │  │  ├─ Qatar
   │     │  │  │  ├─ Qostanay
   │     │  │  │  ├─ Qyzylorda
   │     │  │  │  ├─ Rangoon
   │     │  │  │  ├─ Riyadh
   │     │  │  │  ├─ Saigon
   │     │  │  │  ├─ Sakhalin
   │     │  │  │  ├─ Samarkand
   │     │  │  │  ├─ Seoul
   │     │  │  │  ├─ Shanghai
   │     │  │  │  ├─ Singapore
   │     │  │  │  ├─ Srednekolymsk
   │     │  │  │  ├─ Taipei
   │     │  │  │  ├─ Tashkent
   │     │  │  │  ├─ Tbilisi
   │     │  │  │  ├─ Tehran
   │     │  │  │  ├─ Tel_Aviv
   │     │  │  │  ├─ Thimbu
   │     │  │  │  ├─ Thimphu
   │     │  │  │  ├─ Tokyo
   │     │  │  │  ├─ Tomsk
   │     │  │  │  ├─ Ujung_Pandang
   │     │  │  │  ├─ Ulaanbaatar
   │     │  │  │  ├─ Ulan_Bator
   │     │  │  │  ├─ Urumqi
   │     │  │  │  ├─ Ust-Nera
   │     │  │  │  ├─ Vientiane
   │     │  │  │  ├─ Vladivostok
   │     │  │  │  ├─ Yakutsk
   │     │  │  │  ├─ Yangon
   │     │  │  │  ├─ Yekaterinburg
   │     │  │  │  ├─ Yerevan
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Atlantic
   │     │  │  │  ├─ Azores
   │     │  │  │  ├─ Bermuda
   │     │  │  │  ├─ Canary
   │     │  │  │  ├─ Cape_Verde
   │     │  │  │  ├─ Faeroe
   │     │  │  │  ├─ Faroe
   │     │  │  │  ├─ Jan_Mayen
   │     │  │  │  ├─ Madeira
   │     │  │  │  ├─ Reykjavik
   │     │  │  │  ├─ South_Georgia
   │     │  │  │  ├─ Stanley
   │     │  │  │  ├─ St_Helena
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Australia
   │     │  │  │  ├─ ACT
   │     │  │  │  ├─ Adelaide
   │     │  │  │  ├─ Brisbane
   │     │  │  │  ├─ Broken_Hill
   │     │  │  │  ├─ Canberra
   │     │  │  │  ├─ Currie
   │     │  │  │  ├─ Darwin
   │     │  │  │  ├─ Eucla
   │     │  │  │  ├─ Hobart
   │     │  │  │  ├─ LHI
   │     │  │  │  ├─ Lindeman
   │     │  │  │  ├─ Lord_Howe
   │     │  │  │  ├─ Melbourne
   │     │  │  │  ├─ North
   │     │  │  │  ├─ NSW
   │     │  │  │  ├─ Perth
   │     │  │  │  ├─ Queensland
   │     │  │  │  ├─ South
   │     │  │  │  ├─ Sydney
   │     │  │  │  ├─ Tasmania
   │     │  │  │  ├─ Victoria
   │     │  │  │  ├─ West
   │     │  │  │  ├─ Yancowinna
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Brazil
   │     │  │  │  ├─ Acre
   │     │  │  │  ├─ DeNoronha
   │     │  │  │  ├─ East
   │     │  │  │  ├─ West
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Canada
   │     │  │  │  ├─ Atlantic
   │     │  │  │  ├─ Central
   │     │  │  │  ├─ Eastern
   │     │  │  │  ├─ Mountain
   │     │  │  │  ├─ Newfoundland
   │     │  │  │  ├─ Pacific
   │     │  │  │  ├─ Saskatchewan
   │     │  │  │  ├─ Yukon
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ CET
   │     │  │  ├─ Chile
   │     │  │  │  ├─ Continental
   │     │  │  │  ├─ EasterIsland
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ CST6CDT
   │     │  │  ├─ Cuba
   │     │  │  ├─ EET
   │     │  │  ├─ Egypt
   │     │  │  ├─ Eire
   │     │  │  ├─ EST
   │     │  │  ├─ EST5EDT
   │     │  │  ├─ Etc
   │     │  │  │  ├─ GMT
   │     │  │  │  ├─ GMT+0
   │     │  │  │  ├─ GMT+1
   │     │  │  │  ├─ GMT+10
   │     │  │  │  ├─ GMT+11
   │     │  │  │  ├─ GMT+12
   │     │  │  │  ├─ GMT+2
   │     │  │  │  ├─ GMT+3
   │     │  │  │  ├─ GMT+4
   │     │  │  │  ├─ GMT+5
   │     │  │  │  ├─ GMT+6
   │     │  │  │  ├─ GMT+7
   │     │  │  │  ├─ GMT+8
   │     │  │  │  ├─ GMT+9
   │     │  │  │  ├─ GMT-0
   │     │  │  │  ├─ GMT-1
   │     │  │  │  ├─ GMT-10
   │     │  │  │  ├─ GMT-11
   │     │  │  │  ├─ GMT-12
   │     │  │  │  ├─ GMT-13
   │     │  │  │  ├─ GMT-14
   │     │  │  │  ├─ GMT-2
   │     │  │  │  ├─ GMT-3
   │     │  │  │  ├─ GMT-4
   │     │  │  │  ├─ GMT-5
   │     │  │  │  ├─ GMT-6
   │     │  │  │  ├─ GMT-7
   │     │  │  │  ├─ GMT-8
   │     │  │  │  ├─ GMT-9
   │     │  │  │  ├─ GMT0
   │     │  │  │  ├─ Greenwich
   │     │  │  │  ├─ UCT
   │     │  │  │  ├─ Universal
   │     │  │  │  ├─ UTC
   │     │  │  │  ├─ Zulu
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Europe
   │     │  │  │  ├─ Amsterdam
   │     │  │  │  ├─ Andorra
   │     │  │  │  ├─ Astrakhan
   │     │  │  │  ├─ Athens
   │     │  │  │  ├─ Belfast
   │     │  │  │  ├─ Belgrade
   │     │  │  │  ├─ Berlin
   │     │  │  │  ├─ Bratislava
   │     │  │  │  ├─ Brussels
   │     │  │  │  ├─ Bucharest
   │     │  │  │  ├─ Budapest
   │     │  │  │  ├─ Busingen
   │     │  │  │  ├─ Chisinau
   │     │  │  │  ├─ Copenhagen
   │     │  │  │  ├─ Dublin
   │     │  │  │  ├─ Gibraltar
   │     │  │  │  ├─ Guernsey
   │     │  │  │  ├─ Helsinki
   │     │  │  │  ├─ Isle_of_Man
   │     │  │  │  ├─ Istanbul
   │     │  │  │  ├─ Jersey
   │     │  │  │  ├─ Kaliningrad
   │     │  │  │  ├─ Kiev
   │     │  │  │  ├─ Kirov
   │     │  │  │  ├─ Kyiv
   │     │  │  │  ├─ Lisbon
   │     │  │  │  ├─ Ljubljana
   │     │  │  │  ├─ London
   │     │  │  │  ├─ Luxembourg
   │     │  │  │  ├─ Madrid
   │     │  │  │  ├─ Malta
   │     │  │  │  ├─ Mariehamn
   │     │  │  │  ├─ Minsk
   │     │  │  │  ├─ Monaco
   │     │  │  │  ├─ Moscow
   │     │  │  │  ├─ Nicosia
   │     │  │  │  ├─ Oslo
   │     │  │  │  ├─ Paris
   │     │  │  │  ├─ Podgorica
   │     │  │  │  ├─ Prague
   │     │  │  │  ├─ Riga
   │     │  │  │  ├─ Rome
   │     │  │  │  ├─ Samara
   │     │  │  │  ├─ San_Marino
   │     │  │  │  ├─ Sarajevo
   │     │  │  │  ├─ Saratov
   │     │  │  │  ├─ Simferopol
   │     │  │  │  ├─ Skopje
   │     │  │  │  ├─ Sofia
   │     │  │  │  ├─ Stockholm
   │     │  │  │  ├─ Tallinn
   │     │  │  │  ├─ Tirane
   │     │  │  │  ├─ Tiraspol
   │     │  │  │  ├─ Ulyanovsk
   │     │  │  │  ├─ Uzhgorod
   │     │  │  │  ├─ Vaduz
   │     │  │  │  ├─ Vatican
   │     │  │  │  ├─ Vienna
   │     │  │  │  ├─ Vilnius
   │     │  │  │  ├─ Volgograd
   │     │  │  │  ├─ Warsaw
   │     │  │  │  ├─ Zagreb
   │     │  │  │  ├─ Zaporozhye
   │     │  │  │  ├─ Zurich
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Factory
   │     │  │  ├─ GB
   │     │  │  ├─ GB-Eire
   │     │  │  ├─ GMT
   │     │  │  ├─ GMT+0
   │     │  │  ├─ GMT-0
   │     │  │  ├─ GMT0
   │     │  │  ├─ Greenwich
   │     │  │  ├─ Hongkong
   │     │  │  ├─ HST
   │     │  │  ├─ Iceland
   │     │  │  ├─ Indian
   │     │  │  │  ├─ Antananarivo
   │     │  │  │  ├─ Chagos
   │     │  │  │  ├─ Christmas
   │     │  │  │  ├─ Cocos
   │     │  │  │  ├─ Comoro
   │     │  │  │  ├─ Kerguelen
   │     │  │  │  ├─ Mahe
   │     │  │  │  ├─ Maldives
   │     │  │  │  ├─ Mauritius
   │     │  │  │  ├─ Mayotte
   │     │  │  │  ├─ Reunion
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Iran
   │     │  │  ├─ iso3166.tab
   │     │  │  ├─ Israel
   │     │  │  ├─ Jamaica
   │     │  │  ├─ Japan
   │     │  │  ├─ Kwajalein
   │     │  │  ├─ leapseconds
   │     │  │  ├─ Libya
   │     │  │  ├─ MET
   │     │  │  ├─ Mexico
   │     │  │  │  ├─ BajaNorte
   │     │  │  │  ├─ BajaSur
   │     │  │  │  ├─ General
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ MST
   │     │  │  ├─ MST7MDT
   │     │  │  ├─ Navajo
   │     │  │  ├─ NZ
   │     │  │  ├─ NZ-CHAT
   │     │  │  ├─ Pacific
   │     │  │  │  ├─ Apia
   │     │  │  │  ├─ Auckland
   │     │  │  │  ├─ Bougainville
   │     │  │  │  ├─ Chatham
   │     │  │  │  ├─ Chuuk
   │     │  │  │  ├─ Easter
   │     │  │  │  ├─ Efate
   │     │  │  │  ├─ Enderbury
   │     │  │  │  ├─ Fakaofo
   │     │  │  │  ├─ Fiji
   │     │  │  │  ├─ Funafuti
   │     │  │  │  ├─ Galapagos
   │     │  │  │  ├─ Gambier
   │     │  │  │  ├─ Guadalcanal
   │     │  │  │  ├─ Guam
   │     │  │  │  ├─ Honolulu
   │     │  │  │  ├─ Johnston
   │     │  │  │  ├─ Kanton
   │     │  │  │  ├─ Kiritimati
   │     │  │  │  ├─ Kosrae
   │     │  │  │  ├─ Kwajalein
   │     │  │  │  ├─ Majuro
   │     │  │  │  ├─ Marquesas
   │     │  │  │  ├─ Midway
   │     │  │  │  ├─ Nauru
   │     │  │  │  ├─ Niue
   │     │  │  │  ├─ Norfolk
   │     │  │  │  ├─ Noumea
   │     │  │  │  ├─ Pago_Pago
   │     │  │  │  ├─ Palau
   │     │  │  │  ├─ Pitcairn
   │     │  │  │  ├─ Pohnpei
   │     │  │  │  ├─ Ponape
   │     │  │  │  ├─ Port_Moresby
   │     │  │  │  ├─ Rarotonga
   │     │  │  │  ├─ Saipan
   │     │  │  │  ├─ Samoa
   │     │  │  │  ├─ Tahiti
   │     │  │  │  ├─ Tarawa
   │     │  │  │  ├─ Tongatapu
   │     │  │  │  ├─ Truk
   │     │  │  │  ├─ Wake
   │     │  │  │  ├─ Wallis
   │     │  │  │  ├─ Yap
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Poland
   │     │  │  ├─ Portugal
   │     │  │  ├─ PRC
   │     │  │  ├─ PST8PDT
   │     │  │  ├─ ROC
   │     │  │  ├─ ROK
   │     │  │  ├─ Singapore
   │     │  │  ├─ Turkey
   │     │  │  ├─ tzdata.zi
   │     │  │  ├─ UCT
   │     │  │  ├─ Universal
   │     │  │  ├─ US
   │     │  │  │  ├─ Alaska
   │     │  │  │  ├─ Aleutian
   │     │  │  │  ├─ Arizona
   │     │  │  │  ├─ Central
   │     │  │  │  ├─ East-Indiana
   │     │  │  │  ├─ Eastern
   │     │  │  │  ├─ Hawaii
   │     │  │  │  ├─ Indiana-Starke
   │     │  │  │  ├─ Michigan
   │     │  │  │  ├─ Mountain
   │     │  │  │  ├─ Pacific
   │     │  │  │  ├─ Samoa
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ UTC
   │     │  │  ├─ W-SU
   │     │  │  ├─ WET
   │     │  │  ├─ zone.tab
   │     │  │  ├─ zone1970.tab
   │     │  │  ├─ zonenow.tab
   │     │  │  ├─ Zulu
   │     │  │  └─ __init__.py
   │     │  ├─ zones
   │     │  └─ __init__.py
   │     ├─ tzdata-2026.3.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ LICENSE
   │     │  │  └─ licenses
   │     │  │     └─ LICENSE_APACHE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ urllib3
   │     │  ├─ connection.py
   │     │  ├─ connectionpool.py
   │     │  ├─ contrib
   │     │  │  ├─ emscripten
   │     │  │  │  ├─ connection.py
   │     │  │  │  ├─ emscripten_fetch_worker.js
   │     │  │  │  ├─ fetch.py
   │     │  │  │  ├─ request.py
   │     │  │  │  ├─ response.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pyopenssl.py
   │     │  │  ├─ socks.py
   │     │  │  └─ __init__.py
   │     │  ├─ exceptions.py
   │     │  ├─ fields.py
   │     │  ├─ filepost.py
   │     │  ├─ http2
   │     │  │  ├─ connection.py
   │     │  │  ├─ probe.py
   │     │  │  └─ __init__.py
   │     │  ├─ poolmanager.py
   │     │  ├─ py.typed
   │     │  ├─ response.py
   │     │  ├─ util
   │     │  │  ├─ connection.py
   │     │  │  ├─ proxy.py
   │     │  │  ├─ request.py
   │     │  │  ├─ response.py
   │     │  │  ├─ retry.py
   │     │  │  ├─ ssltransport.py
   │     │  │  ├─ ssl_.py
   │     │  │  ├─ ssl_match_hostname.py
   │     │  │  ├─ timeout.py
   │     │  │  ├─ url.py
   │     │  │  ├─ util.py
   │     │  │  ├─ wait.py
   │     │  │  └─ __init__.py
   │     │  ├─ _base_connection.py
   │     │  ├─ _collections.py
   │     │  ├─ _request_methods.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ urllib3-2.7.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ wheel
   │     │  ├─ bdist_wheel.py
   │     │  ├─ macosx_libfile.py
   │     │  ├─ metadata.py
   │     │  ├─ wheelfile.py
   │     │  ├─ _bdist_wheel.py
   │     │  ├─ _commands
   │     │  │  ├─ convert.py
   │     │  │  ├─ info.py
   │     │  │  ├─ pack.py
   │     │  │  ├─ tags.py
   │     │  │  ├─ unpack.py
   │     │  │  └─ __init__.py
   │     │  ├─ _metadata.py
   │     │  ├─ _setuptools_logging.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ wheel-0.48.0.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ wrapt
   │     │  ├─ arguments.py
   │     │  ├─ caching.py
   │     │  ├─ decorators.py
   │     │  ├─ importer.py
   │     │  ├─ patches.py
   │     │  ├─ proxies.py
   │     │  ├─ signature.py
   │     │  ├─ synchronization.py
   │     │  ├─ weakrefs.py
   │     │  ├─ wrappers.py
   │     │  ├─ _wrappers.c
   │     │  ├─ __init__.py
   │     │  └─ __wrapt__.py
   │     ├─ wrapt-2.3.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ wrapt-stubs
   │     │  └─ __init__.pyi
   │     ├─ _distutils_hack
   │     │  ├─ override.py
   │     │  └─ __init__.py
   │     ├─ _pytest
   │     │  ├─ assertion
   │     │  │  ├─ compare_text.py
   │     │  │  ├─ highlight.py
   │     │  │  ├─ rewrite.py
   │     │  │  ├─ truncate.py
   │     │  │  ├─ util.py
   │     │  │  ├─ _compare_any.py
   │     │  │  ├─ _compare_mapping.py
   │     │  │  ├─ _compare_sequence.py
   │     │  │  ├─ _compare_set.py
   │     │  │  ├─ _guards.py
   │     │  │  ├─ _typing.py
   │     │  │  └─ __init__.py
   │     │  ├─ cacheprovider.py
   │     │  ├─ capture.py
   │     │  ├─ compat.py
   │     │  ├─ config
   │     │  │  ├─ argparsing.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ findpaths.py
   │     │  │  └─ __init__.py
   │     │  ├─ debugging.py
   │     │  ├─ deprecated.py
   │     │  ├─ doctest.py
   │     │  ├─ faulthandler.py
   │     │  ├─ fixtures.py
   │     │  ├─ freeze_support.py
   │     │  ├─ helpconfig.py
   │     │  ├─ hookspec.py
   │     │  ├─ junitxml.py
   │     │  ├─ legacypath.py
   │     │  ├─ logging.py
   │     │  ├─ main.py
   │     │  ├─ mark
   │     │  │  ├─ expression.py
   │     │  │  ├─ structures.py
   │     │  │  └─ __init__.py
   │     │  ├─ monkeypatch.py
   │     │  ├─ nodes.py
   │     │  ├─ outcomes.py
   │     │  ├─ pastebin.py
   │     │  ├─ pathlib.py
   │     │  ├─ py.typed
   │     │  ├─ pytester.py
   │     │  ├─ pytester_assertions.py
   │     │  ├─ python.py
   │     │  ├─ python_api.py
   │     │  ├─ raises.py
   │     │  ├─ recwarn.py
   │     │  ├─ reports.py
   │     │  ├─ runner.py
   │     │  ├─ scope.py
   │     │  ├─ setuponly.py
   │     │  ├─ setupplan.py
   │     │  ├─ skipping.py
   │     │  ├─ stash.py
   │     │  ├─ stepwise.py
   │     │  ├─ subtests.py
   │     │  ├─ terminal.py
   │     │  ├─ terminalprogress.py
   │     │  ├─ threadexception.py
   │     │  ├─ timing.py
   │     │  ├─ tmpdir.py
   │     │  ├─ tracemalloc.py
   │     │  ├─ unittest.py
   │     │  ├─ unraisableexception.py
   │     │  ├─ warnings.py
   │     │  ├─ warning_types.py
   │     │  ├─ _argcomplete.py
   │     │  ├─ _code
   │     │  │  ├─ code.py
   │     │  │  ├─ source.py
   │     │  │  └─ __init__.py
   │     │  ├─ _io
   │     │  │  ├─ pprint.py
   │     │  │  ├─ saferepr.py
   │     │  │  ├─ terminalwriter.py
   │     │  │  ├─ wcwidth.py
   │     │  │  └─ __init__.py
   │     │  ├─ _py
   │     │  │  ├─ error.py
   │     │  │  ├─ path.py
   │     │  │  └─ __init__.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ _virtualenv.pth
   │     ├─ _virtualenv.py
   │     ├─ __editable__.pd_modules-0.1.0.pth
   │     └─ __editable___pd_modules_0_1_0_finder.py
   ├─ pyvenv.cfg
   ├─ Scripts
   │  ├─ activate
   │  ├─ activate.bat
   │  ├─ activate.csh
   │  ├─ activate.fish
   │  ├─ activate.nu
   │  ├─ activate.ps1
   │  ├─ activate.xsh
   │  ├─ activate_this.py
   │  ├─ cffi-gen-src.exe
   │  ├─ deactivate.bat
   │  ├─ f2py.exe
   │  ├─ fonttools.exe
   │  ├─ idna.exe
   │  ├─ markdown-it.exe
   │  ├─ normalizer.exe
   │  ├─ numpy-config.exe
   │  ├─ pip.exe
   │  ├─ pip3.10.exe
   │  ├─ pip3.exe
   │  ├─ py.test.exe
   │  ├─ pydoc.bat
   │  ├─ pyftmerge.exe
   │  ├─ pyftsubset.exe
   │  ├─ pygmentize.exe
   │  ├─ pytest.exe
   │  ├─ python.exe
   │  ├─ pythonw.exe
   │  ├─ tqdm.exe
   │  ├─ ttx.exe
   │  └─ wheel.exe
   └─ share
      └─ man
         └─ man1
            ├─ .tmpYU8y3T
            └─ ttx.1

```