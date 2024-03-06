from CircleClass import Circle
from InheriteLine import Line

class Cylinder( Circle, Line):
    def __init__(self, radius, x ,y, length ):
        Circle.__init__(self, radius)
        Line.__init__(self, x, y, length)

    def get_area(self):
        return ( 2* Circle.get_area(self)) + \
                ( Circle.get_circumference(self) * Line.get_length(self))