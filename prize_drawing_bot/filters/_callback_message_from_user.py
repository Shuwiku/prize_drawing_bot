# -*- coding: utf-8 -*-
"""Фильтр, проверяющий доступ к параметру callback.message.

В некоторых случаях этот параметр может отсутствовать (быть None), или быть
типа не Message, а InaccessibleMessage, например, если сообщение было удалено.
"""

from aiogram.filters import Filter
from aiogram.types import Message, CallbackQuery
from aiogram_i18n.context import I18nContext


class CallbackMessageFromUser(Filter):
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
        if type(callback.message) is Message:
            return True
        await callback.answer(text=i18n.get("callback-not-from-user"))
        return False
