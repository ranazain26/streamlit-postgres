import streamlit as st
from app.db import run_query

st.title("👯 Duplicate Detection")
st.write("Checking for multiple entries with the same Company, Job Title, and City.")

dup_query = """
    SELECT company_name, job_title, city, COUNT(*) as occurrence_count 
    FROM opportunities 
    GROUP BY company_name, job_title, city 
    HAVING COUNT(*) > 1
"""
duplicates = run_query(dup_query)

if duplicates.empty:
    st.success("✅ No duplicates detected in the database.")
else:
    st.warning(f"⚠️ Found {len(duplicates)} duplicate clusters:")
    st.dataframe(duplicates, use_container_width=True)
