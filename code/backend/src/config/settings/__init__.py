from config.settings.celery import *
from config.settings.common import *
from config.settings.db import *
from config.settings.django import *
from config.settings.internalization import *
from config.settings.media import *
from config.settings.sentry import *
from config.settings.ws import *

try:
    from config.settings.localhost import *
except Exception as e:
    print('Exception: %s' % e)
