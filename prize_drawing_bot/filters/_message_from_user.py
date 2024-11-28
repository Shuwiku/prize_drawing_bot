# -*- coding: utf-8 -*-
"""Фильтр, проверяющий доступ к параметру message.from_user.

В некоторых случаях этот параметр может отсутствовать (быть None), например,
если сообщение по какой-либо причине пришло из канала. Этот фильтр помогает
избежать ошибок при обработке сообщений.
"""

from aiogram.filters import Filter
from aiogram.types import Message
from aiogram_i18n.context import I18nContext
from loguru import logger


class MessageFromUser(Filter):
    """Фильтр, проверяющий доступ к параметру message.from_user."""

    async def __call__(
        self,
        message: Message,
        i18n: I18nContext
    ) -> bool:
        """Проверяет доступ к параметру message.from_user.

        Returns:
            bool: True, если есть доступ к параметру message.from_user.
                В противном случае - False.
        """
        logger.debug("Фильтр:\t\tMessageFromUser")  # Логирование

        if message.from_user:
            return True
        await message.answer(text=i18n.get("message-not-from-user"))
        return False
