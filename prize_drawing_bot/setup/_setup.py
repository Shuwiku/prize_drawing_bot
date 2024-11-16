# -*- coding: utf-8 -*-
"""Настраивает бота перед его запуском."""

from pathlib import Path

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
    setup_logging(config.log_format, config.log_level_file,
                  config.log_level_std, config.log_path)

    # Настройка базы данных
    data.init(str(config.database_file))

    # Получение токена бота и настройка бота, диспетчера и интернационализции
    bot_token: str = load_bot_token()
    bot.init(bot_token, str(config.locale_folder), config.locale_default)

    # Проверка файлов локализации
    check_i18n(config.locale_default, str(config.locale_folder))
