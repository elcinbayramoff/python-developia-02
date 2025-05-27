# class Parent:
#     def greet(self):
#         print('Hello from Parent')

# class Child(Parent):
#     def greet_hello(self):
#         print('Hello from Child')

# child1 = Child()
# parent1 = Parent()

# child1.greet()
# child1.greet_hello()

# parent1.greet()


# class Parent:
#     def greet(self):
#         print('Hello from Parent')

# class Child(Parent):
#     def greet(self):
#         print('Hello from Child')

# child1 = Child()
# child1.greet()

# class Person:
#     def __init__(self,name, surname):
#         self.name = name
#         self.surname = surname

#     def get_fullname(self):
#         return f'Person - {self.name},{self.surname}'
    
# class Student(Person):
#     def __init__(self, name, surname, class_name):
#         super().__init__(name, surname)
#         self.class_name = class_name

#     def get_fullname_and_class(self):
#         return f'Person - {self.name},{self.surname},{self.class_name}'

# student1 = Student('Elchin','Bayramli','9-a')
# # print(student1.get_fullname())
# print(student1.get_fullname_and_class())

# class ParentA:
#     def greet(self):
#         print(f'Hello from A')

# class ParentB:
#     def greet(self):
#         print(f'Hello from B')

# class Child(ParentA, ParentB):
#     def welcome(self):
#         super().greet()
#         ParentB.greet(self)

# # print(Child.mro())
# child1 = Child()
# # child1.greet()
# child1.welcome()

# # child1.greet_a()
# # child1.greet_b()
# child1.greet()
# #mro
# # print(Child.mro())
# child1.welcome()



# class Grandparent:
#     def say_hello(self):
#         print('Hello')

# class Parent(Grandparent):
#     ...

# class Child(Parent):
#     ...

# print(Child.mro())
# child = Child()
# child.say_hello()


# class Parent:
#     def say_hello(self):
#         print('Hello')

# class ChildA(Parent):
#     ...

# class ChildB(Parent):
#     ...

# print(ChildA.mro())


# class A:
#     ...

# class B(A):
#     ...

# class C(A):
#     ...

# class D(B,C):
#     ...

# print(D.mro()) # DBCA


# class A:
#     ...

# class B(A):
#     ...

# class C(A):
#     ...

# # class D(A,B,C): # olmaz
# #     ...

# class D(B,C,A): 
#     ...

# print(D.mro()) # DBCA


# class Person:
#     citizenship = 'Azerbaijani'
#     def __init__(self, name, surname):
#         self.is_valid_name(name)

#         self.name = name
#         self.surname = surname

#     def greet(self, symbol):
#         return f'Hello, {self.name} {self.surname}{symbol}'

#     @classmethod
#     def change_citizenship(cls, new_country):
#         cls.citizenship = new_country

#     @staticmethod
#     def is_valid_name(name: str):
#         if name.isalpha() and 2 <= len(name) <= 20:
#             ...
#         else:
#             raise ValueError('Name is invalid')
        
#     def __str__(self):
#         return f'Person {self.name} {self.surname} - {self.citizenship}'


# person1 = Person('Ali','Aliyev')
# person2 = Person('Vali','Valiyev')

# print(person1.citizenship)
# print(person2.citizenship)

# person1.change_citizenship('Turkey')
# print('---------------------------------------')
# print(person1.citizenship)
# print(person2.citizenship)

# print(person1)


# class Account:
#     bank_name = "Python National Bank"
#     def __init__(self, owner, balance):
#         self.validate_amount(balance)

#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.validate_amount(amount)

#         self.balance += amount
#         print(f'{amount} deposited. Balance is {self.balance}')

#     def withdraw(self, amount):
#         self.validate_amount(amount)

#         if amount > self.balance:
#             raise ValueError('Not enough balance')
        
#         self.balance -= amount
#         print(f'{amount} withdrawn. Balance is {self.balance}')

#     @staticmethod
#     def validate_amount(amount):
#         if amount <= 0:
#             raise ValueError('Amount should be positive')
        

# acc1 = Account('Vali',-5) #olmaz
# acc1 = Account('Vali',0) #olmaz

# acc1 = Account('Vali',50)
# acc1.deposit(5)
# acc1.withdraw(25)
# acc1.withdraw(30)

