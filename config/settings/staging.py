"""Application settings for the `staging` application mode."""

# Import `production` settings.
# Note: As the staging environment must always be as close as possible to the production one,
#   we start from there rather than from `base`.
from .production import *  # noqa


# THIRD PARTY APPS =================================================================================

# pip:django-rosetta -------------------------------------------------------------------------------
# Ref: https://django-rosetta.readthedocs.io/

# // THIRD_PARTY_APPS.append("rosetta")  # noqa


# FINALIZATION =====================================================================================

# Build `INSTALLED_APPS`.
INSTALLED_APPS = build_installed_apps()  # noqa
