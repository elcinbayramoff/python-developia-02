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
# print(person1.name)
# person2 = Person('Ali','Aliyev')
# print(person2.name)

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

person1 = Person('Elchin','Bayramli')
person2 = Person('Ali','Aliyev')

# person1.age = 20
# print(person1.age)
# del person1.a

print(person1.greet('.'))
print(person2.greet('?'))