import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Student Risk Prediction System",
    page_icon="🎓",
    layout="wide"
)

# =========================
# HIDE STREAMLIT BRANDING
# =========================

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# PROFESSIONAL CUSTOM CSS
# =========================

st.markdown("""
<style>

/* Main App Background */
.stApp {
    background-color: #f4f6f9;
}

/* Main Headers */
h1, h2, h3 {
    color: #0b3d91;
    font-family: 'Segoe UI', sans-serif;
    font-weight: 700;
}

/* Paragraph Text */
p {
    color: #333333;
    font-size: 16px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #dbe9ff;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background-color: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

/* Buttons */
.stButton>button {
    background-color: #1565c0;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
    font-weight: bold;
}

/* Button Hover */
.stButton>button:hover {
    background-color: #0d47a1;
    color: white;
}

/* Download Button */
.stDownloadButton>button {
    background-color: #2e7d32;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
    font-weight: bold;
}

/* Success Box */
.stSuccess {
    border-radius: 10px;
}

/* Warning Box */
.stWarning {
    border-radius: 10px;
}

/* Error Box */
.stError {
    border-radius: 10px;
}

/* Dataframe Styling */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}

/* Divider */
hr {
    border: 1px solid #d0d7de;
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("data/processed_data.csv")

# =========================
# SIDEBAR
# =========================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
    width=120
)

st.sidebar.title("🎓 Student Analytics System")

st.sidebar.success(
    "AI-Based Academic Monitoring Platform"
)

page = st.sidebar.selectbox(
    "Choose Section",
    [
        "Dashboard",
        "Prediction",
        "Analytics",
        "About Project"
    ]
)

# =========================
# DASHBOARD PAGE
# =========================

if page == "Dashboard":

    st.title(
        "🎓 Student Performance Risk Prediction & Early Warning System"
    )

    st.success(
        "🚀 AI-powered dashboard for monitoring student academic performance and risk levels."
    )

    st.write(
        """
        AI-powered educational analytics platform designed to identify
        academically at-risk students and provide early intervention support.
        """
    )

    st.divider()

    # =========================
    # KPI METRICS
    # =========================

    st.subheader("📊 Key Performance Indicators")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Students",
            len(df)
        )

    with col2:
        st.metric(
            "Average Final Score",
            round(df["Final_Exam_Score"].mean(), 2)
        )

    with col3:
        st.metric(
            "Pass Percentage",
            round(
                (
                    len(df[df["Pass_Fail"] == "Pass"])
                    / len(df)
                ) * 100,
                2
            )
        )

    st.divider()

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
    # DOWNLOAD REPORT
    # =========================

    csv = student_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Student Report",
        data=csv,
        file_name="student_report.csv",
        mime="text/csv"
    )

    st.divider()

    # =========================
    # PERFORMANCE INSIGHTS
    # =========================

    st.subheader("📌 Performance Insights")

    if "Final_Exam_Score" in df.columns:
        st.write(
            "📘 Final Exam Score:",
            int(student_data["Final_Exam_Score"].values[0])
        )

    if "Attendance (%)" in df.columns:
        st.write(
            "📘 Attendance:",
            int(student_data["Attendance (%)"].values[0])
        )

    if "Pass_Fail" in df.columns:
        st.write(
            "📘 Pass / Fail Status:",
            student_data["Pass_Fail"].values[0]
        )

    st.divider()

    # =========================
    # EARLY WARNING ALERT SYSTEM
    # =========================

    st.subheader("🚨 Early Warning Alerts")

    high_risk_students = df[
        (df["Final_Exam_Score"] < 50)
    ]

    if len(high_risk_students) > 0:

        for index, row in high_risk_students.iterrows():

            st.error(
                f"⚠ Student {row['Student_ID']} is academically at HIGH RISK"
            )

            st.write(
                "📌 Immediate academic intervention recommended."
            )

    else:

        st.success(
            "✅ No high-risk students detected."
        )

    st.divider()

    # =========================
    # DATASET PREVIEW
    # =========================

    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head())

# =========================
# PREDICTION PAGE
# =========================

elif page == "Prediction":

    st.title("🎯 Student Risk Prediction")

    st.write(
        """
        Predict the academic risk level of a student using
        attendance and performance indicators.
        """
    )

    st.divider()

    # =========================
    # INPUT SECTION
    # =========================

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

    st.divider()

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

    st.title("📊 Advanced Student Analytics Dashboard")

    st.write(
        """
        Interactive educational analytics and institutional insights.
        """
    )

    st.divider()

    # =========================
    # KPI METRICS
    # =========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Final Score",
            round(df["Final_Exam_Score"].mean(), 2)
        )

    with col2:

        if "Attendance (%)" in df.columns:
            st.metric(
                "Average Attendance",
                round(df["Attendance (%)"].mean(), 2)
            )

    with col3:
        st.metric(
            "Pass Percentage",
            round(
                (
                    len(df[df["Pass_Fail"] == "Pass"])
                    / len(df)
                ) * 100,
                2
            )
        )

    st.divider()

    # =========================
    # FINAL EXAM SCORE DISTRIBUTION
    # =========================

    st.subheader("📌 Final Exam Score Distribution")

    st.bar_chart(df["Final_Exam_Score"])

    # =========================
    # PASS VS FAIL ANALYSIS
    # =========================

    st.subheader("📌 Pass vs Fail Analysis")

    st.bar_chart(df["Pass_Fail"].value_counts())

    # =========================
    # TOP PERFORMERS
    # =========================

    st.subheader("🏆 Top Performing Students")

    top_students = df.sort_values(
        by="Final_Exam_Score",
        ascending=False
    ).head(5)

    st.dataframe(top_students)

    # =========================
    # LOW PERFORMERS
    # =========================

    st.subheader("⚠ Students Needing Attention")

    low_students = df.sort_values(
        by="Final_Exam_Score"
    ).head(5)

    st.dataframe(low_students)

    st.divider()

    # =========================
    # DATASET PREVIEW
    # =========================

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

    • Advanced Analytics Dashboard

    • AI-Based Academic Monitoring

    ### Objective

    To help schools and colleges take proactive intervention
    measures before academic failure occurs.
    """)

# =========================
# FOOTER
# =========================

st.divider()

st.markdown(
    """
    <center>
    <h4>🎓 Student Performance Risk Prediction & Early Warning System</h4>
    <p>Built using Streamlit, Python, Machine Learning & Educational Analytics</p>
    </center>
    """,
    unsafe_allow_html=True
)
