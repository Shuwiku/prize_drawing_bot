# -*- coding: utf-8 -*-
"""Обработчик состояний/команд регистрации в боте."""

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext
from loguru import logger

from data import Database
from filters import CallbackHaveMessage, MessageFromUser
from keyboards.inline import inline_registration_confirm
from states import Register
from utils import change_keyboard, delete_message


router: Router = Router(name=__name__)


@router.message(
    Command("register"),
    MessageFromUser(),
    StateFilter(None)
)
async def command_register(
    message: Message,
    database: Database,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """Запрашивает подтверждение регистрации у пользователя"""
    logger.debug("Обработка команды \"register\".")  # Логирование

    # Если пользователя нет в базе данных - настраиваем машину состояний и
    # запрашиваем у него подтверждение регистрации
    if not database.get_user(uid=message.from_user.id):  # type: ignore
        await state.set_state(state=Register.confirm)
        await message.answer(
            text=i18n.get("user-registration"),
            reply_markup=inline_registration_confirm
        )
        return None

    await message.answer(text=i18n.get("user-registration-already-registered"))


@router.callback_query(F.data == "register_confirm")
@router.message(
    CallbackHaveMessage(),
    StateFilter(Register.confirm)
)
async def callback_state_register_confirm(
    callback: CallbackQuery,
    database: Database,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """Пользователь подтвердил регистрацию.

    Добавляет пользователя в базу данных и отключает машину состояний.
    """
    logger.debug("Пользователь подтвердил регистрацию.")  # Логирование

    message: Message = callback.message  # type: ignore

    await state.clear()
    await change_keyboard(
        chat_id=callback.from_user.id,
        message_id=message.message_id,
        reply_markup=None
    )
    database.add_user(uid=callback.from_user.id)
    await message.answer(
        text=i18n.get("user-registration-confirm-accept"),
        reply_markup=None
    )

    logger.info("Зарегистрирован новый пользователь.")  # Логирование


@router.message(
    MessageFromUser(),
    StateFilter(Register.confirm)
)
async def state_register_default(
    message: Message,
    i18n: I18nContext
) -> None:
    """Обработчик по умолчанию.

    Вызывается в случае, если пользователь по какой-либо причине не нажал на
    кнопку из inline-клавиатуры.
    """
    logger.debug("Обработчик регистрации по умолчанию.")  # Логирование

    await delete_message(
        chat_id=message.from_user.id,  # type: ignore
        message_id=message.message_id - 1
    )
    await message.answer(text=i18n.get("user-registration-confirm-default"))

    # Повторно отправляет сообщение с подтверждением регистрации
    # По сути, то же самое что и /register
    await message.answer(
        text=i18n.get("user-registration"),
        reply_markup=inline_registration_confirm
    )
