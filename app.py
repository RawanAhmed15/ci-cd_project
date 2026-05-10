import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="ITI Data Profiler", layout="wide")

st.title("🚀 ITI CICD Project: Professional Data Profiler")
st.markdown("---")

# أولاً: بنحاول نقرأ ملف الداتا اللي جاي مع المشروع
default_data = "data.csv"

if os.path.exists(default_data):
    df_default = pd.read_csv(default_data)
    st.subheader("✅ Sample Data Loaded (data.csv)")
    st.dataframe(df_default.head())

st.sidebar.header("Operations")
uploaded_file = st.sidebar.file_uploader("Upload another CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Analyzed Data View")
    st.write(df)
    
    st.subheader("📈 Quick Statistics")
    st.write(df.describe())
    
    st.success("Analysis complete!")