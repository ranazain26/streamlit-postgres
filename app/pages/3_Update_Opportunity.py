import streamlit as st
from app import queries


def main():
    st.header("Update Opportunity")
    rows = []
    try:
        rows = queries.list_opportunities()
    except Exception as e:
        st.error(str(e))
        return

    if not rows:
        st.info("No opportunities to update")
        return

    options = {r['id']: f"{r['id']} - {r['title']}" for r in rows}
    selected = st.selectbox("Select opportunity", options=list(options.keys()), format_func=lambda k: options[k])
    record = queries.get_opportunity(selected)
    if not record:
        st.error("Record not found")
        return

    with st.form("update_form"):
        title = st.text_input("Title", value=record.get('title', ''))
        company = st.text_input("Company", value=record.get('company', ''))
        value = st.number_input("Value", value=float(record.get('value') or 0.0))
        status = st.selectbox("Status", ["Open", "Won", "Lost"], index=0)
        deadline = st.date_input("Deadline")
        submitted = st.form_submit_button("Update")
        if submitted:
            data = {"title": title, "company": company, "value": value, "status": status, "deadline": deadline}
            try:
                queries.update_opportunity(selected, data)
                st.success("Updated")
            except Exception as e:
                st.error(str(e))
