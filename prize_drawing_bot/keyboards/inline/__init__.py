# -*- cofing: utf-8 -*-
"""Inline-клавиатуры бота."""

# Это позволяет импортировать клавиатуры напрямую из модуля
# Вместо:   from keyboards.inline._languages_list import inline_languages_list
# Будет:    from keyboards.inline import inline_languages_list
from ._languages_list import inline_languages_list  # noqa: F401
from ._registration_confirm import inline_registration_confirm  # noqa: F401
