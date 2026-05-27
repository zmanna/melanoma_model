# TensorFlow Tools Guide
All details are subject to change as the project progresses.

## Introduction
This guide provides a brief overview of tools relevant to the melanoma model from the TensorFlow library. For a more in depth guide please see TensorFlow's website documentation.

## First Iteration Tools 
During the first iteration of the Melanoma Model the team emphasized a rough and simple design much like what you may see in other convolutional neural network tutorials. 

```Python
import tensorflow as tf 
```
In the code snippet above TensorFlow is imported into the program as it will be the main library used for the machine learning model and there are many online resources for it. 

```Python
from tensorflow.keras.models import Sequential
```
From the TensorFlow library the team imports Sequential. The Sequential model is appropriate because the project is an image processing tool use for identifying skin cancer. Meaning that the linear structure of the CNN style model will be easy to implement using sequential.

```Python
from tensorflow.keras.layers import Conv2D, Flatten, Dense
```
From the TensorFlow library the team imports Conv2D, Flatten, and Dense as they are used to create layers and are essential to build a convolutional neural network. Conv2D applies convolutional operations to input images, flatten provides the ability to flatten inputs without affecting batch size, and dense allows for classification of the image based on the previous convolutional layers.

### Image Preprocessing
In this section we will be covering simple preprocessing tools that will be necessary for images that don't come preprocessed and normalized. 

A tool we may be using is `tf.image` from TensorFlow. So we would normally set a variable to have the name of the data directory and make adjustments as necessary. Some common tools are the following:
* Resize -> tf.image.resize(image, [height, width])
* Flip Horizontally -> tf.image.flip_left_right(image)
* Flip Vertically -> tf.image.flip_up_down(image)
There is much more but we will only be covering those relevant to this project. 

As of now all current data is preprocessed and normalized therefore only a rough outline will be made in preparation of future changes. The outline will be uploaded as `preprocess_outline.ipynb`. When the project encounters unprocessed data we will be adding to the documentation to explain the functions used.

Another thing to keep in mind is that there are many variations of implementation that may not need the use of `tf.image` due to several options and workarounds since TensorFlow is a large library which contains various Keras tools.

## Possibly Necessary Tools 
Depending on the goals of each individual trying to test this project or edit it on their own may want to consider options in the callback section of the TensorFlow library such as BackupAndRestore and CSVLogger to quickly switch between model versions and also track epoch results into a CSV file. 

For CSVLogger the syntax for creating a CSVLogger callback is the following:
```Python
tf.keras.callbacks.CSVLogger(filename, separator=",", append=False)
```
- filename: Filename of the CSV file.
- separator: String used to separate elements in the CSV file. The default is set to ",".
- append: Boolean. If true, the logger will append to the file if it already exists (useful for continuing training). If false, the existing file will be overwritten.

