import lib.Glade
import pygtk
import gtk

from tbToolBox import CtbToolBox
from twProjectView import CtwProjectView
from mnuItems import CmnuItems
from picDrawingArea import CpicDrawingArea

from lib.Drawing import CDrawingArea, CElement, CConnection
from lib.Elements import CElementObject
from lib.Connections import CConnectionObject
#^odstranit^

class CfrmMain(lib.Glade.CWindow):
    name = 'frmMain'
    widgets = ('hboxWorkSpace', 'mnuUseCaseDiagram', 
        'twProjectView', 'lwProperties')
    complexWidgets = {
        'tbToolBox': CtbToolBox, 
        'twProjectView': CtwProjectView,
        'mnuItems': CmnuItems,
        'picDrawingArea': CpicDrawingArea, 
        }
    
    def Init(self):
        self.mnuItems.connect('create_diagram', self.on_mnuItems_create_diagram)
        self.picDrawingArea.connect('get_selected', self.on_picDrawingArea_get_selected)
        self.mnuItems.LoadDiagramsMenu()
        self.form.connect('configure_event', self.on_picDrawingArea_repaint)
        self.form.connect('expose_event', self.on_picDrawingArea_repaint)
    
    
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
    def on_picDrawingArea_repaint(self, widget, data):
        """wgt = self.picDrawingArea.picDrawingArea.window
        gc = wgt.new_gc()
        wgt.draw_drawable(gc, self.Buffer, 0, 0, 0, 0, 100, 100)
        #self.DrawingArea.Paint()"""
        
    def on_mnuItems_create_diagram(self, widget, diagramId):
        self.tbToolBox.SetButtons(diagramId)
        
    def on_picDrawingArea_clicked(self, widget, posx, posy):
        if self.tbToolBox.Selected == None:
            print self.DrawingArea.GetElementAtPosition(posx, posy)
        elif self.tbToolBox.Selected[1] == 'Element':
            ElementType = self.application.ElementFactory.GetElement(self.tbToolBox.Selected[0])
            ElementObject = CElementObject(ElementType)
            CElement(self.DrawingArea, ElementObject).SetPosition(posx, posy)
            self.tbToolBox.ResetSelected()
            self.picDrawingArea.picDrawingArea.set_size_request(*self.DrawingArea.GetSize())
        elif self.tbToolBox.Selected[1] == 'Connection':
            pass
            """
            ConnectionType = self.application.ConnectionFactory.GetConnection(self.tbToolBox.Selected[0])
            ConnectionObject = CConnectionObject(ConnectionType)
            CConnection(self.DrawingArea, ConnectionObject).SetPosition(posx, posy)
            """
        self.DrawingArea.Paint()
        
    def on_picDrawingArea_get_selected(self, widget):
        return self.tbToolBox.GetSelected()