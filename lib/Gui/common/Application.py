import gtk.glade
import gtk

class CApplication:
    windows = ()
    glade = ''
    wins = {}
    main_window = ''
    
    def __init__(self):
        self.wTree = gtk.glade.XML(self.glade)
        for i in self.windows:
            tmp = self.wins[i.name] = i(self)
            for widgetName in tmp.widgets:
                setattr(tmp, widgetName, self.wTree.get_widget(widgetName))
            for widgetName, widgetClass in tmp.complexWidgets.iteritems():
                wgt = widgetClass(self)
                setattr(tmp, widgetName, wgt)
                for widgetName in wgt.widgets:
                    setattr(wgt, widgetName, self.wTree.get_widget(widgetName))
                self.wTree.signal_autoconnect(wgt)
                wgt.Init2()
                wgt.Init()
            tmp.form = self.wTree.get_widget(i.name)
            self.wTree.signal_autoconnect(tmp)
            tmp.Init2()
            tmp.Init()
    
    def GetWindow(self, name):
        return self.wins[name]
    
    def Main(self):
        self.GetWindow(self.main_window).Show()
        gtk.main()
    
    def Quit(self):
        gtk.main_quit()
