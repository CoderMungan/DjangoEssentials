from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


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



#CustomUser Model
class CustomUserManager(BaseUserManager, TimeBasedStampModel):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin, TimeBasedStampModel):
    username = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
   

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

