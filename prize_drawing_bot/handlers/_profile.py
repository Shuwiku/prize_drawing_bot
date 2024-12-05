# -*- coding: utf-8 -*-
"""Обработчик команды/кнопки выводящих профиль пользователя."""

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, User
from aiogram_i18n import I18nContext, LazyProxy
from loguru import logger

from data import Database
from filters import MessageFromUser


router: Router = Router(name=__name__)


@router.message(
    F.text == LazyProxy("button-profile"),
    StateFilter(None)
)
@router.message(
    Command(commands=["profile"]),
    MessageFromUser()
)
async def command_profile(
    message: Message,
    database: Database,
    i18n: I18nContext
) -> None:
    """Выводит профиль пользователя."""
    logger.debug("Обработчик:\tcommand_profile")

    user: User = message.from_user  # type: ignore
    user_data: tuple = database.get_user(uid=user.id)  
    await message.answer(
        text=i18n.get(
            "profile",
            username=user.first_name,
            language=i18n.get(f"locale-{user_data[2]}"),
            draw_count=user_data[1],
            registration_date=user_data[3]
        )
    )
