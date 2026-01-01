# Bike Rental Demand Prediction

This project focuses on predicting hourly bike rental demand using machine learning techniques based on time, calendar, and weather-related features. The goal is to build an accurate prediction model and deploy it as an interactive web application.

## Problem Statement
Accurately forecasting bike rental demand is essential for efficient resource allocation and operational planning. This project aims to predict the total number of bikes rented per hour based on historical usage patterns and environmental conditions.

## Approach
1. Data Cleaning and Preprocessing  
2. Feature Selection and Feature Engineering  
3. Exploratory Data Analysis (EDA)  
4. Model Training and Hyperparameter Tuning  
5. Model Evaluation  
6. Deployment using Streamlit  

## Features Used
- Year (`yr`)
- Month (`mnth`)
- Hour (`hr`)
- Weekday (`weekday`)
- Working Day (`workingday`)
- Holiday (`holiday`)
- Temperature (`temp`)
- Humidity (`hum`)
- Wind Speed (`windspeed`)
- Weather Situation (`weathersit`)

> Note: `casual` and `registered` columns were excluded to prevent data leakage, as they directly contribute to the target variable.

## Models Implemented
- Linear Regression (Baseline)
- Random Forest Regressor (with GridSearchCV)
- XGBoost Regressor
- LSTM (Time-Series Forecasting)

## Model Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## Deployment
The best-performing model was deployed using **Streamlit**, allowing users to input time and weather details and receive real-time bike rental demand predictions.

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- TensorFlow / Keras
- Streamlit
- Joblib

## How to Run the App Locally

```bash
pip install -r requirements.txt
streamlit run app.py
