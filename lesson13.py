# def my_func(n):
#     if n < 0:
#         return
#     print('printden evvel',n) 
#     my_func(n-1) 
#     print('printden sonra',n)

# my_func(5)

# 5! = 5 * 4 * 3 * 2 * 1
# 5 + 4 + 3 + 2 + 1

# def factorial(n):
#     if n == 1:
#         return 1
    
#     return n * (n-1) * (n-2) * (n-3) * 1 # 5 * 4 * 3 * 2 * 1
    
# print(factorial(5))

# def factorial(n):
#     if n == 1:
#         return 1
    
#     return n  * factorial(n-1)

# factorial(100)

# def toplama(a, b):
#     return a * b

# print(toplama(4, 6))
# 1 + 2 + 3 + 4 + 5
# 5 + 4 + 3 + 2 + 1
# def sum_func(n):
#     if n == 1:
#         return n
#     return n + sum_func(n-1)

# print(sum_func(5))

# raise ValueError('Salam') # return
# raise ValidationError({'detail':'User id dogru deyil'}) 

# def division(a, b):
#     if b == 0:
#         raise ZeroDivisionError('0-a bölmə')
#     print(a/b)

# division(4, 0)

# try:
#     a = int(input())
#     b = int(input())
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         raise ZeroDivisionError('0-a bölmə')
# except Exception as e:
#     print('Hi',e)