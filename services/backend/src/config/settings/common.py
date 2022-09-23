from decouple import config


ENVIRONMENT = config('ENVIRONMENT')
ENABLE_DOCS = config('ENABLE_DOCS', default=False, cast=bool)
