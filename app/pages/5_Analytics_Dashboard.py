import streamlit as st
import plotly.express as px
from app.db import run_query

st.title("📊 Analytics Dashboard")

df = run_query("SELECT * FROM opportunities")

if df.empty:
    st.warning("No data to analyze.")
else:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Jobs", len(df))
    c2.metric("Unique Companies", df['company_name'].nunique())
    c3.metric("Remote Roles", len(df[df['work_mode'] == 'Remote']))
    
    # Calculate Average Max Salary Safely
    avg_salary = df['salary_max'].astype(float).mean() if not df['salary_max'].isnull().all() else 0
    c4.metric("Avg Max Salary", f"PKR {avg_salary:,.0f}")

    col1, col2 = st.columns(2)
    with col1:
        fig_pie = px.pie(df, names="category", title="Jobs by Category")
        st.plotly_chart(fig_pie, use_container_width=True)
    with col2:
        fig_bar = px.bar(df, x="work_mode", color="status", title="Work Mode by Status")
        st.plotly_chart(fig_bar, use_container_width=True)
