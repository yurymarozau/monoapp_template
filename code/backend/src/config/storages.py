from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage, S3StaticStorage


class StaticStorage(S3StaticStorage):
    location = settings.AWS_STATIC_LOCATION


class MediaStorage(S3Boto3Storage):
    pass
