import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Student Risk Prediction System",
    page_icon="🎓",
    layout="wide"
)

# =====================================================
# REMOVE STREAMLIT DEFAULT UI
# =====================================================

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# =====================================================
# PROFESSIONAL LIGHT THEME CSS
# =====================================================

st.markdown("""
<style>

/* =====================================================
MAIN BACKGROUND
===================================================== */

.stApp {

    background-color: #f5f7fa;

    font-family: 'Segoe UI', sans-serif;
}

/* =====================================================
HEADINGS
===================================================== */

h1 {

    color: #0f172a !important;

    font-size: 42px !important;

    font-weight: 800 !important;
}

h2 {

    color: #1e293b !important;

    font-weight: 700 !important;
}

h3 {

    color: #334155 !important;

    font-weight: 700 !important;
}

/* =====================================================
TEXT
===================================================== */

p {
    color: #374151;
}

label {
    color: #111827 !important;
}

/* =====================================================
SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {

    background-color: #ffffff;

    border-right: 1px solid #e5e7eb;
}

/* Sidebar text */

section[data-testid="stSidebar"] * {

    color: #111827 !important;
}

/* =====================================================
METRIC CARDS
===================================================== */

[data-testid="metric-container"] {

    background-color: white;

    border-radius: 18px;

    padding: 18px;

    border: 1px solid #e5e7eb;

    box-shadow:
        0px 4px 12px rgba(0,0,0,0.05);
}

/* =====================================================
BUTTONS
===================================================== */

.stButton > button {

    background-color: #2563eb;

    color: white;

    border-radius: 12px;

    border: none;

    height: 3.2em;

    width: 100%;

    font-size: 16px;

    font-weight: 600;
}

/* Hover */

.stButton > button:hover {

    background-color: #1d4ed8;

    color: white;
}

/* =====================================================
DOWNLOAD BUTTON
===================================================== */

.stDownloadButton > button {

    background-color: #16a34a;

    color: white;

    border-radius: 12px;

    border: none;

    height: 3.2em;

    width: 100%;

    font-size: 16px;

    font-weight: 600;
}

/* =====================================================
SUCCESS / WARNING / ERROR
===================================================== */

.stSuccess {

    border-radius: 14px;
}

.stWarning {

    border-radius: 14px;
}

.stError {

    border-radius: 14px;
}

/* =====================================================
DATAFRAME
===================================================== */

[data-testid="stDataFrame"] {

    border-radius: 14px;

    overflow: hidden;

    border: 1px solid #e5e7eb;
}

/* =====================================================
ALERT BOX
===================================================== */

.alert-box {

    padding: 15px;

    border-radius: 12px;

    background-color: #fff1f2;

    border-left: 6px solid #ef4444;

    margin-bottom: 10px;
}

/* =====================================================
RECOMMENDATION BOX
===================================================== */

.recommend-box {

    background-color: #eff6ff;

    padding: 15px;

    border-radius: 12px;

    border-left: 5px solid #2563eb;
}

/* =====================================================
FOOTER
===================================================== */

.footer {

    text-align: center;

    color: gray;

    padding: 20px;

    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/processed_data.csv")

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
        "AI-powered dashboard for monitoring student academic performance and risk levels."
    )

    st.write(
        """
        Educational analytics platform designed to identify
        academically at-risk students and provide early intervention.
        """
    )

    st.divider()

    # KPI CARDS

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

    # SEARCH + ALERTS

    col1, col2 = st.columns([2, 1])

    with col1:

        st.subheader("🔍 Student Search & Details")

        selected_student = st.selectbox(
            "Select Student ID",
            df["Student_ID"],
            key="student_select"
        )

        student_data = df[
            df["Student_ID"] == selected_student
        ]

        st.dataframe(student_data)

        csv = student_data.to_csv(index=False).encode("utf-8")

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

            for index, row in risk_students.iterrows():

                st.markdown(f"""
                <div class="alert-box">
                ⚠ <b>Student {row['Student_ID']}</b>
                is academically at HIGH RISK.
                </div>
                """, unsafe_allow_html=True)

        else:

            st.success(
                "✅ No high-risk students detected."
            )

    st.divider()

    # CHARTS

    st.subheader("📈 Performance Overview")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### Final Exam Score Distribution")

        st.bar_chart(df["Final_Exam_Score"])

    with col2:

        st.write("### Pass vs Fail Analysis")

        st.bar_chart(
            df["Pass_Fail"].value_counts()
        )

    st.divider()

    # TOP & LOW PERFORMERS

    st.subheader("🏆 Student Performance")

    col1, col2 = st.columns(2)

    with col1:

        st.success("🏅 Top Performing Students")

        top_students = df.sort_values(
            by="Final_Exam_Score",
            ascending=False
        ).head(5)

        st.dataframe(top_students)

    with col2:

        st.error("⚠ Students Needing Attention")

        low_students = df.sort_values(
            by="Final_Exam_Score"
        ).head(5)

        st.dataframe(low_students)

    st.divider()

    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head())

# =====================================================
# PREDICTION PAGE
# =====================================================

elif page == "Prediction":

    st.title("🎯 Student Risk Prediction")

    st.write(
        """
        Predict student academic risk level using educational indicators.
        """
    )

    st.divider()

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

    st.divider()

    if st.button("Predict Risk"):

        st.subheader("📊 Prediction Result")

        if final_exam_score < 50 or attendance < 40:

            st.error("🔴 HIGH RISK")

            st.markdown("""
            <div class="recommend-box">

            <h4>📌 Recommendations</h4>

            • Attend remedial coaching classes<br>
            • Increase study hours daily<br>
            • Improve attendance consistency<br>
            • Meet academic mentors weekly

            </div>
            """, unsafe_allow_html=True)

        elif final_exam_score < 75:

            st.warning("🟡 MEDIUM RISK")

            st.markdown("""
            <div class="recommend-box">

            <h4>📌 Recommendations</h4>

            • Practice mock tests<br>
            • Improve revision strategy<br>
            • Increase assignment completion

            </div>
            """, unsafe_allow_html=True)

        else:

            st.success("🟢 LOW RISK")

            st.markdown("""
            <div class="recommend-box">

            <h4>📌 Recommendations</h4>

            • Maintain current performance<br>
            • Continue consistent study habits

            </div>
            """, unsafe_allow_html=True)

# =====================================================
# ANALYTICS PAGE
# =====================================================

elif page == "Analytics":

    st.title("📊 Advanced Analytics Dashboard")

    st.subheader("📈 Final Exam Score Trend")

    st.line_chart(df["Final_Exam_Score"])

    st.subheader("📊 Attendance Analytics")

    if "Attendance (%)" in df.columns:

        st.area_chart(df["Attendance (%)"])

    st.subheader("📄 Dataset")

    st.dataframe(df)

# =====================================================
# ABOUT PAGE
# =====================================================

elif page == "About Project":

    st.title("📘 About Project")

    st.write("""

    ## Student Performance Risk Prediction & Early Warning System

    This project helps educational institutions identify
    academically at-risk students using AI and analytics.

    ### Features

    ✅ Student Risk Prediction

    ✅ Early Warning Alerts

    ✅ Educational Analytics Dashboard

    ✅ Interactive Visualizations

    ✅ Personalized Recommendations

    ✅ Downloadable Student Reports

    ### Technologies Used

    • Python

    • Streamlit

    • Pandas

    • Data Analytics

    • Machine Learning

    """)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">

🎓 Student Performance Risk Prediction & Early Warning System

<br><br>

Built with Streamlit | Python | Machine Learning

</div>
""", unsafe_allow_html=True)

