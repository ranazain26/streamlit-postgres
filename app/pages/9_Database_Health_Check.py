import streamlit as st
from app.db import run_query

st.title("🩺 Database Health Check")

try:
    version = run_query("SELECT version();").iloc[0,0]
    st.success("✅ Connected successfully to PostgreSQL container.")
    st.info(f"**PostgreSQL Version:** {version}")
    
    row_count = run_query("SELECT COUNT(*) FROM opportunities;").iloc[0,0]
    st.metric("Total Records in Database", row_count)
    
    st.subheader("Table Schema (opportunities)")
    schema_query = """
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'opportunities';
    """
    schema_df = run_query(schema_query)
    st.dataframe(schema_df, use_container_width=True)
    
except Exception as e:
    st.error("❌ Database Connection Failed. Please check your docker-compose logs.")
    st.code(str(e))
