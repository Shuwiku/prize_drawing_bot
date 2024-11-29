# -*- coding: utf-8 -*-
"""Фильтры aiogram для обработчиков бота."""

# Это позволяет импортировать классы напрямую из модуля
# Вместо:   from filters._callback_have_message import CallbackHaveMessage
# Будет:    from filters import CallbackHaveMessage
from ._callback_have_message import CallbackHaveMessage  # noqa: F401
from ._message_from_user import MessageFromUser  # noqa: F401
from ._user_registered import UserRegistered  # noqa: F401
