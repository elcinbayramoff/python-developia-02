# def say_hi(name):
#     print(f'Hello, {name}')


# ad = input('Adi daxil edin: ')
# say_hi(ad)

# def addition(a, b):
#     print(a + b)

# def division(b, a):
#     print( a / b )

# addition(5, 10)
# division(10, 5)

#pi * r ** 2
# import math

# def area_calculator(r):
#     area = math.pi * r ** 2
#     print(round(area, 2))

# radius = int(input('Ededi daxil edin: '))
# area_calculator(radius)

# def my_func(a=4, c=3, d=25):
#     print(a, c, d)

# my_func(a=20, d=10)

# def my_func(d,/, e ,*, a, b, c):
#     print(a, b, c, d, e)

# my_func(100, e=200, a=10, b=20, c=30)


# def task(a, b, /, d=20,*, c):
#     print(a, b, d, c)

# task(1, 2, c=4)


# def my_func(a, b, c, d=20):
#     print(a, b, c, d)

# my_func(a=10, c=20, b=30)


# def my_func(a, b, /):
#     print(a, b)

# my_func(a=10, b=20)


# def my_func(a, b, c, d=20):
#     print(a, b, c, d)

# my_func(a=10, c=20, b=30) # keyword key : value
# my_func(10, b=30, c=20) # positional 

#Task 1
# def print_even_numbers(n):
#     for i in range(2, n+1, 2):
#         print(i)

# print_even_numbers(20)

#Task 2

# [1, 2, 3, 4, 5] -> ['1','2','3','4','5']
# def print_revered(lst):
#     # lst_reversed = lst[::-1]
#     lst_reversed = reversed(lst)
#     # lst_reversed = list(map(str, lst_reversed))
#     # print(' '.join(lst_reversed))
#     for i in lst_reversed:
#         print(i, end=' ')

# print_revered([1, 2, 3, 4, 5])

#Task 3

# import time

# def countdown(n):
#     for i in range(n, 0, -1):
#         print(i)
#         time.sleep(1)

#     print("Lift off!")

# countdown(5)