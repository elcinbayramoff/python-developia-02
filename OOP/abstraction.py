from abc import ABC, abstractmethod
import math 

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


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side
    
    def area(self):
        return self.side ** 2
    

class Triangle(Figure):
    def __init__(self, side):
        self.side = side
    
    def perimeter(self):
        return 3 * self.side
    
    def area(self):
        return ((3 ** (1/2)) * self.side ** 2) / 4
        return (math.sqrt(3) * self.side ** 2) / 4
    

circle1 = Circle(5)
circle2 = Circle(10)

square1 = Square(2)
square2 = Square(4)

triangle1 = Triangle(3) 
triangle2 = Triangle(6)

figures = [circle1, circle2, square1, square2, triangle1, triangle2]

for figure in figures:
    print('Area:',figure.area())
    print('Perimeter:',figure.perimeter())
    print('------------------------------------')