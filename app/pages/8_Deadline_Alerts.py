import streamlit as st
from app.db import run_query

st.title("⏰ Deadline Priority Alerts")
st.markdown("Opportunities closing within the next 7 days.")

alert_query = """
    SELECT opportunity_id, company_name, job_title, application_deadline, status 
    FROM opportunities 
    WHERE application_deadline <= CURRENT_DATE + INTERVAL '7 days' 
    AND status = 'Open'
    ORDER BY application_deadline ASC
"""
urgent_jobs = run_query(alert_query)

if urgent_jobs.empty:
    st.info("No active application deadlines within the 7-day window.")
else:
    st.error(f"CRITICAL: {len(urgent_jobs)} opportunities are closing soon!")
    st.dataframe(urgent_jobs, use_container_width=True)
