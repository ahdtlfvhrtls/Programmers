import pandas as pd

df = pd.read_csv('data2.csv')

# - 제거
df_valid = df[df['date'] != '-'].copy()

# Convert to datetime