# -*- coding: utf-8 -*-
"""Настраивает логирование бота."""

import sys
from pathlib import Path

from loguru import logger


def setup_logging(config: dict) -> None:
    """Настраивает логирование бота.

    Args:
        config (dict): Конфигурация логирования.
    """
    logger.remove()  # Убирает настройки по умолчанию
    logger.add(sink=sys.stderr, level=config["log_level"]["std"],
               format=config["log_format"])  # Вывод логов в терминал
    log_files_path: Path = Path(config["log_path"]).resolve()
    logger.add(sink=log_files_path, level=config["log_level"]["file"],
               format=config["log_format"])  # Запись логов в файл
    logger.trace("Логирование настроено.")  # Логирование
