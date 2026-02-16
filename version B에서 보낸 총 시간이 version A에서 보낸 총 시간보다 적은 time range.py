import pandas as pd

df = pd.read_csv('D:/프로그래머스/videos.csv')

# 날짜가 있는 행만 사용
df_valid = df[df['date'] != '-'].copy()


# 시간대별로 A/B 시청 시간 합산
grouped_slot = df_valid.groupby('time_slot').agg(
    total_time_A=('total_user_time_spent_in_mins', 'sum'),
    total_time_B=('user_time_spent_versionB_in_mins', 'sum')
)

# B가 A보다 적은 시간대만 필터
less_B_than_A = grouped_slot[grouped_slot['total_time_B'] < grouped_slot['total_time_A']]

print(grouped_slot)
print("\nB가 A보다 적은 시간대:")
print(less_B_than_A)