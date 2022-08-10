"""
WSGI config for app_blog2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_blog2.settings.local')

application = get_wsgi_application()

from dj_static import Cling

application = Cling(get_wsgi_application())