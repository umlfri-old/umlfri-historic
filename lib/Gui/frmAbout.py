import lib.Glade

class CfrmAbout(lib.Glade.CWindow):
    widgets = ()
    name = 'frmAbout'
    
    def on_cmdOkay_clicked(self, btn):
        self.Hide()
    
    def on_frmAbout_delete_event(self, win, event):
        win.set_property('visible', False)
        return True
