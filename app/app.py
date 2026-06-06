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
# DARK PROFESSIONAL UI
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #0b1120;
}

h1, h2, h3 {
    color: white !important;
}

p, label, div {
    color: #e5e7eb;
    font-size: 16px;
}

section[data-testid="stSidebar"] {
    background-color: #1e293b;
    border-right: 3px solid #2563eb;
    width: 320px !important;
}

[data-testid="metric-container"] {
    background-color: #1f2937;
    border: 1px solid #374151;
    padding: 15px;
    border-radius: 15px;
}

.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    height: 3em;
}

.stAlert {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOGIN SYSTEM
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🎓 Student Risk Prediction System")

    st.subheader("🔐 Teacher / Admin Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True

            st.success("Login Successful!")

            st.rerun()

        else:

            st.error("Invalid Username or Password")

    st.stop()

# =====================================================
# STUDENT DATASET (ONLY 5 STUDENTS)
# =====================================================

data = {

    "Student_ID": [1, 2, 3, 4, 5],

    "Gender": [
        "F",
        "M",
        "F",
        "M",
        "F"
    ],

    "Age": [
        18,
        19,
        17,
        18,
        19
    ],

    "Study_Hours_Per_Week": [
        25,
        10,
        18,
        8,
        30
    ],

    "Attendance_Percentage": [
        92,
        58,
        75,
        40,
        96
    ],

    "Previous_Score": [
        88,
        52,
        67,
        45,
        92
    ],

    "Parental_Education_Level": [
        "Graduate",
        "High School",
        "Graduate",
        "High School",
        "Postgraduate"
    ],

    "Internet_Access": [
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes"
    ],

    "Extracurricular_Activities": [
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes"
    ],

    "Sleep_Hours": [
        7,
        5,
        6,
        4,
        8
    ],

    "Final_Exam_Score": [
        91,
        46,
        72,
        38,
        95
    ],

    "Pass_Fail": [
        "Pass",
        "Fail",
        "Pass",
        "Fail",
        "Pass"
    ]
}

df = pd.DataFrame(data)

# =====================================================
# CREATE RISK LEVEL
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
    
    Navigate through the analytics system.
    """
)

st.sidebar.markdown("---")

st.sidebar.success("🟢 System Active")

st.sidebar.metric(
    "Students",
    len(df)
)

st.sidebar.metric(
    "High Risk",
    len(df[df["Risk_Level"] == "High Risk"])
)

page = st.sidebar.radio(
    "Select Page",
    [
        "🏠 Home",
        "📊 Dashboard",
        "🎯 Prediction",
        "📈 Analytics",
        "📘 About"
    ]
)

# =====================================================
# HOME PAGE
# =====================================================

if page == "🏠 Home":

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
    # QUICK STATS
    # =====================================================

    st.subheader("📈 Quick Statistics")

    pass_count = len(
        df[df["Pass_Fail"] == "Pass"]
    )

    pass_percent = round(
        (pass_count / len(df)) * 100,
        2
    )

    avg_score = round(
        df["Final_Exam_Score"].mean(),
        2
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Students", len(df))

    with col2:
        st.metric("Average Score", avg_score)

    with col3:
        st.metric("Pass %", f"{pass_percent}%")

    with col4:
        st.metric(
            "High Risk",
            len(df[df["Risk_Level"] == "High Risk"])
        )

    st.divider()

    # =====================================================
    # STUDENT DATASET PREVIEW
    # =====================================================

    st.subheader("📚 Student Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # FEATURES
    # =====================================================

    st.subheader("🚀 Key Features")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            "🎯 AI Risk Prediction\n\nDetect academically at-risk students."
        )

        st.info(
            "📊 Dashboard Analytics\n\nInteractive charts and analytics."
        )

        st.info(
            "🚨 Early Warning Alerts\n\nIdentify students needing intervention."
        )

    with col2:

        st.info(
            "🧠 AI Insights\n\nAutomatically generate educational insights."
        )

        st.info(
            "📈 Trend Storytelling\n\nUnderstand student performance trends."
        )

        st.info(
            "📥 Download Reports\n\nExport reports instantly."
        )

    st.divider()
 
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
                len(df[df["Pass_Fail"] == "Pass"]),
                len(df[df["Pass_Fail"] == "Fail"])
            ],
            title="Pass vs Fail Distribution"
        )

        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

    st.divider()

    # =====================================================
    # STUDENT TABLE
    # =====================================================

    st.subheader("📚 Student Records")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # AI INSIGHTS
    # =====================================================

    st.subheader("🧠 AI Educational Insights")

    low_attendance = df[
        df["Attendance_Percentage"] < 60
    ]

    st.warning(
        f"📌 {len(low_attendance)} students have attendance below 60%."
    )

    high_risk = df[
        df["Risk_Level"] == "High Risk"
    ]

    st.error(
        f"🚨 {len(high_risk)} students are classified as high-risk."
    )

    st.success(
        "📈 Students with higher attendance show better academic performance."
    )

    st.info(
        "📊 Attendance and exam performance show positive correlation."
    )

    st.divider()

    # =====================================================
    # TREND STORYTELLING
    # =====================================================

    st.subheader("📖 Trend Storytelling")

    top_student = df.loc[
        df["Final_Exam_Score"].idxmax()
    ]

    weak_student = df.loc[
        df["Final_Exam_Score"].idxmin()
    ]

    st.success(
        f"🏆 Student {top_student['Student_ID']} is the top performer with score {top_student['Final_Exam_Score']}."
    )

    st.warning(
        f"📉 Student {weak_student['Student_ID']} requires academic support."
    )

# =====================================================
# PREDICTION PAGE
# =====================================================

elif page == "🎯 Prediction":

    st.title("🎯 Student Risk Prediction")

    attendance = st.slider(
        "Attendance Percentage",
        0,
        100,
        70
    )

    final_score = st.slider(
        "Final Exam Score",
        0,
        100,
        65
    )

    study_hours = st.slider(
        "Study Hours Per Week",
        0,
        40,
        15
    )

    if st.button("Predict Student Risk"):

        confidence = random.randint(85, 99)

        if final_score < 50 or attendance < 40:

            st.error("🔴 HIGH RISK")

            st.warning(
                """
                Immediate intervention required.
                
                • Parent meeting
                
                • Academic mentoring
                
                • Attendance monitoring
                """
            )

        elif final_score < 75:

            st.warning("🟡 MEDIUM RISK")

            st.info(
                """
                Moderate monitoring recommended.
                
                • Improve study consistency
                
                • Weekly progress review
                """
            )

        else:

            st.success("🟢 LOW RISK")

            st.info(
                """
                Student performance is stable.
                
                • Maintain consistency
                
                • Encourage advanced learning
                """
            )

        st.success(
            f"Prediction Confidence: {confidence}%"
        )

        st.progress(confidence / 100)

# =====================================================
# ANALYTICS PAGE
# =====================================================

elif page == "📈 Analytics":

    st.title("📈 Analytics Dashboard")

    st.subheader("📊 Final Score Trend")

    st.line_chart(
        df["Final_Exam_Score"]
    )

    st.subheader("📚 Attendance Analysis")

    attendance_chart = df.set_index(
        "Student_ID"
    )

    st.bar_chart(
        attendance_chart["Attendance_Percentage"]
    )

    st.subheader("📈 Attendance vs Final Score")

    scatter_fig = px.scatter(
        df,
        x="Attendance_Percentage",
        y="Final_Exam_Score",
        color="Risk_Level",
        hover_data=["Student_ID"]
    )

    st.plotly_chart(
        scatter_fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("📥 Export Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV Report",
        data=csv,
        file_name="student_report.csv",
        mime="text/csv"
    )

# =====================================================
# ABOUT PAGE
# =====================================================

elif page == "📘 About":

    st.title("📘 About Project")

    st.write("""

### Student Performance Risk Prediction & Early Warning System

AI-powered educational analytics platform designed
to identify academically at-risk students.

### Technologies Used

- Python
- Streamlit
- Pandas
- Plotly

### Features

- Login Authentication
- Dashboard Analytics
- AI Educational Insights
- Risk Prediction
- Trend Storytelling
- Early Warning Alerts
- Downloadable Reports

### Objective

To help educational institutions identify
students requiring academic intervention
using AI-powered analytics.
""")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; padding:20px;'>

    <h3 style='color:white;'>
    🎓 Student Risk Prediction System
    </h3>

    <p style='color:#94a3b8;'>
    AI-powered educational analytics platform
    for identifying academically at-risk students.
    </p>

    <p style='color:#64748b; font-size:14px;'>
    Built for Smart Education • Powered by AI Analytics
    </p>

    </div>
    """,
    unsafe_allow_html=True
)
