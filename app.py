import streamlit as st
import pandas as pd

st.write('Hello, *World!* :sunglasses:')
st.write('Hello, Stremlit!!')

df = pd.read_excel('수업설문.xlsx')
st.dataframe(df)