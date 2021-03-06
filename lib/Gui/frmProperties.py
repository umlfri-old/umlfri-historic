import common
import gtk

import gobject

class CfrmProperties(common.CWindow):
    widgets = ('nbProProperties', 'twAttributes', 'twOperations', 'cmdDeleteAttribute', 'cmdDeleteOperation')
    name = 'frmProperties'
    
    def Init(self):
        self.attrModel = gtk.ListStore(gobject.TYPE_STRING, gobject.TYPE_STRING, gobject.TYPE_STRING)
        self.operModel = gtk.ListStore(gobject.TYPE_STRING, gobject.TYPE_STRING, gobject.TYPE_STRING, gobject.TYPE_STRING)
        
        self.twAttributes.append_column(gtk.TreeViewColumn("Scope", gtk.CellRendererText(), text = 0))
        self.twAttributes.append_column(gtk.TreeViewColumn("Name", gtk.CellRendererText(), text = 1))
        self.twAttributes.append_column(gtk.TreeViewColumn("Type", gtk.CellRendererText(), text = 2))
        
        self.twOperations.append_column(gtk.TreeViewColumn("Scope", gtk.CellRendererText(), text = 0))
        self.twOperations.append_column(gtk.TreeViewColumn("Type", gtk.CellRendererText(), text = 1))
        self.twOperations.append_column(gtk.TreeViewColumn("Name", gtk.CellRendererText(), text = 2))
        self.twOperations.append_column(gtk.TreeViewColumn("Parameters", gtk.CellRendererText(), text = 3))
        
        self.twAttributes.set_model(self.attrModel)
        self.twOperations.set_model(self.operModel)
    
    def ShowProperties(self, what, element):
        self.__element = element.GetObject()
        self.__saved = False
        if what == 'attrs':
            self.nbProProperties.set_current_page(0)
        elif what == 'opers':
            self.nbProProperties.set_current_page(1)
        if self.__element.HasAttribute('Attributes'):
            self.nbProProperties.get_nth_page(0).show()
            self.__attributes = self.__element.GetAttribute("Attributes")[:]
            self.attrModel.clear()
            for attr in self.__attributes:
                iter = self.attrModel.append()
                self.__SetAttrLine(iter, attr)
        else:
            self.nbProProperties.get_nth_page(0).hide()
            self.__attributes = None
        if self.__element.HasAttribute('Operations'):
            self.nbProProperties.get_nth_page(1).show()
            self.__operations = self.__element.GetAttribute("Operations")[:]
            self.operModel.clear()
            for oper in self.__operations:
                iter = self.operModel.append()
                self.__SetOperLine(iter, oper)
        else:
            self.nbProProperties.get_nth_page(1).hide()
            self.__operations = None
        self.cmdDeleteAttribute.set_sensitive(False)
        self.cmdDeleteOperation.set_sensitive(False)
        response = self.form.run()
        while response == gtk.RESPONSE_APPLY:
            response = self.form.run()
            self.__Save()
        if response == gtk.RESPONSE_OK:
            self.__Save()
        self.Hide()
        
        return self.__saved
    
    def __Save(self):
        if self.__attributes is not None:
            self.__element.SetAttribute("Attributes", self.__attributes)
        if self.__operations is not None:
            self.__element.SetAttribute("Operations", self.__operations)
        self.__saved = True
    
    def __SetAttrLine(self, iter, attr):
        self.attrModel.set(iter, 0, attr['scope'], 1, attr['name'], 2, attr['type'])
    
    def __SetOperLine(self, iter, oper):
        self.operModel.set(iter, 0, oper['scope'], 1, oper['type'], 2, oper['name'], 3, oper['params'])
        
    def on_cmdNewAttribute_clicked(self, widget):
        attr = {}
        tmp = self.application.GetWindow('frmAttribute')
        tmp.SetParent(self)
        if tmp.ShowFrmAttribute(attr):
            self.__attributes.append(attr)
            iter = self.attrModel.append()
            self.__SetAttrLine(iter, attr)
        
    def on_cmdNewOperation_clicked(self, widget):
        oper = {}
        tmp = self.application.GetWindow('frmOperation')
        tmp.SetParent(self)
        if tmp.ShowFrmOperation(oper):
            self.__operations.append(oper)
            iter = self.operModel.append()
            self.__SetOperLine(iter, oper)
    
    def on_cmdDeleteOperation_clicked(self, widget):
        sel = self.twOperations.get_selection()
        model, iter = sel.get_selected()
        del self.__operations[model.get_path(iter)[0]]
        model.remove(iter)
        self.cmdDeleteOperation.set_sensitive(False)
    
    def on_cmdDeleteAttribute_clicked(self, widget):
        sel = self.twAttributes.get_selection()
        model, iter = sel.get_selected()
        del self.__attributes[model.get_path(iter)[0]]
        model.remove(iter)
        self.cmdDeleteAttribute.set_sensitive(False)
    
    def on_twAttributes_cursor_changed(self, widget):
        self.cmdDeleteAttribute.set_sensitive(True)
    
    def on_twOperations_cursor_changed(self, widget):
        self.cmdDeleteOperation.set_sensitive(True)
    
    def on_twAttributes_row_activated(self, widget, path, column):
        attr = self.__attributes[path[0]]
        if self.application.GetWindow('frmAttribute').ShowFrmAttribute(attr):
            iter = self.attrModel.get_iter(path)
            self.__SetAttrLine(iter, attr)
    
    def on_twOperations_row_activated(self, widget, path, column):
        oper = self.__operations[path[0]]
        if self.application.GetWindow('frmOperation').ShowFrmOperation(oper):
            iter = self.operModel.get_iter(path)
            self.__SetOperLine(iter, oper)
