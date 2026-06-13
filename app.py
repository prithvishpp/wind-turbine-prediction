import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and dataset
model = joblib.load("wind_turbine_model.pkl")
df = pd.read_csv("dataset.csv")

# Sidebar Navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Analytics", "Prediction"]
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

# Analytics Page
if page == "Analytics":

    st.title("Wind Turbine Analytics")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10))

    st.subheader("Dataset Shape")
    st.write(
        f"Rows: {df.shape[0]} | Columns: {df.shape[1]}"
    )

    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

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
            [
                wind_speed,
                theoretical_power,
                wind_direction
            ]
        ])

        prediction = model.predict(data)

        st.success(
            f"Predicted Active Power: {prediction[0]:.2f} kW"
        )
