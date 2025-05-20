"""
Object oriented programming - OOP
procedural programming

"""
# A = []
# list(1,2,3)
# A.append()

# book1.similar_books()
#class attributes
class Person:
    citizenship = 'Azerbaijani'
    a = 5
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.a = 7
    
    def greet(self, symbol):
        return f'Hello, {self.name} {self.surname}{symbol}'


# person1 = Person('Elchin','Bayramli')
# print(person1.ad)
# person2 = Person('Ali','Aliyev')
# print(person2.ad)

# person2.name = 'Vali'
# print(person1.citizenship)
# print(person2.citizenship)

# Person.citizenship = 'Turkish'
# print(person1.citizenship)
# print(person2.citizenship)
# print(person1.name)
# person2 = Person()
# print(person2.name)
# person1.citizenship = 'Turkish'

# del person1.citizenship

# print(person1.citizenship)

# print(person1.citizenship)
# print(person2.citizenship)

# del person2.citizenship
# print(person2.citizenship)

# person1 = Person('Elchin','Bayramli')
# person2 = Person('Ali','Aliyev')

# # person1.age = 20
# # print(person1.age)
# # del person1.a

# print(person1.greet('.'))
# print(person2.greet('?'))
# class User:
#     objects = []

#     def __init__(self,username):
#         self.username = username
#         User.objects.append(self)

#     def __str__(self):
#         return self.username

# user1 = User('elcin')
# user2 = User('ali')

# for user in User.objects:
#     print(user.username)

# class Car:
#     car_count = 0
#     models = []
#     def __init__(self, color, model):   
#         self.color = color
#         self.model = model
#         Car.car_count += 1
#         Car.models.append(model)

#     def set_color(self, new_color):
#         self.color = new_color
#         print('Rengi deyisdi')
    
#     def get_color(self):
#         print(self.color)

# car1 = Car('black','Porsche')
# # print(car1.models)
# car2 = Car('white','Mercedes')
# # print(Car.models)

# # print(len(Car))
# car1.set_color('orange')
# car1.get_color()

#classmethods
#staticmethod
#dunder methods, magic methods

# class User: # def get_user_count() 1048756
#     user_count = 0
#     usernames = []
#     def __init__(self, username, age):
#         User.is_valid_username(username) # uzunlugu yoxlayir, staticmethod
#         User.is_available(username) # olub olmadigini yoxlayir, classmethod
#         self.username = username
#         self.age = age
#         User.user_count += 1
#         User.usernames.append(username)

#     @classmethod
#     def get_user_count(cls):
#         return cls.user_count
    
#     @classmethod
#     def from_string(cls, data:str):
#     #elchin-99
#         username, age = data.split('-')
#         return cls(username, age)

#     @classmethod
#     def is_available(cls, username):
#         if username in cls.usernames:
#             raise KeyError('This username exist, try another!')

#     @staticmethod
#     def is_valid_username(username):
#         if 3 < len(username) < 15:
#             ...
#         else:
#             raise ValueError('Username is not valid!')
    
#     def __str__(self):
#         return f'{self.username}-{self.age}'
    
#     def __repr__(self):
#         index_of_user = self.usernames.index(self.username)
#         return f'{index_of_user}-{self.username}'
    
#     def __gt__(self, other): #user1 > user2 
#         if not isinstance(other, User):
#             return NotImplemented

#         if self.age > other.age:
#             return True
#         else:
#             return False



# user1 = User('elchin',99)
# user5 = User.from_string('elchin1-99')
# print(user5)
# print(User.usernames)
# user2 = User('ali123', 30)

# user3 = User('Vali', 30)


# print(User.usernames)
# print(repr(user3))
# print(user3)

# user_str = str(user1)
# print(user_str)
# User.get_user_count()
# print(User.get_user_count()) 
#from string class method

# print(user2 > user1)

#Lazımsız bölgə

# class A:
#     def __init__(self, value):
#         self.value = value
#     def __eq__(self, other):
#         if isinstance(other, A):
#             print('Comparing an A with an A')
#             return other.value == self.value
#         if isinstance(other, B):
#             print('Comparing an A with a B')
#             return other.value == self.value
#         print('Could not compare A with the other class')

#         return NotImplemented
    

# class B:
#     def __init__(self, value):
#         self.value = value
#     def __eq__(self, other):
#         if isinstance(other, B):
#             print('Comparing a B with another B')
#             return other.value == self.value
#         print('Could not compare B with the other class')
#         return NotImplemented
    

# a1 = A(1)
# b1 = B(1)

# print(a1 == a1)
# print(a1 == b1)
# print(b1 == b1)
# print(b1 == a1)
#Lazımsız bölgədən çıxıldı

# print(type(...))
