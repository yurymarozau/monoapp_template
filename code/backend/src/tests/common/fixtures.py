import random

import pytest


@pytest.fixture
def group_name(faker):
    return faker.pystr()

@pytest.fixture
def permissions(faker):
    return [faker.pystr() for _ in range(random.randint(2, 5))]
