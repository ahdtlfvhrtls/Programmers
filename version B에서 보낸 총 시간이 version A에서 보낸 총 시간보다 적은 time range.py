import pandas as pd

df = pd.read_csv('D:/프로그래머스/videos.csv')

df_valid = df[df['date'] != '-'].copy()

grouped_slot = df_valid.groupby('time_slot').agg(
    total_time_A=('total_user_time_spent_in_mins', 'sum'),
    total_time_B=('user_time_spent_versionB_in_mins', 'sum')
)

