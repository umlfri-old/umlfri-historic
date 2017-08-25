class CWindow:
    widgets = ()
    complexWidgets = {}
    name = ''
    dont_delete = False
    
    def __init__(self, app):
        self.application = app
    
    def Init(self):
        pass
    
    def Init2(self):
        if self.dont_delete:
            self.form.connect('delete-event', self.__on_delete_event)
    
    def Show(self):
        self.form.show()
    
    def Hide(self):
        self.form.hide()
    
    def __on_delete_event(self, win, event):
        win.hide()
        return True
