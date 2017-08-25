#!/usr/bin/python

import gtk
import lib.Elements
import lib.Drawing

elfs = lib.Elements.CElementFactory('etc/definitions/elements')
cofs = lib.Connections.CConnectionFactory('etc/definitions/connections')

tmp = gtk.DrawingArea()

eb = gtk.EventBox()
eb.add(tmp)

win = gtk.Window()
win.add(eb)

eb.show()
win.show()
tmp.show()

draare = lib.Drawing.CDrawingArea(tmp)

###############
## Create Class
cls = elfs.GetElement("Class")
element = lib.Elements.CElementObject(cls)
element.SetAttribute("Name", "hihiaaaaaaaa")
element.SetAttribute("Attributes", [{'type':'+', 'line': "123"}, {'type':'-', 'line': "456"}])
element.SetAttribute("Operations", [])
element.SetAttribute("Abstract", False)
element.SetAttribute("Scope", "public")

clas = lib.Drawing.CElement(draare, element)
clas.SetPosition(100, 100)

###############
## Create Package
cls = elfs.GetElement("Package")
element = lib.Elements.CElementObject(cls)
element.SetAttribute("Name", "hihiaaaaaaaa")

pack = lib.Drawing.CElement(draare, element)
pack.SetPosition(200, 200)

#############
## Create associatoin
ass = cofs.GetConnection("Association")
conObj = lib.Connections.CConnectionObject(ass)
conObj.SetAttribute('Name', 'conn')
conect = lib.Drawing.CConnection(draare,conObj,[(120,165),(25,25),(60,60),(60,80)])

def clicked(widget, event):
    #print conect.AreYouAtPosition(event.x, event.y)
    print draare.GetElementAtPosition(event.x, event.y)


def button_press_event(*args):
    draare.Paint()

def destroy(*args):
    gtk.main_quit()

eb.connect('button_press_event', clicked)
#win.connect('key_press_event', button_press_event)

tmp.connect('configure_event', button_press_event)
tmp.connect('expose_event', button_press_event)

win.connect('destroy', destroy)

gtk.main()
