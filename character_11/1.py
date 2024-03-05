from PersonClass import Person 

def main():
    person1 = Person()
    person1.name = 'Suchada Srisawat'
    person1.height = 157
    person1.weight = 54

    person2 = Person()
    person2.name = 'Chaiyanan Pagdee'
    person2.height = 176
    person2.weight = 74

    print( person.__doc__ )
    print ( person1.person_info() )
    print( person2.person_info() )
