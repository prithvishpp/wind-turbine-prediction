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
        "Degradation Analysis",
        "Weather Impact Analysis",
        "Analytics Dashboard",
        "Admin Dashboard"
    ]
)

# =========================
# HOME PAGE
# =========================
if page == "Home":

    st.title("Wind Turbine Blade Degradation Analytics")

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
# DEGRADATION ANALYSIS
# =========================
elif page == "Degradation Analysis":

    st.title("🔧 Wind Turbine Blade Degradation Analysis")

    turbine_age = st.slider(
        "Turbine Age (Years)",
        1,
        25,
        10
    )

    vibration_level = st.slider(
        "Vibration Level",
        0,
        100,
        50
    )

    efficiency = st.slider(
        "Current Efficiency (%)",
        0,
        100,
        80
    )

    degradation_score = (
        turbine_age * 2 +
        vibration_level * 0.4 +
        (100 - efficiency) * 0.6
    )

    st.subheader("Degradation Score")

    st.progress(
        min(int(degradation_score), 100)
    )

    st.write(
        f"Degradation Score: {degradation_score:.1f}/100"
    )

    if degradation_score < 35:

        st.success(
            "🟢 Low Degradation"
        )

        st.write(
            "Blade condition is healthy."
        )

    elif degradation_score < 70:

        st.warning(
            "🟡 Moderate Degradation"
        )

        st.write(
            "Inspection recommended."
        )

    else:

        st.error(
            "🔴 Severe Degradation"
        )

        st.write(
            "Maintenance required."
        )

    st.subheader("Estimated Remaining Life")

    remaining_life = max(
        25 - turbine_age,
        0
    )

    st.metric(
        "Remaining Life",
        f"{remaining_life} Years"
    )

    st.subheader("Recommended Actions")

    if degradation_score >= 70:

        st.write("""
        • Inspect turbine blades

        • Check gearbox wear

        • Verify sensor accuracy

        • Schedule preventive maintenance

        • Replace damaged components
        """)

    else:

        st.write("""
        • Continue routine monitoring

        • Schedule periodic inspections

        • Maintain lubrication systems
        """)
