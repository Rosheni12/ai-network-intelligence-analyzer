import streamlit as st


def show_insights(summary):

    st.header("💡 AI Insights")

    score = summary.get("network_health_score", 0)
    anomalies = summary.get("anomaly_count", 0)
    https = summary.get("https_percentage", 0)
    privacy = summary.get("privacy_score", 0)

    insights = []

    # ---------------- Insight Logic ----------------

    if score >= 80:
        insights.append("Network is operating in a stable and healthy state.")
    else:
        insights.append("Network shows moderate instability and requires monitoring.")

    if anomalies > 300:
        insights.append("High anomaly activity detected — inspect security logs.")
    else:
        insights.append("Anomaly levels are within acceptable range.")

    if https >= 80:
        insights.append("Strong HTTPS adoption ensures secure communication.")
    else:
        insights.append("HTTPS usage is below optimal security standards.")

    if privacy >= 70:
        insights.append("Privacy score indicates good data protection practices.")
    else:
        insights.append("Privacy score can be improved to reduce exposure risks.")

    # ---------------- UI Layout ----------------

    st.markdown(
        """
        <div style="
            background-color:#161B22;
            padding:18px;
            border-radius:12px;
            border:1px solid #30363D;
        ">
        """,
        unsafe_allow_html=True
    )

    for i, item in enumerate(insights, 1):
        st.markdown(f"**{i}. {item}**")

    st.markdown("</div>", unsafe_allow_html=True)