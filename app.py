import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="홈앤쇼핑 일일 매출 현황",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 커스텀 스타일
st.markdown("""
<style>
* {
    font-family: 'Malgun Gothic', 'AppleGothic', 'NanumGothic', sans-serif;
}
body {
    background-color: #F8F9FA;
}
[data-testid="metric-container"] {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# Supabase REST API에서 데이터 로드
@st.cache_data(ttl=10)
def load_data():
    import requests

    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]

    # Supabase REST API를 통해 데이터 조회
    headers = {
        "apikey": key,
        "Content-Type": "application/json"
    }

    api_url = f"{url}/rest/v1/daily_sales_data?order=date.asc"
    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        st.error(f"데이터 조회 실패: {response.status_code}")
        return None

    data = response.json()

    # DataFrame으로 변환
    df = pd.DataFrame(data)

    # 컬럼명 한글로 변환
    df = df.rename(columns={
        'date': '날짜',
        'visitors': '방문자수',
        'pv': 'PV',
        'orders': '주문건수',
        'conversion_rate': '주문전환율(%)',
        'net_payment': '순결제금액',
        'total_payment': '결제금액'
    })

    # 날짜를 datetime으로 변환
    df['날짜'] = pd.to_datetime(df['날짜'])

    # 불필요한 컬럼 제거
    df = df.drop(['id', 'created_at'], axis=1, errors='ignore')

    return df

def fmt_won(value):
    """원화 포맷 함수"""
    return f"₩{value:,}"

# 데이터 로드
df = load_data()

# 오늘과 어제 데이터
today_sales = df.iloc[-1]['결제금액']
yesterday_sales = df.iloc[-2]['결제금액']
delta = today_sales - yesterday_sales
delta_pct = (delta / yesterday_sales) * 100

# 페이지 제목
st.title("홈앤쇼핑 일일 매출 현황")

# 메트릭 카드 (3개 컬럼)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="오늘 매출",
        value=fmt_won(today_sales),
        label_visibility="visible"
    )

with col2:
    st.metric(
        label="어제 매출",
        value=fmt_won(yesterday_sales),
        label_visibility="visible"
    )

with col3:
    st.metric(
        label="어제 대비 증감률",
        value=f"{delta_pct:+.2f}%",
        delta=f"{delta_pct:+.2f}%",
        label_visibility="visible"
    )

st.divider()

# 차트 영역 (2컬럼)
chart_col1, chart_col2 = st.columns(2)

# 선 차트: 일별 매출 추이
with chart_col1:
    st.subheader("일별 매출 추이")

    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(
        x=df['날짜'],
        y=df['결제금액'],
        mode='lines+markers',
        name='결제금액',
        line=dict(color='#2E86AB', width=3),
        marker=dict(size=5, color='#2E86AB'),
        hovertemplate='<b>%{x|%Y-%m-%d}</b><br>매출: ₩%{y:,}<extra></extra>'
    ))

    fig_line.update_layout(
        title=None,
        xaxis_title="날짜",
        yaxis_title="결제금액 (원)",
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='white',
        font=dict(family="Malgun Gothic, AppleGothic, NanumGothic, sans-serif", size=12),
        height=400,
        margin=dict(l=50, r=20, t=20, b=50)
    )
    fig_line.update_yaxes(gridcolor='#E8E8E8')

    st.plotly_chart(fig_line, use_container_width=True)

# 원 차트: 최근 10일 PV 비중
with chart_col2:
    st.subheader("최근 10일 PV 비중")

    recent_10 = df.tail(10).copy()
    recent_10['날짜_label'] = recent_10['날짜'].dt.strftime('%m/%d')

    fig_pie = go.Figure()
    fig_pie.add_trace(go.Pie(
        labels=recent_10['날짜_label'],
        values=recent_10['PV'],
        hole=0.4,
        marker=dict(
            colors=['#6B9FB6', '#A8C5DD', '#5B8AC5', '#8BA8C7', '#7A9BC4',
                   '#9CBCCF', '#4F7BA8', '#6D92BA', '#7FA3C2', '#5A8AB8'],
            line=dict(color='white', width=2)
        ),
        hovertemplate='<b>%{label}</b><br>PV: %{value:,}<br>비중: %{percent}<extra></extra>'
    ))

    fig_pie.update_layout(
        title=None,
        font=dict(family="Malgun Gothic, AppleGothic, NanumGothic, sans-serif", size=11),
        height=400,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor='white'
    )

    st.plotly_chart(fig_pie, use_container_width=True)

# 하단 데이터 테이블 (옵션)
st.divider()
with st.expander("상세 데이터 보기"):
    display_df = df.copy()
    display_df['날짜'] = display_df['날짜'].dt.strftime('%Y-%m-%d')
    display_df['방문자수'] = display_df['방문자수'].apply(lambda x: f"{x:,}")
    display_df['PV'] = display_df['PV'].apply(lambda x: f"{x:,}")
    display_df['주문건수'] = display_df['주문건수'].apply(lambda x: f"{x:,}")
    display_df['순결제금액'] = display_df['순결제금액'].apply(fmt_won)
    display_df['결제금액'] = display_df['결제금액'].apply(fmt_won)
    st.dataframe(display_df, use_container_width=True, hide_index=True)
