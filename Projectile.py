# Projectile.py
from math import*
from graphics import *
from random import randrange

class Projectile:

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel) / 2.0
        self.yvel = yvel1
        
class Tracker():
    def __init__(self, window, objToTrack):
        self.window = window
        self.objToTrack = objToTrack
        self.objToTrack.draw(self.window)

    # update()

class Target:
    def __init__(self, window):
        p1 = Point(310,110)
        p2 = Point(300,100)

        self.window = window

        rect = Rectangle(p1, p2)
        rect.draw(self.window)

    # How do you know if the target is hit?
