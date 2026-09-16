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
# ========================================
st.divider()
st.header("그래프 3. 날짜별 10위권 일관객 합계")

# 날짜별 10위권 일관객 합계 계산
daily_total = (
    df.groupby("날짜", as_index=False)["일관객"]
    .sum()
    .sort_values("날짜")
)

# 일관객 합계가 가장 큰 3일
top3_days = (
    daily_total
    .nlargest(3, "일관객")
    .sort_values("날짜")
)

fig3 = px.area(
    daily_total,
    x="날짜",
    y="일관객",
    title="날짜별 10위권 일관객 합계",
    labels={
        "날짜": "날짜",
        "일관객": "10위권 일관객 합계"
    }
)

# 마우스를 올렸을 때 날짜와 합계 표시
fig3.update_traces(
    hovertemplate="날짜: %{x|%Y-%m-%d}<br>"
                  "10위권 일관객 합계: %{y:,}명<extra></extra>"
)

# 가장 큰 3일을 그래프 위에 표시
for _, row in top3_days.iterrows():
    fig3.add_annotation(
        x=row["날짜"],
        y=row["일관객"],
        text=f"{row['날짜'].strftime('%Y-%m-%d')}",
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-45
    )

fig3.update_layout(
    xaxis_title="날짜",
    yaxis_title="10위권 일관객 합계(명)",
    hovermode="x unified"
)

st.plotly_chart(
    fig3,
    width="stretch"
)

# ----------------------------------------
# 그래프 3에서 알 수 있는 것
# ----------------------------------------
st.markdown("### 이 그래프로 알 수 있는 것")
st.info("여기에 이 그래프로 알 수 있는 내용을 작성하세요.")


# ========================================
# 그래프 4
# ========================================
st.divider()
st.header("그래프 4. 기간 내 일관객 TOP 10 영화")

# 영화별 일관객 합계와 10위권 기록 일수 계산
movie_summary = (
    df.groupby("영화명")
    .agg(
        일관객합계=("일관객", "sum"),
        기록일수=("날짜", "nunique")
    )
    .reset_index()
)

# 일관객 합계가 가장 많은 TOP 10
top10_movies = (
    movie_summary
    .sort_values("일관객합계", ascending=False)
    .head(10)
    .sort_values("일관객합계", ascending=True)
)

fig4 = px.bar(
    top10_movies,
    x="일관객합계",
    y="영화명",
    orientation="h",
    title="기간 내 일관객 TOP 10 영화",
    labels={
        "일관객합계": "기간 내 일관객 합계",
        "영화명": "영화"
    },
    hover_data={
        "일관객합계": ":,",
        "기록일수": ":,"
    }
)

# 마우스를 올렸을 때 일관객 합계와 10위권 기록 일수 표시
fig4.update_traces(
    hovertemplate="영화: %{y}<br>"
                  "일관객 합계: %{x:,}명<br>"
                  "10위권에 든 날수: %{customdata[0]}일"
)

fig4.update_layout(
    xaxis_title="일관객 합계(명)",
    yaxis_title="영화",
    yaxis={
        "categoryorder": "total ascending"
    }
)

st.plotly_chart(
    fig4,
    width="stretch"
)

# ----------------------------------------
# 그래프 4에서 알 수 있는 것
# ----------------------------------------
st.markdown("### 이 그래프로 알 수 있는 것")
st.info("여기에 이 그래프로 알 수 있는 내용을 작성하세요.")
# ========================================
# 그래프 5
# ========================================
st.divider()
st.header("그래프 5. 월 × 요일별 일관객 합계")

# 날짜에서 월과 요일 추출
heatmap_df = df.copy()

heatmap_df["월"] = heatmap_df["날짜"].dt.month

# 요일을 한글로 변환
weekday_map = {
    0: "월요일",
    1: "화요일",
    2: "수요일",
    3: "목요일",
    4: "금요일",
    5: "토요일",
    6: "일요일"
}

heatmap_df["요일"] = heatmap_df["날짜"].dt.weekday.map(weekday_map)

# 월 × 요일별 일관객 합계
heatmap_data = (
    heatmap_df
    .groupby(["월", "요일"])["일관객"]
    .sum()
    .reset_index()
)

# 피벗 테이블 생성
heatmap_data = heatmap_data.pivot(
    index="월",
    columns="요일",
    values="일관객"
)

# 요일 순서 지정
weekday_order = [
    "월요일",
    "화요일",
    "수요일",
    "목요일",
    "금요일",
    "토요일",
    "일요일"
]

heatmap_data = heatmap_data.reindex(
    columns=weekday_order
)

# 월 순서 지정
heatmap_data = heatmap_data.reindex(
    range(1, 13)
)

# 히트맵
fig5 = px.imshow(
    heatmap_data,
    labels={
        "x": "요일",
        "y": "월",
        "color": "일관객 합계"
    },
    x=weekday_order,
    y=[f"{month}월" for month in heatmap_data.index],
    aspect="auto",
    text_auto=",.0f",
    color_continuous_scale="Blues",
    title="월 × 요일별 10위권 일관객 합계"
)

fig5.update_traces(
    hovertemplate=
    "%{y} %{x}<br>"
    "일관객 합계: %{z:,}명"
    "<extra></extra>"
)

fig5.update_layout(
    xaxis_title="요일",
    yaxis_title="월",
    coloraxis_colorbar_title="일관객 합계"
)

st.plotly_chart(
    fig5,
    width="stretch"
)

# ----------------------------------------
# 그래프 5에서 알 수 있는 것
# ----------------------------------------
st.markdown("### 이 그래프로 알 수 있는 것")
st.info("여기에 이 그래프로 알 수 있는 내용을 작성하세요.")


# ========================================
# 그래프 6
# 앞으로 추가할 그래프 영역
# ========================================
st.divider()
st.header("그래프 6")

st.info("다음 그래프를 여기에 추가하세요.")
