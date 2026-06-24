import streamlit as st
import pandas as pd


def show_summary_table(summary):

    st.subheader("📋 Network Summary")

    df = pd.DataFrame({
        "Metric": [
            "Total Packets",
            "Total Clients",
            "Detected Anomalies",
            "Privacy Score",
            "HTTPS Adoption",
            "Carbon Footprint",
            "Network Health Score"
        ],
        "Value": [
            f"{summary.get('total_packets', 0):,}",
            f"{summary.get('total_clients', 0):,}",
            f"{summary.get('anomaly_count', 0):,}",
            f"{summary.get('privacy_score', 0):.2f}",
            f"{summary.get('https_percentage', 0):.2f}%",
            f"{summary.get('carbon_footprint', 0):.3f} g CO₂",
            f"{summary.get('network_health_score', 0):.2f}/100"
        ]
    })

    st.table(df)