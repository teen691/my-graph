import streamlit as st
import pandas as pd
import plotly.express as px

st.title("영화 데이터 분석 Dashboard")

# 1. 파일 업로드 (경로 에러 방지)
uploaded_file = st.file_uploader("영화 데이터 CSV 파일을 업로드하세요.", type=["csv"])

if uploaded_file is not None:
    # 데이터 불러오기
    df = pd.read_csv(uploaded_file)
    df['날짜'] = pd.to_datetime(df['날짜'])

    # ---------------------------------------------------------
    # 두 번째 그래프: 상위 5개 영화 날짜별 일관객수 추이
    # ---------------------------------------------------------
    st.subheader("상위 5개 영화 날짜별 일관객수 추이")

    # 1. 기간 내 일관객 합계 기준 상위 5개 영화 추출
    top5_movies = df.groupby('영화명')['일별관객수'].sum().nlargest(5).index

    # 2. 상위 5개 영화 데이터 필터링 및 날짜 순 정렬
    df_top5 = df[df['영화명'].isin(top5_movies)].sort_values('날짜')

    # 3. Plotly 대화형 선 그래프 생성
    fig2 = px.line(
        df_top5,
        x='날짜',
        y='일별관객수',
        color='영화명',
        title='관객수 상위 5개 영화 일별 추이',
        labels={'날짜': '날짜', '일별관객수': '일별 관객수(명)', '영화명': '영화 제목'}
    )

    # 4. 범례 및 호버 레이아웃 설정
    fig2.update_layout(
        xaxis_title='날짜',
        yaxis_title='일별 관객수',
        legend_title='영화 목록 (클릭하여 토글)',
        hovermode='x unified'
    )

    # 5. Streamlit 화면 출력
    st.plotly_chart(fig2, use_container_width=True)

else:
    st.info("좌측 또는 상단 버튼을 통해 CSV 파일을 업로드해 주세요.")
