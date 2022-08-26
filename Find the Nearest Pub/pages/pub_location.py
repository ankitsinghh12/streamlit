import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Pub_location"
)

df = pd.read_csv("modified open_pubs.csv")
# make title and header
st.title(" Top Pubs near your area ")
st.header("The map based on the local_authority and postcode given in the text box below: ")
# enter either postal code or local authority

local_auth = st.selectbox('The local authority of the area which you want to search', set(df['local_authority']))
button_1 = st.button("Submit Local Authority")

if button_1:

    df_new = df.loc[(df['local_authority'] == local_auth)]
    st.text("Top pubs in this region are:")
    st.dataframe(df_new)
    st.map(df_new)