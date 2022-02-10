#!/bin/sh
python manage.py makemigrations mainconfigs --noinput
python manage.py migrate
python manage.py runserver 0.0.0.0:9002
exec "$@"