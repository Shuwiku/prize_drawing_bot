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
                         database: Database
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
        language: Optional[str] = database.get_user_language(
            uid=event_from_user.id)
        if language:
            return language
        return str(self.default_locale)

    async def set_locale(self,
                         locale: str,
                         event_from_user: User,
                         database: Database
                         ) -> None:
        """Устанавливает локаль пользователя.

        Args:
            locale (str): Новая локаль пользователя.
            event_from_user (User): Объект пользователя телеграм.
            database (Optional[Database]): Объект базы данных.
                Берётся из мидлваря взаимодействия с базой данных.
        """
        database.set_user_language(uid=event_from_user.id,
                                   language=locale)
