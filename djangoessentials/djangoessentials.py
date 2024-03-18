from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

# TimeBasedStamp Model Start
class TimeBasedStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
# TimeBasedStamp Model End

class MyS3Storage(S3Boto3Storage):
    location = 'media/'  # S3'te files alt dir
    file_overwrite = False  # if have a same name about the file cant overwrite
    default_acl = 'public-read' # just can read permission
