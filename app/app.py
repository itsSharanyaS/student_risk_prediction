
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from pathlib import Path
import tempfile
import os

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="Student Risk Prediction System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# PROFESSIONAL DARK UI
# ==========================================================
st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
}
h1, h2, h3 {
    color: #ffffff !important;
}
p, label {
    color: #e5e7eb;
}
section[data-testid="stSidebar"] {
    background-color: #1e293b;
    border-right: 2px solid #2563eb;
}
[data-testid="metric-container"] {
    background-color: #1f2937;
    border: 1px solid #374151;
    padding: 15px;
    border-radius: 15px;
}
.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    min-height: 45px;
}
.stButton > button:hover {
    background-color: #1d4ed8;
    border: 1px solid #60a5fa;
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# AUTHENTICATION CONFIGURATION
# ==========================================================
# Demo password - change before deployment.
# Prefer storing credentials in Streamlit Secrets.

DEMO_USERNAME = "admin"
DEMO_PASSWORD = "admin123"

FACE_REFERENCE = Path("face_reference.jpg")


def verify_face(uploaded_face):
    """
    Compares the webcam image with the registered reference image.
    Requires DeepFace and a local reference image.
    """
    if not FACE_REFERENCE.exists():
        return False, "Reference image not found."

    try:
        from deepface import DeepFace

        with tempfile.NamedTemporaryFile(
            suffix=".jpg", delete=False
        ) as temp_file:
            uploaded_face.save(temp_file.name)
            temp_path = temp_file.name

        try:
            result = DeepFace.verify(
                img1_path=str(FACE_REFERENCE),
                img2_path=temp_path,
                model_name="Facenet",
                detector_backend="opencv",
                enforce_detection=True
            )

            verified = result.get("verified", False)

            if verified:
                return True, "Face verified successfully."

            return False, "Face does not match."

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    except Exception as e:
        return False, f"Face verification failed: {str(e)}"


# ==========================================================
# SESSION STATE
# ==========================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "login_method" not in st.session_state:
    st.session_state.login_method = None

if "user_name" not in st.session_state:
    st.session_state.user_name = "Admin"


# ==========================================================
# LOGIN PAGE
# ==========================================================
if not st.session_state.logged_in:

    st.markdown("<br><br>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown(
            """
            <div style="text-align:center;">
                <h1>🎓 EduGuard AI</h1>
                <p>Student Performance Risk Prediction System</p>
                <p>🔐 Secure Admin Authentication</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        login_tab, password_tab = st.tabs(
            ["📷 Face Login", "🔑 Password Login"]
        )

        # --------------------------------------------------
        # FACE LOGIN
        # --------------------------------------------------
        with login_tab:

            st.markdown("### Face Recognition")
            st.write(
                "Position your face in front of the camera "
                "and capture an image to verify your identity."
            )

            face_image = st.camera_input(
                "Capture your face",
                key="face_camera"
            )

            if face_image is not None:

                if st.button(
                    "🔍 Verify Face",
                    use_container_width=True
                ):

                    with st.spinner("Verifying your face..."):

                        verified, message = verify_face(face_image)

                    if verified:

                        st.session_state.logged_in = True
                        st.session_state.login_method = "Face Recognition"
                        st.session_state.user_name = "Admin"

                        st.success("Face recognized! Login successful.")
                        st.rerun()

                    else:
                        st.error(message)
                        st.warning(
                            "Face verification failed. "
                            "Please use password login."
                        )

        # --------------------------------------------------
        # PASSWORD LOGIN
        # --------------------------------------------------
        with password_tab:

            st.markdown("### Admin Password Login")

            username = st.text_input(
                "Username",
                key="login_username"
            )

            password = st.text_input(
                "Password",
                type="password",
                key="login_password"
            )

            if st.button(
                "🔓 Login",
                use_container_width=True
            ):

                if (
                    username == DEMO_USERNAME
                    and password == DEMO_PASSWORD
                ):

                    st.session_state.logged_in = True
                    st.session_state.login_method = "Password"
                    st.session_state.user_name = "Admin"

                    st.success("Login successful!")
                    st.rerun()

                else:
                    st.error("Invalid username or password.")

        st.divider()

        st.caption(
            "Authorized access only • Student Analytics System"
        )

    st.stop()


# ==========================================================
# LOGOUT FUNCTION
# ==========================================================
def logout():
    st.session_state.logged_in = False
    st.session_state.login_method = None
    st.session_state.user_name = "Admin"


# ==========================================================
# STUDENT DATASET
# ==========================================================
data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Gender": ["F", "M", "F", "M", "F"],
    "Age": [18, 19, 17, 18, 19],
    "Study_Hours_Per_Week": [25, 10, 18, 8, 30],
    "Attendance_Percentage": [92, 58, 75, 40, 96],
    "Previous_Score": [88, 52, 67, 45, 92],
    "Parental_Education_Level": [
        "Graduate",
        "High School",
        "Graduate",
        "High School",
        "Postgraduate"
    ],
    "Internet_Access": ["Yes", "No", "Yes", "No", "Yes"],
    "Extracurricular_Activities": [
        "Yes", "No", "Yes", "No", "Yes"
    ],
    "Sleep_Hours": [7, 5, 6, 4, 8],
    "Final_Exam_Score": [91, 46, 72, 38, 95],
    "Pass_Fail": ["Pass", "Fail", "Pass", "Fail", "Pass"]
}

df = pd.DataFrame(data)


# ==========================================================
# RISK CLASSIFICATION
# ==========================================================
def get_risk(score):

    if score < 50:
        return "High Risk"

    elif score < 75:
        return "Medium Risk"

    return "Low Risk"


df["Risk_Level"] = df["Final_Exam_Score"].apply(get_risk)


# ==========================================================
# SIDEBAR
# ==========================================================
st.sidebar.markdown("# 🎓 EduGuard AI")
st.sidebar.caption("Student Risk Analytics Platform")

st.sidebar.success("🟢 System Active")

st.sidebar.metric("Total Students", len(df))

st.sidebar.metric(
    "High Risk Students",
    len(df[df["Risk_Level"] == "High Risk"])
)

st.sidebar.markdown("---")

st.sidebar.write(
    f"👤 Logged in as: **{st.session_state.user_name}**"
)

st.sidebar.caption(
    f"Login Method: {st.session_state.login_method}"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dashboard",
        "🎯 Prediction",
        "📈 Analytics",
        "📘 About"
    ]
)

st.sidebar.markdown("---")

if st.sidebar.button("🚪 Logout", use_container_width=True):
    logout()
    st.rerun()


# ==========================================================
# HOME PAGE
# ==========================================================
if page == "🏠 Home":

    st.title("🎓 Student Performance Risk Prediction")
    st.subheader("Early Warning & Academic Analytics System")

    st.write("""
    An educational analytics system designed to analyze student academic data,
    identify students who may be academically at risk, and support
    early intervention.
    """)

    st.success(
        f"Welcome, {st.session_state.user_name}! "
        "You are successfully authenticated."
    )

    st.divider()

    pass_count = len(df[df["Pass_Fail"] == "Pass"])

    pass_percent = round(
        (pass_count / len(df)) * 100, 2
    )

    avg_score = round(
        df["Final_Exam_Score"].mean(), 2
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👨‍🎓 Students", len(df))
    col2.metric("📊 Average Score", avg_score)
    col3.metric("✅ Pass Percentage", f"{pass_percent}%")
    col4.metric(
        "🚨 High Risk",
        len(df[df["Risk_Level"] == "High Risk"])
    )

    st.divider()

    st.subheader("📚 Student Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("🚀 System Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🎯 Student Risk Prediction")
        st.info("📊 Interactive Dashboard")
        st.info("🚨 Early Warning Identification")

    with col2:
        st.info("🧠 Academic Insights")
        st.info("📈 Performance Analytics")
        st.info("📥 CSV Report Export")


# ==========================================================
# DASHBOARD
# ==========================================================
elif page == "📊 Dashboard":

    st.title("📊 Student Dashboard")

    st.caption(
        f"Last Updated: {datetime.now().strftime('%d %B %Y %H:%M')}"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Students", len(df))
    col2.metric(
        "Average Score",
        round(df["Final_Exam_Score"].mean(), 2)
    )
    col3.metric(
        "Highest Score",
        df["Final_Exam_Score"].max()
    )
    col4.metric(
        "Lowest Score",
        df["Final_Exam_Score"].min()
    )

    st.divider()

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
            title="Pass vs Fail Distribution",
            hole=0.45
        )

        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

    st.divider()

    st.subheader("📚 Student Records")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("🧠 Academic Insights")

    low_attendance = df[
        df["Attendance_Percentage"] < 60
    ]

    high_risk = df[
        df["Risk_Level"] == "High Risk"
    ]

    st.warning(
        f"{len(low_attendance)} students have attendance below 60%."
    )

    st.error(
        f"{len(high_risk)} students are classified as High Risk."
    )

    st.info(
        "Attendance and academic performance should be monitored "
        "regularly to identify students requiring support."
    )

    top_student = df.loc[
        df["Final_Exam_Score"].idxmax()
    ]

    weak_student = df.loc[
        df["Final_Exam_Score"].idxmin()
    ]

    st.success(
        f"🏆 Student {top_student['Student_ID']} is the top performer "
        f"with score {top_student['Final_Exam_Score']}."
    )

    st.warning(
        f"📉 Student {weak_student['Student_ID']} requires academic support."
    )


# ==========================================================
# PREDICTION
# ==========================================================
elif page == "🎯 Prediction":

    st.title("🎯 Student Risk Assessment")

    st.write(
        "Enter student academic details to identify their risk category."
    )

    col1, col2 = st.columns(2)

    with col1:

        attendance = st.slider(
            "Attendance Percentage",
            0, 100, 70
        )

        final_score = st.slider(
            "Final Exam Score",
            0, 100, 65
        )

    with col2:

        study_hours = st.slider(
            "Study Hours Per Week",
            0, 40, 15
        )

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

            st.warning("""
            Recommended academic interventions:

            - Arrange academic mentoring
            - Monitor attendance regularly
            - Conduct a student counseling session
            - Provide remedial classes
            """)

        elif risk == "Medium Risk":

            st.warning("🟡 MEDIUM RISK")

            st.info("""
            Recommended actions:

            - Improve study consistency
            - Monitor attendance
            - Conduct weekly progress reviews
            - Provide additional practice
            """)

        else:

            st.success("🟢 LOW RISK")

            st.info("""
            Student performance appears stable.

            - Maintain consistent study habits
            - Continue regular attendance
            - Encourage advanced learning
            """)

        st.metric("Predicted Risk Category", risk)

        st.caption(
            "This is a rule-based risk assessment, not a trained ML model."
        )


# ==========================================================
# ANALYTICS
# ==========================================================
elif page == "📈 Analytics":

    st.title("📈 Analytics Dashboard")

    st.subheader("📊 Final Score Trend")

    st.line_chart(
        df["Final_Exam_Score"]
    )

    st.subheader("📚 Attendance Analysis")

    attendance_chart = df.set_index("Student_ID")

    st.bar_chart(
        attendance_chart["Attendance_Percentage"]
    )

    st.subheader("📈 Attendance vs Final Score")

    scatter_fig = px.scatter(
        df,
        x="Attendance_Percentage",
        y="Final_Exam_Score",
        color="Risk_Level",
        hover_data=["Student_ID"],
        title="Attendance vs Academic Performance",
        size="Study_Hours_Per_Week"
    )

    st.plotly_chart(
        scatter_fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("📥 Export Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV Report",
        data=csv,
        file_name="student_risk_report.csv",
        mime="text/csv"
    )


# ==========================================================
# ABOUT
# ==========================================================
elif page == "📘 About":

    st.title("📘 About the Project")

    st.markdown("""
    ## Student Performance Risk Prediction & Early Warning System

    An educational analytics platform designed to identify academically
    at-risk students and support early academic intervention.

    ### Technologies Used

    - Python
    - Streamlit
    - Pandas
    - Plotly
    - OpenCV / DeepFace for face verification

    ### Features

    - Secure authentication
    - Face recognition
    - Student dashboard
    - Academic risk assessment
    - Analytics and visualization
    - Early warning identification
    - CSV report download

    ### Objective

    To support educational institutions in identifying students requiring
    academic assistance through data analysis and risk assessment.
    """)


# ==========================================================
# FOOTER
# ==========================================================
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;padding:15px;">
        <h3>🎓 Student Risk Prediction System</h3>
        <p>AI-powered educational analytics platform</p>
        <p>Smart Education • Academic Analytics • Early Warning</p>
    </div>
    """,
    unsafe_allow_html=True
)
