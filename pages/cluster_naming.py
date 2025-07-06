import streamlit as st
import pandas as pd

def app():
    st.title("🏷️ Name Your Clusters & Download Data")

    if "clustered_df" not in st.session_state:
        st.warning("⚠️ Please complete the clustering step first.")
        return

    df = st.session_state["clustered_df"]
    cluster_labels = df["cluster"].unique()
    cluster_labels.sort()

    st.markdown("### ✍️ Assign Names to Clusters")

    # Create dictionary for storing names
    cluster_name_map = {}

    for label in cluster_labels:
        default_name = f"Cluster {label}"
        name = st.text_input(f"Name for Cluster {label}:", value=default_name)
        cluster_name_map[label] = name

    # Apply naming
    df["cluster_name"] = df["cluster"].map(cluster_name_map)

    st.write("### 📋 Data with Cluster Names")
    st.dataframe(df.head())

    # Save to session
    st.session_state["named_clustered_df"] = df.copy()

    # Filter cluster
    st.markdown("### 🔍 Filter by Cluster Name")
    selected_names = st.multiselect("Select cluster(s) to filter:", list(cluster_name_map.values()))

    if selected_names:
        filtered_df = df[df["cluster_name"].isin(selected_names)]
    else:
        filtered_df = df

    st.write(f"### 🧾 Filtered Data ({filtered_df.shape[0]} rows)")
    st.dataframe(filtered_df)

    # Download
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name="filtered_clusters.csv",
        mime="text/csv"
    )

# Test independently
if __name__ == "__main__":
    app()
