import streamlit as st

from pages import (
    login_page,
    introduction_page,
    data_upload_page,
    column_selection,
    clustering_model,
    cluster_naming
)

PAGES = {
    "1. Login": login_page.app,
    "2. Introduction": introduction_page.app,
    "3. Data Upload": data_upload_page.app,
    "4. Column Selection + Elbow": column_selection.app,
    "5. Clustering Model": clustering_model.app,
    "6. Cluster Naming + Download": cluster_naming.app,
}


def main():
    st.sidebar.title("🔍 Clustering App Navigation")

    # If not logged in, show only the login page
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        PAGES["1. Login"]()
        return

    # Exclude the login page from selection once logged in
    options = list(PAGES.keys())[1:]
    choice = st.sidebar.radio("Go to Page", options)

    # Defensive check for None
    if choice and choice in PAGES:
        page = PAGES[choice]
        page()
    else:
        st.warning("Please select a page from the sidebar.")


if __name__ == "__main__":
    main()
