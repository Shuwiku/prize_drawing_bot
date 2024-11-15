# -*- coding: utf-8 -*-
"""Обработчик для неизвестных команд."""

from aiogram import Router
from aiogram.types import Message
from aiogram_i18n import I18nContext
from loguru import logger


router: Router = Router(name=__name__)


@router.message()
async def default(message: Message,
                  i18n: I18nContext
                  ) -> None:
    """Обработчик для неизвестных команд.

    Вызывается в том случае, если сообщение пользователя
    не попало ни в какой другой обработчик.

    Добавлять его в роутер/диспетчер в последнюю очередь,
    чтобы он не перехватывал все сообщения!
    """
    logger.debug("Вызван обработчик по умолчанию.")  # Логирование
    await message.answer(text=i18n.get("default"))
