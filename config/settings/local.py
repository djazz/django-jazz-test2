"""Application settings for the `local` application mode."""

# Import base settings.
from .base import *  # noqa


# CACHE ============================================================================================
# Doc: https://docs.djangoproject.com/en/3.1/topics/cache/

# Disable caching.
CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}


# LOGGING ==========================================================================================
# Doc: https://docs.djangoproject.com/en/3.1/topics/logging/

# Remove file logging.
for key in LOGGING["loggers"]:  # noqa
    if "file" in LOGGING["loggers"][key]["handlers"]:  # noqa
        LOGGING["loggers"][key]["handlers"].remove("file")  # noqa
del LOGGING["handlers"]["file"]  # noqa


# SECURITY =========================================================================================

# Allow remote access to the local machine.
from socket import gethostname, gethostbyname
hostname = gethostname()
ALLOWED_HOSTS += [hostname, f"{hostname}.local", gethostbyname(hostname)]  # noqa
del hostname


# SESSION ==========================================================================================
# Doc: https://docs.djangoproject.com/en/3.1/topics/http/sessions/

# The age of session cookies, in seconds.
SESSION_COOKIE_AGE = 2592000  # 30 days


# TEMPLATES ========================================================================================
# Doc: https://docs.djangoproject.com/en/3.1/topics/templates/

# Output to use in template system for invalid (e.g. misspelled) variables.
# Remark: Should only be enabled in order to debug a specific template problem,
#   then cleared once debugging is done.
# // TEMPLATE_STRING_IF_INVALID = "!! INVALID '%s' !!"


# WSGI =============================================================================================

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "config.wsgi.application"


# THIRD PARTY APPS =================================================================================

# pip:django-csp -----------------------------------------------------------------------------------
# Ref: https://django-csp.readthedocs.io/en/latest/configuration.html

# Configuration for the `Content-Security-Policy` header.
# // CSP_SCRIPT_SRC += ["'unsafe-eval'"]  # noqa


# pip:django-extensions ----------------------------------------------------------------------------
# Doc: https://django-extensions.readthedocs.io/

# Specify which address and port the development server should bind to.
# Note: This appears on the command-line when starting it.
RUNSERVERPLUS_SERVER_ADDRESS_PORT = f"{SITE_DOMAIN}:{SITE_PORT}"  # noqa


# pip:django-rosetta -------------------------------------------------------------------------------
# Ref: https://django-rosetta.readthedocs.io/

# // THIRD_PARTY_APPS.append("rosetta")  # noqa


# pip:whitenoise -----------------------------------------------------------------------------------
# Doc: http://whitenoise.evans.io/en/stable/django.html

THIRD_PARTY_APPS.insert(0, "whitenoise.runserver_nostatic")  # noqa


# FINALIZATION =====================================================================================

# Build `INSTALLED_APPS`.
INSTALLED_APPS = build_installed_apps()  # noqa
