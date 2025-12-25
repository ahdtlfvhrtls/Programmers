import pandas as pd

df = pd.read_csv('data2.csv')

df_valid = df[df['date'] != '-'].copy()

df_valid['ads_watched_combined'] = (
    