# Task-7-Advanced-MultiPage-Streamlit-MNIST
Advanced multi-page Streamlit application for MNIST handwritten digit classification using a CNN, with prediction, model performance, data visualization, and project reporting.    python · streamlit · mnist · deep-learning · cnn · tensorflow · keras · machine-learning · image-classification · data-visualization · artificial-intelligence · Msc-ai
# Task 7 – Advanced Multi-Page Streamlit Application

## MNIST Handwritten Digit Classification using Deep Learning

This project implements an advanced multi-page Streamlit web application for handwritten digit classification using the MNIST dataset and a trained Convolutional Neural Network (CNN).

The application converts a trained deep-learning model into an interactive web interface where users can explore the project, perform digit prediction, inspect model performance, visualize the MNIST dataset, explore digit classes, and view the complete project report.

---

## Student Information

| Field | Details |
|---|---|
| Student Name | Saikumar Padala |
| Roll No. | 15 |
| PRN / Student ID | 5711387 |
| Programme | MSc Artificial Intelligence – Part II |
| Assignment | Task 7 |
| Dataset | MNIST Handwritten Digit Dataset |
| Model | Convolutional Neural Network (CNN) |
| Framework | Streamlit |
| Deep Learning Framework | TensorFlow / Keras |

---

## Project Overview

The objective of this project is to develop a professional multi-page Streamlit application that integrates a trained CNN model for MNIST handwritten digit classification.

Instead of providing only a basic prediction interface, the application is organized into multiple sections:

- Dashboard / Home
- Digit Prediction
- Model Performance
- Data Visualization
- Project Report

This structure demonstrates the integration of deep learning inference, data visualization, model evaluation, and web application development.

---

## Features

### 1. Dashboard / Home

The dashboard provides an overview of the complete project.

It presents:

- MNIST dataset information
- Number of classes
- Image dimensions
- Model status
- CNN architecture summary
- Application workflow
- Navigation to different application sections

---

### 2. Digit Prediction

The Digit Prediction page allows users to upload handwritten digit images.

Supported image formats include:

- PNG
- JPG
- JPEG

The uploaded image is processed before being passed to the trained CNN model.

The application displays:

- Uploaded image
- Predicted digit
- Prediction confidence
- Probability information

---

### 3. Model Performance

The Model Performance page displays the evaluation results of the trained CNN.

Observed project results:

| Metric | Result |
|---|---:|
| Test Accuracy | 98.97% |
| Test Loss | 0.0288 |
| Test Samples | 10,000 |

The page also displays the CNN architecture and layer information.

---

### 4. Data Visualization

The Data Visualization page provides an interactive overview of the MNIST dataset.

It includes:

- Training dataset count
- Testing dataset count
- Image dimensions
- Number of classes
- Digit class distribution
- Interactive digit-class exploration
- Representative handwritten samples

---

### 5. Project Report

The application contains an integrated Project Report page.

The report presents:

- Project objective
- Dataset description
- Methodology
- Model architecture
- Technologies used
- Results
- Observations
- Conclusion

This makes the Streamlit application self-documenting.

---

## Dataset

The project uses the MNIST handwritten digit dataset.

| Attribute | Details |
|---|---|
| Dataset | MNIST |
| Training Images | 60,000 |
| Testing Images | 10,000 |
| Image Size | 28 × 28 pixels |
| Image Type | Grayscale |
| Number of Classes | 10 |
| Classes | 0–9 |
| Task | Image Classification |

Each image represents one handwritten digit from 0 to 9.

---

## CNN Architecture

The trained CNN consists of convolutional, pooling, flattening, and dense layers.

| Layer | Type | Output Shape | Parameters |
|---|---|---|---:|
| conv2d | Conv2D | (None, 26, 26, 32) | 320 |
| max_pooling2d | MaxPooling2D | (None, 13, 13, 32) | 0 |
| conv2d_1 | Conv2D | (None, 11, 11, 64) | 18,496 |
| max_pooling2d_1 | MaxPooling2D | (None, 5, 5, 64) | 0 |
| flatten | Flatten | (None, 1600) | 0 |
| dense | Dense | (None, 64) | 102,464 |
| dense_1 | Dense | (None, 10) | 650 |

The final output layer contains 10 units corresponding to the ten MNIST digit classes.

---

## Prediction Workflow

The application follows this workflow:

```text
User uploads image
        ↓
Image preprocessing
        ↓
Grayscale conversion
        ↓
Resize to 28 × 28
        ↓
Normalization
        ↓
CNN inference
        ↓
Class probabilities
        ↓
Predicted digit
        ↓
Confidence / visualization
Technologies Used
Python

Python is used as the primary programming language for application development, image processing, and model inference.

Streamlit

Streamlit is used to build the interactive multi-page web application.

TensorFlow / Keras

TensorFlow and Keras are used for the trained CNN model and prediction process.

NumPy

NumPy is used for numerical operations and image-array processing.

Pillow

Pillow is used for image loading, grayscale conversion, and resizing.

MNIST

MNIST provides the handwritten digit images used for classification.
