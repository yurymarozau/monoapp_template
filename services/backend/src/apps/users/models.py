from django.contrib.auth.models import AbstractUser

from apps.common.models import AbstractUUIDModel


class User(AbstractUser, AbstractUUIDModel):
    pass
