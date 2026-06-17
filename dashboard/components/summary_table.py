import streamlit as st
import pandas as pd

def show_summary_table(summary):

    st.header("📋 Network Summary")

    data = {
        "Metric": [
            "Packets",
            "Clients",
            "Anomalies",
            "Privacy Score",
            "HTTPS %",
            "Carbon Footprint",
            "Health Score"
        ],
        "Value": [
    int(summary.get("total_packets", 0)),
    int(summary.get("total_clients", 0)),
    int(summary.get("anomaly_count", 0)),
    round(summary.get("privacy_score", 0), 2),
    f"{round(summary.get('https_percentage', 0), 2)}%",
    round(summary.get("carbon_footprint", 0), 3),
    round(summary.get("network_health_score", 0), 2)
]
    }

    df = pd.DataFrame(data)

    st.table(df)