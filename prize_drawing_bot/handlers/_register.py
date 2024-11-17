# -*- coding: utf-8 -*-
"""Обработчик состояний/команд регистрации в боте."""

from typing import Any

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InaccessibleMessage, Message
from aiogram_i18n import I18nContext
from loguru import logger

from data import Database
from keyboards.inline import inline_registration_confirm
from states import Register
from utils import remove_keyboard


router: Router = Router(name=__name__)


@router.message(Command("register"))
async def cmd_register(message: Message,
                       database: Database,
                       i18n: I18nContext,
                       state: FSMContext
                       ) -> None:
    """Запрашивает подтверждение регистрации у пользователя.

    Запрашивает подтверждение регистрации у пользователя и
    переводит машину состояний в соответствующее состояние.
    """
    logger.debug("Обработка команды \"register\".")

    if not message.from_user:
        return None

    # Пользователь уже есть в базе данных
    if database.get_user(message.from_user.id):
        key = "user-registration-already-registered"
        await message.answer(text=i18n.get(key))

    # В противном случае переводим машину состояний
    else:
        await state.set_state(Register.confirm)
        await message.answer(text=i18n.get("user-registration"),
                             reply_markup=inline_registration_confirm)


@router.message(Register.confirm)
async def state_register_default(message: Message,
                                 i18n: I18nContext,
                                 state: FSMContext
                                 ) -> None:
    """Обработчик по умолчанию.

    Вызывается в случае, если пользователь по какой-либо причине не нажал на
    кнопку из inline-клавиатуры.
    """
    logger.debug("Обработчик регистрации по умолчанию.")
    await state.set_state(Register.confirm)
    await message.answer(text=i18n.get("user-registration-confirm-default"))


@router.callback_query(F.data == "register_cancel")
async def btn_cal_register_cancel(callback: CallbackQuery,
                                  i18n: I18nContext,
                                  state: FSMContext
                                  ) -> None:
    """Пользователь отменил регистрацию.

    Отключает машину состояний.
    """
    logger.debug("Отмена регистрации.")
    message: Any[InaccessibleMessage, Message] = callback.message
    await state.clear()
    await remove_keyboard(callback.from_user.id, message.message_id)
    await message.answer(text=i18n.get("user-registration-confirm-decline"))
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "register_confirm")
async def btn_state_register_confirm(callback: CallbackQuery,
                                     database: Database,
                                     i18n: I18nContext,
                                     state: FSMContext
                                     ) -> None:
    """Пользователь подтвердил регистрацию.

    Добавляет пользователя в базу данных.
    """
    logger.debug("Подтверждение регистрации.")
    message: Any[InaccessibleMessage, Message] = callback.message
    await state.clear()
    await remove_keyboard(callback.from_user.id, message.message_id)
    if message.from_user:
        database.add_user(callback.from_user.id)
        logger.info("Зарегистрирован новый пользователь.")
        key: str = "user-registration-confirm-accept"
        await message.answer(text=i18n.get(key),
                             reply_markup=None)
