import common
import gtk

class CfrmProperties(common.CWindow):
    widgets = ('nbProProperties',)
    name = 'frmProperties'
    
    def ShowProperties(self, what, element):
        self.__element = element.GetObject()
        self.__attributes = []
        self.__attributes = self.__element.GetAttribute("attrs")
        self.__operations = []
        self.__operations = self.__element.GetAttribute("opers")
        if what == 'attrs':
            self.nbProProperties.set_current_page(0)
        elif what == 'opers':
            self.nbProProperties.set_current_page(1)
        response = self.form.run()
        while response == gtk.RESPONSE_APPLY:
            response = self.form.run()
            self.__Save()
        if response == gtk.RESPONSE_OK:
            self.__Save()
        self.Hide()
        
    def __Save(self):
        self.__element.SetAttribute("attrs", self.__attributes)
        self.__element.SetAttribute("opers", self.__operations)
        
    def on_cmdNewAttribute_clicked(self, widget):
        attr = {}
        if self.application.GetWindow('frmAttribute').ShowFrmAttribute(attr):
            self.__attributes.append(attr)
        
    def on_cmdNewOperation_clicked(self, widget):
        oper = {}
        if self.application.GetWindow('frmOperation').ShowFrmOperation(oper):
            self.__operations.append(oper)
