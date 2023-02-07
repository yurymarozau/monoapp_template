from pytest_factoryboy import register

from tests.users.factories import UserModelFactory
from tests.users.fixtures import *

register(UserModelFactory, 'user_model_instance')
