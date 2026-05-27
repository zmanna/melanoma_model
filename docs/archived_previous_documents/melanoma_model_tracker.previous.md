# Melanoma Model Tracker

## Overview
This document provides a brief explanation of how the model will be tracked in terms of data and iteration as well as it will document the team's thought process and changes as the model changes over time.

Tracking model progress is important to show transparency with users and clients across all domains. AI and machine learning models are all tools and therefore must be properly refined to always be a useful tool and to be as accurate as possible. 

## Initial Design Thoughts
The initial idea the team had developed is a python script that properly and accurately tracks changes in the model. This means all important adjustments of the model to keep track of along with a model iteration ID that is unique to a tweaked version of it. 

Using the CSV file reading and writing library the model will be able to be tracked so that the number of convolutional layers, batch size, etc. can all be viewed over each iteration.. 

Using the `model.fit()` function creates a customizable set of data that we can track and feed to the CSV editing script.

We do have alternate options that are built into Tensorflow such as CSVLogger that must be investigated to make sure that these built in tools don't carry too much bloat or that they are able to track and write important information into a CSV file. 

## Model Architecture Summary

The structure the team had opted for was a convolutional neural network (CNN). This is because there has been a lot of empirical studies on how accurate this model structure is. It has been tested in various image processing model experiment such as MNIST database of handwritten digits, being one of the first applications where it succeeded, which shows nearly one-hundred percent accuracy.

The following sections briefly cover the model's structure:

**Convolutional Layers**: These layers simply act as filters for images. They are the layers that distinguish and extract increasingly complex features in the images to pass on to the next layer. 

**Pooling Layer**: This layer is what received the features that were provided by the previous layer. This layer is best known for reducing spatial size of received features and preserving the most important information in them as it helps reduce computation and helps prevent overfitting.

**Dense Layer**: Dense layers are known to interpret the image features in their entirety to finalize the decision between malignant or benign. 

**Activations (ReLU, Sigmoid)**: ReLU activations are used everywhere in the model except the final output layer. The output layer uses a sigmoid function, which outputs a value between 0 and 1.

**Regularization (Dropout, BatchNormalize)**: Dropout prevents overfitting through the random deactivation of neurons which fores the network to learn more robust/generalized features, and BatchNormalization maintains it stability and while speeding up training.

Through these layers the team had to do experimental testing and make adjustments where necessary in order to balance the complexity and accuracy of the model. Ensuring that the model's architecture follows organized and standard design.

## Data Preprocessing Steps

Data preprocessing are steps taken to make sure any image is ready to go through the model as the model cannot just take any image and read it the same. 

**Image Loading**: Images are loaded in (depends on user folder location) using the `image_dataset_from_directory` function provided by TensorFlow. Images are automatically labeled based on folder names (`benign/`, `malignant/`) and they are resized to 256x256 as those are the model's input size requirements.

**Normalization**: The images are then scaled down from `[0, 255]` to `[0, 1]` through simple division. Allows for a more stable model with faster training. It provides a better working condition for backpropagation.

**Data Splitting**: This is where the team splits up the sets of data. In this case we split it into three sets:
- Training Set (70%): Used to teach the model. Think of it as its practice.
- Validation Set (20%): Used during training to check how well the model is generalizing. Think of this as the solution sheet to track its progress.
- Test Set (10%): Used at the end to check final performance. This was set to shuffle so the model doesn't memorize order of data. Think of it as its exam its been preparing for.

**Batch Preparation**: All data is loaded in batches as it allows the model to work efficiently. Optimizing the memory use and training speed. This way the model can process multiple images at once on the GPU. Otherwise it would take a lot longer if done on the CPU.

**Label Mode**: The team set `label_mode` to "binary" since the project focuses on specifically malignant or benign classification.

## Model Versioning System
Version numbers are assigned linearly and simply (e.g., 1, 2, 3, ...). This is because the project is small and led by a small team so we don't expect any major additions and continuous version changes yet. 

They are incremented based on major changes in important parameters or when we are at the end of a sprint that focused on model changes. 

Model progress is logged onto a .csv file on our GitHub `model` folder named `progress_log.csv`.


## Logging Metrics
The final design choice was to create a function that takes extracts information from the `history` and `conf_matrix` to track the following:

- True Negative: Tracks when the model predicts benign cancer in the image, and its correct (image is benign).


- False Negative: tracks when the model predicts benign cancer in the image, and its incorrect (image is malignant).


- True Positive: Tracks when the model predicts malignant cancer in the image, and its correct (image is malignant).


- False Positive: Tracks when the model predicts malignant cancer in the image, and its incorrect (image is benign). 


- Total: Adds up all values for true positives, false positives, true negatives, and false negatives. This simplifies calculations for other metrics.


- Accuracy: Used to measure how often the model's predictions are correct. This is not the end-all-be-all of accuracy. There are still many things that can influence this variable. True accuracy depends on the domain, scope, and details the problem.

- Precision: This focuses on the quality of the model's positive predictions. In this context we would explain it as "out of all the images the model flagged as malignant how many were actually malignant?"


