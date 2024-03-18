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

DEFAULT_FILE_STORAGE = 'DjangoEssentials.storage.MyS3Storage'
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
