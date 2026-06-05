import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("data/processed_data.csv")

# Page Title
st.set_page_config(page_title="Student Risk Prediction System", layout="wide")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Choose Section",
    ["Dashboard", "Prediction", "Analytics", "About Project"]
)

# =========================
# DASHBOARD PAGE
# =========================
if page == "Dashboard":

    st.title("🎓 Student Performance Risk Prediction & Early Warning System")

    st.write("AI-powered system to identify academically at-risk students.")

    # KPI Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Students", len(df))

    with col2:
        st.metric(
            "Average Score",
            round(df["Final_Exam_Score"].mean(), 2)
        )

    with col3:

        if "Risk_Level" in df.columns:
            high_risk_count = len(
                df[df["Risk_Level"] == "High Risk"]
            )
        else:
            high_risk_count = 0

        st.metric("High Risk Students", high_risk_count)

    # =========================
    # STUDENT SEARCH SYSTEM
    # =========================

    st.subheader("🔍 Student Search System")

    selected_student = st.selectbox(
        "Select Student ID",
        df["Student_ID"]
    )

    student_data = df[df["Student_ID"] == selected_student]

    st.write("### Student Details")

    st.dataframe(student_data)

    ```python
# Safe Performance Insights

if "Assignment_Score" in df.columns:
    st.write(
        "📌 Assignment Score:",
        int(student_data["Assignment_Score"].values[0])
    )

if "Midterm_Score" in df.columns:
    st.write(
        "📌 Midterm Score:",
        int(student_data["Midterm_Score"].values[0])
    )

if "Attendance (%)" in df.columns:
    st.write(
        "📌 Attendance:",
        int(student_data["Attendance (%)"].values[0])
    )
```


    # Dataset Preview
    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head())

# =========================
# PREDICTION PAGE
# =========================
elif page == "Prediction":

    st.title("🎯 Student Risk Prediction")

    attendance = st.slider("Attendance (%)", 0, 100, 75)

    study_hours = st.slider("Study Hours Per Day", 0, 15, 5)

    assignment_score = st.slider("Assignment Score", 0, 100, 60)

    midterm_score = st.slider("Midterm Score", 0, 100, 60)

    final_exam_score = st.slider("Final Exam Score", 0, 100, 60)

    # Prediction Button
    if st.button("Predict Risk"):

        st.subheader("Prediction Result")

        # HIGH RISK
        if final_exam_score < 50 or attendance < 40:

            st.error("⚠ EARLY WARNING ALERT: Student is at HIGH academic risk!")

            st.subheader("📌 Personalized Recommendations")

            st.write("• Attend remedial coaching classes")
            st.write("• Increase study hours daily")
            st.write("• Schedule weekly mentor meetings")
            st.write("• Improve attendance consistency")
            st.write("• Complete pending assignments")

        # MEDIUM RISK
        elif final_exam_score < 75:

            st.warning("⚠ Student is at MEDIUM risk and needs monitoring.")

            st.subheader("📌 Personalized Recommendations")

            st.write("• Revise difficult subjects regularly")
            st.write("• Practice mock tests")
            st.write("• Improve classroom participation")
            st.write("• Increase assignment submission rate")

        # LOW RISK
        else:

            st.success("✅ Student performance is stable.")

            st.subheader("📌 Personalized Recommendations")

            st.write("• Maintain current performance")
            st.write("• Participate in advanced learning activities")
            st.write("• Help peers in collaborative learning")

# =========================
# ANALYTICS PAGE
# =========================
elif page == "Analytics":

    st.title("📊 Student Analytics Dashboard")

    st.write("Interactive charts and educational insights")

    # Final Exam Score Chart
    st.subheader("📌 Final Exam Score Distribution")
    st.bar_chart(df["Final_Exam_Score"])

    # Assignment Score Chart
    st.subheader("📌 Assignment Score Analysis")
    st.line_chart(df["Assignment_Score"])

    # Midterm Score Chart
    st.subheader("📌 Midterm Score Analysis")
    st.area_chart(df["Midterm_Score"])

    # Attendance Chart
    st.subheader("📌 Attendance Analysis")
    st.bar_chart(df["Attendance (%)"])

    # Pass vs Fail Chart
    st.subheader("📌 Pass vs Fail Analysis")
    st.bar_chart(df["Pass_Fail"].value_counts())


# =========================
# STUDENT SEARCH SYSTEM
# =========================

st.subheader("🔍 Student Search System")

selected_student = st.selectbox(
    "Select Student ID",
    df["Student_ID"]
)

student_data = df[df["Student_ID"] == selected_student]

st.write("### Student Details")

st.dataframe(student_data)

# Performance Insights
st.write("### Performance Insights")

st.write(
    "📌 Final Exam Score:",
    int(student_data["Final_Exam_Score"].values[0])
)

st.write(
    "📌 Assignment Score:",
    int(student_data["Assignment_Score"].values[0])
)

st.write(
    "📌 Midterm Score:",
    int(student_data["Midterm_Score"].values[0])
)

st.write(
    "📌 Attendance:",
    int(student_data["Attendance (%)"].values[0])
)

st.write(
    "📌 Pass/Fail Status:",
    student_data["Pass_Fail"].values[0]
)
  
# Dataset Preview
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())



