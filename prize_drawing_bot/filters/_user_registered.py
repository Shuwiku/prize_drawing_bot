# -*- coding: utf-8 -*-
"""Фильтр, проверяющий, есть ли пользователь в базе данных."""

from aiogram.filters import Filter
from aiogram.types import Message
from aiogram_i18n.context import I18nContext
from loguru import logger

from data import Database
from ._message_from_user import MessageFromUser


class UserRegistered(Filter):
    """Фильтр, проверяющий, есть ли пользователь в базе данных."""

    async def __call__(
        self,
        message: Message,
        database: Database,
        i18n: I18nContext
    ) -> bool:
        """Проверяет наличие пользователя в базе данных.

        По id пользователя из сообщения определяет его наличие в базе.

        В случае, если нет возможности получить id пользователя из
        сообщения, вернёт False.

        Returns:
            bool: Зарегистрирован пользователь или нет.
        """
        logger.debug("Фильтр 'UserRegistered'.")  # Логирование

        from_user: MessageFromUser = MessageFromUser()
        is_from_user: bool = await from_user(
            message=message,
            i18n=i18n
        )
        if is_from_user:
            if database.get_user(uid=message.from_user.id):  # type: ignore
                return True
            await message.answer(text=i18n.get("user-not-registered"))
        return False
