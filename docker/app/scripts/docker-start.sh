#!/usr/bin/env bash
# Start the `app` service.


set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


echo "Starting the app (app mode: $APP_MODE)."

case "$APP_MODE" in
  "local")
    # Install pip packages.
    /home/django/pip-install.sh


    # TODO: ??? # Execute DB migrations.
    # TODO: ??? python /app/manage.py migrate

    # Run Django's server.
    python /app/manage.py runserver_plus 0.0.0.0:8000
    ;;

  *)
    # Execute DB migrations.
    python /app/manage.py migrate

    # Collect static files.
    # Note: Here and not in Dockerfile because these are saved in a Docker Volume.
    python /app/manage.py collectstatic --noinput

    # Run the web server.
    /usr/local/bin/gunicorn config.wsgi --bind 0.0.0.0:8000 --chdir=/app
esac
