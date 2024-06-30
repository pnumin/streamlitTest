import streamlit as st
import pandas as pd

st.write('Hello, *World!* :sunglasses:')
st.write('Hello, Stremlit!!')

# 사이드바에 파일 업로드 기능 추가
uploaded_file = st.sidebar.file_uploader("Excel 파일 업로드", type=["xlsx"])