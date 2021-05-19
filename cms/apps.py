from django.apps import AppConfig
from django.db.models.signals import post_migrate


class CmsConfig(AppConfig):
    name = 'cms'

    def ready(self):
        from cms.models import seed_default_data
        post_migrate.connect(seed_default_data, sender=self)
