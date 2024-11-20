# -*- coding: utf-8 -*-
"""Фильтр, проверяющий, есть ли пользователь в базе данных."""

from aiogram.filters import Filter
from aiogram.types import Message
from aiogram_i18n.context import I18nContext

from data import Database
from ._message_from_user import MessageFromUser


class UserRegistered(Filter):
    """Фильтр, проверяющий, есть ли пользователь в базе данных."""

    async def __call__(self, 
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
        from_user: MessageFromUser = MessageFromUser()
        if await from_user(message, i18n):
            if database.get_user(uid=message.from_user.id):  # type: ignore
                return True
            await message.answer(text=i18n.get("user-not-registered"))
        return False
