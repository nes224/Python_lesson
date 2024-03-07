from CircleClass import Circle
from InheriteLine import Line 
from AggregateCylinde import Cylinder

def main():
    circle = Circle( raidus=23)
    line = Line( x=101, y=89, length=6)
    
    cylinder = Cylinder( circle, line )
    print( 'This cylinder has area =', cylinder.get_area())

    del cylinder
    print( 'After delete cylinder. ')
    print( 'Circle radius is', circle.get_radius())
    print( 'Line is', line)

main()