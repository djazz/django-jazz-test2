"""Application settings for the `testing` application mode."""

# Import base settings.
from .base import *  # noqa


# FINALIZATION =====================================================================================

# Build `INSTALLED_APPS`.
INSTALLED_APPS = build_installed_apps()  # noqa
