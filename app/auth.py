import streamlit as st

def get_current_role():
    """Retrieves the current user role from session state."""
    return st.session_state.get("role", None)

def is_admin():
    """Checks if the current active session has Administrator privileges."""
    return get_current_role() == "Admin"

def require_admin():
    """Displays an error block if the user is not an Admin."""
    if not is_admin():
        st.error("🔒 Access Denied. Administrator privileges are required to execute this action.")
        st.stop()
