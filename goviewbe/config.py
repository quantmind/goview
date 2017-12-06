import os
import json


PATH = os.path.dirname(os.path.dirname(__file__))

with open('package.json', 'r') as fp:
    VERSION = json.load(fp)['version']


class Config(object):
    """Base config object for pave services
    """
    SWITCH = None  # Command line arg to use this config
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(PATH, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
