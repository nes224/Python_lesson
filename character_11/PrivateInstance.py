from PrivatePerson import Person

def main():
    person1 = Person()
    person1.set_name('Worapong Tanasilp')
    person1.set_height(179)
    person1.set_weight(82)

    print( person1.person_info() )

    person1.set_height(45)
    person1.set_weight(79)

    print('Person {} change to ({},{})'.format( person1.get_name(), person1.get_height(), person1.get_weight()))

main()