# -*- coding: utf-8 -*-
"""Инструменты для настройки и получения обработчиков бота."""

import importlib
from pathlib import Path
from types import ModuleType

from aiogram import Router
from loguru import logger


__router_handlers: Router = Router(name="router_handlers")


def get_router_handlers(
) -> Router:
    """Возвращает объект роутера обработчиков aiogram.

    Returns:
        aiogram.Router: Объект роутера обработчиков aiogram.
    """
    return __router_handlers


def init(
    handlers: list[str],
    handlers_filename_pattern: str,
    handlers_path: Path
) -> None:
    """Настраивает обработчики бота.

    Использует только те обработчики, которые пользователь добавил в список
    в конфигурации бота.

    Args:
        handlers (list[str]): Список используемых обработчиков.
        handlers_filename_pattern (str): Шаблон названия файлов обработчиков.
        handlers_path (Path): Путь к папке с обработчиками бота.
    """
    global __router_handlers

    # Логирование
    logger.trace(f"Используемые обработчики: {', '.join(handlers)}")

    for i in handlers:

        handler_file: Path = handlers_path / handlers_filename_pattern.format(
            handler_name=i
        )
        # Проверяет существование файла с обработчиком
        if not handler_file.is_file():
            logger.error(f"Обработчик '{i}' не найден!")  # Логирование
            continue

        handler_module: ModuleType = importlib.import_module(
            name=f"{handlers_path.name}._{i}"
        )
        # Проверяет наличие переменной router в файле
        if not hasattr(handler_module, "router"):
            # Логирование
            logger.error(f"В обработчике '{i}' нет объекта роутера!")
            continue

        # Проверяет, что переменная router типа aiogram.Router
        if type(handler_module.router) is not Router:
            text: str = f"В обработчике '{i}' переменная роутера не " \
                "является типом aiogram.Router!"
            logger.error(text)  # Логирование
            continue

        __router_handlers.include_router(
            router=handler_module.router
        )

    logger.trace("Обработчики проверены.")  # Логирование
