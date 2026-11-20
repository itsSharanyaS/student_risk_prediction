            - Maintain study consistency
            - Continue regular attendance
            - Encourage advanced learning
            """)

        st.metric(
            "Predicted Risk Category",
            risk
        )

        st.caption(
            "Risk is assessed using predefined rules, "
            "not a trained machine learning model."
        )


# ==========================================================
# ANALYTICS
# ==========================================================
elif page == "📈 Analytics":

    st.title("📈 Analytics Dashboard")

    st.subheader("Final Score Trend")

    st.line_chart(
        df["Final_Exam_Score"]
    )

    st.subheader("Attendance Analysis")

    attendance_chart = df.set_index("Student_ID")

    st.bar_chart(
        attendance_chart["Attendance_Percentage"]
    )

    st.subheader("Attendance vs Final Exam Score")

    scatter_fig = px.scatter(
        df,
        x="Attendance_Percentage",
        y="Final_Exam_Score",
        color="Risk_Level",
        hover_data=["Student_ID"],
        size="Study_Hours_Per_Week",
        title="Attendance vs Performance"
    )

    st.plotly_chart(
        scatter_fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("📥 Export Report")

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Student CSV Report",
        data=csv,
        file_name="student_risk_report.csv",
        mime="text/csv"
    )


# ==========================================================
# ABOUT
# ==========================================================
elif page == "📘 About":

    st.title("📘 About Project")

    st.markdown("""
    ## Student Performance Risk Prediction & Early Warning System

    An educational analytics application designed to identify
    academically at-risk students.

    ### Technologies Used

    - Python
    - Streamlit
    - Pandas
    - Plotly
    - DeepFace
    - OpenCV

    ### Features

    - Secure login
    - Face verification
    - Student dashboard
    - Risk assessment
    - Academic analytics
    - Early warning identification
    - CSV report generation

    ### Objective

    To help educational institutions identify students who
    may require academic intervention using student data
    analysis and risk assessment.
    """)


# ==========================================================
# FOOTER
# ==========================================================
st.markdown("---")

st.markdown("""
<div style="text-align:center;padding:20px;">
    <h3>🎓 Student Risk Prediction System</h3>
    <p>Academic Analytics • Student Monitoring • Early Warning</p>
</div>
""", unsafe_allow_html=True)
