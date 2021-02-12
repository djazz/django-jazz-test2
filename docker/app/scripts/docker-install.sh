#!/usr/bin/env bash
# Install the `app` service.


echo "Installing the app (app mode: $APP_MODE)..."

# Install pip packages.
pip install --no-cache-dir --upgrade pip setuptools
/home/django/pip-install.sh
