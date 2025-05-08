# import datetime

# Datefield 2025-02-05
# Datetimefield 2025-02-05 08:17
# Timefield 08:17

"""
datetime
time
date
timedelta
"""

# from datetime import date

# d = date(2025,5,2)
# print(d.month)
# print(d.year)
# print(d.day)

# today = date.today()
# print(today)

# if today.year == 2025:
#     print('Correct')

# from datetime import time

# t = time(14,30,23,25)
# print(t.hour, t.minute,t.second, t.microsecond)

# from datetime import datetime

# dt = datetime.now()
# print(dt)

# dt = datetime.now()

#strftime - formatting - datetime -> string
#strptime - parsing - string -> datetime
#21 December 2025
# result = dt.strftime("%d %B %Y")
# print(type(result))

# result = datetime.strptime("21 December 2025 14:33","%d %B %Y %H:%M")
# print(type(result))

# dt = datetime(2025, 12, 21)
# #21-Dec-2025, Sun
# result = dt.strftime("%d-%b-%Y, %a")
# print(result)







# from datetime import datetime

# dt = datetime(2025,12, 25)

# # %B
# result = dt.strftime('%B')
# print(type(result)) # 2025-12-25


# datetime
# date 
# time

#datetime - > string strftime
#string -> datetime strptime
# strftime
# strptime
# from datetime import datetime

# dt = datetime.now()

# if dt.year == 2025:
#     print('True')
# else:
#     print('False')


# print(dt)

