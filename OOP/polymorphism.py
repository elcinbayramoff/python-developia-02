# class Cat:
#     def miaw(self):
#         print('Miaw Miaw!')

# class Dog:
#     def bark(self):
#         print('Bark Bark!')

# class Lion:
#     def roar(self):
#         print('Rooar')

# cat1 = Cat()
# dog1 = Dog()
# lion1 = Lion()

# cat1.miaw()
# dog1.bark()
# lion1.roar()


class Animal:
    def speak(self):
        print()

class Cat(Animal):
    def speak(self):
        print('Miaw Miaw!')

class Dog(Animal):
    def speak(self):
        print('Bark Bark!')

class Lion(Animal):
    def speak(self):
        print('Rooar')

cat1 = Cat()
dog1 = Dog()
lion1 = Lion()
animals = [cat1,dog1,lion1]
for animal in animals:
    animal.speak()