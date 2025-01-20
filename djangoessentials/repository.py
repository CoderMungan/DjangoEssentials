from abc import ABC
from typing import Generic, TypeVar, List, Optional
from django.db.models import Model, QuerySet
from django.core.exceptions import ObjectDoesNotExist

T = TypeVar("T", bound=Model)


class BaseRepository(ABC, Generic[T]):
    def __init__(self, model: T):
        self._model = model

    def get_all(self) -> QuerySet[T]:
        """Fetch all objects."""
        return self._model.objects.all()

    def get_by_id(self, obj_id: int) -> Optional[T]:
        """Fetch a single object by ID."""
        try:
            return self._model.objects.get(id=obj_id)
        except ObjectDoesNotExist:
            return None

    def create(self, data: Optional[dict] = None, **kwargs) -> T:
        """
        Create a new object.
        Supports both a dictionary (`data`) or keyword arguments (`**kwargs`).
        """
        if data is None:
            data = kwargs
        return self._model.objects.create(**data)

    def bulk_create(self, data_list: List[dict]) -> List[T]:
        """Bulk create objects with a list of dictionaries."""
        objects = [self._model(**data) for data in data_list]
        return self._model.objects.bulk_create(objects)

    def update(self, obj_id: int, data: Optional[dict] = None, **kwargs) -> Optional[T]:
        """
        Update an object with the given data.
        Supports both a dictionary (`data`) or keyword arguments (`**kwargs`).
        """
        if data is None:
            data = kwargs

        try:
            obj = self._model.objects.get(id=obj_id)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        except ObjectDoesNotExist:
            return None

    def delete(self, obj_id: int) -> bool:
        """Delete an object by ID."""
        try:
            obj = self._model.objects.get(id=obj_id)
            obj.delete()
            return True
        except ObjectDoesNotExist:
            return False

    def filter(self, data: Optional[dict] = None, **filters) -> QuerySet[T]:
        """
        Filter objects based on given criteria.
        Supports both a dictionary (`data`) or keyword arguments (`**filters`).
        """
        if data is None:
            data = filters
        return self._model.objects.filter(**data)

    def exists(self, data: Optional[dict] = None, **kwargs) -> bool:
        """
        Check if an object exists with the given criteria.
        Supports both a dictionary (`data`) or keyword arguments (`**kwargs`).
        """
        if data is None:
            data = kwargs
        return self._model.objects.filter(**data).exists()

    def count(self, data: Optional[dict] = None, **kwargs) -> int:
        """
        Count objects with the given criteria.
        Supports both a dictionary (`data`) or keyword arguments (`**kwargs`).
        """
        if data is None:
            data = kwargs
        return self._model.objects.filter(**data).count()

    def get_or_create(
        self, defaults: Optional[dict] = None, data: Optional[dict] = None, **kwargs
    ) -> tuple[T, bool]:
        """
        Get or create an object with the given criteria.
        Supports both a dictionary (`data`) or keyword arguments (`**kwargs`).
        """
        if data is None:
            data = kwargs
        return self._model.objects.get_or_create(defaults=defaults, **data)
