import streamlit as st
import joblib
import numpy as np

# Load Model
model = joblib.load("wind_turbine_model.pkl")

# Sidebar Navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "About Project",
        "Model Information",
        "Prediction"
    ]
)

# =========================
# HOME PAGE
# =========================
if page == "Home":

    st.title("Wind Turbine Predictive Maintenance Dashboard")

    st.write("""
    Welcome to the Wind Turbine Predictive Maintenance Dashboard.

    This system predicts wind turbine power output
    and provides maintenance recommendations based
    on turbine operating conditions.
    """)

    st.subheader("Features")

    st.write("""
    ✅ Power Prediction

    ✅ Turbine Health Monitoring

    ✅ Maintenance Alerts

    ✅ Predictive Analytics

    ✅ Machine Learning Based Decision Support
    """)

# =========================
# ABOUT PROJECT PAGE
# =========================
if page == "About Project":

    st.title("About Project")

    st.write("""
    This project uses Machine Learning to predict
    wind turbine power generation.

    Input Parameters:
    • Wind Speed (m/s)
    • Theoretical Power Curve (KWh)
    • Wind Direction (°)

    Output:
    • Predicted Active Power (kW)

    Objective:
    To assist operators in monitoring turbine
    performance and identifying maintenance needs.
    """)

# =========================
# MODEL INFORMATION PAGE
# =========================
if page == "Model Information":

    st.title("Model Information")

    st.write("Machine Learning Algorithm Used:")

    st.success("K-Nearest Neighbors (KNN) Regression")

    st.subheader("Evaluation Metrics")

    st.write("""
    MSE (Mean Squared Error)

    RMSE (Root Mean Squared Error)

    R² Score (Coefficient of Determination)
    """)

    st.info("""
    These metrics are commonly used to evaluate
    machine learning regression models.
    """)

# =========================
# PREDICTION PAGE
# =========================
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

        st.subheader("Turbine Health Status")

        if prediction[0] >= theoretical_power * 0.8:

            st.success(
                "🟢 Healthy Turbine"
            )

            st.write(
                "Performance is close to expected output."
            )

        elif prediction[0] >= theoretical_power * 0.5:

            st.warning(
                "🟡 Needs Inspection"
            )

            st.write(
                "Performance is below expected levels."
            )

        else:

            st.error(
                "🔴 Maintenance Required"
            )

            st.write(
                "Significant power loss detected."
            )

        st.subheader("Maintenance Recommendation")

        if prediction[0] < theoretical_power * 0.5:

            st.write("""
            Possible causes:

            • Blade degradation

            • Gearbox wear

            • Generator inefficiency

            • Sensor malfunction

            • Electrical faults
            """)

        else:

            st.write("""
            No immediate maintenance action required.
            Continue routine monitoring.
            """)
