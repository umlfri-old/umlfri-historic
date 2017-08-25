import lib.Glade
import pygtk

from tbToolBox import CtbToolBox
from twProjectView import CtwProjectView
from mnuItems import CmnuItems

class CfrmMain(lib.Glade.CWindow):
    name = 'frmMain'
    widgets = ('hboxWorkSpace', 'mnuUseCaseDiagram', 
        'picDrawingArea', 'twProjectView', 'lwProperties')
    complexWidgets = {
        'tbToolBox': CtbToolBox, 
        'twProjectView': CtwProjectView,
        'mnuItems': CmnuItems,
        }
    
    def Init(self):
        self.mnuItems.connect('create_diagram', self.on_mnuItems_create_diagram)
        self.mnuItems.LoadDiagramsMenu()
    
    # ** Main menu **
    # File
    def on_frmMain_destroy(self, frm):
        self.ActionQuit(frm)
    
    def on_mnuNew_activate(self, mnu):
        pass
        
    def on_mnuOpen_activate(self, mnu):
        pass
        
    def on_mnuSave_activate(self, mnu):
        pass
        
    def on_mnuSaveAs_activate(self, mnu):
        pass
        
    def on_mnuQuit_activate(self, mnu):
        self.ActionQuit(mnu)
    
    # Edit
    def on_mnuCut_activate(self, mnu):
        pass
        
    def on_mnuCopy_activate(self, mnu):
        pass
        
    def on_mnuPaste_activate(self, mnu):
        pass
        
    def on_mnuDelete_activate(self, mnu):
        pass
        
    # Diagrams
    def on_mnuViewTools_activate(self, mnu):
        # self.tbTools.set_child_visible(mnu.get_active())
        if mnu.get_active():
            self.hboxWorkSpace.pack_start(self.tbToolBox, expand=False, fill=False)
            self.hboxWorkSpace.reorder_child(self.tbToolBox, 0)
        else:
            self.hboxWorkSpace.remove(self.tbToolBox)
            
    # View
    def on_mnuClassDiahram_activate(self, mnu):
        pass
        
    def on_mnuUseCaseDiahram_activate(self, mnu):
        pass
        
    # Help
    def on_mnuAbout_activate(self, mnu):
        self.application.GetWindow('frmAbout').Show()
        
    # Actions
    def ActionQuit(self, widget):
        self.application.Quit()
    
    def ActionNew(self, widget):
        pass
        
    def ActionOpen(self, widget):
        pass
    
    def ActionLoadToolBar(self, widget):
        pass
    
    # Moje vlastne signale
    def on_mnuItems_create_diagram(self, widget, diagramId):
        self.tbToolBox.SetButtons(diagramId)