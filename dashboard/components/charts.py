import streamlit as st
import plotly.express as px
import pandas as pd


def show_charts(summary):

    st.header("📈 Network Analytics")

    col1, col2 = st.columns(2)

    with col1:

        protocol = summary["protocol_distribution"]

        fig = px.pie(
            values=list(protocol.values()),
            names=list(protocol.keys()),
            title="Protocol Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        traffic = summary["traffic_type_distribution"]

        fig = px.bar(
            x=list(traffic.keys()),
            y=list(traffic.values()),
            title="Traffic Type Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        packets = summary["packet_category_distribution"]

        fig = px.pie(
            values=list(packets.values()),
            names=list(packets.keys()),
            title="Packet Category Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col4:

        df = pd.read_csv("data/processed/ai_dataset.csv")

        top_clients = (
            df["src_ip"]
            .value_counts()
            .head(5)
        )

        fig = px.bar(
            x=top_clients.index,
            y=top_clients.values,
            title="Top 5 Clients"
        )

        st.plotly_chart(fig, use_container_width=True)