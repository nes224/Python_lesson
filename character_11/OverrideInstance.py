from OverrideClass import *

def main():
    mammal = Mammal( 'regular animal' )
    dog = Dog()
    cat = Cat()

    print(mammal.get_species(), mammal.make_sound() )
    print( dog.get_species(), dog.make_sound() )
    print( cat.get_species(), cat.make_sound() )

main()