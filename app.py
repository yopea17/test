import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="대시보드", layout="wide")

st.title("📊 Streamlit 대시보드")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("총 사용자", 1234, "+12%")

with col2:
    st.metric("방문자", 5678, "+5%")

with col3:
    st.metric("매출", "$45,200", "+8%")

st.markdown("---")

st.subheader("📈 일일 데이터")

dates = pd.date_range(start=datetime.now() - timedelta(days=30), periods=30)
data = pd.DataFrame({
    '날짜': dates,
    '방문자': np.random.randint(100, 500, 30),
    '전환율': np.random.uniform(0.5, 5, 30)
})

st.line_chart(data.set_index('날짜')['방문자'])

st.markdown("---")

st.subheader("📋 최근 데이터")
st.dataframe(data, use_container_width=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("카테고리별 분포")
    categories = pd.DataFrame({
        '카테고리': ['A', 'B', 'C', 'D'],
        '값': [30, 25, 20, 25]
    })
    st.bar_chart(categories.set_index('카테고리')['값'])

with col2:
    st.subheader("비율")
    st.write("각 카테고리의 비율을 확인하세요")
    st.pie_chart(categories.set_index('카테고리')['값'])

st.markdown("---")
st.success("✅ 대시보드가 정상 작동 중입니다!")
