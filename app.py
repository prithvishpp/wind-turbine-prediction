import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
        "Prediction",
        "Admin Dashboard"
    ]
)

# =========================
# HOME PAGE
# =========================
if page == "Home":

    st.title("Wind Turbine Predictive Maintenance Dashboard")

    st.image(
        "wind_turbine.jpg",
        caption="Wind Turbine Predictive Maintenance System",
        use_container_width=True
    )

    st.markdown("""
    ### Welcome

    This dashboard uses Machine Learning to:

    - Predict wind turbine power output
    - Monitor turbine health
    - Detect maintenance requirements
    - Support predictive maintenance decisions
    - Improve turbine efficiency and reliability
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
# ADMIN DASHBOARD
# =========================
if page == "Admin Dashboard":

    st.title("🔐 Admin Dashboard")

    password = st.text_input(
        "Enter Admin Password",
        type="password"
    )

    if password == "admin123":

        st.success("Admin Access Granted")

        st.subheader("System Status")
        st.success("🟢 System Online")

        st.subheader("Model Details")

        st.write("Model Used: KNN Regression")
        st.write("Deployment: Streamlit Cloud")
        st.write("Prediction Service: Active")

        st.subheader("Dataset Summary")

        st.metric("Records", "50,530")
        st.metric("Features", "3")
        st.metric("Target", "LV ActivePower (kW)")

        st.subheader("Maintenance Analytics")

        st.info("""
        Common Failure Causes:

        • Blade Damage

        • Gearbox Wear

        • Generator Inefficiency

        • Sensor Faults

        • Electrical Problems
        """)

        st.subheader("Model Performance")

        st.metric("R² Score", "0.91")
        st.metric("RMSE", "410")
        st.metric("MSE", "168100")

        st.subheader("Administrator Actions")

        st.button("Generate Maintenance Report")
        st.button("Refresh Dashboard")

    elif password != "":

        st.error("Invalid Password")

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

        # =========================
        # POWER COMPARISON CHART
        # =========================

        st.subheader("Power Comparison")

        chart_data = pd.DataFrame({
            "Power Type": [
                "Theoretical",
                "Predicted"
            ],
            "Power (kW)": [
                theoretical_power,
                prediction[0]
            ]
        })

        fig, ax = plt.subplots()

        ax.bar(
            chart_data["Power Type"],
            chart_data["Power (kW)"]
        )

        ax.set_ylabel("Power (kW)")
        ax.set_title(
            "Theoretical vs Predicted Power"
        )

        st.pyplot(fig)

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
