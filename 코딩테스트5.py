import pandas as pd

df = pd.read_csv('data2.csv')

# group by website
grouped = df.groupby('website')['contact_mail'].apply(
    lambda x: x.isna().all() # 해당 웹사이트가 등장한 모든 row에서 mail이 NaN이면 True
)

# True인 website 개수
answer = grouped.sum()
answer

df[df['contact_mail'].notna()] \
.groupby('contact_mail') \
.size() \
.loc[lambda x: x > 1]


df2 = df.dropna()
df2['contact_mail'].isna().sum()
df2['website'].isna().sum()