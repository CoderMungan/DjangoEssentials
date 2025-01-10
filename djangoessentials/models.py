from django.db import models


# TimeBasedStampModel
class TimeBasedStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
