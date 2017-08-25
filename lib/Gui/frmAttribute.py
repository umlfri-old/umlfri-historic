import common
import gtk

class CfrmAttribute(common.CWindow):
    name = 'frmAttribute'
    widgets = ('edAtrName', 'cboxAtrType', 'cboxAtrScope', 'cboxAtrStereotype',
               'cboxAtrContainment', 'edAtrInitial', 'txtAtrDocumentation',
               'cbAtrDerived', 'cbAtrStatic', 'cbAtrProperty', 'cbAtrConst')
    
    def ShowFrmAttribute(self, attribute = {}):
        if 'name' in attribute:
            self.edAtrName.set_text(attribute['name'])
        else:
            self.edAtrName.set_text("")
        if 'type' in attribute:
            self.cboxAtrType.child.set_text(attribute['type'])
        else:
            self.cboxAtrType.child.set_text("")
        if 'scope' in attribute:
            self.cboxAtrScope.set_active({'public':0, 'private':1, 'protected':2}[attribute['scope']])
        else:
            self.cboxAtrScope.set_active(0)
        if 'stereotype' in attribute:
            self.cboxAtrStereotype.child.set_text(attribute['stereotype'])
        else:
            self.cboxAtrStereotype.child.set_text("")
        if 'containment' in attribute:
            self.cboxAtrContainment.child.set_text(attribute['containment'])
        else:
            self.cboxAtrContainment.child.set_text("")
        if 'initial' in attribute:
            self.edAtrInitial.set_text(attribute['initial'])
        else:
            self.edAtrInitial.set_text("")
        if 'doc' in attribute:
            self.txtAtrDocumentation.get_buffer().set_text(attribute['doc'])
        else:
            self.txtAtrDocumentation.get_buffer().set_text("")
        if 'derived' in attribute:
            self.cbAtrDerived.set_active(attribute['derived'])
        else:
            self.cbAtrDerived.set_active(False)
        if 'static' in attribute:
            self.cbAtrStatic.set_active(attribute['static'])
        else:
            self.cbAtrStatic.set_active(False)
        if 'property' in attribute:
            self.cbAtrProperty.set_active(attribute['property'])
        else:
            self.cbAtrProperty.set_active(False)
        if 'const' in attribute:
            self.cbAtrConst.set_active(attribute['const'])
        else:
            self.cbAtrConst.set_active(False)
        
        res = False
        if self.form.run() == gtk.RESPONSE_OK:
            attribute['name'] = self.edAtrName.get_text()
            attribute['type'] = self.cboxAtrType.get_text_column()
            attribute['scope'] = ['public', 'private', 'protected'][self.cboxAtrScope.get_active()]
            attribute['stereotype'] = self.cboxAtrStereotype.get_text_column()
            attribute['containment'] = self.cboxAtrContainment.get_text_column()
            attribute['initial'] = self.edAtrInitial.get_text()
            buf = self.txtAtrDocumentation.get_buffer()
            attribute['doc'] = buf.get_text(buf.get_start_iter(), buf.get_end_iter())
            attribute['derived'] = self.cbAtrDerived.get_active()
            attribute['static'] = self.cbAtrStatic.get_active()
            attribute['property'] = self.cbAtrProperty.get_active()
            attribute['const'] = self.cbAtrStatic.get_active()
            res = True
        self.Hide()
        return res
