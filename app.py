import streamlit as st
import pandas as pd

st.write('Hello, *World!* :sunglasses:')
st.write('Hello, Stremlit!!')

df = pd.read_excel('data.xlsx')
st.dataframe(df)