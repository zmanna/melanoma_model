# UML And Diagrams

This document provides Mermaid diagrams for the DermaScan prototype. GitHub can render these diagrams directly.

## High-Level System Architecture

```mermaid
flowchart LR
    user["User / Reviewer"] --> browser["Browser UI"]
    browser --> flask["Flask App<br/>dermascan_app/app.py"]
    flask --> uploads["Runtime Uploads<br/>var/uploads/"]
    flask --> cv2["OpenCV Readability Check"]
    flask --> inference["Inference Helper<br/>dermascan_app/inference.py"]
    inference --> model["Keras Model Artifact<br/>artifacts/models/current/"]
    inference --> tfprep["TensorFlow Image Preprocessing"]
    tfprep --> model
    model --> score["Raw Sigmoid Score"]
    score --> response["JSON Prediction Response"]
    response --> browser
```

## Main Inference Sequence

```mermaid
sequenceDiagram
    actor User
    participant Browser
    participant Flask as Flask /upload
    participant Storage as var/uploads
    participant CV as OpenCV
    participant Inference as inference.py
    participant Model as Keras model

    User->>Browser: Select image
    Browser->>Flask: POST /upload
    Flask->>Flask: Validate file presence and extension
    Flask->>Storage: Save upload
    Flask->>CV: Read saved image
    CV-->>Flask: Image readable / not readable
    Flask->>Inference: predict_lesion(image_path)
    Inference->>Model: Lazy load model if needed
    Inference->>Inference: Resize and normalize image
    Inference->>Model: Predict
    Model-->>Inference: Raw score
    Inference-->>Flask: Score
    Flask->>Flask: Apply runtime threshold
    Flask-->>Browser: JSON result
```

## Training And Evaluation Data Flow

```mermaid
flowchart TD
    dataset["data/melanoma_cancer_dataset/"] --> trainSplit["train/ benign + malignant"]
    dataset --> valSplit["validation/ benign + malignant"]
    dataset --> testSplit["test/ benign + malignant"]
    config["ml_pipeline/config/model_parameters.json"] --> trainScript["train_cnn.py"]
    trainSplit --> trainScript
    valSplit --> trainScript
    trainScript --> trainedModel["artifacts/models/current/melanoma_detector.keras"]
    trainScript --> progress["ml_pipeline/registry/progress_log.csv"]
    testSplit --> evalScript["evaluate_cnn.py"]
    trainedModel --> evalScript
    config --> evalScript
    evalScript --> report["Classification Report"]
    evalScript --> matrix["Confusion Matrix"]
```

## Module Dependency Diagram

```mermaid
flowchart LR
    app["dermascan_app/app.py"] --> inference["dermascan_app/inference.py"]
    app --> templates["dermascan_app/templates/"]
    app --> uploads["var/uploads/"]
    inference --> modelArtifact["artifacts/models/current/melanoma_detector.keras"]
    train["ml_pipeline/training/train_cnn.py"] --> config["ml_pipeline/config/model_parameters.json"]
    train --> data["data/melanoma_cancer_dataset/"]
    train --> registry["ml_pipeline/registry/progress_log.csv"]
    train --> modelArtifact
    eval["ml_pipeline/evaluation/evaluate_cnn.py"] --> config
    eval --> data
    eval --> modelArtifact
```

## Class And Module View

The current codebase is script/module-oriented rather than object-oriented. This diagram models modules and major functions.

```mermaid
classDiagram
    class FlaskApp {
        +allowed_file(filename) bool
        +home()
        +about()
        +education()
        +contact()
        +disclaimer()
        +upload_file()
    }

    class InferenceModule {
        +load_model()
        +predict_lesion(image_path) float
    }

    class TrainingScript {
        +plot_metrics(history)
        +log_metrics(history, conf_matrix)
    }

    class EvaluationScript {
        +load test dataset
        +load model artifact
        +classification_report()
        +confusion_matrix()
    }

    FlaskApp --> InferenceModule : calls
    InferenceModule --> "Keras Model" : loads
    TrainingScript --> "Keras Model" : writes
    EvaluationScript --> "Keras Model" : reads
```

## Repository Responsibility Map

```mermaid
flowchart TB
    repo["Repository Root"]
    repo --> appDir["dermascan_app<br/>Runtime application"]
    repo --> pipelineDir["ml_pipeline<br/>Training and evaluation"]
    repo --> artifactDir["artifacts<br/>Model and sample artifacts"]
    repo --> dataDir["data<br/>Local datasets and manifests"]
    repo --> varDir["var<br/>Runtime state"]
    repo --> docsDir["docs<br/>Documentation"]
    repo --> security["SECURITY.md<br/>Security posture"]
```

