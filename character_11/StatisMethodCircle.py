class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.__radius = radius 
    
    def get_area(self):
        return Circle.area( self.__radius)

    @staticmethod
    def area( radius ):
        return Circle.PI * radius * radius
    
    @staticmethod
    def circumference( radius ):
        return 2*Circle.PI*radius

