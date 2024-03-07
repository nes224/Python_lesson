from CircleClass import Circle
from InheriteLine import Line

class Cylinder():
    def __init__(self, radius, x, y, length ):
        self.__circle = Circle(radius)
        self.__line = Line( x, y, length )

    def get_area(self):
        return ( 2 * self.__circle.get_area() ) + \
                ( self.__circle.get_circumference() * self.__line.get_length())