# -*- coding: utf-8 -*-
"""Reply-клавиатура с меню бота."""

from aiogram_i18n import LazyProxy
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton


_keyboard: list[list[KeyboardButton]] = [
    [
        KeyboardButton(text=LazyProxy("button-profile")),
        KeyboardButton(text=LazyProxy("button-language"))
    ]
]
reply_menu = ReplyKeyboardMarkup(
    keyboard=_keyboard,
    resize_keyboard=True
)
