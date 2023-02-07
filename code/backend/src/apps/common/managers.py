from django.db import models

from apps.common.querysets import SoftDeleteQuerySet

# ToDo: create hard delete manager with inheritance soft delete manager from hard


class SoftDeleteManager(models.Manager):
    def __init__(self, all_objects=False, *args, **kwargs):
        self.all_objects = all_objects
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        queryset = SoftDeleteQuerySet(self.model, using=self._db)
        if self.all_objects:
            return queryset
        return queryset.filter(deleted_at=None)

    def delete(self):
        return self.get_queryset().delete()

    def hard_delete(self):
        return self.get_queryset().hard_delete()

    def restore(self):
        return self.get_queryset().restore()

    def alive(self):
        return self.get_queryset().alive()

    def deleted(self):
        return self.get_queryset().deleted()
