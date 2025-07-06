import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def app():
    st.title("🧮 Column Selection & Elbow Method")

    # Step 1: Load uploaded data
    if "raw_data" not in st.session_state:
        st.warning("⚠️ Please upload the data first.")
        return

    df = st.session_state["raw_data"]

    # Step 2: Select numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if not numeric_cols:
        st.error("❌ No numeric columns available for clustering.")
        return

    selected_cols = st.multiselect("Select columns for clustering (numeric only):", numeric_cols)

    if selected_cols:
        X = df[selected_cols]

        # Step 3: Standardize data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Step 4: Elbow method
        st.markdown("### 🔍 Elbow Method to find optimal clusters")
        wcss = []
        k_range = range(1, 11)

        for k in k_range:
            kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
            kmeans.fit(X_scaled)
            wcss.append(kmeans.inertia_)

        # Plot Elbow Curve
        fig, ax = plt.subplots()
        ax.plot(k_range, wcss, marker='o')
        ax.set_xlabel('Number of clusters (k)')
        ax.set_ylabel('WCSS (Inertia)')
        ax.set_title('Elbow Method For Optimal k')
        st.pyplot(fig)

        # Store for next step
        st.session_state["cluster_data"] = X_scaled
        st.session_state["selected_features"] = selected_cols

    else:
        st.info("ℹ️ Please select at least one column to proceed.")

# For direct testing
if __name__ == "__main__":
    app()
