import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Home"
)
# make title and header
st.title("Top Pubs near your area")
st.header("Data details ")

# import the modified data 
df = pd.read_csv("modified_open_pubs.csv")

# print the data frame
st.dataframe(df.head(11))
st.subheader('The total number of rows in the data are :') 
total = df.count()[0]
st.text(total)