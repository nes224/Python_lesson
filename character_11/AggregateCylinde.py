from CircleClass import Circle
from InheriteLine import Line

class Cylinder():
    def __init__(self, circle, line ):
        self.__circle = circle
        self.__line = line 
    
    def get_area(self):
        return ( 2*self.__circle.get_area()) + \
        ( self.__circle.get_circumference() * self.__line.get_length())