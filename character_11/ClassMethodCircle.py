import math 

class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius

    @classmethod
    def from_area(cls, area):
        radius = math.sqrt(area/Circle.PI)
        return cls(radius)
    
    @classmethod
    def from_circumference(cls, circumference):
        radius = circumference / Circle.PI / 2
        return cls(radius)