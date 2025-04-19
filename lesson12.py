# print(Hello world) #SyntaxError
# 'salam' + 5 # TypeError
# def func(*, a, b): #TypeError
#     return a, b
# func(5, 6)

# import salam # ModuleNotFoundError
# 5 / 0 # ZeroDivisionError
# A = {} #KeyError
# A['salam']

# try:
#     # 'salam' + 5
#     # A = {} #KeyError
#     # A['salam']
#     5 / 0
#     # A = [1, 2, 3]
#     # A[5]
# except TypeError:
#     print('type xətası baş verdi')

# except (KeyError, IndexError):
#     print('key və ya index error baş verdi')
# except Exception as e:
#     print(f'Something unknown occured:{e}')

# try:
#     5 / 0
# except Exception as e:
#     print(f'Something unknown occured:{e}')
# else:
#     print('Hər şey qaydasındadır')
# finally:
#     print('Hər zaman burdayıq')


# def symbol_finder(string: str, symbol):
#     return string.count(symbol)

# print(symbol_finder('Salam', 'a'))

# A = [5] * 10
# A = (5,) * 10
# A = [i for i in range(1, 20) if i % 3 == 0]
# print(A)'

# def upper_maker(lst): # ['salam','necesen', 'ne']
#     return [i.upper() for i in lst]


# result = upper_maker(['salam','necesen', 'ne'])
# print(result)

#iki input
#nisbeti a / b
#round(a/b, 2)

# try:
#     # 'salam' + 5
#     # A = {} #KeyError
#     # A['salam']
#     5 / 0
#     # A = [1, 2, 3]
#     # A[5]
# except TypeError:
#     print('type xətası baş verdi')

# except (KeyError, IndexError):
#     print('key və ya index error baş verdi')
# except Exception as e:
#     print(f'Something unknown occured:{e}')

# try:
#     a = int(input())
#     b = int(input())
#     print( a / b)
# except ZeroDivisionError:
#     print()
# except ValueError:
#     print()
# except TypeError:
#     print()
# except Exception as e:
#     ...
