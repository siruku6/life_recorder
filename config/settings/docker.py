import sys

from config.settings.base import *


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': 'postgres',
        'PORT': 5432,
        'TEST': {
            'NAME': 'life_record_test',
        },
    }
}


###########################
#      For development
###########################
# TODO: If there is config/settings/test.py, then this condition can be simplified.
#   In this case, `'test' not in sys.argv` is going to be moved into manage.py.
if DEBUG and 'test' not in sys.argv:
    # 発行されるSQL文を出力するための設定
    LOGGING['loggers']['django.db.backends'] = {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': False,
    }

    # The following lines are for 'django-debug-toolbar'
    def show_toolbar(request):
        return True

    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': show_toolbar, }
