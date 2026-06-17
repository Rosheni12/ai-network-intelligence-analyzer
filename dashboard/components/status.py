import streamlit as st


def show_status(summary):

    score = summary.get("network_health_score", 0)
    risk = summary.get("risk_level", "UNKNOWN")
    clients = summary.get("total_clients", 0)

    # ---------------- Status Logic ----------------

    if score >= 80:
        status = "🟢 HEALTHY"
        msg = "All systems operating normally"
    elif score >= 60:
        status = "🟡 STABLE"
        msg = "Minor fluctuations detected"
    else:
        status = "🔴 CRITICAL"
        msg = "Immediate attention required"

    # ---------------- UI ----------------

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(90deg,#161B22,#1C2128);
            padding:18px;
            border-radius:14px;
            border:1px solid #30363D;
            margin-bottom:15px;
        ">
            <h3 style="margin:0;color:#4FC3F7;">🌐 Live Network Status</h3>

            <h2 style="margin:8px 0;">{status}</h2>

            <p style="color:#B0BEC5;margin:0;">
                {msg}
            </p>

            <hr style="border:0.5px solid #30363D;margin:10px 0;">

            <p style="margin:0;">
                🩺 Health Score: <b>{score:.2f}/100</b> <br>
                ⚠️ Risk Level: <b>{risk}</b> <br>
                👥 Active Clients: <b>{clients}</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )