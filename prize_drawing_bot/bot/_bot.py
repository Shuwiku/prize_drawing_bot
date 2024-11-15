# -*- coding: utf-8 -*-
"""Инструменты для создания и получения объектов бота и диспетчера.

Создаёт и настраивает объекты бота, диспетчера и интернационализации (i18n),
а так же даёт доступ к ним (get_bot, get_dispatcher).
"""

from typing import Final

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores.fluent_runtime_core import FluentRuntimeCore
from loguru import logger

from middlewares import DatabaseMiddleware, I18nMiddlewareManager
from handlers import router_handlers


__bot: Bot
__dispatcher: Dispatcher


def get_bot() -> Bot:
    """Возвращает объект бота.

    Returns:
        aiogram.Bot: Объект бота aiogram.
    """
    return __bot


def get_dispatcher() -> Dispatcher:
    """Возвращает объект диспетчера.

    Returns:
        aiogram.Dispatcher: Объект диспетчера aiogram.
    """
    return __dispatcher


def init(bot_token: str,
         locale_path: str,
         locale_default: str = "en"
         ) -> None:
    """Создаёт и настраивает объекты бота, диспетчера и интернационализации.

    Args:
        bot_token (str): Токен телеграм бота.
        locale_path (str): Путь к файлам локализации "messages.ftl".
        locale_default (str): Локаль по умолчанию для новых пользователей.
            По умолчанию - "en".
    """
    global __bot, __dispatcher

    # Настройка бота
    properties: Final = DefaultBotProperties(
        allow_sending_without_reply=False,
        link_preview_prefer_small_media=True,
        parse_mode=ParseMode.HTML
    )
    __bot = Bot(bot_token, default=properties)

    # Настройка диспетчера
    __dispatcher = Dispatcher()
    __dispatcher.include_router(router_handlers)  # Загрузка обработчиков
    # Мидлварь позволяет получать доступ к базе данных напрямую из обработчиков
    __dispatcher.update.outer_middleware.register(DatabaseMiddleware())

    # Логирование
    logger.trace("Объекты бота и диспетчера созданы и настроены.")

    # Настройка интернационализации (i18n)
    i18n = I18nMiddleware(core=FluentRuntimeCore(path=locale_path),
                          manager=I18nMiddlewareManager(),
                          default_locale=locale_default)
    i18n.setup(dispatcher=__dispatcher)

    logger.trace("Интернационализация настроена.")  # Логирование
