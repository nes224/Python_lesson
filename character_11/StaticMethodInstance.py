from StatisMethodCircle import Circle

def main():
    print( 'Area of circle radius 15 is', Circle.area(15))
    print( 'Circumference of circle radius 20 is', Circle.circumference(20))

    circle1 = Circle(10)
    print('Area of circle 1 is', circle1.get_area())

main()