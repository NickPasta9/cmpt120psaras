# Test.py

from projectile import *
from graphics import *

def main():
    win = GrapWin("Title", 600, 600)
    for i in range(1,20)
        pro = Projectile(45, 40, 100)
        pro.update(i)
        center = Point(pro.getX(),pro.getY())
        r = 5
        circ = circle(center, r)

        t = tracker(win, circ)
        t

    tag = Target(win)

main()
