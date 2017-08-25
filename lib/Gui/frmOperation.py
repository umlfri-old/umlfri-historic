import common
import gtk

class CfrmOperation(common.CWindow):
    name = 'frmOperation'
    widgets = ('edOprName', 'edOprParameters', 'cboxOprReturnType', 'cboxOprScope', 
              'cboxOprStereotype', 'txtOprDocumentation', 'cmdOprOK', 'cmdOprCancel',
              'cbOprAbstract', 'cbOprStatic', 'cbOprConst', 'cbOprReturnArray', 'cbOprPure',
              'cbOprSynchronize', 'cbOprIsQuery')
    
    def ShowFrmOperation(self, operation = {}):
        if 'name' in operation:
            self.edOprName.set_text(operation['name'])
        else:
            self.edOprName.set_text("")

        if 'parameters' in operation:
            self.edOprParameters.set_text(operation['parameters'])
        else:
            self.edOprParameters.set_text("")
        
        if 'abstract' in operation:
            self.cbOprAbstract.set_active(operation['abstract'])
        else:
            self.cbOprAbstract.set_active(0)
        
        if 'static' in operation:
            self.cbOprStatic.set_active(operation['static'])
        else:
            self.cbOprStatic.set_active(0)
        
        if 'const' in operation:
            self.cbOprConst.set_active(operation['const'])
        else:
            self.cbOprConst.set_active(0)
            
        if 'returnarray' in operation:
            self.cbOprReturnArray.set_active(operation['returnarray'])
        else:
            self.cbOprReturnArray.set_active(0)
        
        if 'pure' in operation:
            self.cbOprPure.set_active(operation['pure'])
        else:
            self.cbOprPure.set_active(0)
        
        if 'synchronize' in operation:
            self.cbOprSynchronize.set_active(operation['synchronize'])
        else:
            self.cbOprSynchronize.set_active(0)
        
        if 'isquery' in operation:
            self.cbOprIsQuery.set_active(operation['isquery'])
        else:
            self.cbOprIsQuery.set_active(0)
            
        if 'returntype' in operation:
            self.cboxOprReturnType.set_text_column(operation['returntype'])
        else:
            self.cboxOprReturnType.set_text_column("")
        
        if 'scope' in operation:
            self.cboxOprScope.set_active({'public':0, 'private':1, 'protected':2}[operation['scope']])
        else:
            self.cboxOprScope.set_active(0)
        
        if 'stereotype' in operation:
            self.cboxOprStereotype.set_text_column(operation['stereotype'])
        else:
            self.cboxOprStereotype.set_text_column("")
    
        if 'documentation' in operation:
            self.txtOprDocumentation.get_buffer().set_text(operation['documentation'])
        else:
            self.txtOprDocumentation.get_buffer().set_text("")
          
        if self.form.run() == gtk.RESPONSE_OK:
            operation['name'] = self.edOprName.get_text()
            operation['parameters'] = self.edOprParameters.get_text()
            operation['abstract'] = self.cbOprAbstract.get_active()
            operation['static'] = self.cbOprStatic.get_active()
            operation['const'] = self.cbOprConst.get_active()
            operation['returnarray'] = self.cbOprReturnArray.get_active()
            operation['pure'] = self.cbOprPure.get_active()
            operation['synchronize'] = self.cbOprSynchronize.get_active()
            operation['isquery'] = self.cbOprIsQuery.get_active()
            operation['scope'] = ['public', 'private', 'protected'][self.cboxOprScope.get_active()]
            operation['returntype'] = self.cboxOprReturnType.get_text_column()
            operation['stereotype'] = self.cboxOprStereotype.get_text_column()
            buf = self.txtOprDocumentation.get_buffer()
            operation['documentation'] = buf.get_text(buf.get_start_iter(), buf.get_end_iter())
        self.Hide()      
        