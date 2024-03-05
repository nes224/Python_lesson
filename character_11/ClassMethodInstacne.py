from ClassMethodCircle import Circle

def main():
    circle1 = Circle.from_area(314.159)
    print( 'Radius of circle1 is', circle1.radius)

    circle2 = Circle.from_circumference(125.6636)
    print( 'Radius of circle2 is', circle2.radius)
main()