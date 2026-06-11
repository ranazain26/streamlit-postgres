import streamlit as st
from app import queries, utils
import plotly.express as px


def main():
    st.header("Analytics Dashboard")
    rows = []
    try:
        rows = queries.list_opportunities()
    except Exception as e:
        st.error(str(e))
        return

    df = utils.to_df(rows)
    if df.empty:
        st.info("No data")
        return

    st.subheader("Opportunities by status")
    fig = px.histogram(df, x="status")
    st.plotly_chart(fig, use_container_width=True)
