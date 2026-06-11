import streamlit as st
from app import queries


def main():
    st.header("Delete Opportunity")
    rows = []
    try:
        rows = queries.list_opportunities()
    except Exception as e:
        st.error(str(e))

    if not rows:
        st.info("No opportunities to delete")
        return

    cols = {r['id']: f"{r['id']} - {r['title']} ({r.get('company')})" for r in rows}
    choice = st.selectbox("Select to delete", options=list(cols.keys()), format_func=lambda k: cols[k])
    if st.button("Delete"):
        try:
            queries.delete_opportunity(choice)
            st.success("Deleted")
        except Exception as e:
            st.error(str(e))
