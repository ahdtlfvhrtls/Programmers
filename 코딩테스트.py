import pandas as pd

df = pd.read_csv('D:/프로그래머스/videos.csv')

df_valid = df[df['date'] != '-'].copy()

df_valid['total_clicks_combined'] = df_valid['ads_clicked'] + df_valid['ads_clicked_versionB']

grouped_clicks = df_valid.groupby('date').agg(
    total_clicks=('total_clicks_combined','sum')
)

