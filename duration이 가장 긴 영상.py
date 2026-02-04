import pandas as pd

# CSV 읽기
df = pd.read_csv('D:/프로그래머스/videos.csv')

# 최대 duration 찾기
max_duration = df['duration'].max()

# 최대 duration을 가진 모든 영상 필터링
longest_videos = df[df['duration'] == max_duration]

print("최대 duration:", max_duration)
print("해당 duration 영상 개수:", len(longest_videos))
