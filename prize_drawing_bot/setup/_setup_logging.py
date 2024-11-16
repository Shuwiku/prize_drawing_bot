# -*- coding: utf-8 -*-
"""Настраивает логирование бота."""

import sys
from pathlib import Path

from loguru import logger


def setup_logging(log_format, log_level_file, log_level_std, log_path) -> None:
    """Настраивает логирование бота.

    Args:
        config (dict): Конфигурация логирования.
    """
    logger.remove()  # Убирает настройки по умолчанию
    # Вывод логов в терминал
    logger.add(sink=sys.stderr, level=log_level_std, format=log_format)
    # Запись логов в файл
    logger.add(sink=log_path, level=log_level_file, format=log_format)
    logger.trace("Логирование настроено.")  # Логирование
    logger.info(f"Путь к файлам журнала: {log_path}")  # Логирование
