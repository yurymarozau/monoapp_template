from django.conf import settings
from storages.backends.s3boto3 import S3StaticStorage, S3Boto3Storage


class StaticStorage(S3StaticStorage):
    location = settings.AWS_STATIC_LOCATION


class MediaStorage(S3Boto3Storage):
    pass
