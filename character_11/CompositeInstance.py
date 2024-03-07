from CompositeCylinder import Cylinder

def main():
    cylinder = Cylinder( radius=7, x=35, y=51, length=60 )
    print( 'This cylinder has area =', cylinder.get_area())

main()