# -*- coding: utf-8 -*-
"""Машины состояний бота."""

# Это позволяет импортировать классы напрямую из модуля
# Вместо:   from states._language import Language
# Будет:    from states import Language
from ._language import Language  # noqa: F401
from ._register import Register  # noqa: F401
