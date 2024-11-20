# -*- coding: utf-8 -*-
"""Inline-клавиатура, отправляемая вместе с подтверждением регистрации."""

from typing import Final, Sequence

from aiogram_i18n import LazyProxy
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup


__keyboard: Sequence = [
    [
        InlineKeyboardButton(text=LazyProxy("btn-register"),
                             callback_data="register_confirm"),
        InlineKeyboardButton(text=LazyProxy("btn-cancel"),
                             callback_data="cancel")
    ]
]
inline_registration_confirm: Final = InlineKeyboardMarkup(
    inline_keyboard=__keyboard)
