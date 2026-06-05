import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Student Risk Prediction System",
    layout="wide"
)

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("data/processed_data.csv")

# =========================
# SIDEBAR NAVIGATION
# =========================

page = st.sidebar.selectbox(
    "Choose Section",
    ["Dashboard", "Prediction", "Analytics", "About Project"]
)

# =========================
# DASHBOARD PAGE
# =========================

if page == "Dashboard":

    st.title("🎓 Student Performance Risk Prediction & Early Warning System")

    st.write(
        "AI-powered system to identify academically at-risk students."
    )

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
        st.metric(
            "Pass Students",
            len(df[df["Pass_Fail"] == "Pass"])
        )

    # =========================
    # STUDENT SEARCH SYSTEM
    # =========================

    st.subheader("🔍 Student Search System")

    selected_student = st.selectbox(
        "Select Student ID",
        df["Student_ID"],
        key="student_selector"
    )

    student_data = df[df["Student_ID"] == selected_student]

    st.write("### Student Details")

    st.dataframe(student_data)

    # =========================
    # DOWNLOAD STUDENT REPORT
    # =========================

    csv = student_data.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="⬇ Download Student Report",
        data=csv,
        file_name="student_report.csv",
        mime="text/csv"
    )

    # =========================
    # PERFORMANCE INSIGHTS
    # =========================

    st.write("### Performance Insights")

    if "Final_Exam_Score" in df.columns:
        st.write(
            "📌 Final Exam Score:",
            int(student_data["Final_Exam_Score"].values[0])
        )

    if "Attendance (%)" in df.columns:
        st.write(
            "📌 Attendance:",
            int(student_data["Attendance (%)"].values[0])
        )

    if "Pass_Fail" in df.columns:
        st.write(
            "📌 Pass/Fail Status:",
            student_data["Pass_Fail"].values[0]
        )

    # Dataset Preview
    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head())

# =========================
# PREDICTION PAGE
# =========================

elif page == "Prediction":

    st.title("🎯 Student Risk Prediction")

    attendance = st.slider(
        "Attendance (%)",
        0,
        100,
        75
    )

    study_hours = st.slider(
        "Study Hours Per Day",
        0,
        15,
        5
    )

    assignment_score = st.slider(
        "Assignment Score",
        0,
        100,
        60
    )

    midterm_score = st.slider(
        "Midterm Score",
        0,
        100,
        60
    )

    final_exam_score = st.slider(
        "Final Exam Score",
        0,
        100,
        60
    )

    # =========================
    # PREDICTION BUTTON
    # =========================

    if st.button("Predict Risk"):

        st.subheader("📊 Prediction Result")

        # =========================
        # HIGH RISK
        # =========================

        if final_exam_score < 50 or attendance < 40:

            st.error("🔴 HIGH RISK")

            st.error(
                "⚠ EARLY WARNING ALERT: Student is at HIGH academic risk!"
            )

            st.subheader("📌 Personalized Recommendations")

            st.write("• Attend remedial coaching classes")
            st.write("• Increase study hours daily")
            st.write("• Schedule weekly mentor meetings")
            st.write("• Improve attendance consistency")
            st.write("• Complete pending assignments")

        # =========================
        # MEDIUM RISK
        # =========================

        elif final_exam_score < 75:

            st.warning("🟡 MEDIUM RISK")

            st.warning(
                "⚠ Student is at MEDIUM risk and needs monitoring."
            )

            st.subheader("📌 Personalized Recommendations")

            st.write("• Revise difficult subjects regularly")
            st.write("• Practice mock tests")
            st.write("• Improve classroom participation")
            st.write("• Increase assignment submission rate")

        # =========================
        # LOW RISK
        # =========================

        else:

            st.success("🟢 LOW RISK")

            st.success(
                "✅ Student performance is stable."
            )

            st.subheader("📌 Personalized Recommendations")

            st.write("• Maintain current performance")
            st.write("• Participate in advanced learning activities")
            st.write("• Help peers in collaborative learning")

# =========================
# ANALYTICS PAGE
# =========================

elif page == "Analytics":

    st.title("📊 Student Analytics Dashboard")

    st.write(
        "Interactive charts and educational insights"
    )

    # Final Exam Score Chart
    st.subheader("📌 Final Exam Score Distribution")

    if "Final_Exam_Score" in df.columns:
        st.bar_chart(df["Final_Exam_Score"])

    # Pass vs Fail Chart
    st.subheader("📌 Pass vs Fail Analysis")

    if "Pass_Fail" in df.columns:
        st.bar_chart(df["Pass_Fail"].value_counts())

    # Dataset Preview
    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head())

# =========================
# ABOUT PROJECT PAGE
# =========================

elif page == "About Project":

    st.title("📘 About Project")

    st.write("""
    ## Student Performance Risk Prediction & Early Warning System

    This project helps educational institutions identify students
    who are academically at risk using AI and analytics.

    ### Key Features

    • Early Warning Alerts

    • Student Performance Analytics

    • Personalized Recommendations

    • Interactive Dashboard

    • Student Monitoring System

    • Downloadable Student Reports

    • Risk Visualization System

    ### Objective

    To help schools and colleges take proactive intervention
    measures before academic failure occurs.
    """)
