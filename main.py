import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------

# 기본 설정

# ----------------------------------------

st.set_page_config(
page_title="영화 데이터 그래프 도감 1 - 시간",
page_icon="🎬",
layout="wide"
)

st.title("🎬 영화 데이터 그래프 도감 1 - 시간")
st.write("영화별 일별 관객수 변화를 살펴보는 그래프입니다.")

# ----------------------------------------

# 데이터 불러오기

# ----------------------------------------

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"

df = pd.read_csv(DATA_URL)

# 날짜를 진짜 날짜 형식으로 변환

df["날짜"] = pd.to_datetime(
df["날짜"].astype(str),
format="%Y%m%d"
)

# 일관객을 숫자형으로 변환

df["일관객"] = pd.to_numeric(
df["일관객"],
errors="coerce"
)

# ----------------------------------------

# 그래프 1

# ----------------------------------------

st.header("그래프 1. 영화별 날짜에 따른 일관객 변화")

movie_list = sorted(df["영화명"].dropna().unique())

selected_movie = st.selectbox(
"영화를 선택하세요",
movie_list
)

movie_df = (
df[df["영화명"] == selected_movie]
.sort_values("날짜")
)

fig1 = px.line(
movie_df,
x="날짜",
y="일관객",
markers=True,
title=f"「{selected_movie}」 날짜별 일관객 변화",
labels={
"날짜": "날짜",
"일관객": "일관객 수"
}
)

fig1.update_traces(
hovertemplate="날짜: %{x|%Y-%m-%d}<br>일관객: %{y:,}명<extra></extra>"
)

fig1.update_layout(
xaxis_title="날짜",
yaxis_title="일관객 수(명)",
hovermode="x unified"
)

st.plotly_chart(
fig1,
width="stretch"
)

# ----------------------------------------

# 그래프 1에서 알 수 있는 것

# ----------------------------------------

st.markdown("### 이 그래프로 알 수 있는 것")
st.info("여기에 이 그래프로 알 수 있는 내용을 작성하세요.")

# ========================================

# 그래프 2

# ========================================

st.divider()
st.header("그래프 2. 일관객 합계가 가장 큰 영화 5편의 변화")

# 영화별 전체 기간 일관객 합계 계산

movie_total = (
df.groupby("영화명", as_index=False)["일관객"]
.sum()
.sort_values("일관객", ascending=False)
)

# 일관객 합계가 가장 큰 5편 선택

top5_movies = movie_total.head(5)["영화명"].tolist()

# 상위 5편의 날짜별 일관객 데이터만 추출

top5_df = (
df[df["영화명"].isin(top5_movies)]
.sort_values(["날짜", "영화명"])
)

fig2 = px.line(
top5_df,
x="날짜",
y="일관객",
color="영화명",
markers=True,
title="일관객 합계가 가장 큰 5편의 날짜별 일관객",
labels={
"날짜": "날짜",
"일관객": "일관객 수",
"영화명": "영화"
}
)

fig2.update_traces(
hovertemplate="날짜: %{x|%Y-%m-%d}<br>일관객: %{y:,}명<extra>%{fullData.name}</extra>"
)

fig2.update_layout(
xaxis_title="날짜",
yaxis_title="일관객 수(명)",
hovermode="x unified",
legend_title="영화"
)

st.plotly_chart(
fig2,
width="stretch"
)

# ----------------------------------------

# 그래프 2에서 알 수 있는 것

# ----------------------------------------

st.markdown("### 이 그래프로 알 수 있는 것")
st.info("여기에 이 그래프로 알 수 있는 내용을 작성하세요.")

# ========================================

# 그래프 3

# 앞으로 추가할 그래프 영역

# ========================================

st.divider()
st.header("그래프 3")

st.info("다음 그래프를 여기에 추가하세요.")

# ========================================

# 그래프 4

# 앞으로 추가할 그래프 영역

# ========================================

st.divider()
st.header("그래프 4")

st.info("다음 그래프를 여기에 추가하세요.")
