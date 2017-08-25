class CWindow:
    widgets = ()
    complexWidgets = {}
    name = ''
    
    def __init__(self, app):
        self.application = app
    
    def Init(self):
        pass
    
    def Show(self):
        self.form.show()
    
    def Hide(self):
        self.form.hide()
