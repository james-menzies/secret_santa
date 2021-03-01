"""
WSGI config for secret_santa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

env = os.environ.get("DJANGO_ENV")

if env == "staging":
    settings_file = "settings_staging"
elif env == "production":
    settings_file = "settings"
else:
    settings_file = "settings_dev"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'secret_santa.{settings_file}')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secret_santa.settings_staging')

application = get_wsgi_application()
