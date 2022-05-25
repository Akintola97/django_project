import django_on_heroku
from decouple import config

from dentist_website.settings.dev import ALLOWED_HOSTS, SECRET_KEY


from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'boltdental-website.herokuapp.com'
]

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version':1,
    'disable_existing_loggers': False,
    'formatters':{
    
    'verbose':{
        'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
        'datefmt': "%d/%b/%Y %H:%M:%S"
    },
    'simple': {
        'format':'%(levelname)s %(messages)s'
        },
    },
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'loggin.StreamHandler',
        },
    },
    'loggers':{
        'MYAPP':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    }
}


#heroku settings 
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']