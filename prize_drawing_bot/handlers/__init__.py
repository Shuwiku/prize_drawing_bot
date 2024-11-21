# -*- coding: utf-8 -*-
"""Обработчики событий бота."""

import importlib
from typing import List

from aiogram import Router


# Это пока что первый вариант. В будущем это будет список в файле конфигурации
# бота. Это позволит чуть упростить настройку используемых обработчиков.
# Ещё надо что-то придумать с припиской "handler._". Посмотрим.
_handlers: dict = {}
_required_handlers = [
    "handlers._cancel",
    "handlers._language",
    "handlers._register",
    "handlers._start"
]
_routers: List[Router] = []
for i in _required_handlers:
    _handlers[i] = importlib.import_module(i)
    _routers.append(getattr(_handlers[i], "router"))

router_handlers: Router = Router(name="router_handlers")
router_handlers.include_routers(*_routers)
