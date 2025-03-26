# a = 'Salam' # Olmazz
# a[1] = 'b'
# print(a)

# A = [1, 1.5, True, [1,2,3], 'Salam']
# A[3] = 'a'
# print(A)


# MAX_EDED = 5
# MAX_EDED = 6
# print(MAX_EDED)

# A = [1, 1, 1,'Salam' ,'Salam']
# print(A)
# print(len(A))


# A = ['Ali','Vali','Zahid',['a','b','c'],'Nurlan']

# # A[1:3] = ['Xosrov','Aqshin','Gunel']
# A[3][1] = 'Z'

# print(A)

# .insert()

# A = ['a','b','c','d'] # ['a','b','z','c','d']
# B = ['e','f','g']
# # C = ['x','y','z']
###.extend()
# # B.extend(A)
# # A.insert(2,'z')
# # A.append('z')
####Toplama
# A += B
# print(A)

# A = ['a','b','c','d']

# del A

# print(A)
# A.remove('b') #A = ['a','c','d'].pop(3)
# A.pop(3)

# A = [8, 3, 1, 5, 6, 2, 4, 7]  # [8, 5, 3, 1, 2, 4, 6, 7]

# # A.sort()
# # A.sort(reverse=True)
# B = sorted(A, reverse=True)
# print(B)

# A = [8, 3, 1, 5, 6, 2, 4, 7] # [8, 5, 3, 1, 2, 4, 6, 7]

# A1 = A[:4]
# A1.sort(reverse=True)

# A2 = A[4:]
# A2.sort()
# result = A1 + A2
# print(result)


# A = [1, 2, 3]
# B = A.copy()

# A[2] = 5

# print('A:',A,'B:', B)
# import copy
# A = [['d','e'], ['a','b']]
# B = copy.deepcopy(A)

# A[1][0] = 'z'

# print('A:',A,'B:', B)


#Task1 
# A = [4,2,1,5,7,3,6,8]
# A.sort()

# # A1 = A[:2]

# # A2 = A[2:6]
# # A2.sort(reverse=True)

# # A3 = A[6:]
# # B = A1 + A2 + A3
# # print(B)
# A[2:6] = A[2:6][::-1]
# print(A)

#Task2
# A = []

# name1 = input('1ci işçinin adını daxil edin: ')
# surname1 = input('1ci işçinin soyadını daxil edin: ')
# # A.append([name1, surname1])

# name2 = input('2ci işçinin adını daxil edin: ')
# surname2 = input('2ci işçinin soyadını daxil edin: ')
# # A.append([name2, surname2])

# name3 = input('3ci işçinin adını daxil edin: ')
# surname3 = input('3ci işçinin soyadını daxil edin: ')
# # A.append([name3, surname3])

# A = [[name1, surname1], [name2, surname2], [name3, surname3]]
# print(A)
# choice = int(input('Hansi işçini istəyirsən? '))

# print(A[choice-1])

#Task 3

# A = [1,2,3,2,1]
# # 
# print(A == A[::-1])

# #Task 4

# print(A[::-1])
