from .settings import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
import os

# Local containerized db.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB"),
        'USER': 'postgres',
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        'PORT': 5432,
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATIC_ROOT = '/var/www/secret_santa/static/'

MEDIA_URL='/media/'
MEDIA_ROOT='/var/www/secret_santa/media/'
