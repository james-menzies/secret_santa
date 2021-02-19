from .settings import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATIC_ROOT = '/var/www/secret_santa/static/'

MEDIA_URL='/media/'
MEDIA_ROOT='/var/www/secret_santa/media/'
