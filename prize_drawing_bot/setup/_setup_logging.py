# -*- coding: utf-8 -*-
"""Настраивает логирование бота."""

import sys
from pathlib import Path
from typing import Union

from loguru import logger


def setup_logging(
    log_format: str,
    log_level_file: str,
    log_level_std: str,
    log_files_path: Union[Path, str]
) -> None:
    """Настраивает логирование бота.

    Args:
        log_format (str): Формат логирования.
        log_level_file (str): Уровень логирования для записи в файл.
        log_level_std (str): Уровень логирования для вывода в терминал.
        log_files_path (Union[Path, str]): Путь к файлам логов.
    """
    logger.remove()  # Убирает настройки по умолчанию
    logger.add(  # Вывод логов в терминал
        sink=sys.stderr,
        level=log_level_std,
        format=log_format
    )
    logger.add(  # Запись логов в файл
        sink=log_files_path,
        level=log_level_file,
        format=log_format
    )
    logger.trace("Логирование настроено.")  # Логирование
    logger.info("Путь к файлам журнала:")  # Логирование
    logger.info(f"$ {log_files_path}")  # Логирование
