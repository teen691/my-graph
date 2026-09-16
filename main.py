import pandas as pd
import plotly.express as px

# 1. 해당 기간 일관객 합계 기준 상위 5개 영화 추출
top5_movies = df.groupby('영화명')['일별관객수'].sum().nlargest(5).index

# 2. 상위 5개 영화 데이터 필터링 및 날짜 정렬
df_top5 = df[df['영화명'].isin(top5_movies)].sort_values('날짜')

# 3. Plotly 선 그래프 생성
fig2 = px.line(
    df_top5,
    x='날짜',
    y='일별관객수',
    color='영화명',
    title='상위 5개 영화 날짜별 일관객수 추이',
    labels={'날짜': '날짜', '일별관객수': '일별 관객수(명)', '영화명': '영화 제목'}
)

# 4. 레이아웃 및 범례 인터랙션 설정
fig2.update_layout(
    xaxis_title='날짜',
    yaxis_title='일별 관객수',
    legend_title='영화 목록 (클릭하여 토글)',
    hovermode='x unified'  # 마우스 오버 시 동일 날짜 데이터 비교
)

# 그래프 출력 (Jupyter Notebook 또는 HTML 저장)
fig2.show()
