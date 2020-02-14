import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'myverysecretkey'
    WTF_CSRF_ENABLED = False # not needed for the time being
