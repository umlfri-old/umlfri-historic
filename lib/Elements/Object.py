from lib.lib import UMLException

class CElementObject:
    def __init__(self, type):
        self.type = type
        self.connections = []
        self.attribs = {}
        for i in self.type.GetAttributes():
            self.SetAttribute(i, self.type.GetDefValue(i))            
        self.SetAttribute('Name', 'New ' + type.GetId())        

    def AddConnection(self, connection):
        if connection not in self.connections:
            self.connections.append(connection)
        else:
            raise UMLException("ConnectionAlreadyExists")
            
    def GetConnections(self):
        return self.connections
        
    def GetType(self):
        return self.type
        
    def GetName(self):
        if 'Name' in self.attribs:
            return self.attribs['Name']
        else:
            raise UMLException("KeyError")

    def GetAttribute(self, key):
        if key in self.attribs:
            return self.attribs[key]
        else:
            return None
        
    def GetVisualProperty(self, key):
        return self.attribs[self.type.GetVisAttr(key)]

    def Paint(self, element):
        self.type.Paint(element)

    def RemoveAttribute(self, key):
        if self.attribs.has_key(key):
            del self.attribs[key]
        else:
            raise UMLException("KeyError")
            
    def SetAttribute(self, key, value):
        self.attribs[key] = value
        
    def RemoveConnection(self, connection):
        if connection in self.connections:
            self.connections.remove
        else:
            raise UMLException("ConnectionNotFound")