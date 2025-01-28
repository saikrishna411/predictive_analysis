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
- [License](#license)

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

### POST /upload

#### Description:
Uploads a CSV file containing the manufacturing dataset.

#### Request:
- **Form-data**: `file` (CSV file)

#### Example:
```bash
POST http://127.0.0.1:5000/upload




