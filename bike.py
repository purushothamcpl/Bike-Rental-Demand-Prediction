import streamlit as st
import joblib
import pandas as pd

model = joblib.load("bike_rental_xgb.pkl")

st.title(" Bike Rental Demand Prediction")
st.write("Predict hourly bike rental demand using time and weather features")

yr = st.selectbox("Year (0 = 2011, 1 = 2012, 2 = 2013)",[0, 1, 2])
hr = st.slider("Hour (0–23)", 0, 23, 12)
weekday = st.selectbox("Weekday (0 = Sunday, 6 = Saturday)",[0, 1, 2, 3, 4, 5, 6])
workingday = st.selectbox("Working Day (0 = No Work, 1 = Working",[0, 1])
holiday = st.selectbox("Holiday (0 = No Holiday, 1 = Holiday",[0, 1])
mnth = st.selectbox("Month",list(range(1, 13)))
temp = st.slider("Temperature (normalized)",0.0, 1.0, 0.5)
hum = st.slider("Humidity (normalized)",0.0, 1.0, 0.5)
windspeed = st.slider("Wind Speed (normalized)",0.0, 1.0, 0.3)
weathersit = st.selectbox("Weather Situation (1 = Clear, 4 = Heavy Rain)",[1, 2, 3, 4])


input_data = pd.DataFrame({
    'yr':[yr],
    'hr': [hr],
    'weekday': [weekday],
    'workingday': [workingday],
    'holiday': [holiday],
    'mnth': [mnth],
    'temp': [temp],
    'hum': [hum],
    'windspeed': [windspeed],
    'weathersit': [weathersit]
})

if st.button("Predict Bike Rentals"):
    prediction = model.predict(input_data)
    st.success(f" Estimated Bike Rentals: {int(prediction[0])}")