from django.apps import AppConfig
from django.db.models.signals import post_migrate

from apps.common.permissions import GroupPermissionsService


class AppsConfig(AppConfig):
    name = 'apps'

    def ready(self):
        post_migrate.connect(GroupPermissionsService.post_migrate_callback, sender=self)
