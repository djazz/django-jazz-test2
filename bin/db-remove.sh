#!/usr/bin/env bash
# Delete the user and database for the application.


# Validate parameters.
missing_params=""
[ -z "$POSTGRES_DB" ] && missing_params+=", POSTGRES_DB"
[ -z "$POSTGRES_USER" ] && missing_params+=", POSTGRES_USER"
if [ -n "$missing_params" ]; then
  echo "These environment variables are not defined: ${missing_params:2}."
  exit 1
fi


# Delete the database if it exists.
if [ -n "$( psql -qtAc "SELECT 1 FROM pg_database WHERE datname='${POSTGRES_DB}'" )" ]; then
  echo "Deleting database '${POSTGRES_DB}'..."
  psql --set=ON_ERROR_STOP=1 \
    --host="$POSTGRES_HOST" --port="$POSTGRES_PORT" \
    <<EOSQL
DROP DATABASE "${POSTGRES_DB}";
EOSQL
else
  echo "Database '${POSTGRES_DB}' does not exist."
fi

# Delete the user if it exists.
if [ -n "$( psql postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='${POSTGRES_USER}'" )" ]; then
  echo "Deleting role '${POSTGRES_USER}'..."
  psql --set=ON_ERROR_STOP=1 \
    --host="$POSTGRES_HOST" --port="$POSTGRES_PORT" \
    <<EOSQL
DROP ROLE "${POSTGRES_USER}";
EOSQL
else
  echo "Role '${POSTGRES_USER}' does not exist."
fi
