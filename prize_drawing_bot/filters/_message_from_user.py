# -*- coding: utf-8 -*-
"""Фильтр, проверяющий доступ к параметру message.from_user.

В некоторых случаях этот параметр может отсутствовать (быть None), например, 
если сообщение по какой-либо причине пришло из канала. Этот фильтр помогает
избежать ошибок при обработке сообщений.
"""

from aiogram.filters import Filter
from aiogram.types import Message


class MessageFromUser(Filter):
    """Фильтр, проверяющий доступ к параметру message.from_user.."""
    
    async def __call__(self, 
                       message: Message
                       ) -> bool:
        """Проверяет доступ к параметру message.from_user.

        Returns:
            bool: True, если есть доступ к параметру message.from_user.
                В противном случае - False.
        """
        if message.from_user:
            return True
        return False
