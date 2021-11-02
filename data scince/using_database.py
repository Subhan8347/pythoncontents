import streamlit as st

sidebar = st.sidebar

sidebar.header("Add Smart phone Data here")
sidebar.markdown('_ _ _')

brand = sidebar.text_input('Brand')
name = sidebar.text_input('Name')
price = sidebar.text_input('Price')
ram = sidebar.text_input('Ram')
storage = sidebar.text_input('Storage')