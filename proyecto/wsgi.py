"""
WSGI config for proyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto.settings")

application = get_wsgi_application()

import sys

from site import addsitedir

#ruta de el virtualenv

addsitedir('/src/www/html/virtual/virtual2/lib/python3.5/site-packages')

#ruta de mi aplicacion Django

sys.path = ['/var/www/html/proyecto'] + sys.path