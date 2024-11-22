# -*- coding: utf-8 -*-
"""Обработчики команды/запроса, останавливающих машину состояний."""

from typing import Final

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram_i18n.context import I18nContext

from filters import CallbackHaveMessage, MessageFromUser
from utils import delete_message


router: Final[Router] = Router(name=__name__)


@router.message(
    Command("cancel"),
    MessageFromUser()
)
async def command_cancel(
    message: Message,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """Останавливает машину состояний."""
    if not await state.get_state():  # Машина состояний запущена
        return None

    await state.clear()
    await delete_message(
        chat_id=message.from_user.id,  # type: ignore
        message_id=message.message_id - 1
    )
    await message.answer(text=i18n.get("action-canceled"))


@router.callback_query(F.data == "cancel")
@router.message(CallbackHaveMessage())
async def callback_cancel(
    callback: CallbackQuery,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """Останавливает машину состояний.

    Останавливает машину состояний и убирает inline-клавиатуру.
    """
    if not await state.get_state():  # Машина состояний не запущена
        return

    message: Message = callback.message  # type: ignore

    await message.delete()
    await message.answer(text=i18n.get("action-canceled"))

    await state.clear()
    await callback.answer(show_alert=False)
