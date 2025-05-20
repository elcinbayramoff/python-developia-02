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

class ParentA:
    def greet(self):
        print(f'Hello from A')

class ParentB:
    def greet(self):
        print(f'Hello from B')

class Child(ParentA, ParentB):
    def welcome(self):
        # super().greet()
        ParentB.greet(self)

child1 = Child()
# child1.greet()
# child1.greet_a()
# child1.greet_b()
child1.greet()
#mro
# print(Child.mro())
child1.welcome()