from config.settings.base import *
from config.settings.base import env


DEBUG = env('DEBUG', False)


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


# For localhost
if DEBUG:
    def show_toolbar(request):
        return True

    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': show_toolbar, }
