# -*- coding: utf-8 -*-
"""Обработчик команды начала диалога с ботом."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_i18n import I18nContext
from loguru import logger

from data import Database
from filters import MessageFromUser
from keyboards.reply import reply_menu


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["start"]),
    MessageFromUser()
)
async def command_start(
    message: Message,
    database: Database,
    i18n: I18nContext
) -> None:
    """Выводит краткую информацию о боте."""
    logger.debug("Обработчик:\tcommand_start")  # Логирование

    await message.answer(text=i18n.get("start"))
    await message.answer(
        text=i18n.get("menu"),
        reply_markup=reply_menu
    )

    # Добавляет пользователя в базу данных бота, если его там нет
    uid: int = message.from_user.id  # type: ignore
    if not database.get_user(uid=uid):
        database.add_user(uid=uid)
        logger.info(f"Добавлен новый пользователь: {uid}")  # Логирование
