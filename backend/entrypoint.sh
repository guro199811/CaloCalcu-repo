#!/bin/sh
# entrypoint.sh

# Wait for PostgreSQL to be ready


until nc -z -v -w30 db 5432
do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 5
done

# Run migrations and start the Django application
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

python manage.py runserver 0.0.0.0:8000
