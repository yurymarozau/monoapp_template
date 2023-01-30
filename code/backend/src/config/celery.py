from celery import Celery
from decouple import config


app = Celery(config('APP_NAME'))

app.config_from_object(config('DJANGO_SETTINGS_MODULE'), namespace='CELERY')

app.autodiscover_tasks()
