# Project Structure

The repository is organized to separate source code, model pipeline code, generated or binary artifacts, local data, runtime state, and documentation.

## Canonical Layout

```text
.
├── dermascan_app/
│   ├── app.py
│   ├── inference.py
│   ├── requirements.txt
│   └── templates/
├── ml_pipeline/
│   ├── config/
│   │   └── model_parameters.json
│   ├── evaluation/
│   │   └── evaluate_cnn.py
│   ├── registry/
│   │   └── progress_log.csv
│   └── training/
│       └── train_cnn.py
├── artifacts/
│   ├── models/
│   │   └── current/
│   │       └── melanoma_detector.keras
│   └── sample_inputs/
│       └── legacy_uploads/
├── data/
│   └── README.md
├── var/
│   ├── README.md
│   └── uploads/
├── docs/
│   ├── archived_previous_documents/
│   └── *.md
├── README.md
├── SECURITY.md
└── LICENSE
```

## Naming Rationale

| Name | Rationale |
|---|---|
| `dermascan_app/` | Runtime application code only. This avoids the vague `backend` label and ties the folder to the product prototype. |
| `ml_pipeline/` | Training, evaluation, configuration, and registry files live together as the reproducibility surface. |
| `ml_pipeline/config/` | Parameters that define a model run belong in a predictable config home. |
| `ml_pipeline/registry/` | Historical metrics and model iteration records are treated as registry metadata. |
| `artifacts/` | Binary or non-source assets live outside app and pipeline source. |
| `artifacts/models/current/` | The app has a stable path for the currently packaged model. |
| `artifacts/sample_inputs/legacy_uploads/` | Old uploads are preserved as reviewable samples, not runtime state. |
| `data/` | Local datasets and manifests belong here, but datasets are intentionally not committed. |
| `var/` | Runtime state such as local uploads belongs here and should stay out of source control. |
| `docs/archived_previous_documents/` | Previous documentation is preserved without competing with the active docs. |

## Reproducibility Contract

Future model work should be reproducible from:

- `data/` dataset manifests
- `ml_pipeline/config/model_parameters.json`
- `ml_pipeline/training/train_cnn.py`
- `ml_pipeline/evaluation/evaluate_cnn.py`
- `ml_pipeline/registry/progress_log.csv`
- `artifacts/models/current/melanoma_detector.keras`

Any new model release should record:

- dataset version
- train/validation/test split manifest
- dependency versions
- training command
- evaluation command
- threshold policy
- generated metrics
- model artifact path

