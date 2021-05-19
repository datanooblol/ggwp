import ggwp, os
import configparser

current = os.sep.join(ggwp.__file__.split(os.sep)[:-1])
config_path  = '{0}/config/config.cfg'.format(current)
parser = configparser.ConfigParser()
parser.read(config_path)
__version__ = parser['default']['version']


class EzConfig:

    def __init__(self):
        self.__version__ = __version__