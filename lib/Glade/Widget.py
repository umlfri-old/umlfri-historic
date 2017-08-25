import gobject

class CWidget(gobject.GObject):
    widgets = ()
    def __init__(self, app):
        gobject.GObject.__init__(self)
        self.application = app
    
    def Init(self):
        pass
