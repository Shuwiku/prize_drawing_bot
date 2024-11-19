# -*- coding: utf-8 -*-
"""Обработчик команды начала диалога с ботом."""

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_i18n import I18nContext
from loguru import logger

from data import Database
from filters import MessageFromUser


router: Router = Router(name=__name__)


@router.message(CommandStart(),
                MessageFromUser())
async def cmd_start(message: Message,
                    database: Database,
                    i18n: I18nContext) -> None:
    """Выводит краткую информацию о боте."""
    logger.debug("Обработка команды \"start\".")
    await message.answer(text=i18n.get("start"))
    # Пользователя не в базе данных
    if not database.get_user(uid=message.from_user.id):  # type: ignore
        await message.answer(text=i18n.get("start-user-not-registered"))
