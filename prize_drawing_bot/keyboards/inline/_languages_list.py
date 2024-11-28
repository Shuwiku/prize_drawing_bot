# -*- coding: utf-8 -*-
"""Inline-клавиатура со списком локалей бота."""

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import LazyProxy
from aiogram_i18n.types import InlineKeyboardButton

from utils import get_locales_list


_buttons: list[InlineKeyboardButton] = [
    InlineKeyboardButton(
        text=LazyProxy(f"locale-{i}"),
        callback_data=f"set_language_{i}"
    )
    for i in get_locales_list()
]

_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
_builder.row(
    *_buttons,
    InlineKeyboardButton(
        text=LazyProxy("button-cancel"),
        callback_data="cancel"
    ),
    width=1
)

inline_languages_list: InlineKeyboardMarkup = _builder.as_markup()
