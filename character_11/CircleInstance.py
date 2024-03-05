from CircleClass import Circle

def main():
    circle1 = Circle(10)
    circle2 = Circle(15)
    circle3  =Circle(20)

    print( 'Area of circle1 is', circle1.get_area())
    print( 'Area of circle2 is', circle2.get_area())
    print( 'Circumference of circle3 is', circle3.get_circumference())
    print( 'Number of circle is', Circle.object_count)

    del circle2
    print( 'Delete circle2, Number of circle is', Circle.object_count)

main()
