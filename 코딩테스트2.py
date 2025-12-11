import pandas as pd

df = pd.read_csv('D:/프로그래머스/videos.csv')
df_valid = df[df['date'] != '-'].copy()
df_valid['date'] = pd.to_datetime(df_valid['date'])

daily = df_valid.groupby('date').agg(