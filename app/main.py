import streamlit as st

st.set_page_config(page_title="Opportunity Dashboard", layout="wide")

if "role" not in st.session_state:
    st.session_state["role"] = None

st.title("Internship & Job Tracking Dashboard")

if st.session_state["role"] is None:
    st.subheader("Login")
    role = st.selectbox("Select Role", ["Viewer", "Admin"])
    if st.button("Login"):
        st.session_state["role"] = role
        st.rerun()
else:
    st.write(f"Logged in as: **{st.session_state['role']}**")
    if st.button("Logout"):
        st.session_state["role"] = None
        st.rerun()
    
    st.markdown("### Welcome to the Dashboard")
    st.info("Use the sidebar navigation to access different modules. Admins can manage records, while Viewers can analyze trends and view data.")