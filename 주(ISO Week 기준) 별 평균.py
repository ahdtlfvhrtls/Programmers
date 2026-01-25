import pandas as pd

df = pd.read_csv('data2.csv')

# - 제거
df_valid = df[df['date'] != '-'].copy()

# 날짜 타입으로 변경
df_valid['date'] = pd.to_datetime(df_valid['date'])

# 행렬 조합
df_valid['clicks_A'] = df_valid['ads_clicked']
df_valid['clicks_B'] = df_valid['ads_clicked_versionB']

# 주단위 추출
df_valid['week'] = df_valid['date'].dt.isocalendar().week

# 주별 평균
weekly_group = df_valid.groupby('week').agg(
    avg_clicks_A=('clicks_A', 'mean'),
    avg_clicks_B=('clicks_B', 'mean')
)

# A > B 인것으로 필터
weekly_compare = weekly_group[weekly_group['avg_clicks_A'] > weekly_group['avg_clicks_B']]

print(weekly_group)
print("A > B Condition weeks:")
print(weekly_compare)