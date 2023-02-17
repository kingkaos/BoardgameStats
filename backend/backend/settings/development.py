import os

from decouple import config

from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

# database settings are read from .env file. If no .env file is present, django
# default value (sqlite3 database) are used.
DATABASES = {
    'default': {
        'ENGINE': config(
            'SQL_ENGINE', 
            'django.db.backends.sqlite3'
        ),
        'NAME': config(
            'SQL_DATABASE',
            BASE_DIR / 'db.sqlite3'
        ),
        'USER': config(
            'SQL_USER',
            ''
        ),
        'PASSWORD': config(
            'SQL_PASSWORD',
            ''
        ),
        'HOST': config(
            'SQL_HOST',
            ''
        ),
        'PORT': config(
            'SQL_PORT',
            ''
        )
    }
}
