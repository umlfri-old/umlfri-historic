import gtk, gobject

from lib.Glade import CWidget
from lib.Drawing import CDrawingArea, CElement, CConnection

class CpicDrawingArea(CWidget):
    widgets = ('picDrawingArea', 'picEventBox', 'picVBar', 'picHBar')
    
    __gsignals__ = {
        'get_selected':  (gobject.SIGNAL_RUN_LAST, gobject.TYPE_OBJECT, 
            ())
    }
    
    def Init(self):
        self.Buffer = gtk.gdk.Pixmap(self.picDrawingArea.window, 100, 100)
        gc = self.picDrawingArea.get_style().white_gc # self.Buffer.new_gc(foreground = cmap.alloc_color("white"))
        self.Buffer.draw_rectangle(gc, True, 0, 0, 100, 100)
        self.DrawingArea = CDrawingArea(self.picDrawingArea, self.Buffer)
        self.picEventBox.connect('button_press_event', self.on_picEventBox_button_press_event)
        
    def GetDrawingArea(self):
        return self.picDrawingArea
        
    def GetSize(self):
        return self.picDrawingArea.get_size_request()
        
    def SetSelected(self, selected):
        self.Selected = selected
        
    def on_picEventBox_button_press_event(self, widget, event):
        print self.emit('get_selected')
        
    def on_picVBar_value_changed(self, widget):
        pass
        
    def on_picHBar_value_changed(self, widget):
        print range
        
        
