import pandas as pd

df = pd.read_csv('data2.csv')

# - 제거
df_valid = df[df['date'] != '-'].copy()

# 날짜 타입으로 변경
df_valid['date'] = pd.to_datetime(df_valid['date'])

# 행렬 조합
