import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("wind_turbine_model.pkl")

# Page title
st.title("Wind Turbine Power Prediction")

st.write("Enter turbine operating conditions to predict power output.")

# User inputs
wind_speed = st.number_input(
    "Wind Speed (m/s)",
    min_value=0.0,
    value=10.0
)

theoretical_power = st.number_input(
    "Theoretical Power Curve (KWh)",
    min_value=0.0,
    value=1000.0
)

wind_direction = st.number_input(
    "Wind Direction (°)",
    min_value=0.0,
    max_value=360.0,
    value=180.0
)

# Prediction button
if st.button("Predict Power Output"):

    input_data = np.array([
        [wind_speed,
         theoretical_power,
         wind_direction]
    ])

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Active Power: {prediction[0]:.2f} kW"
    )
