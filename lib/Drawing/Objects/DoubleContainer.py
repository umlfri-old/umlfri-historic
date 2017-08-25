from Container import CContainer
from lib.lib import UMLException

class CDoubleContainer(CContainer):
    def AppendChild(self, child):
        if len(self.GetChilds()) > 1:
            raise UMLException("DCChildCount")
        CContainer.AppendChild(self, child)
