import streamlit as st
import pandas as pd
import plotly.express as px
import io

# 1. 페이지 기본 설정 및 디자인
st.set_page_config(
    page_title="Global MBTI Explorer",
    page_icon="🌏",
    layout="wide"
)

# 커스텀 CSS로 스타일링
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    h1 {
        color: #1e293b;
        font-family: 'Inter', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 데이터 로드
@st.cache_data
def load_data():
    csv_data = """Country,INFJ,ISFJ,INTP,ISFP,ENTP,INFP,ENTJ,ISTP,INTJ,ESFP,ESTJ,ENFP,ESTP,ISTJ,ENFJ,ESFJ
Afghanistan,0.0463,0.061,0.0549,0.046,0.0495,0.0686,0.0511,0.0434,0.0431,0.0527,0.1188,0.0796,0.0652,0.0629,0.0562,0.1006
Albania,0.0748,0.0449,0.0754,0.0334,0.0792,0.1045,0.0686,0.0233,0.0604,0.0405,0.0667,0.1045,0.0381,0.0418,0.0775,0.0665
Algeria,0.08,0.0337,0.141,0.0377,0.0739,0.1556,0.0535,0.033,0.0896,0.0279,0.0327,0.0857,0.0241,0.032,0.0556,0.044
Andorra,0.0791,0.0465,0.0512,0.0419,0.0372,0.1674,0.0465,0.0186,0.0326,0.0372,0.0605,0.1767,0.0187,0.0279,0.1163,0.0651
Angola,0.0771,0.0717,0.0564,0.0403,0.0448,0.1112,0.0492,0.0322,0.0466,0.0547,0.0592,0.0798,0.0368,0.0404,0.0807,0.1192
Antigua and Barbuda,0.0848,0.0853,0.0632,0.0592,0.047,0.1381,0.0279,0.0308,0.0328,0.0548,0.0421,0.1092,0.0245,0.0431,0.0632,0.094
Argentina,0.0884,0.044,0.106,0.0416,0.0544,0.1875,0.0309,0.0255,0.0652,0.0366,0.0245,0.1338,0.0174,0.0342,0.0625,0.0476
Armenia,0.0735,0.0472,0.0839,0.0268,0.0821,0.1138,0.0689,0.0197,0.069,0.0262,0.074,0.1057,0.027,0.0399,0.0792,0.0629
Australia,0.0772,0.0826,0.0478,0.0583,0.0391,0.15,0.0215,0.0202,0.0273,0.0587,0.0355,0.1483,0.0212,0.0304,0.0778,0.1038
Austria,0.0809,0.046,0.0906,0.0378,0.0657,0.1732,0.0347,0.0221,0.0525,0.0367,0.0384,0.1437,0.0226,0.0334,0.0664,0.0553
Azerbaijan,0.0603,0.0561,0.0804,0.0372,0.0663,0.1062,0.0571,0.0285,0.0528,0.0471,0.0857,0.0856,0.0308,0.0578,0.0742,0.0735
Bahamas,0.0847,0.0843,0.0633,0.0559,0.0483,0.132,0.0312,0.0318,0.0416,0.0341,0.0469,0.1077,0.0238,0.0535,0.0702,0.0906
Bahrain,0.076,0.0597,0.0564,0.047,0.051,0.1367,0.0419,0.0234,0.0394,0.051,0.0513,0.1339,0.03,0.03,0.0826,0.0898
Bangladesh,0.0697,0.06,0.0771,0.069,0.0449,0.1498,0.0295,0.0358,0.0418,0.0585,0.0442,0.1041,0.0314,0.0366,0.0639,0.0839
Barbados,0.0911,0.101,0.0642,0.0517,0.0408,0.1497,0.0277,0.0272,0.0498,0.0398,0.0382,0.0954,0.0244,0.0486,0.0669,0.0836
Belarus,0.0609,0.0524,0.1052,0.0412,0.0704,0.1135,0.0452,0.0468,0.0678,0.029,0.063,0.0941,0.0346,0.0664,0.0519,0.058
Belgium,0.0761,0.0563,0.0771,0.0414,0.061,0.1708,0.0297,0.0209,0.0383,0.0444,0.036,0.16,0.0237,0.0288,0.0664,0.0691
Belize,0.0831,0.0786,0.0599,0.0529,0.0472,0.1416,0.0217,0.022,0.0446,0.0583,0.037,0.1184,0.0299,0.039,0.0732,0.0925
Bhutan,0.0646,0.0758,0.0526,0.0625,0.0232,0.1566,0.026,0.014,0.0189,0.0688,0.0597,0.139,0.0119,0.0238,0.0653,0.1369
Brazil,0.0938,0.049,0.0977,0.0383,0.0502,0.189,0.0275,0.0253,0.0645,0.0323,0.0278,0.1336,0.0186,0.0394,0.0631,0.0498
Canada,0.0843,0.0838,0.0592,0.0553,0.046,0.1574,0.0259,0.0229,0.035,0.0476,0.0356,0.1344,0.0221,0.0356,0.0721,0.0826
Chile,0.0935,0.046,0.1041,0.0396,0.0503,0.1963,0.0265,0.027,0.0672,0.0309,0.0254,0.1321,0.016,0.0369,0.0615,0.0468
China,0.056,0.0952,0.0571,0.0841,0.0435,0.1063,0.0303,0.0359,0.0374,0.0681,0.0541,0.0943,0.032,0.0474,0.0569,0.1016
Colombia,0.069,0.0437,0.0861,0.0354,0.06,0.1372,0.0402,0.0226,0.0527,0.0452,0.043,0.1379,0.0249,0.0333,0.0844,0.0844
South Korea,0.0625,0.0766,0.0628,0.0661,0.0504,0.1339,0.0273,0.0311,0.0375,0.0636,0.0456,0.126,0.0294,0.0428,0.0609,0.0835
"""
    df = pd.read_csv(io.StringIO(csv_data))
    # 수치 데이터를 백분율로 변환 (보기 좋게)
    mbti_cols = df.columns[1:]
    df[mbti_cols] = df[mbti_cols] * 100
    return df

df = load_data()
mbti_types = list(df.columns[1:])

# 3. 사이드바 구성
st.sidebar.title("🎮 Analysis Menu")
menu = st.sidebar.radio("Go to", ["Global Overview", "Country Search", "Comparison Tool", "Type Rankings"])

# --- PAGE 1: Global Overview ---
if menu == "Global Overview":
    st.title("🌏 Global MBTI Distribution Overview")
    st.markdown("전 세계 국가별 MBTI 분포 데이터를 한눈에 확인하세요.")
    
    # 요약 지표
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Countries", len(df))
    col2.metric("Most Rare Type (Avg)", "ENTJ")
    col3.metric("Most Common Type (Avg)", "INFP")

    st.subheader("Raw Data (Values in %)")
    st.dataframe(df.style.format(precision=2), use_container_width=True)

# --- PAGE 2: Country Search ---
elif menu == "Country Search":
    st.title("🔍 Country Specific Analysis")
    
    target_country = st.selectbox("Select a Country", df['Country'].unique())
    country_data = df[df['Country'] == target_country].iloc[0]
    
    # 막대 그래프 시각화
    plot_df = pd.DataFrame({
        'MBTI Type': mbti_types,
        'Percentage (%)': country_data[mbti_types].values
    }).sort_values(by='Percentage (%)', ascending=False)
    
    fig = px.bar(plot_df, x='MBTI Type', y='Percentage (%)', 
                 color='Percentage (%)', title=f"MBTI Distribution in {target_country}",
                 color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)
    
    # 가장 높은 타입 3개
    top_3 = plot_df.head(3)
    st.subheader(f"Top 3 Types in {target_country}")
    cols = st.columns(3)
    for i, (idx, row) in enumerate(top_3.iterrows()):
        cols[i].metric(f"Rank {i+1}", row['MBTI Type'], f"{row['Percentage (%)']:.2f}%")

# --- PAGE 3: Comparison Tool ---
elif menu == "Comparison Tool":
    st.title("⚔️ Country Comparison")
    
    col1, col2 = st.columns(2)
    c1 = col1.selectbox("Country A", df['Country'].unique(), index=0)
    c2 = col2.selectbox("Country B", df['Country'].unique(), index=24) # Default to South Korea if list allows
    
    data_a = df[df['Country'] == c1].iloc[0][mbti_types]
    data_b = df[df['Country'] == c2].iloc[0][mbti_types]
    
    comp_df = pd.DataFrame({
        'MBTI': mbti_types * 2,
        'Percentage (%)': list(data_a.values) + list(data_b.values),
        'Country': [c1] * len(mbti_types) + [c2] * len(mbti_types)
    })
    
    fig = px.bar(comp_df, x='MBTI', y='Percentage (%)', color='Country', barmode='group',
                 title=f"Comparison: {c1} vs {c2}")
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 4: Type Rankings ---
elif menu == "Type Rankings":
    st.title("🏆 Type Leaderboard")
    selected_type = st.selectbox("Select MBTI Type to Rank Countries", mbti_types)
    
    rank_df = df[['Country', selected_type]].sort_values(by=selected_type, ascending=False)
    
    fig = px.bar(rank_df.head(15), x='Country', y=selected_type, 
                 title=f"Top 15 Countries with highest {selected_type} population",
                 labels={selected_type: 'Percentage (%)'},
                 color=selected_type)
    st.plotly_chart(fig, use_container_width=True)
    
    st.write(f"**{selected_type}** 유형이 가장 많은 국가는 **{rank_df.iloc[0]['Country']}**이며, 전체의 **{rank_df.iloc[0][selected_type]:.2f}%**를 차지합니다.")

# 하단 푸터
st.sidebar.markdown("---")
st.sidebar.info("Data source provided by user. Developed with Streamlit.")
