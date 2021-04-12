#!/bin/ash
# I use /bin/ash because in alpine container, we can't use bin/bash.

npm install --save-dev

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
