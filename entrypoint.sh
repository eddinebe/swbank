#!/bin/bash

set -e

python manage.py collectstatic --noinput
echo "starting entrypoint script"
exec gunicorn -b 0.0.0.0:8000 project.wsgi:application
