# -*- coding: utf-8 -*-
"""Prize Drawing Bot - телеграм-бот для выбора победителей в розыгрышах.

Создан с использованием фреймворка aiogram для взаимодействия с пользователем,
модуля sqlite3 для взаимодействия с базой данных, и ядра fluent для
интернационализации (i18n).

Автор: Shuwiku (shuwiku@gmail.com);
GitHub: github.com/Shuwiku/prize_drawing_bot;
Лицензия: MIT License.
"""

import asyncio
import json
from pathlib import Path

from loguru import logger

import bot
from setup import setup


CONFIG_FILE: str = "config.json"

# Чтение файла конфигурации
config_file_path: Path = Path(CONFIG_FILE).resolve()  # Абсолютный путь к файлу
with open(config_file_path, mode="r", encoding="utf-8") as f:
    config = json.load(f)
print("Файл конфигурации загружен.")  # "Логирование"

setup(config)  # Настройка бота
logger.info("Запуск диспетчера.")  # Логирование

# Запуск бота
asyncio.run(bot.get_dispatcher().start_polling(bot.get_bot()))
