# INFO: for reading heroku settings
import django_heroku
import dj_database_url

from config.settings.base import *


TEMPLATES[0]['OPTIONS']['loaders'] = \
    ('django.template.loaders.cached.Loader', TEMPLATES_LOADERS),


# Database
db_from_env = dj_database_url.config()
DATABASES = {
    'default': db_from_env
}


# INFO: This must be set at the bottom of settings.py
# https://devcenter.heroku.com/ja/articles/django-app-configuration
django_heroku.settings(locals())
