import random

import pytest


@pytest.fixture
def user(user_model_factory):
    return user_model_factory()

@pytest.fixture
def random_users(user_model_factory):
    amount_to_generate = random.randint(15, 50)
    return [user_model_factory() for _ in range(amount_to_generate)]

@pytest.fixture
def soft_deleted_user(user):
    user.delete()
    return user
