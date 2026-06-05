import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Student Analytics System",
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
# PROFESSIONAL DASHBOARD CSS
# =====================================================

st.markdown("""
<style>

/* =====================================================
MAIN BACKGROUND
===================================================== */

.stApp {
    background-color: #eef2f7;
    color: #1f2937;
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
    color: #1e3a8a !important;
    font-weight: 700 !important;
}

h3 {
    color: #2563eb !important;
    font-weight: 700 !important;
}

/* =====================================================
TEXT
===================================================== */

p, label, div {
    color: #1f2937;
}

/* =====================================================
SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0f172a,
        #1e3a8a
    );
}

/* Sidebar text */

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* =====================================================
METRIC CARDS
===================================================== */

[data-testid="metric-container"] {

    background-color: white;

    border-radius: 18px;

    padding: 18px;

    border: 1px solid #dbe4f0;

    box-shadow:
        0px 4px 12px rgba(0,0,0,0.06);
}

/* =====================================================
BUTTONS
===================================================== */

.stButton > button {

    background: linear-gradient(
        to right,
        #2563eb,
        #1d4ed8
    );

    color: white;

    border-radius: 12px;

    border: none;

    height: 3.2em;

    width: 100%;

    font-size: 16px;

    font-weight: 600;
}

/* Button hover */

.stButton > button:hover {

    background: linear-gradient(
        to right,
        #1d4ed8,
        #1e40af
    );

    color: white;
}

/* =====================================================
DOWNLOAD BUTTON
===================================================== */

.stDownloadButton > button {

    background: linear-gradient(
        to right,
        #15803d,
        #16a34a
    );

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

    background-color: #dcfce7 !important;

    border-radius: 14px;
}

.stWarning {

    background-color: #fef3c7 !important;

    border-radius: 14px;
}

.stError {

    background-color: #fee2e2 !important;

    border-radius: 14px;
}

/* =====================================================
DATAFRAME
===================================================== */

[data-testid="stDataFrame"] {

    border-radius: 14px;

    overflow: hidden;

    border: 1px solid #dbe4f0;
}

/* =====================================================
DIVIDER
===================================================== */

hr {
    border: 1px solid #dbe4f0;
}

/* =====================================================
ALERT BOX
===================================================== */

.alert-box {

    padding: 15px;

    border-radius: 12px;

    background-color: #fff4f4;

    border-left: 6px solid red;

    margin-bottom: 10px;

    box-shadow:
        0px 2px 8px rgba(0,0,0,0.05);
}

/* =====================================================
RECOMMENDATION BOX
===================================================== */

.recommend-box {

    background-color: #eef7ff;

    padding: 15px;

    border-radius: 12px;

    border-left: 5px solid #1976d2;
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

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
    width=120
)

st.sidebar.markdown("## 🎓 Student Analytics System")

st.sidebar.success(
    "AI-Powered Academic Monitoring Platform"
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
# DASHBOARD PAGE
# =====================================================

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

    # STUDENT SEARCH

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
                <br><br>
                Immediate academic intervention recommended.
                </div>
                """, unsafe_allow_html=True)

        else:

            st.success(
                "✅ No high-risk students detected."
            )

    st.divider()

    # PERFORMANCE CHARTS

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

    st.subheader("🏆 Top & Low Performing Students")

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

    # DATASET PREVIEW

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
            • Weekly mentor monitoring<br>
            • Submit pending assignments
            </div>
            """, unsafe_allow_html=True)

        elif final_exam_score < 75:

            st.warning("🟡 MEDIUM RISK")

            st.markdown("""
            <div class="recommend-box">
            <h4>📌 Recommendations</h4>

            • Practice mock tests<br>
            • Improve subject revision<br>
            • Increase classroom participation<br>
            • Strengthen assignment performance
            </div>
            """, unsafe_allow_html=True)

        else:

            st.success("🟢 LOW RISK")

            st.markdown("""
            <div class="recommend-box">
            <h4>📌 Recommendations</h4>

            • Maintain current performance<br>
            • Participate in advanced learning<br>
            • Continue consistent study habits
            </div>
            """, unsafe_allow_html=True)

# =====================================================
# ANALYTICS PAGE
# =====================================================

elif page == "Analytics":

    st.title("📊 Advanced Student Analytics Dashboard")

    st.write(
        """
        Interactive educational analytics and institutional insights.
        """
    )

    st.divider()

    st.subheader("📈 Student Performance Analytics")

    st.line_chart(df["Final_Exam_Score"])

    st.subheader("📊 Attendance Analytics")

    if "Attendance (%)" in df.columns:

        st.area_chart(df["Attendance (%)"])

    st.subheader("📌 Dataset Preview")

    st.dataframe(df)

# =====================================================
# ABOUT PAGE
# =====================================================

elif page == "About Project":

    st.title("📘 About Project")

    st.write("""
    ## Student Performance Risk Prediction & Early Warning System

    This AI-powered educational analytics platform helps schools
    and colleges identify academically at-risk students.

    ### Features

    ✅ Student Risk Prediction

    ✅ Early Warning Alerts

    ✅ Interactive Dashboard

    ✅ Analytics & Visualizations

    ✅ Personalized Recommendations

    ✅ Student Monitoring System

    ✅ Downloadable Reports

    ### Technologies Used

    • Python

    • Streamlit

    • Pandas

    • Machine Learning

    • Educational Data Analytics
    """)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">
🎓 Student Performance Risk Prediction & Early Warning System <br>
Built with Streamlit | Python | Machine Learning | Data Analytics
</div>
""", unsafe_allow_html=True)
