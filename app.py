import streamlit as st
import joblib
import numpy as np

model = joblib.load("wind_turbine_model.pkl")

# Sidebar Navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "About Project", "Prediction"]
)

# Home Page
if page == "Home":

    st.title("Wind Turbine Predictive Maintenance Dashboard")

    st.write("""
    Welcome to the Wind Turbine Predictive Maintenance Dashboard.

    Features:
    - Predict power output
    - Analyze turbine performance
    - Identify potential maintenance issues
    - Visualize operational data
    """)

# About Project Page
if page == "About Project":

    st.title("About Project")

    st.write("""
    This project predicts wind turbine power output
    using Machine Learning.

    Inputs:
    • Wind Speed
    • Theoretical Power Curve
    • Wind Direction

    Output:
    • Predicted Active Power (kW)

    Goal:
    Help monitor turbine performance and support
    predictive maintenance.
    """)

# Prediction Page
if page == "Prediction":

    st.title("Wind Turbine Power Prediction")

    wind_speed = st.number_input(
        "Wind Speed (m/s)",
        value=10.0
    )

    theoretical_power = st.number_input(
        "Theoretical Power Curve (KWh)",
        value=1000.0
    )

    wind_direction = st.number_input(
        "Wind Direction (°)",
        value=180.0
    )

    if st.button("Predict"):

        data = np.array([
            [wind_speed,
             theoretical_power,
             wind_direction]
        ])

        prediction = model.predict(data)

        st.success(
            f"Predicted Active Power: {prediction[0]:.2f} kW"
        )
