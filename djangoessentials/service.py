from abc import ABC
from typing import Generic, TypeVar, Optional
from django.db.models import QuerySet

R = TypeVar("R")


class BaseService(ABC, Generic[R]):
    def __init__(self, repository: R):
        self._repository = repository

    def get_all(self) -> QuerySet:
        """Fetch all objects."""
        return self._repository.get_all()

    def get_by_id(self, obj_id: int) -> Optional[R]:
        """Fetch a single object by ID."""
        return self._repository.get_by_id(obj_id)

    def create(self, data: Optional[dict] = None, **kwargs) -> R:
        """
        Create a new object.
        Supports both a dictionary (`data`) or keyword arguments (`**kwargs`).
        """
        return self._repository.create(data, **kwargs)

    def update(self, obj_id: int, data: Optional[dict] = None, **kwargs) -> Optional[R]:
        """
        Update an object with the given data.
        Supports both a dictionary (`data`) or keyword arguments (`**kwargs`).
        """
        return self._repository.update(obj_id, data, **kwargs)

    def delete(self, obj_id: int) -> bool:
        """Delete an object by ID."""
        return self._repository.delete(obj_id)

    def filter(self, data: Optional[dict] = None, **filters) -> QuerySet:
        """
        Filter objects based on given criteria.
        Supports both a dictionary (`data`) or keyword arguments (`**filters`).
        """
        return self._repository.filter(data, **filters)

    def exists(self, data: Optional[dict] = None, **kwargs) -> bool:
        """
        Check if an object exists with the given criteria.
        Supports both a dictionary (`data`) or keyword arguments (`**kwargs`).
        """
        return self._repository.exists(data, **kwargs)

    def count(self, data: Optional[dict] = None, **kwargs) -> int:
        """
        Count objects with the given criteria.
        Supports both a dictionary (`data`) or keyword arguments (`**kwargs`).
        """
        return self._repository.count(data, **kwargs)

    def get_or_create(
        self, defaults: Optional[dict] = None, data: Optional[dict] = None, **kwargs
    ) -> tuple[R, bool]:
        """
        Get or create an object with the given criteria.
        Supports both a dictionary (`data`) or keyword arguments (`**kwargs`).
        """
        return self._repository.get_or_create(defaults=defaults, data=data, **kwargs)
