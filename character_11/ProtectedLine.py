from ProtectedPoint import Point

class Line( Point ):
    def __init__(self, x, y, length):
        Point.__init__(self, x, y)
        self.__length = length
    
    def set_line(self, x=0, y=0, length=0):
        if x > 0:
            self._x = x 
        if y > 0:
            self._y = y 
        if length > 0:
            self.__length = length
    
    def __str__(self):
        return 'x:{}, y:{}, length:{}'.format(self._x,self._y,self.__length)

