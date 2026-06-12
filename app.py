import streamlit as st
import joblib
import numpy as np

model = joblib.load("wind_turbine_model.pkl")

st.title("Wind Turbine Power Prediction")

wind_speed = st.number_input("Wind Speed (m/s)", value=10.0)
theoretical_power = st.number_input("Theoretical Power Curve (KWh)", value=1000.0)
wind_direction = st.number_input("Wind Direction (°)", value=180.0)

if st.button("Predict"):

    data = np.array([
        [wind_speed, theoretical_power, wind_direction]
    ])

    prediction = model.predict(data)

    st.success(
        f"Predicted Active Power: {prediction[0]:.2f} kW"
    )
