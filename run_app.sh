#!/bin/bash

# Run migrations and run server
python manage.py migrate && gunicorn config.wsgi --bind 0.0.0.0:8000 --workers 3 --log-level=DEBUG
