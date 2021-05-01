from config.settings.base import *


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'life_recorder',
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'NAME': 'life_record_test',
        },
    }
}
