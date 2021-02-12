#!/usr/bin/env bash
# Install pip packages.


[ "$APP_MODE" != "local" ] && pip install --no-cache-dir -r /home/django/docker-requirements.txt
pip install --no-cache-dir -r /app/requirements/${APP_MODE}.txt
