import streamlit as st
from app import queries


def main():
    st.header("Add Opportunity")
    with st.form("add_form"):
        title = st.text_input("Title")
        company = st.text_input("Company")
        value = st.number_input("Value", min_value=0.0, format="%f")
        status = st.selectbox("Status", ["Open", "Won", "Lost"]) 
        deadline = st.date_input("Deadline")
        submitted = st.form_submit_button("Add")
        if submitted:
            data = {"title": title, "company": company, "value": value, "status": status, "deadline": deadline}
            try:
                id = queries.add_opportunity(data)
                st.success(f"Added opportunity id={id}")
            except Exception as e:
                st.error(str(e))
