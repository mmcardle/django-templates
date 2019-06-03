#!/usr/bin/env bash
PYTHONIOENCODING=utf-8

echo "Applying any migrations"
python3 /project/manage.py migrate

nginx -g "daemon on;"
circusd /opt/config/circus.ini
