**DjangoEssentials**

[Join Our Community - Kampus](https://discord.gg/kampus)

**DjangoEssentials** is a Python library designed to streamline and simplify the development of Django applications. This library supports modern software development approaches, such as the **repository-service pattern**, and provides a more modular structure by preventing code repetition. Additionally, it includes essential features such as **model management, data access, and Amazon S3 storage integration**.

**🚀 Features**

**1️⃣ Repository-Service Pattern**

•	**BaseRepository:** A base repository class that manages CRUD operations for Django models.

•	**BaseService:** A service layer that utilizes repositories to manage business logic and reduce code duplication.

**2️⃣ Model Utilities**

•	**TimeBasedStampModel:** An abstract model class that automatically tracks **creation, update, and deletion timestamps**.

**3️⃣ Amazon S3 Storage Integration**

•	**MyS3Storage:** A custom storage class for **handling media files with Amazon S3** in Django applications.

**📥 Installation**

Install the library using pip:

```python
pip install DjangoEssentials
```

**📌 Usage**

**1️⃣ Using the Repository-Service Pattern**

This pattern separates the **data access layer** from the **business logic layer**, making Django applications cleaner and more maintainable.

**📌 Model Example**

Let’s create a **simple Django model** using TimeBasedStampModel:

```python
from django.db import models
from djangoessentials import TimeBasedStampModel

class Product(TimeBasedStampModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
```

**📌 Repository Layer**

The repository interacts with Django models and manages database operations.

```python
from djangoessentials.repository import BaseRepository
from myapp.models import Product

class ProductRepository(BaseRepository[Product]):
    def __init__(self):
        super().__init__(Product)
```

**📌 Service Layer**

The service layer uses the repository to manage business logic and reduce code duplication.

```python
from djangoessentials.service import BaseService
from myapp.repositories import ProductRepository

class ProductService(BaseService[ProductRepository]):
    def __init__(self):
        super().__init__(ProductRepository())

    def get_available_products(self):
        return self._repository.filter(stock__gt=0)
```

**📌 Serializer for DRF**

To expose this model via an API, let’s create a serializer.

```python
from rest_framework import serializers
from myapp.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

**📌 ViewSet for Django REST Framework**

To expose the service through an API, we can use **ModelViewSet**.

```python
from rest_framework import viewsets
from myapp.services import ProductService
from myapp.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductService().get_all()
    
    def get_queryset(self):
        """
        Optionally filter the queryset based on stock availability.
        """
        service = ProductService()
        available_only = self.request.query_params.get('available_only', None)
        if available_only:
            return service.get_available_products()
        return service.get_all()
```

**📌 Register the ViewSet in Django’s Router**

To enable API endpoints, register the viewset in urls.py.

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

**2️⃣ Using TimeBasedStampModel**

To add automatic **created_at, updated_at, and deleted_at** fields to your model:

```python
from django.db import models
from djangoessentials import TimeBasedStampModel

class YourModel(TimeBasedStampModel):
    name = models.CharField(max_length=255)
    # Add your custom fields here
```

This model **automatically tracks timestamps** for each record.

**3️⃣ Amazon S3 Storage Integration**

To use **Amazon S3 as the media storage solution**, configure your Django project as follows.

**📌 Add to settings.py**

```python
import os

USE_S3 = True

if USE_S3:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
```

**📌 Use in a Model**

```python
from django.db import models
from djangoessentials import MyS3Storage

class MyModel(models.Model):
    document = models.FileField(upload_to='documents/', storage=MyS3Storage)
```

This setup ensures that files are **automatically uploaded to Amazon S3**.

**🎯 Advanced Usage**

DjangoEssentials is designed to grow with the community’s needs. Over time, more utilities and helpers will be added to **optimize Django development workflows**.

**🤝 Contributing**

We welcome community contributions! If you’d like to add new features, improve documentation, or report bugs, follow these steps:

1.	**Fork the repository.**

2.	**Create a feature branch:**

```python
git checkout -b feature/AmazingFeature
```

3.	**Commit your changes:**

```python
git commit -am "Add some AmazingFeature"
```

4.	**Push to the branch:**

```python
git push origin feature/AmazingFeature
```

5.	**Open a Pull Request.**

**📩 Contact**

For questions or further information, feel free to contact us:

📧 [**codermungan@gmail.com**](mailto:codermungan@gmail.com)