# -*- coding: utf-8 -*-
"""Фильтр, проверяющий доступ к параметру callback.message.

В некоторых случаях этот параметр может отсутствовать (быть None), или быть
типа не Message, а InaccessibleMessage, например, если сообщение было удалено.
"""

from aiogram.filters import Filter
from aiogram.types import Message, CallbackQuery
from aiogram_i18n.context import I18nContext

from loguru import logger


class CallbackHaveMessage(Filter):
    """Фильтр, проверяющий доступ к параметру callback.message."""

    async def __call__(
        self,
        callback: CallbackQuery,
        i18n: I18nContext
    ) -> bool:
        """Проверяет доступ к параметру callback.message.

        Returns:
            bool: True, если есть доступ к параметру callback.message.
                В противном случае - False.
        """
        logger.debug("Вызван фильтр CallbackHaveMessage")

        # Я не знаю почему и как, но сюда попадают события, которые не должны
        # попадать. Например, если просто ввести команду "/language", то
        # каким-то образом вызовется этот фильтр, хотя, вроде как, не должен
        if type(callback) is not CallbackQuery:
            return False

        if hasattr(callback, "message") and type(callback.message) is Message:
            return True

        await callback.answer(text=i18n.get("callback-have-not-message"))
        return False
