"""
WSGI config for textclassifier project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from utils import  text_process
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "textclassifier.settings")

application = get_wsgi_application()
