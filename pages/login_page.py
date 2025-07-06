import streamlit as st

# Dummy credentials (you can replace with DB or file later)
USER_CREDENTIALS = {
    "rahul": "pass123",
    "admin": "admin123"
}

def login_user(username, password):
    return USER_CREDENTIALS.get(username) == password

def app():
    st.title("🔐 Login Page")
    st.subheader("Please enter your credentials to proceed.")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        if login_user(username, password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password")

# Ensure this runs only when selected from main
if __name__ == "__main__":
    app()
