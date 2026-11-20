    left, right = st.columns(2)
    with left:
        st.bar_chart(df.set_index("Student_ID")["Final_Exam_Score"])
    with right:
        pass_fail_chart = px.pie(
            names=["Pass", "Fail"],
            values=[int((df["Pass_Fail"] == "Pass").sum()), int((df["Pass_Fail"] == "Fail").sum())],
            title="Pass vs Fail Distribution",
            hole=0.45,
        )
        st.plotly_chart(pass_fail_chart, use_container_width=True)
    st.divider()
    st.subheader("📚 Student Records")
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.divider()
    st.subheader("🧠 Academic Insights")
    low_attendance = df[df["Attendance_Percentage"] < 60]
    high_risk = df[df["Risk_Level"] == "High Risk"]
    st.warning(f"{len(low_attendance)} students have attendance below 60%.")
    st.error(f"{len(high_risk)} students are classified as High Risk.")
    st.info("Attendance and academic performance should be monitored regularly for early identification.")
    top_student = df.loc[df["Final_Exam_Score"].idxmax()]
    weak_student = df.loc[df["Final_Exam_Score"].idxmin()]
    st.success(f"🏆 Top Performer: Student {int(top_student['Student_ID'])} with score {int(top_student['Final_Exam_Score'])}.")
    st.warning(f"📉 Student {int(weak_student['Student_ID'])} requires academic support.")

# ==========================================================
# PREDICTION
# ==========================================================
elif page == "🎯 Prediction":
    st.title("🎯 Student Risk Prediction")
    st.write("Enter academic details to assess the student's risk level.")
    left, right = st.columns(2)
    with left:
        attendance = st.slider("Attendance Percentage", 0, 100, 70)
        final_score = st.slider("Final Exam Score", 0, 100, 65)
    with right:
        study_hours = st.slider("Study Hours Per Week", 0, 40, 15)
    if st.button("🔍 Predict Student Risk", use_container_width=True):
        if final_score < 50 or attendance < 40:
            risk = "High Risk"
        elif final_score < 75 or attendance < 60:
            risk = "Medium Risk"
        else:
            risk = "Low Risk"
        st.divider()
        if risk == "High Risk":
            st.error("🔴 HIGH RISK")
            st.warning("Recommended interventions: academic mentoring, attendance monitoring, counseling, and remedial classes.")
        elif risk == "Medium Risk":
            st.warning("🟡 MEDIUM RISK")
            st.info("Recommended actions: improve study consistency, monitor attendance, weekly progress review, and additional practice.")
        else:
            st.success("🟢 LOW RISK")
            st.info("Student performance appears stable. Maintain study consistency, continue regular attendance, and encourage advanced learning.")
        st.metric("Predicted Risk Category", risk)
        st.caption("Risk is assessed using predefined rules, not a trained machine-learning model.")

# ==========================================================
# ANALYTICS
# ==========================================================
elif page == "📈 Analytics":
    st.title("📈 Analytics Dashboard")
    st.subheader("Final Score Trend")
    st.line_chart(df["Final_Exam_Score"])
    st.subheader("Attendance Analysis")
    st.bar_chart(df.set_index("Student_ID")["Attendance_Percentage"])
    st.subheader("Attendance vs Final Exam Score")
    scatter_fig = px.scatter(
        df,
        x="Attendance_Percentage",
        y="Final_Exam_Score",
        color="Risk_Level",
        hover_data=["Student_ID"],
        size="Study_Hours_Per_Week",
        title="Attendance vs Performance",
    )
    st.plotly_chart(scatter_fig, use_container_width=True)
    st.divider()
    st.subheader("📥 Export Report")
    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download Student CSV Report", data=csv_data, file_name="student_risk_report.csv", mime="text/csv")

# ==========================================================
# ABOUT
# ==========================================================
elif page == "📘 About":
    st.title("📘 About Project")
    st.markdown("""\n    ## Student Performance Risk Prediction & Early Warning System

    An educational analytics application designed to identify academically at-risk students.

    ### Technologies Used
    - Python
    - Streamlit
    - Pandas
    - Plotly

    ### Features
    - Admin login
    - Student dashboard
    - Rule-based risk assessment
    - Academic analytics
    - Early warning identification
    - CSV report generation

    ### Objective
    To help educational institutions identify students who may require academic intervention using student data analysis and risk assessment.
    """)

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("---")
st.markdown("<div style='text-align:center;padding:20px'><h3>🎓 Student Risk Prediction System</h3><p>Academic Analytics • Student Monitoring • Early Warning</p></div>", unsafe_allow_html=True)
