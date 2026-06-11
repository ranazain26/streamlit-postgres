import streamlit as st
import pandas as pd
from app.db import run_query, get_engine

st.title("📥 CSV Upload & Export")

tab1, tab2 = st.tabs(["Upload CSV", "Export Data"])

with tab1:
    if st.session_state.get("role") != "Admin":
        st.error("🔒 Admin required for bulk uploads.")
    else:
        uploaded_file = st.file_uploader("Upload Job Sheet (CSV)", type=["csv"])
        if uploaded_file is not None:
            df_upload = pd.read_csv(uploaded_file)
            st.dataframe(df_upload.head())
            if st.button("Insert into Database"):
                try:
                    df_upload.to_sql("opportunities", con=get_engine(), if_exists="append", index=False)
                    st.success("CSV data successfully imported!")
                except Exception as e:
                    st.error(f"Import Failed. Ensure columns match the database schema. Error: {e}")

with tab2:
    st.subheader("Export All Records")
    all_data = run_query("SELECT * FROM opportunities")
    csv_bytes = all_data.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv_bytes, file_name="opportunities_export.csv", mime="text/csv")
