#Task 1

# A = [1, 1, 2, 3, 3, 2, 5, 4, 3, 1]
# A = set(A)
# A = list(A)
# print(A)
"""
int() - integer
float() - float
str() - string
tuple() - tuple
list() - list
dict() - dictionary
set() - set
complex() - complex
"""

#Task 2
# DATABASE = {
# 'username' : 'aysucefeova',
# 'password' : 'aysu123'
# }

# while True:
#     username = input('Username daxil edin:')
#     password = input('Passwordu daxil edin:')

#     if DATABASE['username'] != username or DATABASE['password'] != password:
#         print('Səhv daxil edildi\n')
#     else:
#         print('Daxil oldunuz')
#         break

#Task 3 
# for i in range(5, 0, -1):
#     print('*' * i)

# for i in range(1, 6):
#     print('*' * i)

#Task 5

# def faktorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# 120
# 1, 2, 3, 4, 5 # Duz tapdinsa dayan
# 110
# 1, 2, 3, 4, 5 # Faktorial verilen ededi keçsə dayan

# def is_factorial(n):
#     for i in range(1, n + 1):
#         result = faktorial(i)
#         if result == n:
#             return True
#         elif result > n:
#             return False
        
# n = int(input('Ədədi daxil edin:'))
# print(is_factorial(n))
import random
import time

# def lottery():
#     drawen_numbers = []
#     base = [i for i in range(1, 31)]
#     while len(drawen_numbers) != 30:
#         num = random.choice(base)
#         time.sleep(0.5)
#         if num in drawen_numbers:
#             continue
#         else:
#             print(num)
#             drawen_numbers.append(num)

# lottery()
# import time

# def lottery():
#     base = [i for i in range(1, 31)]
#     for _ in range(30):
#         num = random.choice(base)
#         print(num)
#         print(base)
#         time.sleep(0.5)
#         base.remove(num)
    
# lottery()

#Task 1
#27.10.2024 09:11
# from datetime import datetime

# dt = datetime.now()
# formatted_dt = dt.strftime('%d.%m.%Y %H:%M')
# print(formatted_dt)

#Task 2
# from datetime import date, timedelta

# five_days = timedelta(days=5)
# now = date.today()
# five_days_after = now + five_days
# five_days_before = now - five_days
# print(five_days_before)

#Task 3
# from datetime import date, timedelta

# ramazan_ayi = date(2026,2,19)
# now = date.today()

# result = ramazan_ayi - now
# print(result)

#Task 4

# import random
# from datetime import date


# now = date.today()
# for i in range(5):
#     month = now.month
#     year = now.year
#     day = random.randint(1, 28)
#     new_one =  date(year, month, day)
#     print(new_one)