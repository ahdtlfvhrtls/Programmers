import pandas as pd

df = pd.read_csv('data2.csv')

df_valid = df[df['date'] != '-'].copy()

df_valid['ads_watched_combined'] = (
    df_valid['total_ads_watched_in_mins'] +
    df_valid['ads_watched_vesionB_in_mins']
)
df_valid['clicks_combined'] = (
    df_valid['ads_clicked'] +
    df_valid['ads_clicked_versionB']
)

