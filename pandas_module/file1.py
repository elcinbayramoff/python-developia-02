import pandas as pd
# """
# CTRL+SHIFT+P
# Python select interpreter
# Enter path
# Find
# venv - scripts - python
# """

# a = [1, '7', 2]

# b = pd.Series(a, index = ["x", "y", "z"])

# print(b)

# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

#load data into a DataFrame object:
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df['duration']) 


# import pandas as pd

#df - DataFrame

# df = pd.read_excel('pandas_module/sales.xlsx',sheet_name='Satis',usecols=['Item','Units'])
# df = pd.read_excel('pandas_module/sales.xlsx',sheet_name=0)

# # print(df.head(10))
# # high_total = df[ (df['Units'] == 50) & (df['UnitCost']==19.99)]
# high_total = df[ (df['Units'] == 50) | (df['UnitCost']==19.99)]

# print(high_total)

# total_sum = df['Total'].sum() #mean, max, min

# print(total_sum)

# df['Profit'] = df['Total'] - df['Units'] * df['UnitCost']
# # print(df)
# #.to_excel(file_name, index=False, sheet_name='Satis')

# df.to_excel('pandas_module/sales_updated.xlsx', index=False, sheet_name='Satis1')
# print('Excel faylına əlavə edildi')

# print(df.sort_values(by='Profit', ascending=False))
# print(df.sort_values(['UnitCost','Units'], ascending=[False,True]))
# df.dropna() # delete rows that contain NaN - None values
# df.fillna(0) #Fill NaN values with given value

# df_groupped = df.groupby('Region')['Total'].mean()
# print(df_groupped)

"""
rep
Item
"""
# print(df[(df['Rep']=='Jones') | (df['Item']=='Pencil')])


import pandas as pd

df = pd.read_excel('pandas_module/sales.xlsx',sheet_name=0)

# top_10_rows = df.head(10)
# last_10_rows = df.tail(10)
# print(top_10_rows)
# print(last_10_rows)

# df_pencil = df[df['Item']=='Pencil']

# df_pencil.to_excel('pandas_module/sales_updated.xlsx')


import json

# telebeler = [
# {"name": "Nərgiz", "age": 21},
# {"name": "Elvin", "age": 22},
# {"name": "Kamran", "age": 23}
# ]

# #yazmaq
# with open('json_module/telebe.json','w',encoding='utf-8') as f:
#     json.dump(telebeler, f, indent=4, ensure_ascii=False)

# #oxumaq
# with open('json_module/telebe.json','r',encoding='utf-8') as f:
#     data = json.load(f)

# for telebe in data:
#     # print(type(telebe)
#     print(telebe['name'])

#oxumaq
# with open('json_module/telebe.json','r',encoding='utf-8') as f:
#     data = json.load(f)

# name = input('Adı daxil edin: ')
# age = int(input('Yaşı daxil edin: '))

# new_data = {
#     'name':name,
#     'age':age
#     }

# data.append(new_data)

# #yazmaq
# with open('json_module/telebe_updated.json','w',encoding='utf-8') as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)
