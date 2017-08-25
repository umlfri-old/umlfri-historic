from lib.lib import UMLException
from lib.Connections.Object import CConnectionObject
from math import sqrt

class CConnection:
    def __init__(self, screen, obj, points):
        self.screen = screen
        self.screen.AddConnection(self)
        self.conObject = obj
        self.points = points
        
    def AddPoint(self, index, x, y):
        if index < len(self.points) - 1:
            self.insert(index,(x,y))
        else:
            raise UMLException("PointNotExists")


    def AreYouAtPosition(self, x, y):
        Xo, Yo = self.points[0]
        for i in self.points[1:]:
            A = Yo - i[1]
            B = i[0] - Xo
            C = Xo*i[1] - i[0] * Yo
            T = (-B*Xo + A*Yo - A*y + B*x)/(A**2 + B**2)
            if T < 0:
                if sqrt((Xo - x)**2 + (Yo - y)**2) <=3:
                    return True
            elif T > 1:
                if sqrt((i[0] - x)**2 + (i[1] - y)**2) <=3:
                    return True
            else:
                if abs((abs(A*x + B*y + C))/sqrt(A**2 + B**2)) <=3:
                    return True
            Xo, Yo = i
        else:
            return False

    def MovePoint(self, index, x, y):
        if index < len(self.points) - 1:
            self.points[index] = (x,y)
        else:
            raise UMLException("PointNotExists")

    def Paint(self):
        self.conObject.Paint(self)

    def RemovePoint(self, index):
        if index < len(self.points) - 1:
            self.points.pop(index)
        else:
            raise UMLException("PointNotExists")
    
    def GetPoints(self):
        return self.points

    def GetDrawingArea(self):
        return self.screen
