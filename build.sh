#!/usr/bin/env bash
if [[ $CREATE_SUPERUSER ]];
then
  python world_champ_2022/manage.py createsuperuser --no-input
fi
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py migrate
