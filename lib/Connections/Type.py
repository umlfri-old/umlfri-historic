from Line import CConnectionLine
from Arrow import CConnectionArrow
from math import atan2

class CConnectionType(object):
    def __init__(self, id, line = None, scrArrow = None, destArrow = None, icon = None):
        self.line = line
        self.scrArrow = scrArrow
        self.destArrow = destArrow
        self.id = id
        self.icon = icon
    
    def SetIcon(self, value):
        self.icon = value
    
    def GetIcon(self):
        return self.icon
    
    def GetDestArrow(self):
        return self.destArrow
    
    def GetLine(self):
        return self.line

    def GetSrcArrow(self):
        return self.scrArrow
    
    def GetId(self):
        return self.id
    
    def SetId(self, value):
        self.id = value
    
    def SetDestArrow(self, value):
        self.destArrow = value
    
    def SetSrcArrow(self, value):
        self.scrArrow = value

    def Paint(self, Connection):
        tmp = Connection.GetPoints()
        Xo,Yo = tmp[0]
        for i in tmp[1:]:
            self.line.Paint(Xo,Yo,i[0],i[1],Connection)
            Xo,Yo = i
            
        if self.scrArrow is not None:
            X = tmp[0][0] - tmp[1][0]
            Y = tmp[0][1] - tmp[1][1]
            self.scrArrow.Paint(tmp[0][0],tmp[0][1],atan2(-X,Y),Connection)
        
        if self.destArrow is not None:
            X = tmp[-1][0] - tmp[-2][0]
            Y = tmp[-1][1] - tmp[-2][1]
            self.destArrow.Paint(tmp[-1][0],tmp[-1][1],atan2(-X,Y),Connection)
    
    ID = property(GetId, SetId)
    Icon = property(GetIcon, SetIcon)
    DestinationArrow = property(GetDestArrow, SetDestArrow)
    SourceArrow = property(GetSrcArrow, SetSrcArrow)