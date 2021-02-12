#!/usr/bin/env bash
# Create the user and database for the application.


# Validate parameters.
missing_params=""
[ -z "$POSTGRES_DB" ] && missing_params+=", POSTGRES_DB"
[ -z "$POSTGRES_USER" ] && missing_params+=", POSTGRES_USER"
[ -z "$POSTGRES_PASSWORD" ] && missing_params+=", POSTGRES_PASSWORD"
if [ -n "$missing_params" ]; then
  echo "These environment variables are not defined: ${missing_params:2}."
  exit 1
fi


# Create the user if it does not exist.
if [ -n "$( psql postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='${POSTGRES_USER}'" )" ]; then
  echo "Role '${POSTGRES_USER}' already exists."
else
  echo "Creating role '${POSTGRES_USER}'..."
  psql --set=ON_ERROR_STOP=1 \
    --host="$POSTGRES_HOST" --port="$POSTGRES_PORT" \
    <<EOSQL
CREATE ROLE "${POSTGRES_USER}" WITH LOGIN PASSWORD '${POSTGRES_PASSWORD}';
EOSQL
fi

# Create the database if it does not exist.
if [ -n "$( psql -qtAc "SELECT 1 FROM pg_database WHERE datname='${POSTGRES_DB}'" )" ]; then
  echo "Database '${POSTGRES_DB}' already exists."
else
  echo "Creating database '${POSTGRES_DB}'..."
  psql --set=ON_ERROR_STOP=1 \
    --host="$POSTGRES_HOST" --port="$POSTGRES_PORT" \
    <<EOSQL
CREATE DATABASE "${POSTGRES_DB}";
EOSQL
fi

# Configure permissions.
echo "Configuring permissions for '${POSTGRES_USER}' on '${POSTGRES_DB}'..."
psql --set=ON_ERROR_STOP=1 \
  --host="$POSTGRES_HOST" --port="$POSTGRES_PORT" --dbname="$POSTGRES_DB" \
  <<EOSQL
GRANT USAGE ON SCHEMA public TO "${POSTGRES_USER}";
EOSQL
