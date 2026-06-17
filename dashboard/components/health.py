import streamlit as st


def show_health(summary):

    score = float(summary.get("network_health_score", 0))
    risk = summary.get("risk_level")
    grade = summary.get("health_grade")

    # ---------- Auto fallback ----------
    if not grade:
        if score >= 90:
            grade = "Excellent"
        elif score >= 75:
            grade = "Good"
        elif score >= 60:
            grade = "Fair"
        else:
            grade = "Poor"

    if not risk:
        if score >= 80:
            risk = "LOW"
        elif score >= 60:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

    # ---------- Colors ----------
    if score >= 80:
        color = "#00C853"
        status = "🟢"
    elif score >= 60:
        color = "#FFC107"
        status = "🟡"
    else:
        color = "#F44336"
        status = "🔴"

    st.header("🩺 Network Health")

    # ---------- Hero Score ----------
    st.markdown(
        f"""
        <div style="text-align:center;padding-top:10px;">
            <h1 style="color:{color};font-size:58px;margin-bottom:0;">
                {score:.2f}
            </h1>
            <p style="font-size:20px;margin-top:-10px;">
                Network Health Score
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(min(score / 100, 1.0))

    st.markdown("")

    # ---------- Grade & Risk ----------
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="🏅 Health Grade",
            value=grade
        )

    with col2:
        st.metric(
            label="⚠️ Risk Level",
            value=f"{status} {risk}"
        )