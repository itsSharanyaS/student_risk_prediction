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
# PROFESSIONAL DARK THEME
# =====================================================

st.markdown("""
<style>

/* MAIN BACKGROUND */

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
# CUSTOM STUDENT IDS
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
# SIDEBAR
# =====================================================

st.sidebar.title("🎓 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Dashboard",
        "Prediction",
        "Analytics",
        "About"
    ]
)

# =====================================================
# DASHBOARD PAGE
# =====================================================

if page == "Dashboard":

    st.title(
        "🎓 Student Performance Risk Prediction & Early Warning System"
    )

    st.success(
        "AI-powered dashboard for monitoring student performance."
    )

    st.write(
        """
        Educational analytics platform designed to identify
        academically at-risk students and provide intervention support.
        """
    )

    st.divider()

    # =====================================================
    # KPI CARDS
    # =====================================================

    st.subheader("📊 Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "👨‍🎓 Total Students",
            len(df)
        )

    with col2:

        st.metric(
            "📈 Average Score",
            round(df["Final_Exam_Score"].mean(), 2)
        )

    with col3:

        pass_percent = round(
            (
                len(df[df["Pass_Fail"] == "Pass"])
                / len(df)
            ) * 100,
            2
        )

        st.metric(
            "✅ Pass %",
            f"{pass_percent}%"
        )

    with col4:

        high_risk = len(
            df[df["Final_Exam_Score"] < 50]
        )

        st.metric(
            "🚨 High Risk",
            high_risk
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

        st.bar_chart(
            df["Pass_Fail"].value_counts()
        )

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

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Final Score",
            int(student_data["Final_Exam_Score"].values[0])
        )

    with col2:

        st.metric(
            "Attendance",
            f"{int(student_data['Attendance (%)'].values[0])}%"
        )

    st.success(
        f"Selected Student: {selected_student}"
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
            f"{len(risk_students)} students are at HIGH RISK"
        )

    else:

        st.success(
            "No high-risk students detected"
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

    highest_score = df["Final_Exam_Score"].max()

    lowest_score = df["Final_Exam_Score"].min()

    pass_students = len(
        df[df["Pass_Fail"] == "Pass"]
    )

    fail_students = len(
        df[df["Pass_Fail"] == "Fail"]
    )

    if average_score >= 75:

        st.success(
            f"📈 Overall class performance is GOOD with average score {average_score}."
        )

    elif average_score >= 50:

        st.warning(
            f"📊 Overall class performance is MODERATE with average score {average_score}."
        )

    else:

        st.error(
            f"📉 Overall class performance is POOR with average score {average_score}."
        )

    st.info(
        f"🏆 Highest student score is {highest_score}."
    )

    st.info(
        f"⚠ Lowest student score is {lowest_score}."
    )

    st.success(
        f"✅ {pass_students} students passed successfully."
    )

    st.error(
        f"🚨 {fail_students} students need academic support."
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

    final_score = st.slider(
        "Final Exam Score",
        0,
        100,
        70
    )

    if st.button("Predict Risk"):

        if final_score < 50 or attendance < 40:

            st.error("🔴 HIGH RISK")

        elif final_score < 75:

            st.warning("🟡 MEDIUM RISK")

        else:

            st.success("🟢 LOW RISK")

# =====================================================
# ANALYTICS PAGE
# =====================================================

elif page == "Analytics":

    st.title("📊 Analytics Dashboard")

    st.subheader("📈 Final Score Trend")

    st.line_chart(
        df["Final_Exam_Score"]
    )

    st.subheader("📄 Student Dataset")

    st.dataframe(df)

# =====================================================
# ABOUT PAGE
# =====================================================

elif page == "About":

    st.title("📘 About Project")

    st.write("""

    ### Student Performance Risk Prediction & Early Warning System

    AI-powered educational analytics platform designed
    for identifying academically at-risk students.

    ### Features

    ✅ Student Risk Prediction

    ✅ Dashboard Analytics

    ✅ Early Warning Alerts

    ✅ Interactive Charts

    ✅ AI Educational Insights

    ✅ Student Monitoring

    """)

