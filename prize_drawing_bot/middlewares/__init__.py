# -*- coding: utf-8 -*-
"""Мидлвари бота."""

# Это позволяет импортировать классы напрямую из модуля
# Вместо:   from middlewares._database import DatabaseMiddleware
# Будет:    from middlewares import DatabaseMiddleware
from ._database import DatabaseMiddleware  # noqa: F401
from ._i18n_manager import I18nMiddlewareManager  # noqa: F401
