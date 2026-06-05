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

    st.subheader("Prediction Result")

    # Simple risk logic
    if final_exam_score < 50 or attendance < 40:

        st.error("⚠ EARLY WARNING ALERT: Student is at HIGH academic risk!")

        st.subheader("Recommended Interventions")

        st.write("• Extra tutoring sessions")
        st.write("• Parent-teacher meetings")
        st.write("• Weekly progress tracking")
        st.write("• Attendance improvement plan")

    elif final_exam_score < 75:

        st.warning("⚠ Student is at MEDIUM risk and needs monitoring.")

        st.subheader("Recommendations")

        st.write("• Improve study hours")
        st.write("• Attend revision classes")
        st.write("• Increase assignment practice")

    else:

        st.success("✅ Student performance is stable.")

        st.subheader("Recommendations")

        st.write("• Maintain consistent performance")
        st.write("• Participate in advanced activities")
