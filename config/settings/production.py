"""Application settings for the `production` application mode."""

# Import base settings.
from .base import *  # noqa


# THIRD PARTY APPS =================================================================================

# pip:easy-thumbnails ------------------------------------------------------------------------------
# Ref: https://easy-thumbnails.readthedocs.io/en/latest/ref/settings/

# Optimization.
# See: https://developers.google.com/speed
THUMBNAIL_OPTIMIZE_COMMAND = {
    "png": "/usr/bin/optipng {filename}",
    "gif": "/usr/bin/optipng {filename}",
    "jpeg": "/usr/bin/jpegoptim {filename}",
}


# pip:whitenoise -----------------------------------------------------------------------------------
# Doc: http://whitenoise.evans.io/en/stable/django.html

# Enable forever-cachable files and gzip support.
# // STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# FINALIZATION =====================================================================================

# Build `INSTALLED_APPS`.
INSTALLED_APPS = build_installed_apps()  # noqa
