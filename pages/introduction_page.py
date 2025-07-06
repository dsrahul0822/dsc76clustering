import streamlit as st

def app():
    st.title("📊 Clustering Application - Introduction")

    st.markdown(
        """
        ### 🔍 What is Clustering?
        Clustering is an unsupervised machine learning technique used to group similar data points together. It helps identify patterns or segments within your data without any prior labeling.

        ---

        ### 🧠 What This App Does
        This application allows you to:
        - Upload your own `.csv` data
        - Choose columns for clustering
        - Automatically find the best number of clusters using **Elbow Method**
        - Choose clustering algorithm: **K-Means** or **Hierarchical**
        - Assign meaningful names to clusters
        - Download filtered cluster data
        - Visualize them using scatter plots

        ---

        ### 💼 Real-World Use Cases
        - Customer segmentation
        - Fraud detection
        - Grouping users by behavior
        - Product categorization
        - Marketing targeting

        ---

        ### 🧭 How to Use This App
        1. Upload your `.csv` dataset
        2. Choose columns for clustering
        3. Use Elbow Method to decide optimal clusters
        4. Apply K-Means or Hierarchical clustering
        5. Name the clusters and download filtered data
        6. Visualize clusters with scatter plots

        ---

        👈 Use the sidebar to navigate through each step.
        """
    )

    st.success("You're ready to get started! Use the sidebar to move to the Data Upload page.")

# For testing independently (optional)
if __name__ == "__main__":
    app()
