import uuid
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class FilmWork:
    """ DataClass описывающий таблицу film_work """

    __slots__ = ["id", "title", "description", "creation_date", "certificate", "file_path", "rating", "type",
                 "created_at", "updated_at"]

    id: uuid.UUID
    title: str
    description: str
    creation_date: datetime
    certificate: datetime
    file_path: datetime
    rating: float
    type: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class Genre:
    """ DataClass описывающий таблицу genre """
    __slots__ = ["id", "name", "description", "created_at", "updated_at"]

    id: uuid.UUID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class Person:
    """ DataClass описывающий таблицу person """

    __slots__ = ["id", "full_name", "birth_date", "created_at", "updated_at"]

    id: uuid.UUID
    full_name: str
    birth_date: datetime
    created_at: datetime
    updated_at: datetime


