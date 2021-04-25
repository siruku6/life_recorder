#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ

env = environ.Env(
    ENVIRONMENT=(str, 'DOCKER')
)
VIRTUAL_ENVIRONMENT = env('ENVIRONMENT')


def main():
    """Run administrative tasks."""
    settings_file = 'docker' if VIRTUAL_ENVIRONMENT == 'DOCKER' else 'localhost'
    settings_path = 'config.settings.{}'.format(settings_file)
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


if __name__ == '__main__':
    main()
