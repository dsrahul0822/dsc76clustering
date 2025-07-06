import streamlit as st
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
import pandas as pd

def app():
    st.title("🔧 Apply Clustering Algorithm")

    # Load scaled data and selected features
    if "cluster_data" not in st.session_state or "selected_features" not in st.session_state:
        st.warning("⚠️ Please complete column selection first.")
        return

    X = st.session_state["cluster_data"]
    selected_features = st.session_state["selected_features"]

    # Algorithm selection
    algo = st.selectbox("Select Clustering Algorithm:", ["KMeans", "Hierarchical"])

    # Common hyperparameter: number of clusters
    n_clusters = st.slider("Select number of clusters (k):", min_value=2, max_value=10, value=3)

    if algo == "KMeans":
        init_method = st.selectbox("Select Init Method:", ["k-means++", "random"])
        model = KMeans(n_clusters=n_clusters, init=init_method, random_state=42, n_init=10)
    else:
        model = AgglomerativeClustering(n_clusters=n_clusters)

    # Perform clustering
    if st.button("Run Clustering"):
        labels = model.fit_predict(X)

        # Store labels in original df
        df = st.session_state["raw_data"].copy()
        df["cluster"] = labels
        st.session_state["clustered_df"] = df
        st.session_state["cluster_labels"] = labels

        st.success("✅ Clustering Completed Successfully!")

        # Show silhouette score
        try:
            score = silhouette_score(X, labels)
            st.metric("Silhouette Score", round(score, 3))
        except Exception as e:
            st.warning(f"Couldn't calculate silhouette score: {e}")

        # Show few records with cluster labels
        st.write("### Preview with Cluster Labels")
        st.dataframe(df[selected_features + ["cluster"]].head())

    else:
        st.info("👆 Adjust settings and click 'Run Clustering' to start.")

# For testing directly
if __name__ == "__main__":
    app()
