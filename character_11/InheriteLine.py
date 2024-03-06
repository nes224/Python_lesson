from InheritePoint import Point

class Line( Point ):
    def __init__(self, x, y, length):
        Point.__init__(self, x, y)
        #super().__init__( x, y )
        self.__length = length
    
    def set_line(self, x=0, y=0, length=0 ):
        #Point.set_point(self, x, y)
        super().set_point( x, y)
        if length > 0:
            self.__length = length
        
    def get_length(self):
        return self.__length

    def __str__(self):
        return Point.__str__(self) + ', length:{}'.format(self.__length)