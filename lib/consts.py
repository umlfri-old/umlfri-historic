from os.path import join, dirname, abspath

FONT_TYPE = 'Arial 14' 
ROOT_PATH = abspath(join(dirname(__file__), '..'))
ETC_PATH = join(ROOT_PATH, 'etc')
DEFINITIONS_PATH = join(ETC_PATH, 'definitions')
DIAGRAMS_PATH = join(DEFINITIONS_PATH, 'diagrams')
ELEMENTS_PATH = join(DEFINITIONS_PATH, 'elements')
CONNECTIONS_PATH = join(DEFINITIONS_PATH, 'connections')

ICONS_PATH = join(ROOT_PATH, 'icons')
ARROW_IMAGE = join(ICONS_PATH, 'arrow.png')
ELEMENT_IMAGE = join(ICONS_PATH, 'element.png')
VIEW_IMAGE = join(ICONS_PATH, 'view.png')
FOLDER_IMAGE = join(ICONS_PATH, 'folder.png')