# -*- coding: utf-8 -*-
"""Обработчик команды выводящей меню бота."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_i18n.context import I18nContext
from loguru import logger

from keyboards.reply import reply_menu


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["menu"])
)
async def command_menu(
    message: Message,
    i18n: I18nContext
) -> None:
    """Выводит меню бота с прикрепленной reply-клавиатурой."""
    logger.debug("Обработчик:\tcommand_menu")  # Логирование

    await message.answer(
        text=i18n.get("menu"),
        reply_markup=reply_menu
    )
