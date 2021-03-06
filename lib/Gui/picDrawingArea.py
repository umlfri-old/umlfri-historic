import gtk, gtk.gdk, gobject

from lib.consts import SELECT_SQUARE_COLOR, SELECT_SQUARE_SIZE

from common import CWidget
from lib.Drawing import CDrawingArea, CElement, CConnection

from lib.Drawing import CDrawingArea, CElement, CConnection
from lib.Elements import CElementObject
from lib.Connections import CConnectionObject
#^odstranit^ ???

targets = [('document/uml', 0, gtk.TARGET_SAME_WIDGET)]

class CpicDrawingArea(CWidget):
    name = 'picDrawingArea'
    widgets = ('picDrawingArea', 'picEventBox', 'picVBar', 'picHBar')
    
    __gsignals__ = {
        'get_selected':  (gobject.SIGNAL_RUN_LAST, gobject.TYPE_PYOBJECT, 
            ()), 
        'set_selected':  (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, 
            (gobject.TYPE_PYOBJECT, )), 
        'selected_item':  (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, 
            (gobject.TYPE_PYOBJECT, )), 
        

    }
    dnd = False
    
    def Init(self):
        self.picEventBox.drag_dest_set(gtk.DEST_DEFAULT_ALL, targets, gtk.gdk.ACTION_MOVE)
        self.Buffer = gtk.gdk.Pixmap(self.picDrawingArea.window, 1000, 1000)
        self.DrawingArea = CDrawingArea(self.picDrawingArea, self.Buffer)
        
        self.AdjustScrollBars()
        self.Paint()
        
        
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
        
    def GetRelativePos(self, posx, posy):
        return int(-self.picHBar.get_value() + posx), int(-self.picVBar.get_value() + posy)
        
    def Paint(self):
        self.DrawingArea.Paint()
        self.Repaint()
        
    def Repaint(self):
        posx, posy = int(self.picHBar.get_value()), int(self.picVBar.get_value())
        sizx, sizy = self.GetWindowSize()
        wgt = self.picDrawingArea.window
        gc = wgt.new_gc()
        wgt.draw_drawable(gc, self.Buffer, posx, posy, 0, 0, sizx, sizy)
        if self.dnd:
            self.__DrawDragRect(0,0, True, False)
        
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
        toolBtnSel =  self.emit('get_selected')
        posx, posy = self.GetAbsolutePos(event.x, event.y)
        if toolBtnSel is None:
            itemSel = self.DrawingArea.GetElementAtPosition(posx, posy)
            if itemSel is not None:
                if itemSel in self.DrawingArea.GetSelected():
                    if (event.state & gtk.gdk.CONTROL_MASK):
                        self.DrawingArea.RemoveFromSelection(itemSel)
                        self.Paint()
                    elif event.button == 1:
                        self.__DragBegin(event)
                    else:
                        self.Paint()
                elif not (event.state & gtk.gdk.CONTROL_MASK):
                    self.DrawingArea.DeselectAll()
                    self.DrawingArea.AddToSelection(itemSel)
                    self.emit('selected_item', itemSel)
                    if event.button == 1:
                        self.__DragBegin(event)
                    self.Paint()
                else:
                    self.DrawingArea.AddToSelection(itemSel)
                    self.emit('selected_item', None)
                    self.Paint()
            elif self.DrawingArea.SelectedCount() > 0:
                if not (event.state & gtk.gdk.CONTROL_MASK):
                    self.DrawingArea.DeselectAll()
                    self.emit('selected_item', None)
                    self.Paint()
        
        elif toolBtnSel[0] == 'Element':
            ElementType = self.application.ElementFactory.GetElement(toolBtnSel[1])
            ElementObject = CElementObject(ElementType)
            CElement(self.DrawingArea, ElementObject).SetPosition(posx, posy)
            self.emit('set_selected', None)
            self.Paint()
            
        elif toolBtnSel[0] == 'Connection':
            pass
            #ConnectionType = self.application.ConnectionFactory.GetConnection(self.tbToolBox.toolBtnSel[0])
            #ConnectionObject = CConnectionObject(ConnectionType)
            #CConnection(self.DrawingArea, ConnectionObject).SetPosition(posx, posy)
        
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
           
    def on_picEventBox_drag_motion(self, widget, context, x, y, time):
        self.__DrawDragRect(x,y)
    
    def on_picEventBox_drag_drop(self, widget, context, x, y, time):
        dx, dy = self.__GetDelta(x, y)
        self.DrawingArea.MoveSelection(dx, dy)
        
    def on_picEventBox_drag_end(self, widget, context):
        self.dnd = False
        self.Paint()
        
    def __Scroll(self, scrollbar, direction):
        tmp = scrollbar.get_adjustment()
        if direction == gtk.gdk.SCROLL_UP:
            tmp.value = max(tmp.lower, tmp.value - 20)
        elif direction == gtk.gdk.SCROLL_DOWN:
            tmp.value = min(tmp.upper - tmp.page_size, tmp.value + 20)
        scrollbar.set_adjustment(tmp)
        
    def __DragBegin(self, event):
        self.picEventBox.drag_begin(targets, gtk.gdk.ACTION_MOVE, event.button, event)
        self.DragStartPos = self.GetAbsolutePos(event.x, event.y)
        self.DragRect = self.DrawingArea.GetSelectSquare()
        cmap = self.picDrawingArea.window.get_colormap()
        self.DragGC = self.picDrawingArea.window.new_gc(foreground = cmap.alloc_color(SELECT_SQUARE_COLOR), 
            function = gtk.gdk.XOR, line_width = SELECT_SQUARE_SIZE)
        self.__DrawDragRect(event.x, event.y, False)
        self.dnd = True
        
    def  __GetDelta(self, x, y):
        sizx, sizy = self.GetDrawingAreaSize()
        selx, sely = self.DragRect[1]
        sizx, sizy = sizx - selx, sizy - sely
        tmpx, tmpy = self.GetAbsolutePos(x,y)
        dx, dy = tmpx - self.DragStartPos[0], tmpy - self.DragStartPos[1]
        posx, posy = self.DragRect[0]
        tmpx, tmpy = posx + dx, posy + dy
        tmpx = min(max(0, tmpx), sizx)
        tmpy = min(max(0, tmpy), sizy)
        return tmpx - posx, tmpy - posy
        
    
    def __DrawDragRect(self, x, y, erase = True, draw = True):
        if erase:
            self.picDrawingArea.window.draw_rectangle(self.DragGC, False, self.__oldx, self.__oldy, *self.DragRect[1])
        if draw:
            tmpx, tmpy = self.GetRelativePos(*self.DragRect[0])
            dx, dy = self.__GetDelta(x, y)
            self.picDrawingArea.window.draw_rectangle(self.DragGC, False, int(tmpx + dx), int(tmpy + dy), *self.DragRect[1])
            self.__oldx, self.__oldy = int(tmpx + dx), int(tmpy + dy)
