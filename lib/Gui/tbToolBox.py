from lib.Glade import CWidget

import gtk
from gtk.gdk import pixbuf_new_from_file

from lib.consts import ARROW_IMAGE

class CtbToolBox(CWidget):
    widgets = ('tbToolBox', )
    
    def Init(self):
        self.DiagramType = None
        pixbuf = pixbuf_new_from_file(ARROW_IMAGE)
        newIconWidget = gtk.Image()
        newIconWidget.set_from_pixbuf(pixbuf)
        newIconWidget.show()
        arrowBtn = self.tbToolBox.get_nth_item(0)
        arrowBtn.set_icon_widget(newIconWidget)
        
    def __InsertButton(self, Type, TypeDesc, Group):
        newIconWidget = gtk.Image()
        newIconWidget.set_from_pixbuf(Type.GetIcon())
        newIconWidget.show()
        newButton = gtk.RadioToolButton(Group, None)
        #newButton.set_label(Type.GetId())
        newButton.set_icon_widget(newIconWidget)
        newButton.connect("toggled", self.on_tbButton_toggled, Type.GetId(), TypeDesc)
        newButton.show()
        self.tbToolBox.insert(newButton, -1)
        
    def __InsertSeparator(self):
        newSeparator = gtk.SeparatorToolItem()
        newSeparator.show()
        self.tbToolBox.insert(newSeparator, -1)
                
    def SetButtons(self, DiagramId):
        print DiagramId
        self.DiagramType = self.application.DiagramFactory.GetDiagram(DiagramId)
        if self.DiagramType is None:
            raise Exception('tbToolBox.DiagramType is None')
        ArrowButton = self.tbToolBox.get_nth_item(0)
        for button in self.tbToolBox.get_children():
            self.tbToolBox.remove(button)
            
        self.tbToolBox.insert(ArrowButton, -1)
        
        ElementNameList = self.DiagramType.GetElements()
        if len(ElementNameList) > 0:
            self.__InsertSeparator()
            for ElementName in ElementNameList:
                ElementType = self.application.ElementFactory.GetElement(ElementName)
                self.__InsertButton(ElementType, 'Element', ArrowButton)
            
        ConnectionNameList = self.DiagramType.GetConnections()
        if len(ConnectionNameList) > 0:
            self.__InsertSeparator()
            for ConnectionName in ConnectionNameList:
                ConnectionType = self.application.ConnectionFactory.GetConnection(ConnectionName)
                self.__InsertButton(ConnectionType, 'Connection', ArrowButton)
            
        
    def on_tbButton_toggled(self, widget, ItemId, ItemDesc):
        pass
        