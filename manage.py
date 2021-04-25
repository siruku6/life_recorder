#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ


def main():
    """Run administrative tasks."""
    settings_path = decide_settings_path()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_path)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def decide_settings_path():
    env = environ.Env(
        ENVIRONMENT=(str, 'DOCKER')
    )
    VIRTUAL_ENVIRONMENT = env('ENVIRONMENT')

    if VIRTUAL_ENVIRONMENT == 'DOCKER':
        settings_file = 'docker'
    elif VIRTUAL_ENVIRONMENT == 'HEROKU':
        settings_file = 'heroku'
    else:
        settings_file = 'localhost'
    settings_path = 'config.settings.{}'.format(settings_file)

    return settings_path


if __name__ == '__main__':
    main()
