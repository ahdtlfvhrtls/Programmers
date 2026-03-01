import pandas as pd

df = pd.read_csv('data2.csv')

# group by website
grouped = df.groupby('website')['contact_mail'].apply(
    lambda x: x.isna().all() # 해당 웹사이트가 등장한 모든 row에서 mail이 NaN이면 True
)

# True인 website 개수
answer = grouped.sum()
answer

하나의 이메일이 여러 플랫폼에서 쓰인 경우는 몇 개인가?
df[df['contact_mail'].notna()] \
.groupby('contact_mail') \
.size() \
.loc[lambda x: x > 1]

df.groupby('website')['contact_mail'] \
.apply(lambda x: x.isna().all()) \
.sum()

len(df[df['contact_mail'].notna() & df['website'].notna()])

df['domain'] = df['contact_mail'].str.split('@').str[-1]


df2 = df.dropna()
# contact_mail 없는 플랫폼 수는?
df2['contact_mail'].isna().sum()
# website 없는 플랫폼 수는?
df2['website'].isna().sum()