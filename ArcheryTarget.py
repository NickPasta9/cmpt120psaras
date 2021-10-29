#ArcheryTarget.py
from graphics import *

def main():
    win = GraphWin('Archery Target',800,800)
    colors = ["white","black","blue","red","yellow"]

    color = 0
    for radius in range(75*5,1,-75):
        c = Circle(Point(400,400),radius)
        c.setFill(colors[color])
        c.draw(win)
        color = color + 1

main()
