import streamlit as st
import pandas as pd

# Load dataset

df = pd.read_csv("dataset.csv")

# Sidebar Navigation

st.sidebar.title("Navigation")

page = st.sidebar.radio(
"Go to",
["Home", "Analytics"]
)

# Home Page

if page == "Home":

```
st.title("Wind Turbine Predictive Maintenance Dashboard")

st.write("""
Welcome to the Wind Turbine Predictive Maintenance Dashboard.

Features:
- Dataset Analytics
- Root Cause Analysis
- Performance Monitoring
- Predictive Maintenance Insights
""")
```

# Analytics Page

if page == "Analytics":

```
st.title("Wind Turbine Analytics")

st.subheader("Dataset Preview")
st.dataframe(df.head(10))

st.subheader("Dataset Shape")
st.write(
    f"Rows: {df.shape[0]} | Columns: {df.shape[1]}"
)

st.subheader("Summary Statistics")
st.dataframe(df.describe())
```
