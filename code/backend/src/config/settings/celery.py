from decouple import config


CELERY_BROKER_URL = f'redis://{config("BROKER_HOST")}:{config("BROKER_PORT")}/{config("BROKER_DB")}'

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_DEFAULT_QUEUE = 'low'

CELERY_IMPORTS = (
    # 'apps.exampleapp.routines',
)

CELERY_TASK_ROUTES = {
    # example
    # 'apps.exampleapp.routines.PeriodicExampleTask': {'queue': 'low'},
}
