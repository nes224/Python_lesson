class Person_2:
    def __init__(self, name='-', height=0, weight=0):
        self.__name = name
        self.__height = height
        self.__weight = weight
        print('create person[{}]'.format( self.__name.split( ' ' )[0]))
    
    def __str__(self):
        return 'Name: {}, Height: {}, Weight: {}'.format(
            self.__name, self.__height, self.__weight)
    
    def __del__(self):
        print('destroy Person[{}]'.format( self.__name.split( ' ' )[0]))

    