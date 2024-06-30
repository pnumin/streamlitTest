import streamlit as st
import pandas as pd 

st.write('Hello, *World!* :sunglasses:')
st.write('Hello, Stremlit!!')

# 사이드바에 파일 업로드 기능 추가
uploaded_file = st.sidebar.file_uploader("파일 업로드", type=["csv"])

if uploaded_file is not None:
    # csv 파일 읽기
    data = pd.read_csv(uploaded_file, encoding='cp949')

    st.write("업로드한 데이터:")
    st.write(data)

    # 데이터프레임 정보 표시
    st.write("데이터프레임 정보:")
    st.write(data.describe())
 
else:
    st.write("Excel 파일을 업로드해주세요.")