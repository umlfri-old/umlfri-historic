import gobject

class SelectedMessage(gobject.GObject):
    def __init__(self, selected):
        gobject.GObject.__init__(self)
        self.Selected = selected
        
    def GetSelected(self):
        return self.Selected
    