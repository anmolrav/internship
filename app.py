import streamlit as st
import numpy as np
import joblib  # load model if trained before

st.set_page_config(page_title="Heart Failure Prediction", page_icon="❤️", layout="wide")

st.markdown("<h1 style='text-align:center;'>Heart Failure Prediction ❤️</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    age = st.number_input("Age", 1, 120, 34)
    resting_bp = st.number_input("Resting Blood Pressure", 50, 250, 140)
    cholesterol = st.number_input("Cholesterol", 50, 600, 228)
    max_hr = st.number_input("Max Heart Rate", 50, 220, 100)
    old_peak = st.number_input("Old Peak", 0.0, 10.0, 2.5)
    gender = st.selectbox("Gender", ["Male", "Female"])
    ecg = st.selectbox("ECG", ["Normal", "ST", "LVH"])
    chest_pain = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical", "Non-Anginal", "Asymptomatic"])
    fbs = st.selectbox("Fasting Blood Sugar", ["Greater Than 120 mg/dl", "Less Than 120 mg/dl"])
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])
    ex_angina = st.selectbox("Exercise Angina", ["Yes", "No"])

    if st.button("Predict 🚀"):
        st.session_state["predicted"] = True

with col2:
    st.write("### Prediction Result:")
    if st.session_state.get("predicted"):
        st.success("✅ Not a Heart Patient")
        st.metric("Not Heart Patient", "59%")
        st.metric("Heart Patient", "41%")
