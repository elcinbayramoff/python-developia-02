# A = {
#     "Name":'Elchin',
#     'surname':'Bayramli'
#     # 'age' : 90

#      }

# # print(A['age'])
# value = A.get('age', 20)
# print(value)


# A = {
#     'name':'Elchin',
#     'surname':'Bayramli',
#     'age' : 90
#     }

# keys = A.keys()
# print(list(keys))

# values = A.values()
# print(list(values))

# items = A.items()
# print(list(items))

# A = {
#     # 'name':'Elchin',
#     'surname':'Bayramli',
#     'age' : 90
#     }

# # del A

# # A.clear()
# value = A.pop('name', 'Ali')
# print(value)
# print(A)

"""
name
surname
age

Elchin
Bayramli
90
"""
# A = {
#     'name':'Elchin',
#     'surname':'Bayramli',
#     'age' : 90
#     }

# for key in A.keys():
#     print(key)

# for key in A:
#     print(key)

# for value in A.values():
#     print(value)

# for key in A:
#     print(A[key]) #print(A['surname'])

# for a, b in A.items():
#     # a, b = item
#     print(a, b)

# for key, value in A.items():
#     # a, b = item
#     print(key, value)

# A = {
#     'name':'Elchin',
#     'surname':'Bayramli',
#     'age' : 90,
#     5:'Bos ver',
#     'personal_data':{
#         'phone_number':'+994707777777',
#         'id':'1111111',
#         'private_data':{
#             'parol':'123456'
#         }
#     }
#     }

# print(A['personal_data']['private_data']['parol'])

A = {
    'name':'Elchin',
    'surname':'Bayramli',
    'age' : 90
}

# A['name'] = 'Ali'
# A['phone_number'] = '+994777777777'
# print('name' in A)

# {
#     'salam':5,
#     'sagol':7
# }

# a = input('Ededi daxil edin: ')
# print(len(a.strip()))

# a = int(input('Ededi daxil edin:'))

# digit_count = 0

# while a > 0: # a=0
#     a //= 10
#     digit_count += 1

# print(digit_count)

#Task2

# a, b = 0, 1
# num = int(input('Ededi daxil edin: ')) # 30
# while a <= num:
#     print(a) # 34
#     a, b = b, a + b # 34


#Task3
# a = int(input('Ededi daxil edin:'))

# _sum = 0

# while a > 0: # a=0
#     _sum += a % 10
#     a = a // 10
    

# print(_sum)
#1234 // 10 = 123
#1234 % 10 = 4


# a = 122345

a = int(input('Ededi daxil edin: '))
a = str(a)

count = 0
flag = False
while count < len(a):
    if a[count] == a[count + 1]:
        flag = True
        break
    
    count += 1

if flag:
    print('Eyni yanaşı ədəd tapıldı')
else:
    print('Eyni yanaşı ədəd tapılmadı')