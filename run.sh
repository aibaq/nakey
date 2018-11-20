#!/usr/bin/env bash
source '../envs/nakey/bin/activate'
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
