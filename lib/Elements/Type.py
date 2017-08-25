##### SetIcon/GetIcon
from traceback import print_stack

class CElementType:
    def __init__(self, id):
        self.icon = None
        self.id = id
        self.attributes = []
        self.connections = []
        self.appearance = None
        self.visAttrs = {}
    
    def AppendAttribute(self, value, type, propid = None, options = None):
        if propid is not None:
            self.visAttrs[propid] = value
        self.attributes.append((value, type, options))
    
    def AppendConnection(self, value, with, allowrecursive):
        self.connections.append((value, with, allowrecursive))
    
    def GetAppearance(self):
        return self.appearance
    
    def GetConnections(self):
        return self.connections
    
    def GetIcon(self):
        return self.icon
    
    def GetId(self):
        return self.id
    
    def Paint(self, element):
        x, y = element.GetPosition()
        self.appearance.Paint(x, y, element)
    
    def SetAppearance(self, appearance):
        self.appearance = appearance
    
    def SetIcon(self, pixbuf):
        self.icon = pixbuf
    
    def SetId(self, id):
        self.id = id
    
    def GetVisAttr(self, id):
        if id in self.visAttrs:
            return self.visAttrs[id]
        else:
            raise UMLException('VisAttrDontExists')
