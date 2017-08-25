from Container import CContainer

class CHBox(CContainer):
    def GetHeight(self, element):
        h = 0
        for i in self.childs:
            h += i.GetHeight(element)
        return h

    def Paint(self, x, y, element, w = None, h = None):
        if w is None:
            w = self.GetWidth(element)
        for i in self.childs:
            h = i.GetHeight(element)
            i.Paint(x, y, element, w, h)
            y += h