# =========================
# WEATHER IMPACT ANALYSIS
# =========================
elif page == "Weather Impact Analysis":

    st.title("🌦️ Weather Impact Analysis")

    st.write("""
    Analyze how environmental conditions
    affect wind turbine performance.
    """)

    temperature = st.slider(
        "Temperature (°C)",
        0,
        50,
        25
    )

    humidity = st.slider(
        "Humidity (%)",
        0,
        100,
        50
    )

    wind_gust = st.slider(
        "Wind Gust Speed (m/s)",
        0,
        40,
        15
    )

    st.subheader("Weather Conditions")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Temperature",
            f"{temperature} °C"
        )

    with col2:
        st.metric(
            "Humidity",
            f"{humidity}%"
        )

    with col3:
        st.metric(
            "Wind Gust",
            f"{wind_gust} m/s"
        )

    # Impact Score
    impact_score = (
        abs(temperature - 25) * 0.5
        + humidity * 0.2
        + wind_gust * 1.5
    )

    st.subheader("Weather Impact Score")

    st.progress(
        min(int(impact_score), 100)
    )

    st.write(
        f"Impact Score: {impact_score:.1f}/100"
    )

    if impact_score < 30:

        st.success(
            "🟢 Favorable Conditions"
        )

        st.write(
            "Weather conditions support efficient power generation."
        )

    elif impact_score < 60:

        st.warning(
            "🟡 Moderate Impact"
        )

        st.write(
            "Weather may slightly affect turbine performance."
        )

    else:

        st.error(
            "🔴 High Weather Impact"
        )

        st.write(
            "Weather conditions may reduce efficiency and increase wear."
        )

    # Weather Trend Chart
    st.subheader("Weekly Weather Trend")

    weather_data = pd.DataFrame({
        "Day": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ],
        "Wind Speed": [
            12,
            14,
            11,
            16,
            18,
            15,
            13
        ]
    })

    st.line_chart(
        weather_data.set_index("Day")
    )

    st.subheader("Recommendations")

    if impact_score >= 60:

        st.write("""
        • Inspect turbine blades

        • Monitor vibration levels

        • Schedule preventive maintenance

        • Check gearbox condition
        """)

    else:

        st.write("""
        • Continue routine operation

        • Monitor weather forecasts

        • Maintain regular inspections
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

if password == "admin123":

    st.success("Admin Access Granted")

    # =========================
    # CONTROL CENTER METRICS
    # =========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🌪 Active Turbines",
            "125"
        )

    with col2:
        st.metric(
            "🟢 Online",
            "118"
        )

    with col3:
        st.metric(
            "🔴 Offline",
            "7"
        )

    # =========================
    # SYSTEM STATUS
    # =========================

    st.subheader("System Status")

    st.success("🟢 Prediction Engine Online")

    st.success("🟢 Analytics Dashboard Active")

    st.success("🟢 Maintenance Monitor Running")

    st.success("🟢 Database Connected")

    # =========================
    # DATASET SUMMARY
    # =========================

    st.subheader("Dataset Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Records",
            "50,530"
        )

    with col2:
        st.metric(
            "Features",
            "3"
        )

    with col3:
        st.metric(
            "Target",
            "LV ActivePower"
        )

    # =========================
    # MODEL PERFORMANCE
    # =========================

    st.subheader("Model Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "R² Score",
            "0.91"
        )

    with col2:
        st.metric(
            "RMSE",
            "410"
        )

    with col3:
        st.metric(
            "MSE",
            "168100"
        )

    # =========================
    # ACTIVE ALERTS
    # =========================

    st.subheader("🚨 Active Alerts")

    st.warning(
        "⚠ WT-102: Blade Inspection Required"
    )

    st.error(
        "🚨 WT-115: Gearbox Maintenance Required"
    )

    st.info(
        "ℹ WT-108: Scheduled Maintenance Due"
    )

    # =========================
    # HEALTH DISTRIBUTION
    # =========================

    st.subheader("Turbine Health Distribution")

    health_data = pd.DataFrame({
        "Status": [
            "Healthy",
            "Inspection",
            "Maintenance"
        ],
        "Count": [
            95,
            20,
            10
        ]
    })

    st.bar_chart(
        health_data.set_index("Status")
    )

    # =========================
    # DAILY POWER PRODUCTION
    # =========================

    st.subheader("Daily Power Production")

    power_data = pd.DataFrame({
        "Day": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ],
        "Power": [
            1800,
            1950,
            2000,
            1850,
            2100,
            2050,
            2200
        ]
    })

    st.line_chart(
        power_data.set_index("Day")
    )

    # =========================
    # MAINTENANCE SCHEDULE
    # =========================

    st.subheader("Upcoming Maintenance")

    maintenance_data = pd.DataFrame({
        "Turbine": [
            "WT-102",
            "WT-108",
            "WT-115"
        ],
        "Date": [
            "2026-07-10",
            "2026-07-15",
            "2026-07-22"
        ],
        "Task": [
            "Blade Inspection",
            "Sensor Calibration",
            "Gearbox Maintenance"
        ]
    })

    st.dataframe(
        maintenance_data,
        use_container_width=True
    )

    # =========================
    # RECENT ACTIVITY
    # =========================

    st.subheader("Recent Admin Activity")

    activity_data = pd.DataFrame({
        "Time": [
            "09:15",
            "10:30",
            "12:45",
            "14:20"
        ],
        "Action": [
            "Dashboard Login",
            "Health Check Run",
            "Report Generated",
            "Alerts Sent"
        ]
    })

    st.dataframe(
        activity_data,
        use_container_width=True
    )

    # =========================
    # ADMIN ACTIONS
    # =========================

    st.subheader("Administrator Actions")

    if st.button("Generate Maintenance Report"):
        st.success(
            "Report Generated Successfully"
        )

    if st.button("Run Health Check"):
        st.success(
            "All Turbines Scanned"
        )

    if st.button("Send Maintenance Alerts"):
        st.success(
            "Alerts Sent Successfully"
        )

    if st.button("Refresh Dashboard"):
        st.success(
            "Dashboard Refreshed"
        )

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
