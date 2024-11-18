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

from loguru import logger

import bot
from config import load_config
from setup import setup


CONFIG_FILE: str = "config.json"

load_config(CONFIG_FILE)  # Чтение файла конфигурации
setup()  # Настройка бота
logger.info("Запуск диспетчера.")  # Логирование

asyncio.run(bot.get_dispatcher().start_polling(bot.get_bot(),  # Запуск бота
                                               skip_updates=True))
