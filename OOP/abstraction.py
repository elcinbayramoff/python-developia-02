from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def perimeter(self):
        ...
    
    @abstractmethod
    def area(self):
        ...
    

class Circle(Figure):
    def __init__(self,radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def area(self):
        return 3.14 * self.radius ** 2

circle1 = Circle(5)
print(circle1.perimeter())
print(circle1.area())