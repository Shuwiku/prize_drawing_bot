# -*- coding: utf-8 -*-
"""Настраивает бота перед его запуском."""

import asyncio
import os

import bot
import data
from config import Config, get_config
from ._check_i18n import check_i18n
from ._load_bot_token import load_bot_token
from ._setup_logging import setup_logging


def setup() -> None:
    """Настраивает бота перед его запуском.

    Args:
        config (dict): Конфигурация бота.
    """
    config: Config = get_config()

    # Настройка логирования
    setup_logging(log_format=config.log_format,
                  log_level_file=config.log_level_file,
                  log_level_std=config.log_level_std,
                  log_files_path=config.log_files_path)

    # Настройка базы данных
    data.init(database_file_path=config.database_file_path)

    # Получение токена бота и настройка бота, диспетчера и интернационализции
    bot_token: str = load_bot_token()
    bot.init(bot_token=bot_token,
             locale_path=config.locales_folder_path,
             locale_default=config.locale_default,
             parse_mode=config.parse_mode)

    # Проверка файлов локализации
    check_i18n(locale_default=config.locale_default,
               locale_path=config.locales_folder_path)

    # Это надо только для windows
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
