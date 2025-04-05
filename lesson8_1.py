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

import turtle
import math


t = turtle.Turtle()
t.speed(0)  
t.color("red")  
turtle.bgcolor("black")  

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

t.penup()
for i in range(1, 16):   
    t.goto(0, -50 * i)  
    t.pendown()    

    
    for n in range(0, 628, 5):  
        angle = n / 100  
        x, y = corazon(angle)  
        t.goto(x * i, y * i)  

    t.penup()  


t.hideturtle()
turtle.done()