class CConnectionObject(object):
    def __init__(self, type, source = None, dest = None):
        self.type = type
        self.source = source
        self.destination = dest

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
    
    Source = property(GetSource, SetSource)
    Destination = property(GetDestination, SetDestination)