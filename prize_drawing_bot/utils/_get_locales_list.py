# -*- coding: utf-8 -*-
"""Функция, которая получает список локалей бота."""

from pathlib import Path
from typing import Union

from config import Config


__locales_list: list[str]


def get_locales_list(
) -> list[str]:
    """Получает список локалей бота.

    Получает все поддиректории директории с локализацией.

    Args:
        locale_folders_path (Union[Path, str]): Путь к папке с локализацией.

    Returns:
        list[str]: Список локалей бота.
    """
    global __locales_list

    try:
        return __locales_list
    except NameError:
        pass

    # TODO: Это костыль и он будет исправлен в будущем
    locale_path: Union[Path, str] = Config.locales_folder_path

    __locales_list = [
        str(dir_.name)
        for dir_ in Path(locale_path).parent.iterdir()
        if dir_.is_dir()
    ]
    return __locales_list
