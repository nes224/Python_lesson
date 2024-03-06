from CylinderClass import Cylinder

def main():
    cylinder = Cylinder( radius = 12, x=25, y=30, length=55)
    print( 'This cylinder has area =', cylinder.get_area())

main()