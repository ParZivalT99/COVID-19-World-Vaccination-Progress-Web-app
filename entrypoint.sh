#!/bin/bash
python manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python manage.py insert_dataset
python3 manage.py runserver 0.0.0.0:8000