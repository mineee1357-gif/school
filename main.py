import streamlit as st

st.set_page_config(
    page_title="방배중학교 소개",
    page_icon="🏫",
    layout="wide"
)

st.title("🏫 방배중학교 소개")
st.subheader("서울특별시 서초구의 공립 중학교")

st.image(
    "https://images.unsplash.com/photo-1509062522246-3755977927d7?w=1200",
    use_container_width=True
)

menu = st.sidebar.radio(
    "메뉴",
    ["학교 소개", "학교 정보", "교육 목표", "학교 생활", "오시는 길"]
)

if menu == "학교 소개":
    st.header("학교 소개")

    st.write("""
방배중학교는 서울특별시 서초구에 위치한 공립 중학교입니다.

학생들이 올바른 인성과 창의성을 갖춘 미래 인재로 성장할 수 있도록
다양한 교육활동과 체험 프로그램을 운영하고 있습니다.

학교는 학업뿐 아니라 스포츠, 예술, 동아리 활동 등
학생들의 다양한 재능을 키울 수 있는 교육환경을 제공하고 있습니다.
""")

    st.success("배움과 꿈이 함께하는 행복한 학교")

elif menu == "학교 정보":

    st.header("학교 기본 정보")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("설립", "1980년")
        st.metric("학교 유형", "공립")
        st.metric("학교급", "중학교")

    with col2:
        st.metric("위치", "서울특별시 서초구")
        st.metric("학생 수", "약 770명")
        st.metric("교직원", "약 70명")

    st.info("""
주소 : 서울특별시 서초구 동광로 144

대표전화 : 02-532-1342
""")

elif menu == "교육 목표":

    st.header("교육 목표")

    st.markdown("""
### 🎯 목표

- 올바른 인성을 갖춘 학생
- 스스로 배우는 창의적인 학생
- 서로 존중하고 배려하는 학생
- 건강한 신체와 마음을 가진 학생
- 미래 사회를 준비하는 디지털 인재
""")

    st.progress(100)

elif menu == "학교 생활":

    st.header("학교 생활")

    tab1, tab2, tab3 = st.tabs(["📚 수업", "🎨 동아리", "⚽ 체육"])

    with tab1:
        st.write("""
- 국어
- 영어
- 수학
- 사회
- 과학
- 정보
- 음악
- 미술
- 기술가정
""")

    with tab2:
        st.write("""
다양한 자율동아리와 학생 자치 활동을 통해
학생들이 자신의 적성과 재능을 키울 수 있습니다.
""")

    with tab3:
        st.write("""
체육 활동과 학교 스포츠클럽을 통해
건강한 학교생활을 지원합니다.
""")

elif menu == "오시는 길":

    st.header("오시는 길")

    st.write("""
**주소**

서울특별시 서초구 동광로 144
""")

    st.markdown("""
### 학교 홈페이지

http://bangbae.sen.ms.kr
""")

st.divider()

st.caption("© 2026 Bangbae Middle School Introduction Website")
