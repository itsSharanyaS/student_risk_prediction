import streamlit as st
import pandas as pd
import os

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Student Risk Prediction System",
    page_icon="🎓",
    layout="wide"
)

# =====================================================
# SAFE CSS
# =====================================================

st.markdown("""
<style>

/* MAIN APP */

.stApp {
    background-color: #0f172a;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* HEADINGS */

h1, h2, h3, h4 {
    color: white !important;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #020617;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* METRICS */

[data-testid="metric-container"] {
    background: #1e293b;
    border-radius: 15px;
    padding: 15px;
    border: 1px solid #334155;
}

/* BUTTONS */

.stButton > button {
    width: 100%;
    border-radius: 10px;
    background: #2563eb;
    color: white;
    border: none;
    height: 3em;
    font-weight: bold;
}

.stDownloadButton > button {
    width: 100%;
    border-radius: 10px;
    background: #16a34a;
    color: white;
    border: none;
    height: 3em;
    font-weight: bold;
}

/* ALERT BOX */

.alert-box {
    background-color: rgba(239,68,68,0.15);
    padding: 15px;
    border-left: 5px solid red;
    border-radius: 10px;
    margin-bottom: 10px;
}

/* RECOMMEND BOX */

.recommend-box {
    background-color: rgba(37,99,235,0.15);
    padding: 15px;
    border-left: 5px solid #2563eb;
    border-radius: 10px;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA SAFELY
# =====================================================

DATA_PATH = "data/processed_data.csv"

try:

    if not os.path.exists(DATA_PATH):

        st.error(f"""
        ❌ Dataset not found.

        Expected file location:
        {DATA_PATH}

        Make sure:
        1. data folder exists
        2. processed_data.csv exists
        3. file is uploaded to GitHub
        """)

        st.stop()

    df = pd.read_csv(DATA_PATH)

except Exception as e:

    st.error(f"❌ Error loading dataset: {e}")
    st.stop()

# =====================================================
# CHECK REQUIRED COLUMNS
# =====================================================

required_columns = [
    "Student_ID",
    "Final_Exam_Score",
    "Pass_Fail"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if len(missing_columns) > 0:

    st.error(f"""
    ❌ Missing columns in CSV:

    {missing_columns}

    Available columns:
    {list(df.columns)}
    """)

    st.stop()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🎓 Student Analytics")

st.sidebar.success(
    "AI-Powered Academic Monitoring"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Prediction",
        "Analytics",
        "About Project"
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
        "AI-powered dashboard for monitoring student academic performance."
    )

    st.write("""
    Educational analytics platform designed to identify
    academically at-risk students.
    """)

    st.divider()

    # =================================================
    # KPI CARDS
    # =================================================

    st.subheader("📊 Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

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

        pass_percent = round(
            (
                len(df[df["Pass_Fail"] == "Pass"])
                / len(df)
            ) * 100,
            2
        )

        st.metric(
            "Pass Percentage",
            f"{pass_percent}%"
        )

    with col4:

        high_risk = len(
            df[df["Final_Exam_Score"] < 50]
        )

        st.metric(
            "High Risk Students",
            high_risk
        )

    st.divider()

    # =================================================
    # STUDENT SEARCH
    # =================================================

    col1, col2 = st.columns([2,1])

    with col1:

        st.subheader("🔍 Student Search")

        selected_student = st.selectbox(
            "Select Student ID",
            df["Student_ID"].unique()
        )

        student_data = df[
            df["Student_ID"] == selected_student
        ]

        st.dataframe(
            student_data,
            use_container_width=True
        )

        csv = student_data.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "⬇ Download Report",
            data=csv,
            file_name="student_report.csv",
            mime="text/csv"
        )

    with col2:

        st.subheader("🚨 Early Warning Alerts")

        risk_students = df[
            df["Final_Exam_Score"] < 50
        ]

        if len(risk_students) > 0:

            for _, row in risk_students.head(5).iterrows():

                st.markdown(f"""
                <div class="alert-box">
                ⚠ <b>{row['Student_ID']}</b>
                is academically at HIGH RISK
                </div>
                """, unsafe_allow_html=True)

        else:

            st.success(
                "✅ No high-risk students"
            )

    st.divider()

    # =================================================
    # CHARTS
    # =================================================

    st.subheader("📈 Performance Analytics")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### Final Exam Scores")

        chart_data = df["Final_Exam_Score"]

        st.bar_chart(chart_data)

    with col2:

        st.write("### Pass vs Fail")

        pass_fail = df["Pass_Fail"].value_counts()

        st.bar_chart(pass_fail)

    st.divider()

    # =================================================
    # TOP / LOW STUDENTS
    # =================================================

    col1, col2 = st.columns(2)

    with col1:

        st.success("🏅 Top Students")

        top_students = df.sort_values(
            by="Final_Exam_Score",
            ascending=False
        ).head(5)

        st.dataframe(
            top_students,
            use_container_width=True
        )

    with col2:

        st.error("⚠ Students Needing Attention")

        low_students = df.sort_values(
            by="Final_Exam_Score"
        ).head(5)

        st.dataframe(
            low_students,
            use_container_width=True
        )

# =====================================================
# PREDICTION PAGE
# =====================================================

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
        70
    )

    midterm_score = st.slider(
        "Midterm Score",
        0,
        100,
        70
    )

    final_exam_score = st.slider(
        "Final Exam Score",
        0,
        100,
        70
    )

    if st.button("Predict Risk"):

        if final_exam_score < 50 or attendance < 40:

            st.error("🔴 HIGH RISK")

            st.markdown("""
            <div class="recommend-box">
            <h4>Recommendations</h4>

            • Attend remedial classes<br>
            • Increase study hours<br>
            • Improve attendance<br>
            • Meet mentors weekly

            </div>
            """, unsafe_allow_html=True)

        elif final_exam_score < 75:

            st.warning("🟡 MEDIUM RISK")

        else:

            st.success("🟢 LOW RISK")

# =====================================================
# ANALYTICS PAGE
# =====================================================

elif page == "Analytics":

    st.title("📊 Advanced Analytics")

    st.subheader("Final Exam Trend")

    st.line_chart(
        df["Final_Exam_Score"]
    )

    st.subheader("Pass vs Fail")

    st.bar_chart(
        df["Pass_Fail"].value_counts()
    )

    st.subheader("Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True
    )

# =====================================================
# ABOUT PAGE
# =====================================================

elif page == "About Project":

    st.title("📘 About Project")

    st.write("""

    ## Student Performance Risk Prediction & Early Warning System

    AI-powered educational analytics platform.

    ### Features

    ✅ Student Risk Prediction

    ✅ Interactive Dashboard

    ✅ Educational Analytics

    ✅ Downloadable Reports

    ### Technologies

    • Python

    • Streamlit

    • Pandas

    """)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">

🎓 Student Performance Risk Prediction & Early Warning System

<br><br>

Built with Streamlit + Python

</div>
""", unsafe_allow_html=True)
