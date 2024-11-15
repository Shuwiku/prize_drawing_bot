# -*- coding: utf-8 -*-
"""Проверка файлов интернационализации бота."""

import sys
from pathlib import Path
from typing import Final

from fluent.syntax import ast, parse
from fluent.runtime import FluentLocalization, FluentResourceLoader
from loguru import logger


def __get_default_locale_keys(file_path: str) -> list[str]:
    """Получает все ключи из файла локализации по умолчанию.

    Args:
        file_path (str): Путь к файлу локализации.

    Returns:
        list[str]: Ключи локализации.
    """
    with open(file_path, mode="r", encoding="utf-8") as f:
        locale_data: str = f.read()
    resources: ast.Resource = parse(locale_data)
    keys: list[str] = [elem.id.name for elem in resources.body
                       if isinstance(elem, ast.Message)]
    return keys


def check_i18n(locale_default: str,
               locale_folders: str,
               ) -> None:
    """Проверяет файлы интернационализации бота.

    Args:
        locale_default (str): Локаль бота по умолчанию.
        locale_folders (str): Путь к папкам с файлами локализации messages.ftl.
    """
    text: str = f"Проверка файлов локализации на основе \"{locale_default}\"."
    logger.trace(text)
    locale_default_file: str = locale_folders.format(locale=locale_default) + \
        "/messages.ftl"
    locale_keys: list[str] = __get_default_locale_keys(locale_default_file)
    loader: Final = FluentResourceLoader(locale_folders)
    for locale in ["en", "ru"]:
        i18n: ... = FluentLocalization([locale], ["messages.ftl"], loader)
        for data in locale_keys:
            res = i18n.format_value(data)
            if res == data:
                text: str = \
                    f"В локализации '{locale}' не указан параметр '{data}'!"
                logger.warning(text)
    logger.trace("Файлы локализации проверены.")
