# -*- coding: utf-8 -*-
"""Функции для создания, настройки и получения объекта бота aiogram."""

from typing import Final

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from loguru import logger


__bot: Bot


def get_bot(
) -> Bot:
    """Возвращает объект бота aiogram.

    Returns:
        Bot: Объект бота.
    """
    return __bot


def init(
    bot_token: str,
    parse_mode: str
) -> None:
    """Создаёт и настраивает объект бота aiogram.

    Args:
        bot_token (str): Токен телеграм бота.
        parse_mode (str): Режим форматирования текста в сообщениях бота.
    """
    global __bot

    # Базовые настройки бота
    properties: Final = DefaultBotProperties(
        allow_sending_without_reply=False,
        link_preview_prefer_small_media=True,
        parse_mode=parse_mode
    )

    __bot = Bot(
        default=properties,
        token=bot_token
    )

    logger.trace("Объект бота создан.")  # Логирование
