# CircleInterception.py

from graphics import*
import math

def Circle_coordinates():
    win = GraphWin("Intersection circle",800,800)

    win.setCoords(-10,-10,10,10)
    Line(point(0,10),point(0,-10)).draw(win)
    Line(point(10,0),point(-10,0)).draw(win)

    radius = int(input("Enter the radius for the circle: "))
    c1 = Circle(Point(0,0), radius)
    c1.draw(win)

    Yintercept = int(input("Enter the y-intercept from -10 to 10: "))
    Line(point(10,intercept),point(-10,intercept)).draw(win)

    x = (radius*radius) - (Yintercept*Yintercept)
    x1 = math.sqrt(x)
    x2 = - (math.sqrt(x))
    p1 = point(x1< Yintercept)
    p1.setFill('red')
    p1.draw(win)
    p2 = point(x2,Yintercept)
    p2.setFill('red')
    p2.draw(win)

    print("The first x value of interception is",x1,
          "\nThe second x value of interception is",x2)
    return ""

def main():
    print(Circle_coordinates())
main()
    
    
