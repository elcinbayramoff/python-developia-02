#Task1
# word = input("Sözü daxil edin: ")
# word_length = len(word)

# if word_length > 5:
#     print('Boyuk')

# elif word_length == 5:
#     print('Normal')

# else:
#     print('Kicik')

#Task2

# A = (10,13,17,25,34,65)
# A_even = A[::2]
# A_odd = A[1::2]

# sum_even = sum(A_even)
# sum_odd = sum(A_odd)
# print(sum_even, sum_odd)

# if sum_even > sum_odd:
#     print('Cut')
# else:
#     print('Tek')

#Task3

# a = input('Sozu daxil edin: ')
# first_letter = a[0]

# if first_letter.isupper():
#     print('Boyuk')

# elif first_letter.islower():
#     print('Kicik')

# else:
#     print('Yanlis simvol')

#Task 4

# 1 3 4 5 8 9
# [1,3,4,5,8,9]

# A = list(map(int, input('Listi daxil edin: ').split()))
# #['3', '4', '5', '6', '7', '8']
# print(A)

# if 7 in A:
#     print('Şanslı nömrə tapıldı!')
# else:
#     print('Şanslı nömrə tapılmadı!')

#Task 5

# a = input('Stringi daxil et:')

# a_length = len(a)

# if a_length % 2 == 0:
#     print('Cut')

# else:
#     print('Tek')

#Koklerin tapilmasi
# import math

# a, b, c = map(float, input('a b c daxil edin: ').split())

# D = b ** 2 - 4 * a * c

# if D == 0:
#     x = (-b)/(2*a)
#     print(f'Kokler bereaberdir: {x}')

# elif D < 0:
#     print('Heqiqi koku yoxdur')

# else:
#     x1 = (-b + (D) ** 0.5) / (2*a)
#     x2 = (-b - math.sqrt(D)) / (2*a)
#     print(f'Kokler {x1},{x2}')
