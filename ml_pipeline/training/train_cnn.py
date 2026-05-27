"""Train the DermaScan CNN baseline.

This script expects a local directory dataset under
`data/melanoma_cancer_dataset/` with train/validation/test splits and
`benign` / `malignant` class folders. It writes the current model artifact to
`artifacts/models/current/melanoma_detector.keras` and appends summary metrics
to `ml_pipeline/registry/progress_log.csv`.
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, Activation
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os
import json
import csv
from pathlib import Path

IMAGE_SIZE = (256, 256)
PIPELINE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = PIPELINE_ROOT.parent
CONFIG_PATH = PIPELINE_ROOT / 'config' / 'model_parameters.json'
DATA_DIR = PROJECT_ROOT / 'data' / 'melanoma_cancer_dataset'
MODEL_OUTPUT_PATH = PROJECT_ROOT / 'artifacts' / 'models' / 'current' / 'melanoma_detector.keras'
PROGRESS_LOG_PATH = PIPELINE_ROOT / 'registry' / 'progress_log.csv'

with open(CONFIG_PATH, 'r') as f:
    params = json.load(f)

version = params['version']
benign_images = params['benign_images']
malignant_images = params['malignant_images']
convolutional_layers = params['convolutional_layers']
dense_layers = params['dense_layers']
dense_nodes = params['dense_nodes']
batch_size = params['batch_size']
dropout = params['dropout']
epochs = params['epochs']
threshold = params['threshold']

training_dir = DATA_DIR / 'train'
validation_dir = DATA_DIR / 'validation'
test_dir = DATA_DIR / 'test'

train = tf.keras.utils.image_dataset_from_directory(
    training_dir,
    label_mode='binary',
    image_size=IMAGE_SIZE,
    batch_size=batch_size,
    shuffle=True
)

val = tf.keras.utils.image_dataset_from_directory(
    validation_dir,
    label_mode='binary',
    image_size=IMAGE_SIZE,
    batch_size=batch_size,
    shuffle=True
)

test = tf.keras.utils.image_dataset_from_directory(
    test_dir,
    label_mode='binary',
    image_size=IMAGE_SIZE,
    batch_size=batch_size,
    shuffle=False
)

class_names = test.class_names

train = train.map(lambda x,y: (x/255.0, y))
val = val.map(lambda x,y: (x/255.0, y))
test = test.map(lambda x,y: (x/255.0, y))

layers = [
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3)),
    MaxPooling2D()
]

nodes = 64
for i in range(1, convolutional_layers):
    layers.append(Conv2D(nodes, (3, 3), activation='relu'))
    layers.append(BatchNormalization())
    layers.append(Activation('relu'))
    layers.append(MaxPooling2D(pool_size=(2,2)))
    nodes *= 2

layers.append(Flatten())

for i in range(dense_layers):
    layers.append(Dense(dense_nodes, activation='relu'))

layers.append(Dropout(dropout))
layers.append(Dense(1, activation='sigmoid'))

model = Sequential(layers)

model.summary()
print("Version:", version)
print("Benign training images:", len(os.listdir(training_dir / "benign")))
print("Malignant training images:", len(os.listdir(training_dir / "malignant")))
print("Benign validation images:", len(os.listdir(validation_dir / "benign")))
print("Malignant validation images:", len(os.listdir(validation_dir / "malignant")))
print("Batch Size:", batch_size)
print("Dropout Rate:", dropout)
print("Epochs:", epochs)

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy', tf.keras.metrics.Precision(), tf.keras.metrics.Recall()]
)

history = model.fit(
    train,
    epochs=epochs,
    validation_data=val
)

def plot_metrics(history):
    """Display training and validation curves for key Keras metrics."""
    metrics = ['loss', 'accuracy', 'precision', 'recall']
    for metric in metrics:
        plt.plot(history.history[metric], label=f'Train {metric}')
        plt.plot(history.history[f'val_{metric}'], label=f'Val {metric}')
        plt.title(f'{metric.capitalize()} Over Epochs')
        plt.xlabel('Epochs')
        plt.ylabel(metric.capitalize())
        plt.legend()
        plt.show()

def log_metrics(history, conf_matrix):
    """Append aggregate confusion-matrix metrics to the progress log."""
    true_negatives = conf_matrix[0][0]
    false_positives = conf_matrix[0][1]
    false_negatives = conf_matrix[1][0]
    true_positives = conf_matrix[1][1]

    total = true_negatives + false_positives + false_negatives + true_positives
    accuracy = (true_negatives + true_positives) / total
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    f1_score = 2 * ((precision * recall) / (precision + recall))

    new_iteration = [
        version,
        benign_images,
        malignant_images,
        convolutional_layers,
        dense_layers,
        dense_nodes,
        batch_size,
        dropout,
        epochs,
        threshold,
        accuracy,
        precision,
        recall,
        f1_score
    ]
    
    with open(PROGRESS_LOG_PATH, mode='a', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(new_iteration)

plot_metrics(history)

model.save(MODEL_OUTPUT_PATH)

model = tf.keras.models.load_model(MODEL_OUTPUT_PATH)

y_pred_prob = model.predict(test)
y_pred = (y_pred_prob > threshold).astype(int)

y_true = np.concatenate([y for x, y in test], axis=0)

print("\nClassification Report:\n", classification_report(y_true, y_pred, target_names=class_names))

conf_matrix = confusion_matrix(y_true, y_pred)
log_metrics(history, conf_matrix)

plt.figure(figsize=(6, 5))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
