import django_on_heroku
from decouple import config

from dentist_website.settings.dev import ALLOWED_HOSTS, SECRET_KEY


from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    ''
]

