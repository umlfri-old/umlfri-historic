class CElement:
    def __init__(self, drwngArea, obj):
        self.drawArea = drwngArea
        self.drawArea.AddElement(self)
        self.objct = obj
        self.position = (0,0)

    def AreYouAtPosition(self, x, y):
        width = self.objct.GetType().GetAppearance().GetWidth(self)
        height = self.objct.GetType().GetAppearance().GetHeight(self)
        
        if  (self.position[0] <= x <= self.position[0] + width) and (self.position[1] <= y <= self.position[1] + height):
            return True
        else:
            return False
        
    def GetElementObject(self):
        return self.objct

    def GetPosition(self):
        return self.position

    def Paint(self):
        self.objct.Paint(self)

    def SetPosition(self, x, y):
        self.position = (x, y)
        
    def GetDrawingArea(self):
        return self.drawArea