import factory

from apps.users.models import User


class UserModelFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('pystr')
    class Meta:
        model = User
