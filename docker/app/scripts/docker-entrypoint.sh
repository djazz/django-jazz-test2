#!/usr/bin/env bash
# Start the `app` service only when the `POSTGRES_HOST` service is ready.
# See: https://docs.docker.com/compose/startup-order/


set -e

# // # Parse `POSTGRES_URL` to retrieve the DB name, user and password.
# // IFS=$'\t' read POSTGRES_HOST POSTGRES_PORT POSTGRES_DB POSTGRES_USER POSTGRES_PASSWORD <<< "$( python3 <<EOCODE
# // from urllib.parse import urlparse
# // db_url = urlparse("${POSTGRES_URL}")
# // host, port = f"{db_url.netloc}:5432".split(":")[:2]
# // print(f"{host}\t{port}\t{db_url.path.strip('/')}\t{db_url.username}\t{db_url.password}")
# // EOCODE
# // )"

# Check whether the `POSTGRES_HOST` service is ready by trying to connect to it.
function postgres_ready() {
python <<EOCODE
from psycopg2 import connect, OperationalError
from sys import exit
try:
    connect(
        host="$POSTGRES_HOST",
        port="$POSTGRES_PORT",
        dbname="$POSTGRES_DB",
        user="$POSTGRES_USER",
        password="$POSTGRES_PASSWORD",
    )
except OperationalError:
    exit(-1)
exit(0)
EOCODE
}


echo "Entrypoint (app mode: ${APP_MODE})."
echo "Checking access to the '${POSTGRES_HOST}' service.."

# Sleep until `postgres` is ready.
until postgres_ready; do
  >&2 echo "Waiting for '${POSTGRES_HOST}' service to become available."
  sleep 1
done

# When `postgres` is ready, execute the given custom command or start this service.
>&2 echo "Continuing, '${POSTGRES_HOST}' service is ready."
exec "$@"
