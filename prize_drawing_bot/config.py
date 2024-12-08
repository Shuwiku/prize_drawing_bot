# -*- coding: utf-8 -*-
"""Загружает и обрабатывает данные из файла конфигурации бота."""

import json
import sys
from dataclasses import dataclass, fields, field
from pathlib import Path
from typing import Any, List


__config: "Config"
__config_data: dict
# Переменные конфигурации, которые являются путями.
# Этот список нужен для того, чтобы понять, к которым переменным надо
# применять Path(data).resolve(). Я просто не придумал ничего лучше.
__paths: list[str] = [
    "database_file_path",
    "locales_folder_path",
    "log_files_path"
]


@dataclass
class Config:
    """Конфигурация бота по умолчанию."""

    # Путь к папке скриптов бота
    _bot_path: Path = Path("prize_drawing_bot").resolve()

    # Путь к папке с обработчиками бота
    _bot_handlers_path: Path = _bot_path / "handlers"

    # Шаблон для имени файлов обработчиков бота
    _bot_handlers_filename_pattern: str = "_{handler_name}.py"

    # Путь к файлу базы данных
    database_file_path: Path = Path("database.sqlite3").resolve()

    # TODO: Мне не нравится текущая реализация этого, надо изменить
    # Формат даты регистрации пользователя в базе данных
    datetime_format: str = "%d-%m-%Y %H:%M"

    # Список используемых обработчиков бота
    handlers: List[str] = field(
        default_factory=lambda: [
            "cancel",
            "language",
            "register",
            "start"
        ]
    )

    # Локаль по умолчанию для новых пользователей
    locale_default: str = "ru"

    # Путь к файлам локализации
    locales_folder_path: Path = Path("locales/{locale}").resolve()

    # Формат логирования
    log_format: str = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>" \
        " | <level>{level: <8}</level> | <level>{message}</level>"

    # Минимальный уровень логирования для записи в файл
    log_level_file: str = "INFO"

    # Минимальный уровень логирования для вывода в консоль
    log_level_std: str = "TRACE"

    # Путь к файлам логов
    log_files_path: Path = Path("{time:YYYY.MM.DD HH-mm-ss}.log").resolve()

    # Режим форматирования текста в сообщениях бота
    parse_mode: str = "HTML"


def _set_config_data(
    field: str
) -> None:
    """Настраивает поле конфигурации.

    Пытается получить данные из загруженного файла конфигурации. В случае
    неудачи берёт значение по умолчанию.

    Args:
        field (str): Поле конфигурации. (__config_data[field] / Config.field).
    """
    if field.startswith("_"):
        return None

    data: Any = __config_data.get(field)

    # Если в файле конфигурации не указан параметр - использует
    # значение по умолчанию
    if not data or data is None:
        text: str = f"Не удалось получить значение из поля: \"{field}\"." \
            " Для этого поля будут применены настройки по умолчанию."
        print(text)  # "Логирование"
        data = getattr(Config, field)

    # Если параметр указан (см. проверку выше) и параметр находится в списке
    # параметров-путей - применяет Path(data).resolve()
    elif field in __paths:
        data = Path(data).resolve()

    setattr(__config, field, data)


def get_config(
) -> Config:
    """Возвращает объект конфигурации.

    Returns:
        config.Config: Объект конфигурации.
    """
    try:
        return __config
    except NameError:
        # "Логирование"
        print("Данные конфигурации были запрошены до загрузки файла.")
        sys.exit()


def load_config(
    file_name: str
) -> None:
    """Загружает данные из файла конфигурации.

    Args:
        file_name (str): Имя файла конфигурации.
    """
    global __config, __config_data

    # Абсолютный путь к файлу конфигурации
    file_path: Path = Path(file_name).resolve()
    print(f"Путь к файлу конфигурации: \n$ {file_path}")  # "Логирование"

    with open(file_path, mode="r", encoding="utf-8") as f:
        __config_data = json.load(f)

    __config = Config()
    for i in fields(Config):
        _set_config_data(i.name)

    print("Файл конфигурации загружен.")  # "Логирование"
