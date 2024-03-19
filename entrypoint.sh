#!/bin/sh

python manage.py migrate --no-input
python collectstatic --no-input

gunicorn todo.wsgi:application --bind 0.0.0.0:8000