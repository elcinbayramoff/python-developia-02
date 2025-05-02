"""
r(default) - read | Tapmırsa error | sadəcə oxumaq üçün
w - write | Tapmırsa yenisini yaradır | İçindəki datanı silir
a - append | Tapmırsa yenisini yaradır | İçindəki datanı saxlayır
x - create | Yenisini yaradır| Tapırsa error
r+ - datanı silmir read/write
w+ - datanı silir  read/write
"""

# def func(a=5):
#     ...

# func(a=5)

# file = open('data.txt','r')
# # data = file.read()
# # data = file.readlines()
# # data = file.readline()
# # print(data)
# # for line in file:
# #     print(line.strip())

# data = file.readlines()
# print('Data',data)
# for line in data:
#     print(line.strip())

# file.close()


# f = open('data.txt')
# # print(f.readline())
# # print(f.readline())
# print(1, f.read())
# print(2, f.read())
# f.close()


# f = open('data.txt', 'r')
# f.read()
# f.close()

# A = ['a','b','c','d']
# A = [i + '\n' for i in A]
# with open('data.txt', 'w') as f:
#     f.write('Salam')
#     f.writelines(A)

# with open('data.txt', 'a') as f:
#     f.write('\nSalam')

# def file_operator(file_name, file_data):
#     ...

# file_name = input('Faylın adını daxil edin: ')
# file_data = input('Faylın datasını daxil edin: ')

# with open(file_name, 'w', encoding='utf-8') as f:
#     f.write(file_data)
"""
w+ r+
"""
# with open('data.txt', 'r+', encoding='utf-8') as f:
#     f.write('Necəsən')
#     f.seek(0)
#     f.write('salam')



# with open('data.txt', 'w+') as f:
    # f.write('Salam')
    # f.seek(0)
    # f.write('Hi') 

# with open('data.txt', 'w+', encoding='utf-8') as f:
#     f.write('Necəsən?')

# with open('data.txt', 'w') as f:
#     f.read()


# with open('data.txt','r') as f:
    # data = f.read()
    # data = f.readlines() #['Hello\n', 'Hi']
    # data = f.readline()
    # for line in f:
    #     print(line.strip())
# A = ['salam','necesen','Hi']
# with open('data.txt', 'w') as f:
    # f.write('Salam')
    # f.writelines(A)
    
# with open('data.txt', 'w+', encoding='utf-8') as f:
#     f.write('Necəsən')
#     f.seek(1)
#     data = f.read()
#     print(data)


"""
data.txt
Salam necesen
"""

# file_name = input()
# file_data = input()