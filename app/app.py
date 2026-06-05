# =====================================================
# PROFESSIONAL DARK DASHBOARD CSS
# =====================================================

st.markdown("""
<style>

/* =====================================================
MAIN BACKGROUND
===================================================== */

.stApp {

    background-color: #0f172a;

    color: white;

    font-family: 'Segoe UI', sans-serif;
}

/* =====================================================
HEADINGS
===================================================== */

h1 {

    color: #ffffff !important;

    font-size: 42px !important;

    font-weight: 800 !important;
}

h2 {

    color: #e2e8f0 !important;

    font-weight: 700 !important;
}

h3 {

    color: #cbd5e1 !important;

    font-weight: 700 !important;
}

/* =====================================================
TEXT
===================================================== */

p {

    color: #e2e8f0;
}

label {

    color: #ffffff !important;
}

/* =====================================================
SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #020617,
            #0f172a
        );

    border-right: 1px solid #334155;
}

/* Sidebar text */

section[data-testid="stSidebar"] * {

    color: white !important;
}

/* =====================================================
METRIC CARDS
===================================================== */

[data-testid="metric-container"] {

    background-color: #1e293b;

    border-radius: 18px;

    padding: 18px;

    border: 1px solid #334155;

    box-shadow:
        0px 4px 12px rgba(0,0,0,0.35);
}

/* Metric text */

[data-testid="metric-container"] label {

    color: #cbd5e1 !important;
}

[data-testid="metric-container"] div {

    color: white !important;
}

/* =====================================================
BUTTONS
===================================================== */

.stButton > button {

    background:
        linear-gradient(
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

/* Hover */

.stButton > button:hover {

    background:
        linear-gradient(
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

    background:
        linear-gradient(
            to right,
            #16a34a,
            #15803d
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

    background-color: rgba(34,197,94,0.15) !important;

    border-radius: 14px;
}

.stWarning {

    background-color: rgba(251,191,36,0.15) !important;

    border-radius: 14px;
}

.stError {

    background-color: rgba(239,68,68,0.15) !important;

    border-radius: 14px;
}

/* =====================================================
DATAFRAME
===================================================== */

[data-testid="stDataFrame"] {

    border-radius: 14px;

    overflow: hidden;

    border: 1px solid #334155;
}

/* =====================================================
ALERT BOX
===================================================== */

.alert-box {

    padding: 15px;

    border-radius: 12px;

    background-color: rgba(239,68,68,0.15);

    border-left: 6px solid #ef4444;

    margin-bottom: 10px;
}

/* =====================================================
RECOMMENDATION BOX
===================================================== */

.recommend-box {

    background-color: rgba(37,99,235,0.15);

    padding: 15px;

    border-radius: 12px;

    border-left: 5px solid #2563eb;
}

/* =====================================================
DIVIDER
===================================================== */

hr {

    border: 1px solid #334155;
}

/* =====================================================
FOOTER
===================================================== */

.footer {

    text-align: center;

    color: #94a3b8;

    padding: 20px;

    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

