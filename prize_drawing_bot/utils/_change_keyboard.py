# -*- coding: utf-8 -*-
"""Функция, которая убирает клавиатуру из сообщения по id."""

from typing import Optional

from aiogram_i18n.types import InlineKeyboardMarkup
from loguru import logger

import bot


@logger.catch
async def change_keyboard(chat_id: int,
                          message_id: int,
                          reply_markup: Optional[InlineKeyboardMarkup] = None
                          ) -> None:
    """Изменяет inline-клавиатуру в сообщении.

    Args:
        chat_id (int): id чата (пользователя).
        message_id (int): id сообщения с клавиатурой.
        reply_markup (Optional[InlineKeyboardMarkup]): Новая клавиатура.
            По умолчанию - None.
    """
    await bot.get_bot().edit_message_reply_markup(chat_id=chat_id,
                                                  message_id=message_id,
                                                  reply_markup=reply_markup)
