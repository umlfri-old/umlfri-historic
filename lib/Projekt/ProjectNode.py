from lib.lib import UMLException

class CProjectNode(object):
    def __init__(self, parent, name, type):
        self.parent = parent
        self.childs = []
        self.drawingareas = []        
        self.type = type
    
    def GetType(self):
        return self.type
    
    def AddChild(self, child):
        if child not in self.childs:
            self.childs.append(child)
            child.parent = self
        else:
            raise UMLException("ExistsChild")
            

    def AddDrawingArea(self, area):
        if area not in self.drawingareas:
            self.drawingareas.append(area)
        else:
            raise UMLException("ExistsArea")

    def GetChild(self, index):
        if index <= len(self.childs) - 1:
            return self.childs[index]
        else:
            raise UMLException("NodeNotExists")
    
    def GetChilds(self):
        return self.childs
    
    def GetParent(self):
        return self.parent

    def RemoveChild(self, child):
        if child in self.childs: 
            self.childs.remove(child)
        else:
            raise UMLException("ChildNotExists")
    
    def RemoveDrawingArea(self, area):
        if area in self.drawingareas:
            self.drawingareas.remove(area)
        else:
            raise UMLException("AreaNotExists")

    def SetParent(self, parent):
        self.parent = parent
        
    Parent = property(GetParent,SetParent)
