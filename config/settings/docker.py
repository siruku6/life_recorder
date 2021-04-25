from config.settings.base import *
from config.settings.base import env


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', False)


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


# For localhost
if DEBUG:
    def show_toolbar(request):
        return True

    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': show_toolbar, }
