import gtk, gtk.gdk, gobject

import common

from lib.Glade import CWidget
from lib.Drawing import CDrawingArea, CElement, CConnection

from lib.Drawing import CDrawingArea, CElement, CConnection
from lib.Elements import CElementObject
from lib.Connections import CConnectionObject
#^odstranit^ ???

class CpicDrawingArea(CWidget):
    widgets = ('picDrawingArea', 'picEventBox', 'picVBar', 'picHBar')
    
    __gsignals__ = {
        'get_selected':  (gobject.SIGNAL_RUN_LAST, gobject.TYPE_OBJECT, 
            ()), 
        'set_selected':  (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, 
            (gobject.TYPE_OBJECT, )), 

    }
    
    def Init(self):
        self.picEventBox.drag_source_set(gtk.gdk.BUTTON1_MASK, [('document/uml', 0, gtk.TARGET_SAME_WIDGET)], gtk.gdk.ACTION_MOVE)
        self.picEventBox.drag_dest_set(gtk.DEST_DEFAULT_ALL, [('document/uml', 0, gtk.TARGET_SAME_WIDGET)], gtk.gdk.ACTION_MOVE)
        self.Buffer = gtk.gdk.Pixmap(self.picDrawingArea.window, 1000, 1000)
        self.DrawingArea = CDrawingArea(self.picDrawingArea, self.Buffer)
        #self.picVBar.set_property('fixed_slider_length', False)
        #self.picHBar.set_property('fixed_slider_length', False)
        
        self.AdjustScrollBars()
        self.Paint()
        #tmp = (1,2,3), (10,3,5)
        #tmp = [max(i) for i in zip(*tmp)]
        
    def GetDrawingArea(self):
        return self.picDrawingArea
        
    def GetWindowSize(self):
        tmpx, tmpy =  self.picDrawingArea.window.get_size()
        return (int(tmpx), (tmpy))
        
    def GetDrawingAreaSize(self):
        tmp = [int(max(i)) for i in zip(self.DrawingArea.GetSize(), self.picDrawingArea.window.get_size())]
        return tuple(tmp)
        
    def GetAbsolutePos(self, posx, posy):
        return int(self.picHBar.get_value() + posx), int(self.picVBar.get_value() + posy)
        
    def Paint(self):
        self.DrawingArea.Paint()
        self.Repaint()
        
    def Repaint(self):
        posx, posy = int(self.picHBar.get_value()), int(self.picVBar.get_value())
        sizx, sizy = self.GetWindowSize()
        wgt = self.picDrawingArea.window
        gc = wgt.new_gc()
        wgt.draw_drawable(gc, self.Buffer, posx, posy, 0, 0, sizx, sizy)
        
    def AdjustScrollBars(self):
        dasx, dasy = self.GetDrawingAreaSize()
        wisx, wisy = self.GetWindowSize()
        
        tmp = self.picHBar.get_adjustment()
        tmp.upper = dasx 
        tmp.page_size = wisx
        self.picHBar.set_adjustment(tmp)
        
        tmp = self.picVBar.get_adjustment()
        tmp.upper = dasy 
        tmp.page_size = wisy
        self.picVBar.set_adjustment(tmp)
        
    def on_picEventBox_button_press_event(self, widget, event):
        toolBtnSel =  self.emit('get_selected').GetSelected()
        posx, posy = self.GetAbsolutePos(event.x, event.y)
        if toolBtnSel is None:
            itemSel = self.DrawingArea.GetElementAtPosition(posx, posy)
            if itemSel is not None:
                if not (event.state & gtk.gdk.CONTROL_MASK):
                    self.DrawingArea.DeselectAll()
                    self.DrawingArea.AddToSelection(itemSel)
                elif itemSel in self.DrawingArea.GetSelected():
                    self.DrawingArea.RemoveFromSelection(itemSel)
                else:
                    self.DrawingArea.AddToSelection(itemSel)
                self.Paint()
            elif self.DrawingArea.SelectedCount() > 0:
                print "2",
                if not (event.state & gtk.gdk.CONTROL_MASK):
                    self.DrawingArea.DeselectAll()
                    self.Paint()
                    
            print self.DrawingArea.GetSelectSquare()
        
        elif toolBtnSel[0] == 'Element':
            ElementType = self.application.ElementFactory.GetElement(toolBtnSel[1])
            ElementObject = CElementObject(ElementType)
            CElement(self.DrawingArea, ElementObject).SetPosition(posx, posy)
            CElement(self.DrawingArea, ElementObject).SetPosition(posx, posy)
            self.emit('set_selected', common.SelectedMessage(None))
            self.Paint()
            
        elif toolBtnSel[0] == 'Connection':
            pass
            """
            ConnectionType = self.application.ConnectionFactory.GetConnection(self.tbToolBox.toolBtnSel[0])
            ConnectionObject = CConnectionObject(ConnectionType)
            CConnection(self.DrawingArea, ConnectionObject).SetPosition(posx, posy)
            """
        
    def on_picDrawingArea_configure_event(self, widget, tmp):
        self.Repaint()
        
    def on_picDrawingArea_expose_event(self, widget, tmp):
        self.Repaint()
        
    def on_picVBar_value_changed(self, widget):
        self.Repaint()
        
    def on_picHBar_value_changed(self, widget):
        self.Repaint()
        
    def on_picDrawingArea_size_allocate(self, widget, tmp):
        self.AdjustScrollBars()
        self.Repaint()
        
    def on_picEventBox_scroll_event(self, widget, event):
        if  event.state & gtk.gdk.SHIFT_MASK :
            self.__Scroll(self.picHBar, event.direction)
        else:
            self.__Scroll(self.picVBar, event.direction)
        self.Repaint()
        
    def on_picEventBox_drag_begin(self, widget, context):
        print 'begin'
    
    def on_picEventBox_drag_motion(self, widget, context, x, y, time):
        print 'motion', x, y
    
    def on_picEventBox_drag_drop(self, widget, context, x, y, time):
        print 'drop', x, y
        
    def __Scroll(self, scrollbar, direction):
        tmp = scrollbar.get_adjustment()
        if direction == gtk.gdk.SCROLL_UP:
            tmp.value = max(tmp.lower, tmp.value - 10)
        elif direction == gtk.gdk.SCROLL_DOWN:
            tmp.value = min(tmp.upper - tmp.page_size, tmp.value + 10)
        scrollbar.set_adjustment(tmp)
        
        
