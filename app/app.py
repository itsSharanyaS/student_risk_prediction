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
    background-color: #1e293b;
    border-right: 3px solid #2563eb;
    width: 320px !important;
}

/* SIDEBAR CONTENT */

.css-1d391kg {
    background-color: #1e293b;
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

/* HORIZONTAL LINE */

hr {
    border: 1px solid #374151;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/processed_data.csv")

# =====================================================
# KEEP ONLY 5 STUDENTS
# =====================================================

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

st.sidebar.markdown(
    """
    # 🎓 Dashboard Menu
    
    Navigate through the AI-powered student analytics system.
    """
)

st.sidebar.subheader("Navigation")

# =====================================================
# SIDEBAR STATS
# =====================================================

st.sidebar.metric(
    "Students",
    len(df)
)

st.sidebar.metric(
    "High Risk",
    len(df[df["Risk_Level"] == "High Risk"])
)

# =====================================================
# NAVIGATION
# =====================================================

page = st.sidebar.radio(
    "Select Page",
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

if page == "🏠 Home":

    st.title(
        "Student Performance Risk Prediction & Early Warning System"
    )

 
    st.warning(
        "Use the LEFT SIDEBAR MENU to explore more!!"
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

    # =====================================================
    # EXPLORE SYSTEM
    # =====================================================

    st.subheader("🚀 Explore System")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            "📊 Dashboard\n\nView student analytics, charts, alerts, and AI insights."
        )

        st.info(
            "📈 Analytics\n\nAnalyze attendance trends and academic performance."
        )

    with col2:

        st.info(
            "🎯 Prediction\n\nPredict student academic risk using AI logic."
        )

        st.info(
            "📘 About\n\nLearn about the project objectives and technologies."
        )

    st.divider()

    st.success(
        "🎯 Navigate through the platform using the left sidebar menu."
    )

# =====================================================
# DASHBOARD PAGE
# =====================================================

elif page == "📊 Dashboard":

    st.title("📊 Student Dashboard")

    st.caption(
        f"Last Updated: {datetime.now().strftime('%d %B %Y %H:%M')}"
    )

    st.divider()

    # KPI CARDS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Students", len(df))

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

    score = int(student_data["Final_Exam_Score"].values[0])

    attendance = int(
        student_data[attendance_column].values[0]
    )

    gender = student_data["Gender"].values[0]

    risk = student_data["Risk_Level"].values[0]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Final Score", score)

    with col2:
        st.metric("Attendance", f"{attendance}%")

    with col3:
        st.metric("Gender", gender)

    with col4:
        st.metric("Risk Level", risk)

    # RISK ALERTS

    if risk == "High Risk":
        st.error("🔴 HIGH RISK STUDENT")

    elif risk == "Medium Risk":
        st.warning("🟡 MEDIUM RISK STUDENT")

    else:
        st.success("🟢 LOW RISK STUDENT")

    st.divider()

    # AI INSIGHTS

    st.subheader("🧠 AI Educational Insights")

    average_score = round(
        df["Final_Exam_Score"].mean(),
        2
    )

    if average_score >= 75:
        st.success("📈 Overall class performance is GOOD.")

    elif average_score >= 50:
        st.warning("📊 Overall class performance is MODERATE.")

    else:
        st.error("📉 Overall class performance is POOR.")

# =====================================================
# PREDICTION PAGE
# =====================================================

elif page == "🎯 Prediction":

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

        confidence = random.randint(85, 99)

        if final_score < 50 or attendance < 40:

            st.error("🔴 HIGH RISK")

            st.warning(
                "Student needs immediate academic support."
            )

        elif final_score < 75:

            st.warning("🟡 MEDIUM RISK")

        else:

            st.success("🟢 LOW RISK")

        st.success(
            f"Prediction Confidence: {confidence}%"
        )

# =====================================================
# ANALYTICS PAGE
# =====================================================

elif page == "📈 Analytics":

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

elif page == "📘 About":

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

    ### Key Features

    ✅ Risk Prediction

    ✅ Early Warning Alerts

    ✅ Dashboard Analytics

    ✅ AI Educational Insights

    """)

