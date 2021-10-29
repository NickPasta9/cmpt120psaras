# Line_Segment_Info.py

from graphics import *
import math

def main():
    win = GraphWin("Click Me!",500,500)
    win.setCoords(0,0,500,500)
    message = Text(Point(250,450),"Click on two points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    print("Point 1:",round(p1.getX(),4),round(p1.getY(),4))

    p2 = win.getMouse()
    p2.draw(win)
    print("Point 2:",round(p2.getX(),4),round(p2.getY(),4))

    line = Line(p1,p2)
    line.draw(win)

    midX = (p1.getX()+p2.getX()) / 2
    midY = (p1.getY()+p2.getY()) / 2
    mid = Point(midX,midY)
    mid.setFill("cyan")
    mid.draw(win)

    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    if dx != 0:
        slope = dy/dx
        slope = round(slope,4)
    else:
        slope = "undefined"
    print("Slope:",slope)

    length = math.sqrt(dx**2 + dy**2)
    print("Length",round(length,4),"pixels")

main()
