import pandas as pd

df = pd.read_csv('D:/프로그래머스/videos.csv')
df_valid = df[df['date'] != '-'].copy()
df_valid['date'] = pd.to_datetime(df_valid['date'])

daily = df_valid.groupby('date').agg(
    clicks_A=('ads_clicked','sum'),
    clicks_B=('ads_clicked_versionB','sum'),
    time_A=('total_user_time_spent_in_mins','sum'),
    time_B=('user_time_spent_versionB_in_mins','sum')
)

daily['ratio_A'] = daily['clicks_A'] / daily['time_A']
daily['ratio_B'] = daily['clicks_B'] / daily['time_B']

daily_compare = daily[daily['ratio_A'] > daily['ratio_B']]



print("A 비율이 더 높은 날짜 수:", len(daily_compare))
print("전체 날짜 수:", len(daily))