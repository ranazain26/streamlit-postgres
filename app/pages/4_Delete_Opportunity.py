import streamlit as st
from app.db import run_query
from app.queries import delete_opportunity_by_id

st.title("🗑️ Delete Opportunity")

if st.session_state.get("role") != "Admin":
    st.error("🔒 Access Denied. Admin login required.")
else:
    df = run_query("SELECT opportunity_id, company_name, job_title FROM opportunities")
    if df.empty:
        st.warning("No records to delete.")
    else:
        options = {row['opportunity_id']: f"{row['company_name']} - {row['job_title']}" for _, row in df.iterrows()}
        selected_id = st.selectbox("Select Record to Delete", options=list(options.keys()), format_func=lambda x: options[x])
        
        if st.button("Delete Permanently", type="primary"):
            delete_opportunity_by_id(selected_id)
            st.success("Record deleted permanently.")
            st.rerun()
