# DjangoEssentials

DjangoEssentials is a Python library designed to streamline and enhance the development process of Django applications. It offers a collection of commonly used Django models and deployment settings, encapsulating repetitive patterns and configurations into a reusable package. The library is intended to evolve with contributions from the community, making it a collaborative project.

## Features

- **TimeBasedStampModel:** An abstract model providing time-based fields for tracking creation, update, and deletion times of model instances.
- **MyS3Storage:** A custom storage class for Django, facilitating integration with Amazon S3 for media storage, with features such as non-overwriting of files with the same name and public read access by default.

## Getting Started

Below are instructions on how to install DjangoEssentials and examples of how to use its features in your Django projects.

### Installation

Install DjangoEssentials using pip:

```bash
pip install DjangoEssentials
```

### Usage

- **TimeBasedStampModel**

Inherit from TimeBasedStampModel to add automatic creation, update, and soft deletion timestamps to your models.

```python

from django.db import models
from djangoessentials import TimeBasedStampModel

class YourModel(TimeBasedStampModel):
    name = models.CharField(max_length=255)
    # Add your fields here

```

- **MyS3Storage**

Configure your Django project to use MyS3Storage for handling media files with Amazon S3.

```python
# settings.py
USE_S3 = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3Boto3Storage'
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]
```
Than

```python
from django.db import models
from djangoessentials import MyS3Storage

class MyModel(models.Model):
    document = models.FileField(upload_to='documents/', storage=MyS3Storage)
    # Add your fields here
```

### Advanced Usage

DjangoEssentials aims to provide more utilities and helpers over time, driven by community contributions and the evolving needs of Django developers.

### Contributing
We welcome contributions from the community, whether it's adding new features, improving documentation, or reporting bugs. Please follow these steps to contribute:

Fork the repository.
- Create your feature branch (git checkout -b feature/AmazingFeature).
- Commit your changes (git commit -am 'Add some AmazingFeature').
- Push to the branch (git push origin feature/AmazingFeature).
- Open a Pull Request.

### Contact
For questions or additional information, please reach out to codermungan@gmail.com
