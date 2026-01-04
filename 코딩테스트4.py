import pandas as pd

df = pd.read_csv('data2.csv')

df_valid = df[df['date'] != '-'].copy()

df_valid['ads_watched_combined'] = (
    df_valid['total_ads_watched_in_mins'] +
    df_valid['ads_watched_vesionB_in_mins']
)

grouped = df_valid.groupby('date').agg(
    