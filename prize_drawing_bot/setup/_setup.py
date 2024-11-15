# -*- coding: utf-8 -*-
"""Настраивает бота перед его запуском."""

from pathlib import Path

import bot
import data
from ._check_i18n import check_i18n
from ._load_bot_token import load_bot_token
from ._setup_logging import setup_logging


def setup(config: dict) -> None:
    """Настраивает бота перед его запуском.

    Args:
        config (dict): Конфигурация бота.
    """
    # Настройка логирования
    setup_logging(config["logger"])

    # Настройка базы данных
    database_file_path: Path = Path(config["database_file"]).resolve()
    data.init(str(database_file_path))

    # Получение токена бота и настройка бота, диспетчера и интернационализции
    bot_token: str = load_bot_token()
    bot.init(bot_token, config["locale_folder"], locale_default="ru")

    # Проверка файлов локализации
    check_i18n(config["locale_default"], config["locale_folder"])
