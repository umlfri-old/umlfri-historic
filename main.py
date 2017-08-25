#!/usr/bin/python

import pygtk

pygtk.require('2.0')

import lib.Glade
import os.path

from lib.Gui import CfrmMain, CfrmAbout
from lib.Diagrams import CDiagramFactory
from lib.Elements import CElementFactory
from lib.Connections import CConnectionFactory

from lib.consts import DIAGRAMS_PATH, ELEMENTS_PATH, CONNECTIONS_PATH

class Application(lib.Glade.CApplication):
    windows = (CfrmMain, CfrmAbout)
    glade = os.path.join(os.path.dirname(__file__), 'gui/gui.glade')
    main_window = 'frmMain'
    
    def __init__(self):
        self.DiagramFactory = CDiagramFactory(DIAGRAMS_PATH)
        self.ElementFactory = CElementFactory(ELEMENTS_PATH)
        self.ConnectionFactory = CConnectionFactory(CONNECTIONS_PATH)
        lib.Glade.CApplication.__init__(self)
        self.Project = None

Application().Main()
