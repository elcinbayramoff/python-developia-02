# def my_func(a, b, *positional, **keyword):
#     print(a, b)
#     print(positional)
#     print(keyword)

# def my_func(a, b, c, *args, **kwargs):
#     print(a, b, c) #1, 3, 20
#     print(args) # 4, 5, 6, 7
#     print(kwargs)# 30, 40


# my_func(1, 3, 4, 5, 6, 7, c=20, d=30, e=40)


#args - dovre sal cap et

# def my_func(a, b, *args, **kwargs):
#     print(args, kwargs)
#     for arg in args:
#         print(arg)
#     print('---------------------------')

#     for value in kwargs.values():
#         print(value)

# my_func(1, 3, 4, 5, 6, 7, c=20, d=30, e=40) # 4, 5, 6, 7, 20, 30 ,40

# def average(a, b):
#     _sum = addition(a, b)
#     return _sum / 2

# def addition(a, b):
#     # print('hello')
#     return a + b


# result = addition(3, 4)
# print(result)

# print(average(3, 4))


# def is_odd_exists(lst): #[2, 3, 4, 5]
#     for i in lst:
#         if i % 2 == 1:
#             return True 
#     return False

# result = is_odd_exists([2, 6, 4, 8])
# print(result)

# a = 5

# def my_func1():
#     #enclosing
#     a = 10
#     def my_func2():
#         #local
#         print('Local',a)
#         ...
#     #enclosing
#     a = 7
#     my_func2()

# #global
# a = 20
# my_func1()
# print(a)