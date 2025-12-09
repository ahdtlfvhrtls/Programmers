import pandas as pd

df = pd.read_csv('D:/프로그래머스/videos.csv')
max_duration = df['duration'].max()

longest_videos = df[df['duration'] == max_duration]

print("최대 duration:", max_duration)
print("해당 duration 영상 개수:", len(longest_videos))
print(longest_videos)
