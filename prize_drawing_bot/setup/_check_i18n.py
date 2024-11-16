# -*- coding: utf-8 -*-
"""Проверка файлов интернационализации бота."""

# Мне немного сложно работать с этим, ибо по PyFluent довольно мало адекватной
# документации, поэтому большинство вопросов пришлось решать через ChatGPT.
# Возможно это можно сделать лучше, но я не знаю как.

import sys
from pathlib import Path
from typing import Union, Final

from fluent.syntax import ast, parse
from fluent.runtime import FluentLocalization, FluentResourceLoader
from loguru import logger


def __get_default_locale_keys(file_path: Union[Path, str]) -> list[str]:
    """Получает все ключи из файла локализации по умолчанию.

    Args:
        file_path (Union[pathlib.Path, str]): Путь к файлу локализации.

    Returns:
        list[str]: Ключи локализации.
    """
    with open(file_path, mode="r", encoding="utf-8") as f:
        locale_data: str = f.read()

    # Получает данные из файла
    resources: ast.Resource = parse(locale_data)

    # Сортирует данные. Оставляет только сообщения
    return [i.id.name for i in resources.body if isinstance(i, ast.Message)]


def __get_locales_list(locale_path: Union[Path, str]) -> list[str]:
    """Получает список локалей бота.

    Получает все поддиректории директории с локализацией.

    Args:
        locale_folders_path (Union[Path, str]): Путь к папке с локализацией.

    Returns:
        list[str]: Список локалей бота.
    """
    return [str(dir_.name) for dir_ in Path(locale_path).parent.iterdir()
            if dir_.is_dir()]


def check_i18n(locale_default: str,
               locale_path: Union[Path, str],
               ) -> None:
    """Проверяет файлы интернационализации бота.

    Args:
        locale_default (str): Локаль бота по умолчанию.
        locale_path (Union[Path, str]): Путь к папке с файлами локализации.
            Должно быть что-то по типу: "locales/{locale}".
    """
    # Логирование
    logger.trace(f"Проверка файлов локализации на основе: {locale_default}")

    # Путь к файлу с локализацией по умолчанию
    locale_default_folder: str = str(locale_path).format(locale=locale_default)
    locale_default_file: Path = Path(locale_default_folder) / "messages.ftl"

    # Если локаль по умолчанию отсутствует или нет файла messages.ftl
    if not locale_default_file.is_file():
        text: str = f"Файл локализации по пути: '{locale_default_file}' не " \
            "найден!"
        logger.error(text)  # Логирование
        sys.exit()

    # Ключи из файла локализации по умолчанию
    locale_keys: list[str] = __get_default_locale_keys(locale_default_file)

    # Загрузчик fluent
    loader: Final = FluentResourceLoader(str(locale_path))

    for locale in __get_locales_list(locale_path):
        i18n: FluentLocalization = \
            FluentLocalization([locale], ["messages.ftl"], loader)

        for key in locale_keys:

            if i18n.format_value(key) == key:
                text: str = f"В локализации '{locale}' не указан ключ '{key}'!"
                logger.warning(text)  # Логирование

    logger.trace("Файлы локализации проверены.")  # Логирование
