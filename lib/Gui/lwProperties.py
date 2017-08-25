from lib.Glade import CWidget

import gobject
import gtk
import gtk.gdk

class ClwProperties(CWidget):
    widgets = ('lwProperties',)
    
    def Init(self):
        self.listStore = gtk.ListStore(str, bool, str, bool)
        row = self.listStore.append()
        self.listStore.set(row, 0, 'Name', 1, False, 2, 'CCCCC', 3, True)
        row1 = self.listStore.append()
        self.listStore.set(row1, 0, 'Type', 1, False, 2, 'Integer', 3, True)
        
        self.StrRenderer = gtk.CellRendererText()
        self.ComboRenderer = gtk.CellRendererCombo()
        
        self.Column1 = gtk.TreeViewColumn('Name')
        self.Column1.pack_start(self.StrRenderer, True)
        self.Column1.add_attribute(self.StrRenderer, 'text', 0)
        self.Column1.add_attribute(self.StrRenderer, 'editable', 1)
        
        self.Column2 = gtk.TreeViewColumn('Value')
        self.Column2.pack_start(self.StrRenderer, True)
        self.Column2.add_attribute(self.StrRenderer, 'text', 2)
        self.Column2.add_attribute(self.StrRenderer, 'editable', 3)
        
        self.lwProperties.append_column(self.Column1)
        self.lwProperties.append_column(self.Column2)
        
        self.lwProperties.set_model(self.listStore)
        