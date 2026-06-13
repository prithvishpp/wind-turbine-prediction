```python
import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load Model
model = joblib.load("wind_turbine_model.pkl")

# Session State for History
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "About Project",
        "Model Information",
        "Prediction",
        "Analytics Dashboard",
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

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Turbines", "125")

    with col2:
        st.metric("Healthy", "110")

    with col3:
        st.metric("Maintenance", "15")

    st.subheader("Features")

    st.write("""
    ✅ Power Prediction

    ✅ Turbine Health Monitoring

    ✅ Maintenance Alerts

    ✅ Predictive Analytics

    ✅ Machine Learning Based Decision Support
    """)

# =========================
# ABOUT PROJECT
# =========================
elif page == "About Project":

    st.title("About Project")

    st.write("""
    This project uses Machine Learning to predict
    wind turbine power generation and support
    predictive maintenance.

    Input Parameters:
    • Wind Speed (m/s)

    • Theoretical Power Curve (KWh)

    • Wind Direction (°)

    Output:
    • Predicted Active Power (kW)

    Goal:
    Improve reliability and reduce maintenance costs.
    """)

# =========================
# MODEL INFORMATION
# =========================
elif page == "Model Information":

    st.title("Model Information")

    st.success("Algorithm: K-Nearest Neighbors (KNN) Regression")

    st.subheader("Evaluation Metrics")

    st.write("""
    • Mean Squared Error (MSE)

    • Root Mean Squared Error (RMSE)

    • R² Score
    """)

# =========================
# ANALYTICS DASHBOARD
# =========================
elif page == "Analytics Dashboard":

    st.title("📊 Maintenance Analytics Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average Power", "1850 kW")

    with col2:
        st.metric("Failure Rate", "6%")

    with col3:
        st.metric("Efficiency", "92%")

    analytics_data = pd.DataFrame({
        "Category": [
            "Healthy",
            "Inspection",
            "Maintenance"
        ],
        "Count": [
            70,
            20,
            10
        ]
    })

    st.subheader("Failure Statistics")
    st.bar_chart(
        analytics_data.set_index("Category")
    )

    st.info("""
    Common Failure Causes:

    • Blade Damage

    • Gearbox Wear

    • Generator Inefficiency

    • Sensor Faults

    • Electrical Problems
    """)

# =========================
# ADMIN DASHBOARD
# =========================
elif page == "Admin Dashboard":

    st.title("🔐 Admin Dashboard")

    password = st.text_input(
        "Enter Admin Password",
        type="password"
    )

    if password == "admin123":

        st.success("Admin Access Granted")

        st.metric("Records", "50,530")
        st.metric("Features", "3")
        st.metric("Target", "LV ActivePower")

        st.metric("R² Score", "0.91")
        st.metric("RMSE", "410")
        st.metric("MSE", "168100")

        st.button("Generate Maintenance Report")
        st.button("Refresh Dashboard")

    elif password != "":
        st.error("Invalid Password")

# =========================
# PREDICTION PAGE
# =========================
elif page == "Prediction":

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

        # Chart
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

        # Health Score
        health_score = min(
            (prediction[0] / max(theoretical_power, 1)) * 100,
            100
        )

        st.subheader("Turbine Health Score")

        st.progress(int(health_score))

        st.write(
            f"Health Score: {health_score:.1f}%"
        )

        # Risk
        st.subheader("Failure Risk Assessment")

        if prediction[0] >= theoretical_power * 0.8:
            st.success("🟢 Low Risk")
            cost = 0

        elif prediction[0] >= theoretical_power * 0.5:
            st.warning("🟡 Medium Risk")
            cost = 5000

        else:
            st.error("🔴 High Risk")
            cost = 25000

        # Cost
        st.subheader("Estimated Maintenance Cost")

        st.metric(
            "Estimated Cost (₹)",
            f"{cost:,}"
        )

        # History
        st.session_state.history.append(
            round(float(prediction[0]), 2)
        )

        st.subheader("Prediction History")

        st.write(
            st.session_state.history
        )

        # Turbine Health
        st.subheader("Turbine Health Status")

        if prediction[0] >= theoretical_power * 0.8:

            st.success("🟢 Healthy Turbine")

        elif prediction[0] >= theoretical_power * 0.5:

            st.warning("🟡 Needs Inspection")

        else:

            st.error("🔴 Maintenance Required")

        # Maintenance Recommendation
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

        # Download Report
        report = f'''
WIND TURBINE MAINTENANCE REPORT

Predicted Power: {prediction[0]:.2f} kW
Wind Speed: {wind_speed}
Theoretical Power: {theoretical_power}
Wind Direction: {wind_direction}
Health Score: {health_score:.1f}%
Estimated Cost: ₹{cost:,}
'''

        st.download_button(
            "📄 Download Maintenance Report",
            report,
            file_name="maintenance_report.txt"
        )
```
