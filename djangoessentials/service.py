from abc import ABC
from typing import Generic, TypeVar
from django.db.models import QuerySet

R = TypeVar("R")


class BaseService(ABC, Generic[R]):
    def __init__(self, repository: R):
        self._repository = repository

    def get_all(self) -> QuerySet:
        return self._repository.get_all()

    def get_by_id(self, obj_id: int):
        return self._repository.get_by_id(obj_id)

    def create(self, data: dict):
        return self._repository.create(data)

    def update(self, obj_id: int, data: dict):
        return self._repository.update(obj_id, data)

    def delete(self, obj_id: int):
        return self._repository.delete(obj_id)

    def filter(self, **filters) -> QuerySet:
        return self._repository.filter(**filters)
