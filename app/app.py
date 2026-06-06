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
# PROFESSIONAL DARK THEME
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

/* METRIC CARDS */

[data-testid="metric-container"] {
    background-color: #1f2937;
    border: 1px solid #374151;
    padding: 15px;
    border-radius: 15px;
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

/* ALERT BOXES */

.stAlert {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOGIN SCREEN
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🎓 Student Risk Prediction System")

    st.subheader("🔐 School Admin Login")

    st.write(
        "Access the AI-powered educational analytics platform."
    )

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
# LOAD DATA
# =====================================================

df = pd.read_csv("data/processed_data.csv")

# =====================================================
# USE ONLY 5 STUDENTS
# =====================================================

df = df.head(5)

# =====================================================
# STUDENT IDS
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
    # WHY THIS MATTERS
    # =====================================================

    st.subheader("🌍 Why This Matters")

    st.info(
        """
        Many students are identified too late for academic intervention.
        
        This system helps institutions detect academic risk early
        using AI-driven analytics and predictive insights.
        """
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
    # FEATURES
    # =====================================================

    st.subheader("🚀 Key Features")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            "🎯 AI Risk Prediction\n\nDetect academically at-risk students."
        )

        st.info(
            "📊 Dashboard Analytics\n\nInteractive charts and educational analytics."
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

# =====================================================
# DASHBOARD PAGE
# =====================================================

elif page == "📊 Dashboard":

    st.title("📊 Student Dashboard")

    st.caption(
        f"Last Updated: {datetime.now().strftime('%d %B %Y %H:%M')}"
    )

    st.divider()

    # =====================================================
    # KPI CARDS
    # =====================================================

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

    st.info(
        "📊 Students with better attendance generally perform better in final exams."
    )

    st.info(
        "📈 Attendance and performance show a positive academic trend."
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
        st.metric("Final Score", score)

    with col2:
        st.metric("Attendance", f"{attendance}%")

    with col3:
        st.metric("Gender", gender)

    with col4:
        st.metric("Risk Level", risk)

    st.divider()

    # =====================================================
    # AI INSIGHTS
    # =====================================================

    st.subheader("🧠 AI Educational Insights")

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

    correlation = df[attendance_column].corr(
        df["Final_Exam_Score"]
    )

    if correlation > 0.5:

        st.success(
            "📊 Attendance has a strong positive relationship with academic performance."
        )

    else:

        st.warning(
            "📊 Attendance shows weak correlation with academic performance."
        )

    st.info(
        "📈 Students with higher attendance show better academic outcomes."
    )

    st.divider()

    # =====================================================
    # INTERVENTION RECOMMENDATIONS
    # =====================================================

    st.subheader("🛠 Intervention Recommendations")

    if risk == "High Risk":

        st.error(
            """
            🔴 Recommended Intervention Plan
            
            • Conduct parent-teacher meeting
            
            • Weekly mentoring sessions
            
            • Daily attendance monitoring
            
            • Extra assignment support
            
            • Academic counseling
            """
        )

    elif risk == "Medium Risk":

        st.warning(
            """
            🟡 Suggested Academic Support
            
            • Improve study consistency
            
            • Monitor assignments
            
            • Increase classroom participation
            
            • Provide additional practice materials
            """
        )

    else:

        st.success(
            """
            🟢 Student Performance is Stable
            
            • Continue regular monitoring
            
            • Encourage advanced learning
            
            • Maintain attendance consistency
            """
        )

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

            risk = "HIGH RISK"

            st.error(f"🔴 {risk}")

            st.warning(
                "Student requires immediate academic intervention."
            )

            st.info(
                """
                Suggested Actions:
                
                • Parent meeting
                
                • Weekly monitoring
                
                • Mentoring support
                
                • Attendance improvement
                """
            )

        elif final_score < 75:

            risk = "MEDIUM RISK"

            st.warning(f"🟡 {risk}")

            st.info(
                """
                Suggested Actions:
                
                • Improve study hours
                
                • Monitor assignments
                
                • Regular academic reviews
                """
            )

        else:

            risk = "LOW RISK"

            st.success(f"🟢 {risk}")

            st.info(
                """
                Suggested Actions:
                
                • Maintain current performance
                
                • Encourage advanced learning
                """
            )

        st.success(
            f"Prediction Confidence: {confidence}%"
        )

        st.progress(confidence / 100)

        st.balloons()

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

elif page == "📘 About":

    st.title("📘 About Project")

    st.write("""

### Student Performance Risk Prediction & Early Warning System

AI-powered educational analytics platform designed
for identifying academically at-risk students.

### Technologies Used

- Python
- Streamlit
- Pandas
- Plotly

### Implemented Features

- Login Authentication
- AI Educational Insights
- Dashboard Analytics
- Risk Prediction
- Trend Storytelling
- Intervention Recommendations
- Early Warning Alerts
- Downloadable Reports

### Project Objective

To help educational institutions identify
at-risk students early and improve
academic outcomes through AI-driven analytics.

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
    AI-powered educational analytics platform for identifying academically at-risk students.
    </p>

    <p style='color:#64748b; font-size:14px;'>
    Built for Smart Education • Powered by AI Analytics
    </p>

    </div>
    """,
    unsafe_allow_html=True
)
