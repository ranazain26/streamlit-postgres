import streamlit as st
from app.db import run_query
from app.queries import execute_write

st.title("✏️ Update Opportunity")

if st.session_state.get("role") != "Admin":
    st.error("🔒 Access Denied. Admin login required.")
else:
    df = run_query("SELECT opportunity_id, company_name, job_title FROM opportunities")
    if df.empty:
        st.warning("No records found.")
    else:
        options = {row['opportunity_id']: f"{row['company_name']} - {row['job_title']} (ID: {row['opportunity_id']})" for _, row in df.iterrows()}
        selected_id = st.selectbox("Select Record", options=list(options.keys()), format_func=lambda x: options[x])
        
        if selected_id:
            current = run_query(f"SELECT * FROM opportunities WHERE opportunity_id = {selected_id}").iloc[0]
            with st.form("update_form"):
                new_status = st.selectbox("Status", ["Open", "Closed", "Expired", "Shortlisted"], index=["Open", "Closed", "Expired", "Shortlisted"].index(current['status']))
                new_deadline = st.date_input("Deadline", value=current['application_deadline'])
                new_salary_min = st.number_input("Min Salary", value=float(current['salary_min'] or 0))
                new_salary_max = st.number_input("Max Salary", value=float(current['salary_max'] or 0))
                
                if st.form_submit_button("Update"):
                    q = """UPDATE opportunities SET status = :status, application_deadline = :deadline, salary_min = :s_min, salary_max = :s_max WHERE opportunity_id = :id"""
                    execute_write(q, {"status": new_status, "deadline": new_deadline, "s_min": new_salary_min, "s_max": new_salary_max, "id": selected_id})
                    st.success("Record updated!")
