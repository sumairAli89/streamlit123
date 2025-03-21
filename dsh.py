import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px

def main():
    st.title("📊 Data Visualization Dashboard")


uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  
    st.write("### Data Preview")
    st.dataframe(df)

    
    st.write("### Data Summary")
    st.write(df.describe())  

    
    st.write("### Missing Values")
    st.write(df.isnull().sum())

    
    column = st.selectbox("Select a column for Visualization", df.columns)

    
    st.write("### Matplotlib Bar Chart")
    fig, ax = plt.subplots()
    df[column].value_counts().plot(kind="bar", ax=ax, color="skyblue")
    st.pyplot(fig)

    
    st.write("### Seaborn Histogram")
    fig, ax = plt.subplots()  
    sns.histplot(df[column], bins=20, kde=True, ax=ax)
    st.pyplot(fig)


    st.write("### Plotly Pie Chart")
    fig = px.pie(df, names=column, title=f"Distribution of {column}")
    st.plotly_chart(fig)
    if __name__ == "__main__":
         main()

