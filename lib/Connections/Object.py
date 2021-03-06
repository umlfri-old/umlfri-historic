class CConnectionObject(object):
    def __init__(self, type, source = None, dest = None):
        self.type = type
        self.source = source
        self.destination = dest
        self.attributes = {}

    def GetType(self):
        return self.type
    
    def SetType(self, value):
        self.type = value

    def GetDestination(self):
        return self.destination

    def GetSource(self):
        return self.source

    def SetDestination(self, dest):
        self.destination = dest

    def SetSource(self, source):
        self.source = source 
    
    def Paint(self, Connection):
        self.type.Paint(Connection)
    
    def GetAttribute(self, key):
        if key in self.attributes:
            return self.attributes[key]
        else:
            raise UMLException("BadKey")
    
    def SetAttribute(self, key, value):
        self.attributes[key] = value        
    
    def RemoveAttribute(self, key):
        if key in self.attributes:
            del self.attributes[key]
        else:
            raise UMLException("BadKey")
    
    def GetVisualProperty(self, key):
        return self.attributes[self.type.GetVisAttr(key)]
        
    Source = property(GetSource, SetSource)
    Destination = property(GetDestination, SetDestination)