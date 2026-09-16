import pandas as pd
import plotly.express as px
import streamlit as st

# 1. 데이터 불러오기 (예시: CSV 파일을 읽어오는 경우)
# 실제 데이터 파일 경로나 생성 방식에 맞게 수정해주세요.
df = pd.read_csv('movie_data.csv') 

# 2. 상위 5개 영화 추출
top5_movies = df.groupby('영화명')['일별관객수'].sum().nlargest(5).index

# 3. 데이터 필터링 및 날짜 정렬
df_top5 = df[df['영화명'].isin(top5_movies)].sort_values('날짜')

# 4. Plotly 선 그래프 생성
fig2 = px.line(
    df_top5,
    x='날짜',
    y='일별관객수',
    color='영화명',
    title='상위 5개 영화 날짜별 일관객수 추이',
    labels={'날짜': '날짜', '일별관객수': '일별 관객수(명)', '영화명': '영화 제목'}
)

# 5. 레이아웃 설정 및 Streamlit 출력
fig2.update_layout(
    xaxis_title='날짜',
    yaxis_title='일별 관객수',
    legend_title='영화 목록 (클릭하여 토글)',
    hovermode='x unified'
)

st.plotly_chart(fig2, use_container_width=True)
