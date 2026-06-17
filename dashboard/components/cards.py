import streamlit as st

def show_kpi_cards(summary):

    st.subheader("📊 Network Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📦 Total Packets",
            summary["total_packets"]
        )

    with col2:
        st.metric(
            "👥 Total Clients",
            summary["total_clients"]
        )

    with col3:
        st.metric(
            "🚨 Anomalies",
            summary["anomaly_count"]
        )

    st.divider()

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "🔒 Privacy Score",
            summary["privacy_score"]
        )

    with col5:
        st.metric(
            "🌐 HTTPS %",
            f"{summary['https_percentage']}%"
        )

    with col6:
        st.metric(
            "🌱 Carbon (g CO₂)",
            summary["carbon_footprint"]
        )