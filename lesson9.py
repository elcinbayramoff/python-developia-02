# a = {False, 0, 0, 2, 3, 3, 4, 5}

# print(len(a))

# print(a[0]) olmaz

# for i in a:
#     print(i)

# a = {True, 2, 3, 4, 5}

# print( 1 in a )

# a.add(100)
# a = {'salam', 4, 5}

# a.update('Python')
# a.remove(100)
# a.discard(100)
# a.pop()
# del a
# print(a)

# A = {1, 2, 3, 4}
# B = {5, 6, 7, 8}

# C = A.union(B)
# D = A | B 
# print(D)

# A.update(B)
# A |= B
# print(A)


# A = {1, 2, 3, 4}
# B = {5, 6, 3, 4}

# C = A.intersection(B)
# print(C)

# A.intersection_update(B)
# print(A)

# C = A.difference(B)
# print(C)

# A.difference_update(B)
# print(A)
# print(type({}))

# A = {'name':'Elchin'}
# A.clear()
# print(A)

# A = {1,2,3,4}
# A.clear()
# print(A)


# A = {1, 2, 3, 4}
# B = {5, 6, 3, 4}

# C = A.symmetric_difference(B)
# print(C)

# A.symmetric_difference_update(B)
# print(A)

# A = [1, 2, 3, 4, 5]

# A_set = set(A)
# if len(A) != len(A_set):
#     print('Dublikat var')

# else:
#     print('Dublikat yoxdur')


# A = {True, 5, 3, 1, False, 'Hello'}
# A.discard(10)
# A.remove(1)
# print(A)
# A.remove(1)
# print(A)

# A = {
#     1: {
#      "name":"Elchin",
#      "surname":"Bayramli"
#      },
#     2:     {
#      "name":"Ali",
#      "surname":"Aliyev"
#      },
#     3:     {
#      "name":"Vali",
#      "surname":"Valiyev"
#      }
# }

# print(A[2])

# sentence = 'salam bax salam bura salam bax'
# words = {

# }

# extracted_words = sentence.split()

# for word in extracted_words:
#     if word in words:
#         words[word] += 1
#     else:
#         words[word] = 1

# print(words)
# data = {
#     'salam':'hello',
#     'necesen':'how r u'
# }

# word = input('Sözü daxil edin:')

# if word in data:
#     print('İçindədir')
# else:
#     print("İçində deyil")

# translation = {
#     'I':'Mən',
#     'go':'gedirəm',
#     'home':'ev',
#     'very':'çox',
#     'late':'gec'
# }
# sentence = '  I go home very late school   '
# sentence = sentence.strip()
# words = sentence.split()
# translated_words = []

# for word in words:
#     translated_word = translation.get(word, word)
#     translated_words.append(translated_word)

# translated_sentence = ' '.join(translated_words)
# print(translated_sentence)

# sentence = '  salam necesen yaxsisan?  '
# # a = '_salam_necesen_yaxsisanmi?'
# print(sentence.split())

# a = int(input()) # 123456789
"""
1000
200
30
4
"""

# a = input('Ədədi daxil edin: ')

# # digits = list(map(int, list(a)))
# emsal = 10 ** (len(a) - 1)

# for i in a:
#     print(int(i) * emsal)
#     emsal //= 10

# 12345
# 10000 #10 ** 4
# 2000 #10 ** 3
# 300 # 10 ** 2
# 40 # 10 ** 1
# 5 # 10 ** 0