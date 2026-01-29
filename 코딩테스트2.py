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

df['total_user_combined'] = df['total_user_time_spent_in_mins'] + df['user_time_spent_versionB_in_mins']
df['total_ads_combined'] = df['total_ads_watched_in_mins'] + df['ads_watched_vesionB_in_mins']

target = df[df['time_slot'].isin(['06:00-11:59','12:00-17:59'])]

total_user = target['total_user_combined'].sum()
total_ads = target['total_ads_combined'].sum()


print("A 비율이 더 높은 날짜 수:", len(daily_compare))
print("전체 날짜 수:", len(daily))