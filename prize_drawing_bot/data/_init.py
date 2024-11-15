# -*- coding: utf-8 -*-
"""Инструменты для инициализации и получения объекта базы данных."""

from loguru import logger

from ._database import Database


__database: Database


def get_database() -> Database:
    """Возвращает объект базы данных.

    Returns:
        Database: Объект базы данных.
    """
    return __database


def init(database_file_path: str) -> None:
    """Создаёт объект даны данных, который хранится в закрытой переменной."""
    global __database
    __database = Database(database_file_path)
    logger.trace("Объект базы данных создан.")
