import pandas as pd

df = pd.read_csv('D:/프로그래머스/videos.csv')
df['total_user_combined'] = df['total_user_time_spent_in_mins'] + df['user_time_spent_versionB_in_mins']

