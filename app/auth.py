import streamlit as st


def require_login():
    # Placeholder: simple password protect using session state
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        password = st.sidebar.text_input("Admin password", type="password")
        if st.sidebar.button("Login"):
            # In real app validate properly
            if password == "admin":
                st.session_state["logged_in"] = True
                st.experimental_rerun()
            else:
                st.sidebar.error("Invalid password")
