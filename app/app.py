import streamlit as st
import pandas as pd

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
# SAFE DARK THEME
# =====================================================

st.markdown("""
<style>

/* APP BACKGROUND */

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

# CREATE STUDENT IDS 1 TO N

df["Student_ID"] = range(1, len(df) + 1)

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
# DASHBOARD
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
        Educational analytics platform for identifying
        academically at-risk students.
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
            "Total Students",
            len(df)
        )

    with col2:
        st.metric(
            "Average Score",
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
            "Pass %",
            f"{pass_percent}%"
        )

    with col4:

        high_risk = len(
            df[df["Final_Exam_Score"] < 50]
        )

        st.metric(
            "High Risk",
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

        st.bar_chart(
            df["Final_Exam_Score"]
        )

    with col2:

        st.write("### Pass vs Fail")

        st.bar_chart(
            df["Pass_Fail"].value_counts()
        )

    st.divider()

    # =====================================================
    # STUDENT SEARCH
    # =====================================================

    st.subheader("🔍 Student Details")

    selected_student = st.selectbox(
        "Select Student",
        df["Student_ID"]
    )

    student_data = df[
        df["Student_ID"] == selected_student
    ]

    st.dataframe(student_data)

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

        st.dataframe(risk_students)

    else:

        st.success(
            "No high-risk students detected"
        )

    st.divider()

    # =====================================================
    # TOP STUDENTS
    # =====================================================

    st.subheader("🏆 Top Performing Students")

    top_students = df.sort_values(
        by="Final_Exam_Score",
        ascending=False
    ).head(5)

    st.dataframe(top_students)

# =====================================================
# PREDICTION PAGE
# =====================================================

elif page == "Prediction":

    st.title("🎯 Risk Prediction")

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

    st.title("📊 Analytics")

    st.subheader("Final Score Trend")

    st.line_chart(
        df["Final_Exam_Score"]
    )

    st.subheader("Dataset Preview")

    st.dataframe(df)

# =====================================================
# ABOUT PAGE
# =====================================================

elif page == "About":

    st.title("📘 About Project")

    st.write("""

    ### Student Performance Risk Prediction & Early Warning System

    Features:

    ✅ Student Risk Prediction

    ✅ Dashboard Analytics

    ✅ Early Warning Alerts

    ✅ Interactive Charts

    ✅ Student Monitoring

    """)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
    "### 🎓 Built using Streamlit + Python"
)

