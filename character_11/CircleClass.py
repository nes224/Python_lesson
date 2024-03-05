class Circle:
    PI = 3.14159
    object_count = 0

    def __init__(self,radius):
        self.__radius = radius
        Circle.object_count += 1
    
    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def get_area(self):
        return Circle.PI * self.__radius * self.__radius
    
    def get_circumference(self):
        return 2 * Circle.PI * self.__radius

    def __del__(self):
        Circle.object_count -= 1

