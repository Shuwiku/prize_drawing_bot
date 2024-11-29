# -*- coding: utf-8 -*-
"""База данных.

Класс базы данных, инструменты для создания и получения объекта базы данных.
"""

from pathlib import Path
from typing import Union

from loguru import logger

# Это так же позволит импортировать класс напрямую из модуля
# Вместо:   from data._database import Database
# Будет:    from data import Database
from ._database import Database


__database: Database


def get_database(
) -> Database:
    """Возвращает объект базы данных.

    Returns:
        Database: Объект базы данных.
    """
    return __database


def init(
    database_file_path: Union[Path, str]
) -> None:
    """Создаёт объект даны данных, который хранится в закрытой переменной."""
    global __database

    __database = Database(database_file=database_file_path)

    # Логирование
    logger.trace("Объект базы данных создан.")
    logger.info("Путь к файлу базы данных:")
    logger.info(f"$ {database_file_path}")
