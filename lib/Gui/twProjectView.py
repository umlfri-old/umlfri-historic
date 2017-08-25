from lib.Glade import CWidget

import gtk
import gtk.gdk

class CtwProjectView(CWidget):
    widgets = ('twProjectView', )
    
    def Init(self):
        # vytvorime si najpv model
        self.TreeModel = gtk.TreeStore(gtk.gdk.Pixbuf, str)
        
        #spravime jediny column
        self.Column = gtk.TreeViewColumn('Elements')
        self.twProjectView.append_column(self.Column)
        self.PbRenderer = gtk.CellRendererPixbuf()
        self.StrRenderer = gtk.CellRendererText()
        
        self.Column.pack_start(self.PbRenderer, False)
        self.Column.pack_start(self.StrRenderer, True)
        
        self.twProjectView.set_model(self.TreeModel)
        
    def Fill(self):
        pass
        