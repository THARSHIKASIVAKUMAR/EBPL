import streamlit as st
import pandas as pd
from logic.predictor import predict_defect

st.set_page_config(page_title="Q-ControlX", layout="wide")

st.title("🔍 Q-ControlX – Real-Time Quality Prediction")
st.markdown("Simulate sensor input to predict potential defects.")

# Input form for 5 sensors
with st.form("sensor_input_form"):
    col1, col2, col3, col4, col5 = st.columns(5)
    sensor_1 = col1.number_input("Sensor 1", value=0.0)
    sensor_2 = col2.number_input("Sensor 2", value=5.0)
    sensor_3 = col3.number_input("Sensor 3", value=10.0)
    sensor_4 = col4.number_input("Sensor 4", value=3.0)
    sensor_5 = col5.number_input("Sensor 5", value=7.0)

    submitted = st.form_submit_button("🔎 Predict Defect")

if submitted:
    input_data = pd.DataFrame([{
        "sensor_1": sensor_1,
        "sensor_2": sensor_2,
        "sensor_3": sensor_3,
        "sensor_4": sensor_4,
        "sensor_5": sensor_5
    }])
    
    try:
        prob = predict_defect(input_data)
        st.success(f"🧠 Defect Probability: **{prob:.2%}**")
        if prob > 0.5:
            st.error("❌ High risk of defect. Suggest immediate inspection.")
        else:
            st.success("✅ Quality within acceptable range.")
    except Exception as e:
        st.error(f"Prediction error: {e}")
