# -*- coding: utf-8 -*-
"""Обработчики событий бота."""

from typing import Final, List

from aiogram import Router

from . import (_register,
               _start)


__routers: Final[List[Router]] = [_register.router,
                                  _start.router]
router_handlers: Router = Router(name="router_handlers")
router_handlers.include_routers(*__routers)
