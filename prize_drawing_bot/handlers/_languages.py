# -*- coding: utf-8 -*-
"""Обработчик команды, выводящей список локалей бота."""

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram_i18n.context import I18nContext
from loguru import logger

from filters import MessageFromUser
from utils import get_locales_list


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["languages"]),
    MessageFromUser(),
    StateFilter(None)
)
async def command_languages(
    message: Message,
    i18n: I18nContext,
) -> None:
    """Выводит список доступных локалей бота."""
    logger.debug("Обработчик:\tcommand_languages")  # Логирование
    await message.answer(
        text=i18n.get(
            "languages-list",
            languages=", ".join(get_locales_list())
        )
    )
