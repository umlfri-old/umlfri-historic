import xml.dom.minidom
import os
import os.path
from lib.lib import UMLException
from Type import CConnectionType
from Line import CConnectionLine
from Arrow import CConnectionArrow
from gtk.gdk import pixbuf_new_from_file

from lib.Drawing.Objects import ALL

class CConnectionFactory:
    def __init__(self, path):
        self.types = {}
        self.path = path
        for file in os.listdir(self.path):
            self.__Load(os.path.join(self.path, file))

    def GetConnection(self, type):
        return self.types[type]

    def __Load(self, file_path):
        dom = xml.dom.minidom.parse(file_path)
        root = dom.documentElement
        if root.tagName != 'ConnectionType':
            raise UMLException("XMLError")
        if not root.hasAttribute('id'):
            raise UMLException("XMLError")
        id = root.getAttribute('id')
        sarr = {}
        darr = {}
        ls = {}
        icon = None
        for i in root.childNodes:
            if i.nodeType not in (xml.dom.minidom.Node.ELEMENT_NODE, xml.dom.minidom.Node.DOCUMENT_NODE):
                continue
            en = i.tagName
            if en == 'Icon':
                if not i.hasAttribute('path'):
                    raise UMLException("XMLError")
                icon = pixbuf_new_from_file(i.getAttribute('path'))
            elif en == 'SrcArrow':
                if i.hasAttribute('possible'):
                    sarr['possible'] = i.getAttribute('possible')
                if i.hasAttribute('default'):
                    sarr['default'] = i.getAttribute('default')
            elif en == 'DestArrow':
                if i.hasAttribute('possible'):
                    darr['possible'] = i.getAttribute('possible')
                if i.hasAttribute('default'):
                    darr['default'] = i.getAttribute('default')
            elif en == 'Appearance':
                for j in i.childNodes:
                    if j.nodeType not in (xml.dom.minidom.Node.ELEMENT_NODE, xml.dom.minidom.Node.DOCUMENT_NODE):
                        continue
                    en = j.tagName
                    if en == 'LineStyle':
                        if j.hasAttribute('color'):
                            ls['color'] = j.getAttribute('color')
                        if j.hasAttribute('style'):
                            ls['style'] = j.getAttribute('style')
                        if j.hasAttribute('width'):
                            ls['width'] = j.getAttribute('width')
                    elif en == 'ArrowStyle':
                        if j.hasAttribute('fill'):
                            darr['fill'] = sarr['fill'] = j.getAttribute('fill')
                        if j.hasAttribute('color'):
                            darr['color'] = sarr['color'] = j.getAttribute('color')
                        if j.hasAttribute('style'):
                            darr['style'] = sarr['style'] = j.getAttribute('style')
                        if j.hasAttribute('size'):
                            darr['size'] = sarr['size'] = j.getAttribute('size')
        self.types[id] = CConnectionType(id, CConnectionLine(**ls),
                                    CConnectionArrow(**sarr), CConnectionArrow(**darr), icon)
