#!/bin/bash

#echo "Waiting for PostgreSQL to be ready..."
#until psql -h postgres_db -U user -d population_db -c '\q'; do
#  echo "PostgreSQL is not ready, waiting..."
#  sleep 2
#done
#
#echo "Running Alembic migrations..."
alembic upgrade head


exec "$@"
