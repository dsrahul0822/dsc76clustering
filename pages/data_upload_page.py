import streamlit as st
import pandas as pd
import os

def app():
    st.title("📁 Upload Your CSV Data")

    st.markdown("Please upload a `.csv` file for clustering analysis.")

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state["raw_data"] = df  # Store in session for later use

            # Save it in the data folder
            os.makedirs("data", exist_ok=True)
            df.to_csv("data/uploaded_data.csv", index=False)

            st.success("✅ File uploaded and saved successfully!")
            st.write("### Preview of Uploaded Data:")
            st.dataframe(df.head())

            st.info(f"Shape of data: {df.shape[0]} rows × {df.shape[1]} columns")

        except Exception as e:
            st.error(f"❌ Error while reading the file: {e}")
    else:
        st.warning("⚠️ No file uploaded yet.")

# For direct test
if __name__ == "__main__":
    app()
