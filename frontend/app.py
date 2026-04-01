import streamlit as st
import requests

st.set_page_config(page_title="AI Pollution Dashboard", page_icon="🌍", layout="wide")

st.title("🌍 AI Pollution Dashboard - Delhi NCR")
st.markdown("Real-time AQI monitoring, forecasting & policy recommendations powered by AI")

# Backend URL
BASE_URL = "http://127.0.0.1:8000"

col1, col2 = st.columns(2)

with col1:
    # Current AQI
    st.subheader("📊 Current AQI")
    try:
        aqi = requests.get(f"{BASE_URL}/aqi/current").json()
        aqi_val = aqi["AQI"]
        color = "green" if aqi_val < 100 else "orange" if aqi_val < 200 else "red"
        st.metric("AQI", aqi_val)
        st.metric("PM2.5", aqi["PM2.5"])
        st.metric("PM10", aqi["PM10"])
    except:
        st.error("Backend not running. Start uvicorn first.")

with col2:
    # Prediction
    st.subheader("🔮 AQI Forecast (Next 5 Days)")
    try:
        pred = requests.get(f"{BASE_URL}/aqi/predict").json()
        st.line_chart(pred["next_5_days"])
        st.write(f"Trend: {pred['trend']}")
    except:
        st.error("Backend not running.")

st.subheader("🏭 Top Pollution Sources")
try:
    sources = requests.get(f"{BASE_URL}/sources").json()
    for s in sources["top_sources"]:
        st.write(f"- {s}")
except:
    st.error("Backend not running.")

st.subheader("📢 Policy Recommendations")
try:
    rec = requests.get(f"{BASE_URL}/recommendations").json()
    for action in rec["actions"]:
        st.success(action)
except:
    st.error("Backend not running.")
