#!/usr/bin/env bash

# wait for Postgres to start
function postgres_ready(){
python << END
import sys
import psycopg2
from decouple import config
try:
    conn = psycopg2.connect(
      dbname=config('NAME_PSQL'),
      user=config('USER_PSQL'),
      password=config('PASSWORD_PSQL'),
      host=config('HOST_PSQL', 'localhost')
    )
    conn.close()
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

until python manage.py migrate; do
  sleep 2
  echo "migrate not finished!";
done

python manage.py runserver 0.0.0.0:8000
