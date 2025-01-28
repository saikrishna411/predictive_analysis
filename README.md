# Predictive Analysis for Manufacturing Operations

This project is aimed at developing a RESTful API to predict machine downtime or production defects using manufacturing data. The API allows users to upload a dataset, train a machine learning model, and predict outcomes like downtime flags based on input data.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Endpoints](#endpoints)
  - [POST /upload](#post-upload)
  - [POST /train](#post-train)
  - [POST /predict](#post-predict)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Testing with Postman](#testing-with-postman)


---

## Overview

This project uses a **supervised machine learning model** to predict machine downtime or production defects in manufacturing operations. It includes the following main features:
- **Upload**: Allows uploading of a CSV file for the dataset.
- **Train**: Trains a machine learning model based on the dataset.
- **Predict**: Accepts JSON input and returns predictions like downtime flags along with confidence scores.

---

## Technologies Used

- **Python**: The core language for building the API and machine learning model.
- **Flask**: A micro web framework for building the RESTful API.
- **scikit-learn**: For machine learning model implementation (e.g., Logistic Regression, Decision Tree).
- **Postman/cURL**: For testing the API endpoints.
- **pandas**: For data manipulation and processing.
- **numpy**: For numerical operations.

---

## Endpoints
### POST/upload

#### Description:
Uploads a CSV file containing the manufacturing dataset.

#### Request:
- **Form-data**: `file` (CSV file)

#### Example:
```bash
POST http://127.0.0.1:5000/upload
```

### POST/train

#### Description:
Trains a machine learning model (Logistic Regression or Decision Tree) using the uploaded dataset. Returns performance metrics

#### Request:
- No data required in the body. The model will be trained using the uploaded dataset (sample_data.csv).

#### Example:
```bash
POST http://127.0.0.1:5000/train
```
### POST/predict

#### Description:
Makes predictions on input data (JSON format) using the trained model. Returns predictions with confidence scores.

#### Request:
- **JSON**: 
`{
  "feature_1": value,
  "feature_2": value,
}`

#### Example:
```bash
POST http://127.0.0.1:5000/predict
```
## Setup and Installation
### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/predictive-analysis-api.git
cd predictive-analysis-api
```

### 2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Ensure the data folder exists, or it will be created upon the first file upload.
---
## Usage
### 1.Start the API server:

```bash
python app.py
```

### 2.Access the API:

The API will be available at ```http://127.0.0.1:5000/.```
Use Postman or any HTTP client to test the endpoints

---

## Testing with Postman
#### To test the API, follow these steps:

## 1.Upload CSV File:

- Set the method to POST.
- Use the URL```http://127.0.0.1:5000/upload.```
- Under the Body tab, choose form-data.
- Add a key file and upload your CSV file.

## 2.Train Model:

- Set the method to POST.
- Use the URL ```http://127.0.0.1:5000/train.```
- The model will be trained on the uploaded dataset.
## 3.Make Predictions:

- Set the method to POST.
- Use the URL ```http://127.0.0.1:5000/predict.```
- Under the Body tab, choose raw and JSON.
- Add input features as a JSON object (e.g., {"feature_1": 5.2, "feature_2": 3.1}).





