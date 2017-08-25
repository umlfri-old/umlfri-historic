from common import CWidget
from lib.lib import UMLException

class CtxtNotes(CWidget):
    widgets = ('txtNotes', )
    
    def Init(self):
        self.txtNotes.set_sensitive(False)
    
    def Fill(self, Element):
        self.element = Element
        if Element is None:
            self.txtNotes.get_buffer().set_text("")
            self.txtNotes.set_sensitive(False)
            return
        attrs = Element.GetObject().GetAttributes()
        type = Element.GetObject().GetType()
        cnt = 0
        for k in type.GetAttributes(): # attrs.items():
            v = attrs[k]
            atrtype = type.GetAttribute(k)
            if atrtype[0] == 'note':
                if cnt > 0:
                    raise UMLException("TooMuchNotes")
                self.txtNotes.get_buffer().set_text(v)
                self.txtNotes.set_sensitive(True)
                self.attr = k
                cnt += 1
