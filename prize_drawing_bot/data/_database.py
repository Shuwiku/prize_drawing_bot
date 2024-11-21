# -*- coding: utf-8 -*-
"""Класс базы данных."""

import sqlite3
from pathlib import Path
from sqlite3 import Connection, Cursor
from typing import Any, Optional, Union

from loguru import logger

from . import _queries


class Database:
    """Класс базы данных."""

    _connection: Connection

    def __init__(
        self,
        database_file: Union[Path, str]
    ) -> None:
        """Инициализация объекта базы данных.

        Создаёт сессию с указанной базой данных, настраивает её и
        предоставляет методы для управления.

        Args:
            database_file (str): Путь к файлу базы данных.
        """
        self._connection = sqlite3.connect(database=database_file)
        self.__create_tables()
        self.__create_indexes()

    def __create_indexes(self) -> None:
        """Создаёт индексы базы данных."""
        self._execute(query=_queries.create_index_user_uid)
        logger.trace("Индексы базы данных созданы.")  # Логирование

    def __create_tables(self) -> None:
        """Создаёт таблицы базы данных."""
        self._execute(query=_queries.create_table_user)
        logger.trace("Таблицы базы данных созданы.")  # Логирование

    def _execute(
        self,
        query: str,
        parameters: Optional[tuple] = None
    ) -> Any:
        """Выполняет запросы к базе данных.

        Используется для оптимизации кода, чтобы не засорять его.

        Args:
            query (str): Запрос к базе данных
            parameters (Optional[tuple]): Аргументы, передаваемые с запросом.
                По умолчанию - None.

        Returns:
            Any: Результат выполнения запроса.
        """
        with self._connection:
            cursor: Cursor = self._connection.cursor()

            if parameters:
                cursor.execute(
                    query,
                    parameters
                )
            else:
                cursor.execute(query)

            result: Any = cursor.fetchone()
            cursor.close()
            return result

    def add_user(
        self,
        uid: int
    ) -> None:
        """Добавляет пользователя в базу данных.

        Args:
            uid (int): ID пользователя в телеграм.
        """
        self._execute(
            query=_queries.add_user,
            parameters=(uid,)
        )

    def get_user(
        self,
        uid: int
    ) -> Any:
        """Получает данные пользователя из базы данных.

        Args:
            uid (int): ID пользователя в телеграм.

        Returns:
            Any: Данные пользователя.
        """
        return self._execute(
            query=_queries.get_user,
            parameters=(uid,)
        )

    def get_user_language(
        self,
        uid: int
    ) -> Optional[str]:
        """Получает локаль пользователя.

        Args:
            uid (int): ID пользователя в телеграм.

        Returns:
            str: Локаль пользователя.
        """
        result: Optional[tuple] = self._execute(
            query=_queries.get_user_language,
            parameters=(uid,)
        )
        return result[0] if result else None

    def set_user_language(
        self,
        uid: int,
        language: str
    ) -> Any:
        """Устанавливает локаль пользователя.

        Args:
            uid (int): ID пользователя в телеграм.
            language (str): Новая локаль пользователя.
        """
        self._execute(
            query=_queries.set_user_language,
            parameters=(language, uid)
        )
