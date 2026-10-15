import pandas as pd

df = pd.read_csv('auth.log.csv')

failed = df[df['message'].str.contains('Failed',  case=True, na=False)]
per_ip = failed.groupby('src_ip').size()

top_ip = per_ip.sort_values(ascending=False).nlargest(50)

print(top_ip)