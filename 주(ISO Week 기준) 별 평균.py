import pandas as pd

df = pd.read_csv('data2.csv')

# Filter valid dates
df_valid = df[df['date'] != '-'].copy()
