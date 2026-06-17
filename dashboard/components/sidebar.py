import streamlit as st


def show_sidebar():
    st.sidebar.title("🌐 AI Network Intelligence Analyzer")

    st.sidebar.markdown("---")

    st.sidebar.header("📌 Navigation")

    st.sidebar.write("🏠 Dashboard")
    st.sidebar.write("📊 Analytics")
    st.sidebar.write("🚨 Anomalies")
    st.sidebar.write("💡 AI Insights")

    st.sidebar.markdown("---")

    st.sidebar.success("System Status: Online")