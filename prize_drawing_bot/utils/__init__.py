# -*- coding: utf-8 -*-
"""Полезные небольшие функции бота."""

# Это позволяет импортировать функции напрямую из модуля
# Вместо:   from utils._change_keyboard import change_keyboard
# Будет:    from utils import change_keyboard
from ._change_keyboard import change_keyboard  # noqa: F401
from ._delete_message import delete_message  # noqa: F401
from ._locales_list import get_locales_list, set_locales_list  # noqa: F401
