class Mammal:
    def __init__(self, species ):
        self.__species = species
    
    def get_species(self):
        return 'I am a ' + self.__species
    
    def make_sound(self):
        return '-Grrrrr'

class Dog( Mammal ):
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    def make_sound(self):
        return '-Woof! Woof!'
    
class Cat( Mammal ):
    def __init__(self):
        Mammal.__init__(self, 'Cat')
    
    def make_sound(self):
        return '-Meow'