# -*- coding: utf-8 -*-
"""Функции для создания и настройки интернационализации бота."""

from pathlib import Path
from typing import Union

from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores.fluent_runtime_core import FluentRuntimeCore
from loguru import logger

from ._dispatcher import get_dispatcher
from middlewares import I18nMiddlewareManager


def init(
    locale_default: str,
    locales_path: str
) -> None:
    """Создаёт и настраивает объект интернационализации aiogram.

    Args:
        locale_default (str): Локаль по умолчанию для новых пользователей.
        locales_path (str): Путь к файлам локализации "messages.ftl".
    """
    i18n = I18nMiddleware(
        core=FluentRuntimeCore(
            path=locales_path,
            raise_key_error=False
        ),
        default_locale=locale_default,
        manager=I18nMiddlewareManager()
    )
    i18n.setup(dispatcher=get_dispatcher())

    # Логирование
    logger.trace("Интернационализация настроена.")
    logger.info("Путь к файлам локализации:")
    logger.info(f"$ {Path(locales_path) / 'messages.ftl'}")
