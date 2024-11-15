# -*- coding: utf-8 -*-
"""Менеджер интернационализации на базе класса BaseManager."""

from typing import Optional

from aiogram_i18n.managers import BaseManager
from aiogram.types.user import User

from data import Database


class I18nMiddlewareManager(BaseManager):
    """Менеджер интернационализации на базе класса BaseManager."""

    async def get_locale(self,
                         event_from_user: User,
                         database: Optional[Database] = None
                         ) -> str:
        """Получает локаль пользователя.

        Args:
            event_from_user (User): Объект пользователя телеграм
            database (Optional[Database]): Объект базы данных.
                Берётся из мидлваря взаимодействия с базой данных.

        Returns:
            str: Локаль пользователя.
                Если пользователя нет - вернёт локаль по умолчанию.
        """
        if database:
            language: Optional[str] = \
                database.get_user_language(event_from_user.id)
            if language:
                return language
        return str(self.default_locale)

    async def set_locale(self,
                         locale: str,
                         event_from_user: User,
                         database: Optional[Database] = None
                         ) -> None:
        """Устанавливает локаль пользователя.

        Args:
            locale (str): Новая локаль пользователя.
            event_from_user (User): Объект пользователя телеграм.
            database (Optional[Database]): Объект базы данных.
                Берётся из мидлваря взаимодействия с базой данных.
        """
        if database:
            database.set_user_language(event_from_user.id, locale)
