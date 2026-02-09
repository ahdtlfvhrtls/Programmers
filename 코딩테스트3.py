import pandas as pd

# CSV 읽기
df = pd.read_csv('data2.csv')

# 날짜가 '-'인 행 제거
df_valid = df[df['date'] != '-'].copy()

# A+B 합치기
df_valid['ads_watched_combined'] = (
    df_valid['total_ads_watched_in_mins'] +
    df_valid['ads_watched_vesionB_in_mins']
)
df_valid['clicks_combined'] = (
    df_valid['ads_clicked'] +
    df_valid['ads_clicked_versionB']
)

# 날짜별로 합계 계산
grouped = df_valid.groupby('date').agg(
    total_ads_watched=('ads_watched_combined', 'sum'),
    total_clicks=('clicks_combined', 'sum')
)

# 광고 시청 시간이 0인 날은 나누기 에러 방지를 위해 제외
grouped = grouped[grouped['total_ads_watched'] > 0].copy()

# 클릭 비율 계산

result = grouped.sort_values('click_ratio')
print(result.head(1))