# -*- coding: utf-8 -*-
"""Функция, которая убирает клавиатуру из сообщения по id."""

from loguru import logger

import bot


@logger.catch
async def remove_keyboard(chat_id: int, message_id: int) -> None:
    """Убирает клавиатуру из сообщения.

    Args:
        chat_id (int): id чата (пользователя).
        message_id (int): id сообщения с клавиатурой.
    """
    await bot.get_bot().edit_message_reply_markup(chat_id=chat_id,
                                                  message_id=message_id,
                                                  reply_markup=None)
