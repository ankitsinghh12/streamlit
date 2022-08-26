import streamlit as st

st.title("Welcome to my Dashboard")

st.header("This is a Header")

st.subheader("This is SubHeader")

st.markdown("This is a markdown")

st.text("This is the text")

code_snippet = '''

import streamlit as st

st.title("Welcome to my Dashboard")

st.header("This is a Header")

st.subheader("This is SubHeader")

st.markdown("This is a markdown")

st.text("This is the text")



'''

button_click = st.button('show Code')

if button_click == True:
    st.code(code_snippet)