- Recall: Recall is used to measure how often the model identifies positive cases. Specifically, the proportion of true positives out of all actual positive cases. For our context we would describe it as "out of all the actual malignant cases, how many did the model correctly flag as malignant?"


- F1 Score: A metric used to combine precision and recall. This is used to find a more accurate sense of model performance. This is because the false positives and false negatives are crucial since they can have more severe consequences. 

In the next section we will describe why the F1 score matters more in the context of this project.

## Why F1 Score Matters in Medical Diagnosis
In the previous section we briefly discussed the logging metrics and their meanings. F1 score was specifically described to be important due to false positives and false negatives being crucial.

### False Positives
Let's say that a user decides to try our model. They upload their image and test it and get a false positive. Meaning that the image is benign but was predicted to be malignant. 

This may cause unnecessary fear, resource use, and expenses. It cannot necessarily be avoided as machine learning tools are never perfect but for a small project the team cannot allow for this to cause trouble. Hence, why the team plans to make it very clear to the user that this is just a tool and any real concern should result in a consultation with a real medical professional.

### False Negatives 
Now let's say that a user decides to try our mode. They upload their image and test it and get a false negative. Meaning that the image is malignant but was predicted to be benign.

This is detrimental because if someone has genuine concern and the tool tells them they are fine then the user will take this as fact and may not catch the cancer early enough. Therefore, it can have life-altering implications. The team needs to make sure that its clear to the user that the project is not real medical advice and that they should always seek medical professionals for more guidance. 

## Thresholding and Model Decision Making
The model has specific threshold decisions that have been tested. There are some things to take note of first. Such as:
- no machine learning model is 100% accurate/correct 
- no machine learning model will be able to replace medical advice from a professional 
- machine learning models are not made to replace medical workers nor will they in the near future
- machine learning models are tools

The team uses thresholding values to assist in mass errors such as the ones described above. For example we adjust the threshold for predicting benign or malignant and as of typing this it is currently set at `0.7`. This ensures that we can assume malignant more accurately than possibly misclassifying it as benign. As of typing this a test was run where the model only missed about 6-8% of malignant images. This is not perfect and is not meant to be and nor does it mean that it is usable in real-world applications yet as the environment in which its tested is very controlled and calculated.

I repeat, this model is not meant to definitively provide medical advice. Seek a medical professional if you have any concerns.

## Current Limitations
There are many limitations to machine learning models right now. We will cover how some of those limitations have impacted our development in the machine learning model below.

**Dataset Size and Diversity Limitation**: 
Data size isn't exactly a problem we encountered since the dataset we found was very hefty. The quality was also not much of an issue since it was from a reputable source with consistent quality. 

The problem specifically lies with the diversity. Although the images are reputable and have a consistent quality along with it being preprocessed this doesn't account for images of varying quality, size, skin color, skin lesion, and more. This means that unless the image inputted into the model isn't set up the same way as the dataset it was trained on then the results won't be the same or nearly as accurate. Especially if the image going through it isn't even cancer.

**Risks of overfitting**:
During training the team has to be very cautious of overfitting as it decreases the model's ability to generalize. It causes the model to become too sensitive to changes and therefore can perform poorly on data it hasn't seen. This was common for us when we ran too many epochs but otherwise we were careful to make changes to keep it relatively under control.

**Lack of external validation**:
Due to the domain of the problem this project seeks to solve we cannot easily depend on controlled data. External validation would be required for stronger claims on this model's performance.

**Assumptions/Biases Built into the Model**:
This model assumes that all images are properly labeled and that the image is skin cancer. This model may also have unknown biases depending on the dataset. This means it may have biases towards certain demographics, images, image type, or scanning equipment.

## Planned Improvement and Future Work 
The team isn't quite sure how much further we may pursue this project as it requires a great understanding of the domain in which the problem resides and must be carefully thought out. Just one meeting with a medical professional opened our eyes to the extent of issues we had not yet considered for this model. Therefore it would need a lot more careful planning, testing, and warnings with using the model.

## Security and Privacy Considerations
### Project Scope and Disclaimer
This project was academic and experimental. It was intended to be a technical demonstration of how machine learning models can be applied to skin cancer classification tasks. The user is allowed to upload images and test its functionality but the project was not built for production use or real-world deployment. 

USERS UPLOAD IMAGES AT THEIR OWN RISK 

### Lack of Security and Privacy Protections
There are no security mechanisms in place such as encryption, authentication, or secure image storage. This means no images are guaranteed secure. Users should be aware that uploading any sensitive or identifying information/images could expose them.

### Use at Your Own Risk 
We do this as a standard to make sure the user understands that these experimental tools are not meant to be used seriously. For your safety and ours.

- By uploading an image, users acknowledge that the system does not meet clinical, legal, or security standards.
- The team accepts no liability for any consequences arising from use of the tool, including but not limited to data breaches, misdiagnoses, or user reliance on the output.

### Not a Medical Device
Again we do this to ensure that both parties are safe and that there are no misunderstandings.

- The project is not FDA-approved, HIPAA-compliant, or a certified medical device.
- Users are strongly advised to consult qualified medical professionals for any concerns regarding skin cancer or related health issues.

