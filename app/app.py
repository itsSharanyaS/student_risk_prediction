import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("data/processed_data.csv")

# Page Title
st.set_page_config(page_title="Student Risk Prediction System", layout="wide")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Choose Section",
    ["Dashboard", "Prediction", "Analytics", "About Project"]
)

# =========================
# DASHBOARD PAGE
# =========================
if page == "Dashboard":

    st.title("🎓 Student Performance Risk Prediction & Early Warning System")

    st.write("AI-powered system to identify academically at-risk students.")

    # KPI Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Students", len(df))

    with col2:
        st.metric(
            "Average Score",
            round(df["Final_Exam_Score"].mean(), 2)
        )

    with col3:

        if "Risk_Level" in df.columns:
            high_risk_count = len(
                df[df["Risk_Level"] == "High Risk"]
            )
        else:
            high_risk_count = 0

        st.metric("High Risk Students", high_risk_count)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

# =========================
# PREDICTION PAGE
# =========================
elif page == "Prediction":

    st.title("🎯 Student Risk Prediction")

    attendance = st.slider("Attendance (%)", 0, 100, 75)

    study_hours = st.slider("Study Hours Per Day", 0, 15, 5)

    assignment_score = st.slider("Assignment Score", 0, 100, 60)

    midterm_score = st.slider("Midterm Score", 0, 100, 60)

    final_exam_score = st.slider("Final Exam Score", 0, 100, 60)

    # Prediction Button
    if st.button("Predict Risk"):

        st.subheader("Prediction Result")

        # HIGH RISK
        if final_exam_score < 50 or attendance < 40:

            st.error("⚠ EARLY WARNING ALERT: Student is at HIGH academic risk!")

            st.subheader("📌 Personalized Recommendations")

            st.write("• Attend remedial coaching classes")
            st.write("• Increase study hours daily")
            st.write("• Schedule weekly mentor meetings")
            st.write("• Improve attendance consistency")
            st.write("• Complete pending assignments")

        # MEDIUM RISK
        elif final_exam_score < 75:

            st.warning("⚠ Student is at MEDIUM risk and needs monitoring.")

            st.subheader("📌 Personalized Recommendations")

            st.write("• Revise difficult subjects regularly")
            st.write("• Practice mock tests")
            st.write("• Improve classroom participation")
            st.write("• Increase assignment submission rate")

        # LOW RISK
        else:

            st.success("✅ Student performance is stable.")

            st.subheader("📌 Personalized Recommendations")

            st.write("• Maintain current performance")
            st.write("• Participate in advanced learning activities")
            st.write("• Help peers in collaborative learning")

# =========================
# ANALYTICS PAGE
# =========================
elif page == "Analytics":

    st.title("📊 Student Analytics Dashboard")

    st.subheader("Risk Distribution")

    if "Risk_Level" in df.columns:
        st.bar_chart(df["Risk_Level"].value_counts())

    st.subheader("Pass vs Fail Analysis")

    if "Pass_Fail" in df.columns:
        st.bar_chart(df["Pass_Fail"].value_counts())

    st.subheader("Final Exam Score Distribution")

    st.bar_chart(df["Final_Exam_Score"])

# =========================
# ABOUT PROJECT PAGE
# =========================
elif page == "About Project":

    st.title("📘 About Project")

    st.write("""
    ## Student Performance Risk Prediction & Early Warning System

    This project helps educational institutions identify students
    who are academically at risk using AI and analytics.

    ### Key Features:
    
    • Early Warning Alerts
    
    • Student Performance Analytics
    
    • Personalized Recommendations
    
    • Interactive Dashboard
    
    • Risk Monitoring System

    ### Objective:
    
    To help schools and colleges take proactive intervention
    measures before academic failure occurs.
    """)
```
