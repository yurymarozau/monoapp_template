from django.contrib.auth.models import AbstractUser, UserManager

from apps.common.models import AbstractBaseModel


class User(AbstractBaseModel, AbstractUser):
    user_objects = UserManager()
