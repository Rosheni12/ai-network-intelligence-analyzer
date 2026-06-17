import streamlit as st
import json
import pandas as pd
from datetime import datetime


def show_export(summary):

    st.header("⬇ Export Reports")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # ---------------- JSON Export ----------------
    json_data = json.dumps(summary, indent=4)

    st.download_button(
        label="📥 Download JSON Summary",
        data=json_data,
        file_name=f"network_summary_{timestamp}.json",
        mime="application/json"
    )

    # ---------------- CSV Export ----------------
    df = pd.DataFrame([summary])

    csv_data = df.to_csv(index=False)

    st.download_button(
        label="📥 Download CSV Summary",
        data=csv_data,
        file_name=f"network_summary_{timestamp}.csv",
        mime="text/csv"
    )

    # ---------------- AI Report Export (if available) ----------------
    if "ai_report" in summary and summary["ai_report"]:

        st.download_button(
            label="📥 Download AI Report",
            data=summary["ai_report"],
            file_name=f"ai_report_{timestamp}.txt",
            mime="text/plain"
        )
    else:
        st.info("AI Report will be available after generation.")