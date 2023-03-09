import os

from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

# database settings are read from .env file. If no .env file is present, django
# default value (sqlite3 database) are used.
DATABASES = {
    'default': {
        'ENGINE': os.environ.setdefault(
            'SQL_ENGINE',
            'django.db.backends.sqlite3'
        ),
        'NAME': os.environ.setdefault(
            'SQL_DATABASE',
            f'{BASE_DIR}/db.sqlite3'
        ),
        'USER': os.environ.setdefault(
            'SQL_USER',
            ''
        ),
        'PASSWORD': os.environ.setdefault(
            'SQL_PASSWORD',
            ''
        ),
        'HOST': os.environ.setdefault(
            'SQL_HOST',
            ''
        ),
        'PORT': os.environ.setdefault(
            'SQL_PORT',
            ''
        )
    }
}
