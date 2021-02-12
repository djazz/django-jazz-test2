"""Configuration for ASGI servers.

It exposes the ASGI callable as a module-level variable named `application`
that can be used by any ASGI server.

**Doc:** Django 3.1:
  [How to deploy with ASGI](https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/)

**Learn:** ASGI is a spiritual successor to WSGI for asynchronous applications.
"""
from django.core.asgi import get_asgi_application

from config.bootstrap import bootstrap


# Bootstrap the application.
bootstrap()

# Create the ASGI callable.
application = get_asgi_application()
