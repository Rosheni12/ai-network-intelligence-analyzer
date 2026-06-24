import streamlit as st


def show_status(summary):

    status = summary.get("network_status", "🟢 HEALTHY")
    health_score = summary.get("network_health_score", 0)
    health_grade = summary.get("health_grade", "Good")
    risk_level = summary.get("risk_level", "LOW")
    anomaly_count = summary.get("anomaly_count", 0)
    total_clients = summary.get("total_clients", 0)
    privacy_score = summary.get("privacy_score", 0)

    if "HEALTHY" in status:
        color = "#22C55E"
        message = "All systems operating normally."

    elif "WARNING" in status:
        color = "#FACC15"
        message = "Potential issues detected. Monitor the network."

    else:
        color = "#EF4444"
        message = "Critical network condition detected."

    st.markdown(
        f"""
        <div style="
            background:#161B22;
            padding:20px;
            border-radius:12px;
            border-left:6px solid {color};
            box-shadow:0px 4px 12px rgba(0,0,0,0.35);
        ">

        <h3 style="margin:0;color:white;">🌐 Live Network Status</h3>

        <h2 style="margin:10px 0;color:{color};">
            {status}
        </h2>

        <p style="color:#B0BEC5;">
            {message}
        </p>

        <hr style="border:0.5px solid #30363D;">

        <p style="font-size:16px;line-height:2;">

        🩺 <b>Health Score:</b> {health_score}/100<br>
        🏅 <b>Health Grade:</b> {health_grade}<br>
        ⚠️ <b>Risk Level:</b> {risk_level}<br>
        🚨 <b>Anomalies Detected:</b> {anomaly_count}<br>
        👥 <b>Active Clients:</b> {total_clients}<br>
        🔒 <b>Privacy Score:</b> {privacy_score}

        </p>

        </div>
        """,
        unsafe_allow_html=True
    )