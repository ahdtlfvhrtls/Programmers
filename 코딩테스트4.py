import pandas as pd

df = pd.read_csv('data2.csv')

df_valid = df[df['date'] != '-'].copy()

df_valid['ads_watched_combined'] = (
    df_valid['total_ads_watched_in_mins'] +
    df_valid['ads_watched_vesionB_in_mins']
)
df_valid['clicks_combined'] = (
    df_valid['ads_clicked'] +
    

grouped = df_valid.groupby('date').agg(
    total_ads_watched=('ads_watched_combined', 'sum'),
    total_clicks=('clicks_combined', 'sum')
)