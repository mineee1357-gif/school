import streamlit as pd
import pandas as pd
import plotly.express as px

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="국가별 MBTI 분포 현황",
    page_icon="📊",
    layout="wide"
)

# 2. 예시 데이터 생성 (실제 데이터가 있다면 이 부분을 변경하시면 됩니다)
@st.cache_data
def load_data():
    data = {
        'Country': ['South Korea', 'United States', 'Japan', 'Germany', 'United Kingdom', 'Brazil', 'France', 'Australia'],
        'Most_Common_MBTI': ['INFP', 'INFP', 'INFP', 'INFP', 'ENFP', 'ENFP', 'INFP', 'ENFP'],
        'Total_Sample': [15000, 45000, 22000, 18000, 25000, 30000, 19000, 14000],
        'Introvert_Ratio(%)': [62, 49, 68, 54, 47, 41, 56, 48],
        'Extravert_Ratio(%)': [38, 51, 32, 46, 53, 59, 44, 52]
    }
    return pd.DataFrame(data)

df = load_data()

# 3. 메인 타이틀 및 소개
st.title("🌍 글로벌 MBTI 분포 대시보드")
st.markdown("""
이 사이트는 전 세계 국가들의 MBTI 성격 유형 분포를 시각적으로 확인하기 위해 만들어졌습니다.
왼쪽 사이드바에서 원하는 국가를 선택하거나, 아래 차트에서 전반적인 트렌드를 확인해 보세요!
""")

st.divider()

# 4. 사이드바 - 국가 선택 필터
st.sidebar.header("🔍 필터 옵션")
selected_countries = st.sidebar.multiselect(
    "조회할 국가를 선택하세요:",
    options=df['Country'].unique(),
    default=df['Country'].unique()
)

# 필터링된 데이터
filtered_df = df[df['Country'].isin(selected_countries)]

# 5. 주요 지표 (Metrics) 표현
if not filtered_df.empty:
    st.subheader("📌 요약 통계")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="조회된 국가 수", value=f"{len(filtered_df)} 개국")
    with col2:
        # 가장 흔한 MBTI (가장 많이 등장한 유형)
        top_mbti = filtered_df
