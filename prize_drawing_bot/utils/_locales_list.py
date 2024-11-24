# -*- coding: utf-8 -*-
"""Функции для получения списка локалей бота."""

from pathlib import Path


__locales_list: list[str] = []


def get_locales_list(
) -> list[str]:
    """Возвращает список локалей бота

    Returns:
        list[str]: Список локалей бота.
    """
    return __locales_list


def set_locales_list(
    locale_folders_path: Path
) -> None:
    """Получает список локалей бота.

    Получает все поддиректории директории с локализацией и сохраняет список
    в закрытую переменную.

    Args:
        locale_folders_path (Path): Путь к папке с локализацией.
            Должно быть вида: "C://путь_к_папке/locales/{locale}"
    """
    global __locales_list

    __locales_list = [
        str(dir_.name)
        for dir_ in Path(locale_folders_path).parent.iterdir()
        if dir_.is_dir()
    ]
