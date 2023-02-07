import os

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENVIRONMENT = config('ENVIRONMENT')

ENABLE_DOCS = config('ENABLE_DOCS', default=False, cast=bool)

REQUEST_TIME_LOG_THRESHOLD = config('REQUEST_TIME_LOG_THRESHOLD', default=5, cast=int)
