# -*- coding: utf-8 -*-
"""Docstring."""

from aiogram.filters import Filter
from aiogram.types import Message


class MessageFromUser(Filter):
    """DOCSTRING."""
    
    async def __call__(self, 
                       message: Message
                       ) -> bool:
        """DOCSTRING."""
        if message.from_user:
            return True
        return False
