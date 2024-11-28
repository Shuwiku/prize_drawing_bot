# -*- coding: utf-8 -*-
"""Функции для создания, настройки и получения объекта диспетчера aiogram."""

from aiogram import Dispatcher
from loguru import logger

from handlers import get_router_handlers
from middlewares import DatabaseMiddleware


__dispatcher: Dispatcher


def get_dispatcher(
) -> Dispatcher:
    """Возвращает объект диспетчера aiogram.

    Returns:
        Dispatcher: Объект диспетчера.
    """
    return __dispatcher


def init(
) -> None:
    """Создаёт и настраивает объект диспетчера aiogram."""
    global __dispatcher

    __dispatcher = Dispatcher()
    __dispatcher.include_router(router=get_router_handlers())

    # Мидлварь позволяет получать доступ к базе данных напрямую из обработчиков
    __dispatcher.update.outer_middleware.register(
        middleware=DatabaseMiddleware()
    )

    logger.trace("Объект диспетчера создан.")  # Логирование
