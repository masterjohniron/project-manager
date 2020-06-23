import pandas as pd
import os

file_name = 'server_delopy.csv'
date = [pd.to_datetime('2020-05-23')]
hour = [11]
location = ['1360 stree dd']
number = [22]
company = ['alibaba']

result = pd.DataFrame(columns=('date', 'hour', 'location', 'number', 'company'))
data = {'date': date, 'hour': hour, 'location': location, 'number': number, 'company': company}
result = result.append(pd.DataFrame(data), ignore_index=True)
print(result)
if os.path.exists(file_name):
    result.to_csv(file_name, index=None, mode='a', header=False)  # 保存文档，如果已存在，则不保存列名
else:
    result.to_csv(file_name, index=None, mode='a')
