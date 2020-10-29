import os
class Configuration(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATABASE = '/tmp/flsite.db'
    MAX_CONTENT_LENGTH = 1024 * 1024
