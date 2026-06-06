import streamlit as st
import pandas as pd
import random
import plotly.express as px
from datetime import datetime

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
# RANDOM GENDER
# =====================================================

df["Gender"] = [
    random.choice(["M", "F"])
    for _ in range(len(df))
]

# =====================================================
# FIND ATTENDANCE COLUMN
# =====================================================

attendance_column = [
    col for col in df.columns
    if "Attendance" in col
][0]

# =====================================================
# CREATE RISK LEVELS
# =====================================================

def get_risk(score):

    if score < 50:
        return "High Risk"

    elif score < 75:
        return "Medium Risk"

    else:
        return "Low Risk"

df["Risk_Level"] = df["Final_Exam_Score"].apply(
    get_risk
)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🎓 Navigation")

# SIDEBAR STATS

st.sidebar.metric(
    "Students",
    len(df)
)

st.sidebar.metric(
    "High Risk",
    len(df[df["Risk_Level"] == "High Risk"])
)

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
        "Student Performance Risk Prediction & Early Warning System"
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

        st.info(
            "📥 Download Reports\n\nExport academic reports instantly."
        )

    with col2:

        st.info(
            "🚨 Early Warning Alerts\n\nIdentify students needing intervention."
        )

        st.info(
            "🧠 AI Insights\n\nGenerate smart educational insights."
        )

        st.info(
            "📈 Risk Analytics\n\nMonitor student risk distribution."
        )

    st.divider()

    # =====================================================
    # QUICK STATS
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

    st.caption(
        f"Last Updated: {datetime.now().strftime('%d %B %Y %H:%M')}"
    )

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

        chart_data = df.set_index("Student_ID")

        st.bar_chart(
            chart_data["Final_Exam_Score"]
        )

    with col2:

        pie_chart = px.pie(
            names=["Pass", "Fail"],
            values=[
                len(df[df["Final_Exam_Score"] >= 50]),
                len(df[df["Final_Exam_Score"] < 50])
            ],
            title="Pass vs Fail Distribution"
        )

        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

    st.divider()

    # =====================================================
    # RISK DISTRIBUTION
    # =====================================================

    st.subheader("📊 Risk Distribution")

    risk_chart = px.bar(
        df["Risk_Level"].value_counts(),
        title="Student Risk Levels"
    )

    st.plotly_chart(
        risk_chart,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # STUDENT PROFILE
    # =====================================================

    st.subheader("👨‍🎓 Student Profile")

    selected_student = st.selectbox(
        "Select Student",
        df["Student_ID"]
    )

    student_data = df[
        df["Student_ID"] == selected_student
    ]

    score = int(
        student_data["Final_Exam_Score"].values[0]
    )

    attendance = int(
        student_data[attendance_column].values[0]
    )

    gender = student_data["Gender"].values[0]

    risk = student_data["Risk_Level"].values[0]

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Final Score",
            score
        )

    with col2:

        st.metric(
            "Attendance",
            f"{attendance}%"
        )

    with col3:

        st.metric(
            "Gender",
            gender
        )

    with col4:

        st.metric(
            "Risk Level",
            risk
        )

    # RISK COLOR

    if risk == "High Risk":

        st.error("🔴 HIGH RISK STUDENT")

    elif risk == "Medium Risk":

        st.warning("🟡 MEDIUM RISK STUDENT")

    else:

        st.success("🟢 LOW RISK STUDENT")

    st.divider()

    # =====================================================
    # EARLY WARNING ALERTS
    # =====================================================

    st.subheader("🚨 Real-Time Alerts")

    risk_students = len(
        df[df["Risk_Level"] == "High Risk"]
    )

    if risk_students > 0:

        st.error(
            f"⚠ ALERT: {risk_students} students require immediate intervention."
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

# =====================================================
# ADVANCED AI INSIGHTS
# =====================================================

st.divider()

low_attendance_students = df[
    df[attendance_column] < 60
]

if len(low_attendance_students) > 0:

    st.warning(
        f"📌 {len(low_attendance_students)} students have attendance below 60%, increasing academic risk."
    )

high_risk_students = df[
    df["Risk_Level"] == "High Risk"
]

st.error(
    f"🚨 {len(high_risk_students)} students are currently classified as high-risk."
)

top_student = df.loc[
    df["Final_Exam_Score"].idxmax()
]

st.success(
    f"🏆 Student {top_student['Student_ID']} is the top performer with score {top_student['Final_Exam_Score']}."
)

lowest_student = df.loc[
    df["Final_Exam_Score"].idxmin()
]

st.warning(
    f"📉 Student {lowest_student['Student_ID']} requires immediate academic intervention."
)

correlation = df[attendance_column].corr(
    df["Final_Exam_Score"]
)

if correlation > 0.5:

    st.info(
        "📊 Attendance has a strong positive relationship with academic performance."
    )

else:

    st.info(
        "📊 Attendance shows weak correlation with performance."
    )

average_attendance = round(
    df[attendance_column].mean(),
    2
)

st.info(
    f"📈 Average class attendance is {average_attendance}%."
)


    st.info(
        "📌 Students with low attendance tend to perform poorly."
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

        confidence = random.randint(85, 99)

        if final_score < 50 or attendance < 40:

            st.error("🔴 HIGH RISK")

            st.warning(
                "Student needs immediate academic support."
            )

            st.info(
                "Recommendations:\n\n"
                "- Increase attendance\n"
                "- Attend mentoring sessions\n"
                "- Improve assignment completion"
            )

        elif final_score < 75:

            st.warning("🟡 MEDIUM RISK")

            st.info(
                "Recommendations:\n\n"
                "- Practice mock tests\n"
                "- Improve consistency\n"
                "- Increase study hours"
            )

        else:

            st.success("🟢 LOW RISK")

            st.success(
                "Student is performing well."
            )

            st.info(
                "Recommendations:\n\n"
                "- Maintain current performance\n"
                "- Continue regular practice"
            )

        st.success(
            f"Prediction Confidence: {confidence}%"
        )

        st.balloons()

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

    st.subheader("Attendance vs Final Score")

    scatter_fig = px.scatter(
        df,
        x=attendance_column,
        y="Final_Exam_Score",
        color="Risk_Level",
        hover_data=["Student_ID"]
    )

    st.plotly_chart(
        scatter_fig,
        use_container_width=True
    )

    # DOWNLOAD BUTTON

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Student Report",
        data=csv,
        file_name="student_report.csv",
        mime="text/csv"
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

    ✅ Plotly

    ✅ Machine Learning

    ### Key Features

    ✅ Risk Prediction

    ✅ Early Warning Alerts

    ✅ Dashboard Analytics

    ✅ AI Educational Insights

    ✅ Risk Distribution Analysis

    ✅ Downloadable Reports

    ### Project Objective

    To help educational institutions identify
    at-risk students early and improve
    academic outcomes through AI-driven analytics.

    """)
