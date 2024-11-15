# -*- coding: utf-8 -*-
"""Мидлварь для взаимодействия с базой данных."""

from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from data import Database, get_database


class DatabaseMiddleware(BaseMiddleware):
    """Мидлварь для взаимодействия с базой данных."""

    def __init__(self) -> None:
        """Инициализация мидлваря."""
        super().__init__()
        self.database: Database = get_database()

    async def __call__(self,
                       handler: Callable,
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Awaitable:
        """Выдаёт обработчику объект базы данных."""
        data["database"] = self.database
        return await handler(event, data)
