import streamlit as st
import pandas as pd
import random

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Student Risk Prediction System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# PROFESSIONAL DARK UI
# =====================================================

st.markdown("""
<style>

/* MAIN APP */

.stApp {
    background-color: #0b1120;
}

/* TITLES */

h1, h2, h3 {
    color: white !important;
}

/* TEXT */

p, label, div {
    color: #e5e7eb;
    font-size: 16px;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* BUTTONS */

.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    height: 3em;
}

/* METRIC CARDS */

[data-testid="metric-container"] {
    background-color: #1f2937;
    border: 1px solid #374151;
    padding: 15px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/processed_data.csv")

# KEEP ONLY 5 STUDENTS

df = df.head(5)

# =====================================================
# CREATE STUDENT IDS
# =====================================================

df["Student_ID"] = range(1, len(df) + 1)

# =====================================================
# RANDOM GENDER VALUES
# =====================================================

df["Gender"] = [
    random.choice(["M", "F"])
    for _ in range(len(df))
]

# =====================================================
# FIND ATTENDANCE COLUMN AUTOMATICALLY
# =====================================================

attendance_column = [
    col for col in df.columns
    if "Attendance" in col
][0]

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🎓 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Dashboard",
        "Prediction",
        "Analytics",
        "About"
    ]
)

# =====================================================
# HOME PAGE
# =====================================================

if page == "Home":

    st.title(
        "🎓 Student Performance Risk Prediction & Early Warning System"
    )

    st.write(
        """
        AI-powered educational analytics platform designed
        to identify academically at-risk students and
        provide early intervention support.
        """
    )

    st.divider()

    # =====================================================
    # FEATURE CARDS
    # =====================================================

    st.subheader("🚀 Key Features")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            "🎯 Risk Prediction\n\nDetect students at academic risk."
        )

        st.info(
            "📊 Analytics Dashboard\n\nVisualize student performance trends."
        )

    with col2:

        st.info(
            "🚨 Early Warning Alerts\n\nIdentify students needing intervention."
        )

        st.info(
            "🧠 AI Insights\n\nGenerate smart educational insights."
        )

    st.divider()

    # =====================================================
    # QUICK STATISTICS
    # =====================================================

    st.subheader("📈 Quick Statistics")

    pass_count = len(
        df[df["Final_Exam_Score"] >= 50]
    )

    pass_percent = round(
        (pass_count / len(df)) * 100,
        2
    )

    high_risk = len(
        df[df["Final_Exam_Score"] < 50]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Students",
            len(df)
        )

    with col2:

        st.metric(
            "Average Score",
            round(df["Final_Exam_Score"].mean(), 2)
        )

    with col3:

        st.metric(
            "Pass %",
            f"{pass_percent}%"
        )

    with col4:

        st.metric(
            "High Risk",
            high_risk
        )

    st.divider()

    st.success(
        "🚀 Use the sidebar to explore Dashboard, Prediction, and Analytics."
    )

# =====================================================
# DASHBOARD PAGE
# =====================================================

elif page == "Dashboard":

    st.title("📊 Student Dashboard")

    st.subheader("Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Students",
            len(df)
        )

    with col2:

        st.metric(
            "Average Score",
            round(df["Final_Exam_Score"].mean(), 2)
        )

    with col3:

        st.metric(
            "Highest Score",
            df["Final_Exam_Score"].max()
        )

    with col4:

        st.metric(
            "Lowest Score",
            df["Final_Exam_Score"].min()
        )

    st.divider()

    # =====================================================
    # CHARTS
    # =====================================================

    st.subheader("📈 Performance Analytics")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### Final Exam Scores")

        chart_data = df.set_index("Student_ID")

        st.bar_chart(
            chart_data["Final_Exam_Score"]
        )

    with col2:

        st.write("### Pass vs Fail")

        pass_fail_data = pd.DataFrame({
            "Category": ["Pass", "Fail"],
            "Count": [
                len(df[df["Final_Exam_Score"] >= 50]),
                len(df[df["Final_Exam_Score"] < 50])
            ]
        }).set_index("Category")

        st.bar_chart(pass_fail_data)

    st.divider()

    # =====================================================
    # STUDENT DETAILS
    # =====================================================

    st.subheader("🔍 Student Details")

    selected_student = st.selectbox(
        "Select Student",
        df["Student_ID"]
    )

    student_data = df[
        df["Student_ID"] == selected_student
    ]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Final Score",
            int(student_data["Final_Exam_Score"].values[0])
        )

    with col2:

        st.metric(
            "Attendance",
            f"{int(student_data[attendance_column].values[0])}%"
        )

    with col3:

        st.metric(
            "Gender",
            student_data["Gender"].values[0]
        )

    st.divider()

    # =====================================================
    # EARLY WARNING ALERTS
    # =====================================================

    st.subheader("🚨 Early Warning Alerts")

    risk_students = df[
        df["Final_Exam_Score"] < 50
    ]

    if len(risk_students) > 0:

        st.error(
            f"{len(risk_students)} students are at HIGH RISK."
        )

    else:

        st.success(
            "No high-risk students detected."
        )

    st.divider()

    # =====================================================
    # AI EDUCATIONAL INSIGHTS
    # =====================================================

    st.subheader("🧠 AI Educational Insights")

    average_score = round(
        df["Final_Exam_Score"].mean(),
        2
    )

    if average_score >= 75:

        st.success(
            "📈 Overall class performance is GOOD."
        )

    elif average_score >= 50:

        st.warning(
            "📊 Overall class performance is MODERATE."
        )

    else:

        st.error(
            "📉 Overall class performance is POOR."
        )

    st.info(
        f"🏆 Highest score: {df['Final_Exam_Score'].max()}"
    )

    st.info(
        f"⚠ Lowest score: {df['Final_Exam_Score'].min()}"
    )

# =====================================================
# PREDICTION PAGE
# =====================================================

elif page == "Prediction":

    st.title("🎯 Student Risk Prediction")

    attendance = st.slider(
        "Attendance %",
        0,
        100,
        75
    )

    study_hours = st.slider(
        "Study Hours",
        0,
        15,
        5
    )

    assignment_score = st.slider(
        "Assignment Score",
        0,
        100,
        70
    )

    final_score = st.slider(
        "Final Exam Score",
        0,
        100,
        70
    )

    if st.button("Predict Risk"):

        if final_score < 50 or attendance < 40:

            st.error("🔴 HIGH RISK")

            st.warning(
                "Student needs immediate academic support."
            )

        elif final_score < 75:

            st.warning("🟡 MEDIUM RISK")

            st.info(
                "Student performance requires monitoring."
            )

        else:

            st.success("🟢 LOW RISK")

            st.success(
                "Student is performing well."
            )

# =====================================================
# ANALYTICS PAGE
# =====================================================

elif page == "Analytics":

    st.title("📈 Analytics Dashboard")

    st.subheader("Final Score Trend")

    st.line_chart(
        df["Final_Exam_Score"]
    )

    st.subheader("Attendance Analysis")

    attendance_chart = df.set_index(
        "Student_ID"
    )

    st.bar_chart(
        attendance_chart[attendance_column]
    )

# =====================================================
# ABOUT PAGE
# =====================================================

elif page == "About":

    st.title("📘 About Project")

    st.write("""

    ### Student Performance Risk Prediction & Early Warning System

    AI-powered educational analytics platform designed
    for identifying academically at-risk students.

    ### Technologies Used

    ✅ Python

    ✅ Streamlit

    ✅ Pandas

    ✅ Machine Learning

    ### Key Features

    ✅ Risk Prediction

    ✅ Early Warning Alerts

    ✅ Dashboard Analytics

    ✅ AI Educational Insights

    """)


