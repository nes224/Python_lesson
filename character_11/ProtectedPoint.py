class Point:
    def __init__( self, x, y ):
        self._x = x
        self._y = y 
    
    def set_point(self, x=0, y=0 ):
        if x > 0:
            self._x = x
        if y > 0:
            self._y = y 
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def __str__(self):
        return 'x:{}, y:{}'.format( self._x, self._y )