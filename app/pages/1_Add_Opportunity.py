import streamlit as st
from app.queries import execute_write
import datetime

st.title("➕ Add New Opportunity")

if st.session_state.get("role") != "Admin":
    st.error("🔒 Access Denied. Admin login required to add records.")
else:
    with st.form("add_job_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            comp = st.text_input("Company Name*")
            title = st.text_input("Job Title*")
            cat = st.selectbox("Category", ["Data Science", "AI", "Web Development", "Cyber Security", "Software Engineering"])
            city = st.text_input("City")
            country = st.text_input("Country", value="Pakistan")
        with col2:
            mode = st.selectbox("Work Mode", ["Remote", "Onsite", "Hybrid"])
            s_min = st.number_input("Min Salary", value=50000)
            s_max = st.number_input("Max Salary", value=150000)
            exp = st.selectbox("Experience Level", ["Entry-Level", "Mid-Level", "Senior"])
            deadline = st.date_input("Deadline", min_value=datetime.date.today())
        
        skills = st.text_area("Required Skills*")
        link = st.text_input("Source Link")
        
        if st.form_submit_button("Save Record"):
            if not comp or not title or not skills:
                st.error("Please fill required fields (*).")
            else:
                q = """INSERT INTO opportunities (company_name, job_title, category, city, country, work_mode, required_skills, salary_min, salary_max, experience_level, application_deadline, source_link)
                       VALUES (:comp, :title, :cat, :city, :country, :mode, :skills, :s_min, :s_max, :exp, :deadline, :link)"""
                execute_write(q, {"comp": comp, "title": title, "cat": cat, "city": city, "country": country, "mode": mode, "skills": skills, "s_min": s_min, "s_max": s_max, "exp": exp, "deadline": deadline, "link": link})
                st.success("Record added successfully!")
