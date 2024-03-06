class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def set_point(self, x=0, y=0):
        if x > 0:
            self.__x = x
        if y > 0:
            self.__y = y
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def __str__(self):
        return 'x:{}, y:{}'.format( self.__x, self.__y)