#!/bin/bash
flask db init && flask db migrate && flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app