from lib.lib import UMLException

class CElementObject:
    def __init__(self, type, name):
        self.type = type
        self.connections = []
        self.attribs = {}

    def AddConnection(self, connection):
        if connection not in self.connections:
            self.connections.append(connection)
        else:
            raise UMLException("ConnectionAlreadyExists")
            
    def AddAttribute(self, key, value):
        if not self.attribs.has_key(key):
            self.attribs[key] = value
        else:
            raise UMLException("KeyAlreadyExists")
            
    #def AddVisualProperty(self, key, value):
    #    if not self.visualProp.has_key(key):
    #        self.visualProp[key] = value
    #    else:
    #        raise UMLException("KeyAlreadyExists")
    #    
    def GetConnections(self):
        return self.connections
        
    def GetType(self):
        return self.type

    def GetVisualProperty(self, key):
        return self.attribs[self.type.GetVisAttr(key)]

    def Paint(self, element):
        self.type.Paint(element)

    def RemoveAttribute(self, key):
        if self.attribs.has_key(key):
            del self.attribs[key]
        else:
            raise UMLException("KeyError")
        
    def RemoveConnection(self, connection):
        if connection in self.connections:
            self.connections.remove
        else:
            raise UMLException("ConnectionNotFound")