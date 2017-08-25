FONT_TYPE = '-*-*-*-*-*-*-*-*-*-*-*-*-*-*' 

from os.path import join, dirname, abspath

ROOT_PATH = abspath(join(dirname(__file__), '..'))
ETC_PATH = join(ROOT_PATH, 'etc')
DEFINITIONS_PATH = join(ETC_PATH, 'definitions')
DIAGRAMS_PATH = join(DEFINITIONS_PATH, 'diagrams')
ELEMENTS_PATH = join(DEFINITIONS_PATH, 'elements')
CONNECTIONS_PATH = join(DEFINITIONS_PATH, 'connections')

ICONS_PATH = join(ROOT_PATH, 'icons')
ARROW_IMAGE = join(ICONS_PATH, 'arrow.png')