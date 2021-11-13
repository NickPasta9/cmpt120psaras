#graphics.py

    def getP1(self): return self.p1.clone()

    def getP2(self): return self.p2.clone()

    def getCenter(self):
        p1 = self.p1
        p2 = self.p2
        return Point((p1.x+p2.x)/2.0, (p1.y+p2.y)/2.0)

Class Rectangle(_BBox):

    def __init__(self, p1, p2):
        _BBox.__init__(self, p1, p2)

    def __repr__(self):
        return "Rectangle((), ())".format(str(self.p1), str(self.p2))

    def _draw(self, canvas):
        p1 = self.p1
        p2 = self.p2
        x1,y1 = canvas.toScreen(p1.x,p1.y)
        x2,y2 = canvas.toScreen(p2.x,p2.y)
        return canvas.create_rectangle(x1,y1,x2,y2,options)

    def clone(self):
        other = Rectangle(self.pi, self(.p2)
        other.config = self.config.copy()
        
