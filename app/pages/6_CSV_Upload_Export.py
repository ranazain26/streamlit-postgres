import streamlit as st
import pandas as pd
from app import queries, utils


def main():
    st.header("CSV Upload / Export")
    st.info("Upload CSV to bulk add or export existing data.")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded is not None:
        df = pd.read_csv(uploaded)
        st.write(df.head())
        st.info("Bulk insert not implemented in scaffold. Implement in `app/queries.py`.")

    if st.button("Export as CSV"):
        rows = queries.list_opportunities()
        df = utils.to_df(rows)
        st.download_button("Download CSV", data=df.to_csv(index=False), file_name="opportunities.csv")
