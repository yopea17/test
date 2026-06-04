import streamlit as st

st.title("🎉 Streamlit 설치 성공!")
st.write("Streamlit이 정상적으로 작동합니다.")
st.write(f"현재 폴더: {st.session_state if 'test' not in st.session_state else 'OK'}")

# 간단한 상호작용 테스트
name = st.text_input("이름을 입력하세요:")
if name:
    st.write(f"안녕하세요, {name}님!")
