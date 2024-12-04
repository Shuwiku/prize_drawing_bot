# -*- coding: utf-8 -*-
"""Reply-клавиатуры бота."""

# Это позволяет импортировать клавиатуры напрямую из модуля
# Вместо:   from keyboards.reply._menu import reply_menu
# Будет:    from keyboards.reply import reply_menu
from ._menu import reply_menu  # noqa: F401
