class Person:
    def __init__(self):
        self.__name = ''
        self.__height = 0
        self.__weight = 0

    def set_name(self, name):
        self.__name = name
    
    def set_height(self,height):
        if height >= 50:
            self.__height = height
        else:
            print('Invalid height.')
    
    def set_weight(self, weight):
        if weight >= 3:
            self.__weight = weight
        else:
            print('Invalid weight')
    
    def get_name(self):
        return self.__name
    def get_height(self):
        return self.__height
    def get_weight(self):
        return self.__weight

    