# -*- coding: utf-8 -*-
"""Загружает токен бота из переменных окружения."""

import os
import sys
from dotenv import load_dotenv
from typing import Optional

from loguru import logger


def load_bot_token(
) -> str:
    """Загружает токен бота из переменных окружения.

    Returns:
        str: Токен бота.
    """
    load_dotenv()  # Загружает файл ".env"
    bot_token: Optional[str] = os.getenv("BOT_TOKEN")
    if not bot_token or not bot_token.strip():
        logger.error("Токен бота не указан!")  # Логирование
        sys.exit()
    return bot_token
