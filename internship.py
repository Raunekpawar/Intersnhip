# -*- coding: utf-8 -*-


**Import Library**
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

"""**Import Data**"""

from sklearn.datasets import load_digits

df = load_digits()

import matplotlib.pyplot as plt

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, df['images'], df['target']):
    ax.set_axis_off()
    ax.imshow(image, cmap='gray', interpolation='nearest')
    ax.set_title("Training: %d" % label)

plt.show()

"""**Describe Data**

Data for Hand Written Digit Prediction typically consists of a labeled dataset containing handwritten digits and their corresponding numerical labels. The key components of this dataset include:

1. Images of Handwritten Digits: The dataset contains a collection of grayscale or color images, where each image represents a handwritten digit (0-9). These images are usually of a standardized size and format, such as 28x28 pixels for the popular MNIST dataset.

2. Labels: Each image in the dataset is associated with a numerical label that indicates the digit it represents. These labels serve as the ground truth for training and evaluating the predictive model.

3. Training and Testing Sets: The dataset is typically divided into two subsets: a training set and a testing set. The training set is used to train the machine learning model, while the testing set is used to evaluate the model's accuracy and generalization.

4. Variability: To ensure the model's robustness, the dataset may include variations in handwriting styles, sizes, and orientations. This helps the model learn to recognize digits under different conditions.

5. Noise and Distortions: Real-world handwritten data often contains noise, smudges, or slight distortions. Including such variations in the dataset helps the model become more resilient to imperfect input.

6. Size and Diversity: A larger and more diverse dataset improves the model's ability to generalize and recognize digits from various sources and handwriting styles.

7. Data Augmentation: Data augmentation techniques, such as rotation, scaling, and adding noise, can be applied to increase the dataset's size and enhance the model's robustness.

Overall, a well-constructed dataset for Handwritten Digit Prediction plays a crucial role in training and evaluating machine learning models. High-quality data helps ensure that the model can accurately recognize and classify handwritten digits in real-world scenarios.

**Data Preprocessing**
"""

df.images.shape

df.images[0]

df.images[0].shape

len(df.images)

n_samples = len(df.images)
data = df.images.reshape((n_samples, -1))

data[0]

data[0].shape

data.shape

"""**Train Test Split**"""

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data, df.target, test_size=0.3)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

"""**Explaination**


**Project Title:** Handwritten Digit Recognition

**Project Objective:** The objective of this project is to develop a machine learning model capable of accurately recognizing handwritten digits. Handwritten digit recognition has various real-world applications, such as automated data entry, postal code recognition, and digit-based CAPTCHA solving. This project aims to leverage a Random Forest classifier, a powerful machine learning algorithm, to achieve this goal.

**Project Description:**

In this project, we are building a system to recognize handwritten digits, which is essential for a wide range of applications in the field of image processing and character recognition.

**Data:** We have a dataset containing handwritten digits, which are represented as arrays of pixel values. Each digit is a 8x8 grid of grayscale pixels. For example, a digit "5" might be represented as follows:

```
[ 0.,  0.,  5., 13.,  9.,  1.,  0.,  0.,
  0.,  0., 13., 15., 10., 15.,  5.,  0.,
  0.,  3., 15.,  2.,  0., 11.,  8.,  0.,
  0.,  4., 12.,  0.,  0.,  8.,  8.,  0.,
  0.,  5.,  8.,  0.,  0.,  9.,  8.,  0.,
  0.,  4., 11.,  0.,  1., 12.,  7.,  0.,
  0.,  2., 14.,  5., 10., 12.,  0.,  0.,
  0.,  0.,  6., 13., 10.,  0.,  0.,  0.]
```


**Visualization:** Throughout the project, we can use various data visualizations to understand the model's behavior better. These visualizations may include confusion matrices, accuracy and loss curves, and sample digit recognition results.

The ultimate goal of this project is to create an accurate and reliable handwritten digit recognition system that can be used in various applications where automatic digit recognition is required.
"""
