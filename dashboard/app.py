import os
import sys
import time
import streamlit as st

# -------------------------------
# Add project root to Python path
# -------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

# -------------------------------
# Core imports
# -------------------------------
from components.charts import show_charts
from src.analytics.summary import AnalyticsSummary
from components.sidebar import show_sidebar
from components.cards import show_kpi_cards
from components.health import show_health
from components.status import show_status
from dashboard.core.validator import validate_summary
from components.insights_panel import show_insights
from components.summary_table import show_summary_table
from components.gemini_report import generate_ai_report
from components.export_panel import show_export

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="AI Network Intelligence Analyzer",
    page_icon="🌐",
    layout="wide"
)

# -------------------------------
# Load CSS
# -------------------------------
def load_css():
    css_path = os.path.join(
        os.path.dirname(__file__),
        "styles",
        "style.css"
    )

    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# -------------------------------
# Sidebar
# -------------------------------
show_sidebar()

st.sidebar.header("⚙ Controls")

auto_refresh = st.sidebar.checkbox("🔄 Auto Refresh (5s)")

if auto_refresh:
    time.sleep(5)
    st.rerun()

# -------------------------------
# Load Data
# -------------------------------

summary = AnalyticsSummary(
    "data/processed/ai_dataset.csv"
).generate_summary()

summary = validate_summary(summary)

# -------------------------------
# Title
# -------------------------------
st.title("🌐 AI Network Intelligence Analyzer")
st.markdown("### 🟢 Live Network Monitoring Dashboard")
st.divider()

# -------------------------------
# Dashboard Flow (IMPORTANT ORDER)
# -------------------------------
show_status(summary)
st.divider()

show_kpi_cards(summary)
st.divider()

show_health(summary)
st.divider()

show_charts(summary)
st.divider()

show_insights(summary)
st.divider()

# -------------------------------
# Gemini AI Report Section
# -------------------------------
st.header("🧠 Gemini AI Report")

if st.button("🚀 Generate AI Report"):

    with st.spinner("🧠 Gemini is analyzing your network..."):
        report = generate_ai_report(summary)

    st.success("✅ AI Analysis Completed Successfully!")
    st.info("🤖 Generated using Gemini Flash AI")
    report = generate_ai_report(summary)
    st.markdown("## 📑 AI Network Intelligence Report")

    with st.container(border=True):
        st.markdown(report)

st.divider()

show_summary_table(summary)
st.divider()

show_export(summary)