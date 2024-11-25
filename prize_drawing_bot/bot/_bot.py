# -*- coding: utf-8 -*-
"""Инструменты для создания и получения объектов бота и диспетчера.

Создаёт и настраивает объекты бота, диспетчера и интернационализации (i18n),
а так же даёт доступ к ним (get_bot, get_dispatcher).
"""

from pathlib import Path
from typing import Final, Union

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores.fluent_runtime_core import FluentRuntimeCore
from loguru import logger

from handlers import get_router_handlers
from middlewares import DatabaseMiddleware, I18nMiddlewareManager


__bot: Bot
__dispatcher: Dispatcher


def get_bot(
) -> Bot:
    """Возвращает объект бота.

    Returns:
        aiogram.Bot: Объект бота aiogram.
    """
    return __bot


def get_dispatcher(
) -> Dispatcher:
    """Возвращает объект диспетчера.

    Returns:
        aiogram.Dispatcher: Объект диспетчера aiogram.
    """
    return __dispatcher


def init(
    bot_token: str,
    locale_default: str,
    locales_path: Union[Path, str],
    parse_mode: str
) -> None:
    """Создаёт и настраивает объекты бота, диспетчера и интернационализации.

    Args:
        bot_token (str): Токен телеграм бота.
        locale_default (str): Локаль по умолчанию для новых пользователей.
        locales_path (str): Путь к файлам локализации "messages.ftl".
        parse_mode (str): Режим форматирования текста в сообщениях бота.
    """
    global __bot, __dispatcher

    # Настройка бота
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

    # Настройка диспетчера
    __dispatcher = Dispatcher()
    __dispatcher.include_router(router=get_router_handlers())
    # Мидлварь позволяет получать доступ к базе данных напрямую из обработчиков
    __dispatcher.update.outer_middleware.register(
        middleware=DatabaseMiddleware()
    )

    logger.trace("Объект диспетчера создан.")  # Логирование

    # Настройка интернационализации (i18n)
    i18n = I18nMiddleware(
        core=FluentRuntimeCore(
            path=locales_path,
            raise_key_error=False
        ),
        default_locale=locale_default,
        manager=I18nMiddlewareManager()
    )
    i18n.setup(dispatcher=__dispatcher)

    # Логирование
    logger.trace("Интернационализация настроена.")
    logger.info("Путь к файлам локализации:")
    logger.info(f"$ {Path(locales_path) / 'messages.ftl'}")
