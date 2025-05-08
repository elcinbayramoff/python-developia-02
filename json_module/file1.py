import json

# json_data = '{"name":"Elchin","surname":"Bayramli"}'

# data = json.loads(json_data) # python-da json stringini dict obyektine

# print(data['name'])


# data = {
#     'name':'Elchin',
#     'surname':'Bayramli'
# }

# json_data = json.dumps(data) #dict obyektini json stringine cevirir
# print(json_data)

# data = {'name':'Elchin','surname':'Bayramli','age':99}

# # json_data = json.dumps(data, indent=4, separators=('.','-'))
# json_data = json.dumps(data, sort_keys=True)
# print(json_data)

# data = {'name':'Elçin','surname':'Bayramlı','age':99}

# with open('data.json','w',encoding='utf-8') as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)

# with open('data.json','r') as f:
#     data = json.load(f)
#     print(type(data))