import streamlit as st
from app import queries, utils


def main():
    st.header("View / Search Opportunities")
    rows = []
    try:
        rows = queries.list_opportunities()
    except Exception as e:
        st.error(str(e))

    df = utils.to_df(rows)
    st.dataframe(df)
