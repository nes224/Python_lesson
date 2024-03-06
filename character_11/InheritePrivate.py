from InheritePoint import Point
from InheriteLine import Line

def main():
    point1 = Point( 15, 30 )
    print( 'point1', point1 )
    point1.set_point( y=41 )
    print( 'move to', point1 )

    line1 = Line( 22, 19, 45 )
    print( 'line1', line1 )
    line1.set_line( x=27, length=34 )
    print( 'move and resize', line1 )

main()