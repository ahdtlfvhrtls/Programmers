import pandas as pd

df = pd.read_csv('data2.csv')

# group by website
grouped = df.groupby('website')['contact_mail'].apply(
    lambda x: x.isna().all() # 해당 웹사이트가 등장한 모든 row에서 mail이 NaN이면 True
)

# True인 website 개수
answer = grouped.sum()
answer

# 하나의 이메일이 여러 플랫폼에서 쓰인 경우는 몇 개인가?
df[df['contact_mail'].notna()] \
.groupby('contact_mail') \
.size() \
.loc[lambda x: x > 1]

# 모든 row에서 contact_mail이 NULL인 website 수는?
df.groupby('website')['contact_mail'] \
.apply(lambda x: x.isna().all()) \
.sum()

# contact_mail도 있고 website도 있는 정상 데이터 수는?
len(df[df['contact_mail'].notna() & df['website'].notna()])

# 가장 많이 사용된 이메일 도메인은?
df['domain'] = df['contact_mail'].str.split('@').str[-1]

# 웹사이트가 없는 이메일이 몇 개의 고유 이메일인가?
filtered = df[df['website'].isna() & df['contact_mail'].notna()]
unique_count = filtered['contact_mail'].nunique()

missing_mail = df[df['contact_mail'].isna() & df['website'].notna()]

df2 = df.dropna()

df2['mail_domain'] = df2['contact_mail'].str.split('@').str[-1]
# contact_mail 없는 플랫폼 수는?
df2['contact_mail'].isna().sum()
# website 없는 플랫폼 수는?
df2['website'].isna().sum()