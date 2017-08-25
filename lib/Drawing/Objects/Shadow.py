from DoubleContainer import CDoubleContainer

class CShadow(CDoubleContainer):
    def __init__(self, padding):
        CDoubleContainer.__init__(self)
        self.padding = int(padding)

    def GetPadding(self):
        return self.padding

    def GetHeight(self, element):
        return self.GetChilds()[0].GetHeight(element)

    def GetWidth(self, element):
        return self.GetChilds()[0].GetWidth(element)

    def Paint(self, x, y, element, w = None, h = None):
        if w is None:
            w = self.GetWidth(element)
        if h is None:
            h = self.GetHeight(element)
        self.GetChilds()[1].Paint(x + self.padding, y + self.padding,
                                    element, w, h)
        self.GetChilds()[0].Paint(x, y, element, w, h)

    def SetPadding(self, padding):
        self.padding = padding
