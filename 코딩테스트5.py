import pandas as pd

df = pd.read_csv('data2.csv')

# group by website
grouped = df.groupby('website')['contact_mail'].apply(
    lambda x: x.isna().all()
df2 = df.dropna()
