import pandas as pd

df = pd.read_csv('D:/프로그래머스/videos.csv')
df['total_user_combined'] = df['total_user_time_spent_in_mins'] + df['user_time_spent_versionB_in_mins']
df['total_ads_combined'] = df['total_ads_watched_in_mins'] + df['ads_watched_vesionB_in_mins']

target = df[df['time_slot'].isin(['06:00-11:59','12:00-17:59'])]

