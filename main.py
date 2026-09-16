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
# 앞으로 추가할 그래프 영역
# ========================================
st.divider()
st.header("그래프 4")

st.info("다음 그래프를 여기에 추가하세요.")
