"""Configuration for WSGI servers.

It exposes the WSGI callable as a module-level variable named `application`
that can be used by any WSGI server.
Django‘s development server uses this if `WSGI_APPLICATION` refers to this.

**Doc:** Django 3.1:
  [How to deploy with WSGI](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/)

**Learn:** The Web Server Gateway Interface (WSGI, pronounced _whiskey_ or _WIZ-ghee_) is a simple
  calling convention for web servers to forward requests to web applications written in Python.
"""
from django.core.wsgi import get_wsgi_application

from config.bootstrap import bootstrap


# Bootstrap the application.
bootstrap()

# Create the WSGI callable.
application = get_wsgi_application()
