import os
from configobj import ConfigObj

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

config = ConfigObj(
    os.path.join(os.path.dirname(BASE_DIR), 'settings.conf')
)
