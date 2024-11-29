# -*- coding: utf-8 -*-
"""Инструменты для создания и получения объектов бота, диспетчера и i18n."""

from pathlib import Path
from typing import Union

from . import _bot, _dispatcher, _i18n

# Это позволяет импортировать функции напрямую из модуля
# Вместо:   from bot._bot import get_bot
# Будет:    from bot import get_bot
from ._bot import get_bot  # noqa: F401
from ._dispatcher import get_dispatcher  # noqa: F401


def init(
    bot_token: str,
    locale_default: str,
    locales_path: Union[Path, str],
    parse_mode: str
) -> None:
    """Создаёт и настраивает объекты бота, диспетчера и интернационализации.

    Args:
        bot_token (str): Токен телеграм бота.
        locale_default (str): Локаль по умолчанию для новых пользователей.
        locales_path (str): Путь к файлам локализации "messages.ftl".
        parse_mode (str): Режим форматирования текста в сообщениях бота.
    """
    _bot.init(
        bot_token=bot_token,
        parse_mode=parse_mode
    )
    _dispatcher.init()
    _i18n.init(
        locale_default=locale_default,
        locales_path=str(locales_path)
    )
