# import random

# # for i in range(1000000):
# #     a = random.random()
# #     if a == float(0):
# #         print('Tapıldı')

# #randint
# # a = random.randint(1, 10)
# # a =  random.uniform(1, 10)
# # print(a)

# # A = ['a','b','c']

# # random.shuffle(A)
# # print(A)


# # A = ['a','b','c','d','e']

# # a = random.choice(A)
# # print(a)

# # print(random.choices(A,k=6))

# # A = [1, 2, 3, 4, 5, 6]

# # def zer():
# #     # a = random.choice(A)
# #     # b = random.choice(A)
# #     # return [a, b]

# #     a = random.randint(1, 6)
# #     b = random.randint(1, 6)
# #     return a, b
# #     # return random.choices(A, k=2)

# # print(zer())


# a = random.randint(1, 100) 
# n = 0
# user1 = 'Əli'
# user2 = 'Elçin'
# while True:
#     if n % 2 == 0:
#         main_user = user1
#     else:
#         main_user = user2
#     n += 1
#     user_input = int(input(f'Ededi daxil edin, {main_user}: '))
#     if user_input == a:
#         print(f'Tapdiniz, {main_user}')
#         break
#     elif user_input > a:
#         print('Aşağıdadır')
#     else:
#         print('Yuxarıdadır')

a = int(input())#5
"""
*****
****
***
**
*
*
**
***
****
*****
"""
for i in range(1, a+1):
    print('*' * i)