from lib.Glade import CWidget
from lib.Projekt import CProject, CProjectNode
from gtk.gdk import pixbuf_new_from_file
from lib.consts import ELEMENT_IMAGE, VIEW_IMAGE, FOLDER_IMAGE

import gtk
import gtk.gdk

class CtwProjectView(CWidget):
    widgets = ('twProjectView', )
    
    def Init(self):
        # vytvorime si najpv model
        self.TreeStore = gtk.TreeStore(str, gtk.gdk.Pixbuf)
        # ikonky
        self.icons = {  'View' : pixbuf_new_from_file(VIEW_IMAGE),
                        'Element' : pixbuf_new_from_file(ELEMENT_IMAGE),
                        'Folder' : pixbuf_new_from_file(FOLDER_IMAGE) }
        
        parent = self.TreeStore.append(None)
        self.TreeStore.set(parent, 0, 'untitled', 1, self.icons['View'])
        x = self.TreeStore.append(parent)
        self.TreeStore.set(x, 0, 'Logical View', 1, self.icons['Folder'] )
        y = self.TreeStore.append(x)
        self.TreeStore.set(y, 0, 'Elements', 1, self.icons['Folder'] )
       
        #spravime jeden column
        self.Column = gtk.TreeViewColumn('Elements')
        self.twProjectView.append_column(self.Column)
        
        #nastavime renderer
        self.StrRenderer = gtk.CellRendererText()
        self.PbRenderer = gtk.CellRendererPixbuf()
        
        self.Column.pack_start(self.PbRenderer, False)
        self.Column.add_attribute(self.PbRenderer, 'pixbuf', 1)
        self.Column.pack_start(self.StrRenderer, True)
        self.Column.add_attribute(self.StrRenderer, 'text', 0)
        
        self.twProjectView.set_model(self.TreeStore)
        
        #projekt view
        self.Projekt = CProject()
        root = CProjectNode(
        
    def Fill(self):
        pass
        