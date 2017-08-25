#!/usr/bin/python

import gtk
import lib.Connections
import lib.Drawing

fuckstory = lib.Connections.CConnectionFactory('etc/definitions/connections')


tmp = gtk.DrawingArea()

eb = gtk.EventBox()
eb.add(tmp)

win = gtk.Window()
win.add(eb)

eb.show()
tmp.show()
win.show()

draare = lib.Drawing.CDrawingArea(tmp)

ass = fuckstory.GetConnection("Association")
conObj = lib.Connections.CConnectionObject(ass)
conect = lib.Drawing.CConnection(draare,conObj,[(60,60),(60,90),(25,25),(110,100)])



def clicked(widget, event):
    print conect.AreYouAtPosition(event.x, event.y)


def button_press_event(*args):
    conect.Paint()

def destroy(*args):
    gtk.main_quit()


eb.connect('button_press_event', clicked)
win.connect('key_press_event', button_press_event)
win.connect('destroy', destroy)
gtk.main()
