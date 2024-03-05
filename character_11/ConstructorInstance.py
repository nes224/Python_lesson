from ConstructorPerson import Person_2
def main():
    person1 = Person_2()
    person2 = Person_2('Test Test1')
    person3 = Person_2('Test Test2', 176)
    person4 = Person_2( weight=82, name='Worapong Tanasilp')

    print(person1)
    print(person2)
    print(person3)
    print(person4)

    print('\nDelete person3 when program running.')
    del person3

    print('\nDelete all person when program terminate.')

main()