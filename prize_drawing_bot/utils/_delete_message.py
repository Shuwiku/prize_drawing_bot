# -*- coding: utf-8 -*-
"""Функция, удаляющая сообщение по его id."""

from loguru import logger

import bot


@logger.catch
async def delete_message(
    chat_id: int,
    message_id: int
) -> None:
    """Удаляет сообщение бота.

    Args:
        chat_id (int): id чата (пользователя).
        message_id (int): id сообщения.
    """
    await bot.get_bot().delete_message(
        chat_id=chat_id,
        message_id=message_id
    )
