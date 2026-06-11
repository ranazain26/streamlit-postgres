import streamlit as st
from app.db import run_query

st.title("🔍 Browse & Search")

search_term = st.text_input("Search by Title or Company")
col1, col2 = st.columns(2)
cat_filter = col1.multiselect("Category", ["Data Science", "AI", "Web Development", "Cyber Security", "Software Engineering"])
mode_filter = col2.multiselect("Work Mode", ["Remote", "Onsite", "Hybrid"])

query = "SELECT * FROM opportunities WHERE 1=1"
if search_term:
    query += f" AND (job_title ILIKE '%%{search_term}%%' OR company_name ILIKE '%%{search_term}%%')"
if cat_filter:
    query += f" AND category IN ('{"','".join(cat_filter)}')"
if mode_filter:
    query += f" AND work_mode IN ('{"','".join(mode_filter)}')"

df = run_query(query)
st.metric("Records Found", len(df))
st.dataframe(df, use_container_width=True)
