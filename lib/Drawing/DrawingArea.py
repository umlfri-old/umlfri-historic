from lib.lib import UMLException
import pango
import lib.consts

class CDrawingArea:
    def __init__(self, widget, drawable = None):
        self.widget = widget
        self.font = pango.FontDescription(lib.consts.FONT_TYPE)
        self.pango = (self.widget.create_pango_context(), self.widget.create_pango_layout(""))
        self.pango[1].set_font_description(self.font)
        self.elements = []
        self.elementsreverse = []
        self.connections = []
        
        if drawable is None:
            self.drawable = self.widget.window
        else:
            self.drawable = drawable
        
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

    def GetSize(self):
        return (1000, 1000)
        
    def GetDrawable(self):
        return self.drawable        
        
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
