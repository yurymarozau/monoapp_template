from django.apps import AppConfig
from django.db.models.signals import post_migrate

# from apps.auth.permissions import groups_synchronisation_callback


class AppsConfig(AppConfig):
    name = 'apps'

    def ready(self):
        pass
        # post_migrate.connect(groups_synchronisation_callback, sender=self)
