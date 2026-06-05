import streamlit as st
import pandas as pd
import joblib

# Load dataset
df = pd.read_csv("data/processed_data.csv")

# Load model
model = joblib.load("models/risk_model.pkl")

st.title("🎓 Student Risk Prediction System")

st.subheader("Processed Dataset")
st.dataframe(df)

st.subheader("Risk Level Distribution")
st.bar_chart(df["Risk_Level"].value_counts())

st.subheader("Predict Student Risk")

attendance = st.slider("Attendance (%)", 0, 100, 75)
study_hours = st.slider("Study Hours", 0, 15, 5)
assignment_score = st.slider("Assignment Score", 0, 100, 60)
midterm_score = st.slider("Midterm Score", 0, 100, 60)
final_exam_score = st.slider("Final Exam Score", 0, 100, 60)

if st.button("Predict Risk"):

    sample = [[
        0,
        0,
        attendance,
        study_hours,
        assignment_score,
        midterm_score,
        final_exam_score,
        0,0,0,0
    ]]

    prediction = model.predict(sample)

    risk = prediction[0]

    st.subheader("Prediction Result")

    if risk == "High Risk":
        st.error("⚠ EARLY WARNING ALERT: Student is at HIGH academic risk!")

    elif risk == "Medium Risk":
        st.warning("⚠ Student is at MEDIUM risk and needs monitoring.")

    else:
        st.success("✅ Student performance is stable.")
