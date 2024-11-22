# -*- coding: utf-8 -*-
"""Обработчики команды/запроса, останавливающих машину состояний."""

from typing import Final

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n.context import I18nContext
from loguru import logger

from filters import CallbackHaveMessage, MessageFromUser
from utils import delete_message


router: Final[Router] = Router(name=__name__)


@router.message(
    Command(commands=["cancel"]),
    MessageFromUser()
)
async def command_cancel(
    message: Message,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """Останавливает машину состояний.

    Останавливает машину состояний и удаляет сообщение бота 
    с inline-клавиатурой.
    """
    logger.debug("Обработчик 'command_cancel'.")

    # Машина состояний НЕ запущена
    if not await state.get_state():
        return None

    await state.clear()  # Выключает машину состояний

    # Удаляет сообщение бота с inline-клавиатурой
    await delete_message(
        chat_id=message.from_user.id,  # type: ignore
        message_id=message.message_id - 1
    )

    await message.answer(text=i18n.get("action-canceled"))


@router.callback_query(
    F.data == "cancel",
    CallbackHaveMessage()
)
async def callback_cancel(
    callback: CallbackQuery,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """Останавливает машину состояний.

    Останавливает машину состояний и удаляет сообщение бота 
    с inline-клавиатурой.
    """
    logger.debug("Обработчик 'callback_cancel'.")

    if not await state.get_state():  # Машина состояний НЕ запущена
        return

    message: Message = callback.message  # type: ignore

    await state.clear()  # Выключает машину состояний
    await message.delete()  # Удаляет сообщение бота с inline-клавиатурой

    await message.answer(text=i18n.get("action-canceled"))
    await callback.answer(show_alert=False)
