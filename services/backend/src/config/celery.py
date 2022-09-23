from celery import Celery
from decouple import config
from os import environ


app = Celery(config('APP_NAME'))

app.config_from_object(environ['DJANGO_SETTINGS_MODULE'], namespace='CELERY')

app.autodiscover_tasks()
