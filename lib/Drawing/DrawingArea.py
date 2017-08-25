from lib.lib import UMLException
import pango

class CDrawingArea:
    def __init__(self, widget):
        self.widget = widget
        self.font = pango.FontDescription('Arial 12')
        self.pango = (self.widget.create_pango_context(), self.widget.create_pango_layout(""))
        self.pango[1].set_font_description(self.font)
        self.elements = []
        self.elementsreverse = []
        self.connections = []
        
    def AddElement(self, element):
        if element not in self.elements:
            self.elements.append(element)
            self.elementsreverse.insert(0, element)
        else:
            raise UMLException("ElementAlreadyExists")
        
    def AddConnection(self, connection):
        if connection not in self.connections:
            self.connections.append(connection)
        else:
            raise UMLException("ConnectionAlreadyExists")
        
    def DeleteElement(self, element):
        if element in self.elements:
            self.elements.remove(element)
            self.elementsreverse.remove(element)
        else:
            raise UMLException("ElementDoesNotExists")
        
    def DeleteConnection(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
        else:
            raise UMLException("ConnectionDoesNotExists")

    def GetElementAtPosition(self, x, y):
        for c in self.connections:
            if c.AreYouAtPosition(x, y):
                return c
                
        for e in self.elementsreverse:
            if e.AreYouAtPosition(x, y):
                return e
            
        return None
        
    def GetWidget(self):
        return self.widget
    
    def GetPango(self):
        return self.pango

    def Paint(self):
        for e in self.elements:
            e.Paint()
        
        for c in self.connections:
            c.Paint()
