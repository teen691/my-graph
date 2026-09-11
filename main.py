import pandas as pd
import plotly.express as px
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="영화 데이터 그래프 도감 1 - 시간",
    layout="wide",
)

st.title("🎬 영화 데이터 그래프 도감 1 - 시간")


# 데이터 로드 및 전처리 함수 (캐싱 적용)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"
    df = pd.read_csv(url)

    # 날짜 열을 datetime 형식으로 변환 (YYYYMMDD)
    df["날짜"] = pd.to_datetime(df["날짜"].astype(str), format="%Y%m%d")

    return df


# 데이터 불러오기
df = load_data()

st.markdown("---")

# -------------------------------------------------------------------
# 구역 1: 영화별 일관객 변화
# -------------------------------------------------------------------
st.header("1. 영화별 일일 관객수 추이")

# 영화 목록 추출 및 선택 드롭다운
movie_list = sorted(df["영화명"].unique())
selected_movie = st.selectbox(
    "관람객 추이를 확인할 영화를 선택하세요:", movie_list
)

# 선택한 영화의 데이터 필터링
filtered_df = df[df["영화명"] == selected_movie].sort_values("날짜")

# Plotly 선 그래프 생성
fig1 = px.line(
    filtered_df,
    x="날짜",
    y="일관객",
    title=f"<{selected_movie}> 일별 관객수 변화",
    labels={"날짜": "날짜", "일관객": "일일 관객수 (명)"},
    hover_data={"날짜": "|%Y-%m-%d", "일관객": ":,d"},
    markers=True,
)

fig1.update_layout(hovermode="x unified")

# 그래프 출력
st.plotly_chart(fig1, use_container_width=True)

# 그래프 해석 문구 자리
st.info("💡 **이 그래프로 알 수 있는 것:** 여에 작성할 내용을 입력하세요.")

st.markdown("---")

# -------------------------------------------------------------------
# 구역 2: (추가 예정 그래프 구역)
# -------------------------------------------------------------------
st.header("2. 추가 그래프 구역")
st.text("새로운 시간 관련 그래프가 들어갈 자리입니다.")

# st.info("💡 **이 그래프로 알 수 있는 것:** 여기에 작성할 내용을 입력하세요.")
