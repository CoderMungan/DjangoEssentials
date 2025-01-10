from abc import ABC
from typing import Generic, TypeVar, List, Optional, Any
from django.db.models import Model, QuerySet
from django.core.exceptions import ObjectDoesNotExist

T = TypeVar("T", bound=Model)


class BaseRepository(ABC, Generic[T]):
    def __init__(self, model: T):
        self._model = model

    def get_all(self) -> QuerySet[T]:
        return self._model.objects.all()

    def get_by_id(self, obj_id: int) -> Optional[T]:
        try:
            return self._model.objects.get(id=obj_id)
        except ObjectDoesNotExist:
            return None

    def get_or_none(self, **kwargs) -> Optional[T]:
        try:
            return self._model.objects.get(**kwargs)
        except ObjectDoesNotExist:
            return None

    def create(self, data: dict) -> T:
        return self._model.objects.create(**data)

    def bulk_create(self, data_list: List[dict]) -> List[T]:
        objects = [self._model(**data) for data in data_list]
        return self._model.objects.bulk_create(objects)

    def update(self, obj_id: int, data: dict) -> Optional[T]:
        try:
            obj = self._model.objects.get(id=obj_id)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        except ObjectDoesNotExist:
            return None

    def delete(self, obj_id: int) -> bool:
        try:
            obj = self._model.objects.get(id=obj_id)
            obj.delete()
            return True
        except ObjectDoesNotExist:
            return False

    def filter(self, **filters) -> QuerySet[T]:
        return self._model.objects.filter(**filters)

    def exists(self, **kwargs) -> bool:
        return self._model.objects.filter(**kwargs).exists()

    def count(self, **kwargs) -> int:
        return self._model.objects.filter(**kwargs).count()

    def get_or_create(self, defaults: dict = None, **kwargs) -> tuple[T, bool]:
        return self._model.objects.get_or_create(defaults=defaults, **kwargs)
