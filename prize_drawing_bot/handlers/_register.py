# -*- coding: utf-8 -*-
"""Обработчик состояний/команд регистрации в боте."""

from typing import Any

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InaccessibleMessage, Message
from aiogram_i18n import I18nContext
from loguru import logger

from data import Database
from filters import MessageFromUser
from keyboards.inline import inline_registration_confirm
from states import Register
from utils import remove_keyboard


router: Router = Router(name=__name__)


@router.message(Command("register"),
                MessageFromUser(),
                StateFilter(None))
async def cmd_register(message: Message,
                       database: Database,
                       i18n: I18nContext,
                       state: FSMContext
                       ) -> None:
    """Запрашивает подтверждение регистрации у пользователя.

    Запрашивает подтверждение регистрации у пользователя и
    переводит машину состояний в соответствующее состояние.
    """
    logger.debug("Обработка команды \"register\".")  # Логирование

    # Если пользователя нет в базе данных - настраиваем машину состояний и
    # запрашиваем у него подтверждение регистрации
    if not database.get_user(uid=message.from_user.id):  # type: ignore
        await state.set_state(state=Register.confirm)
        await message.answer(text=i18n.get("user-registration"),
                             reply_markup=inline_registration_confirm)
        return None

    await message.answer(text=i18n.get("user-registration-already-registered"))


@router.message(Register.confirm,
                MessageFromUser())
async def state_register_default(message: Message,
                                 i18n: I18nContext
                                 ) -> None:
    """Обработчик по умолчанию.

    Вызывается в случае, если пользователь по какой-либо причине не нажал на
    кнопку из inline-клавиатуры.
    """
    logger.debug("Обработчик регистрации по умолчанию.")  # Логирование
    await remove_keyboard(chat_id=message.from_user.id,  # type: ignore
                          message_id=message.message_id - 1)
    await message.answer(text=i18n.get("user-registration-confirm-default"))
    await message.answer(text=i18n.get("user-registration"),
                         reply_markup=inline_registration_confirm)


@router.callback_query(F.data == "register_cancel")
@router.message(Register.confirm)
async def btn_cal_register_cancel(callback: CallbackQuery,
                                  i18n: I18nContext,
                                  state: FSMContext
                                  ) -> None:
    """Пользователь отменил регистрацию.

    Отключает машину состояний.
    """
    logger.debug("Отмена регистрации.")  # Логирование
    message: Any[InaccessibleMessage, Message] = callback.message
    await state.clear()
    await remove_keyboard(chat_id=callback.from_user.id, 
                          message_id=message.message_id)
    await message.answer(text=i18n.get("user-registration-confirm-decline"))
    await callback.answer(show_alert=False)


@router.callback_query(F.data == "register_confirm")
@router.message(Register.confirm)
async def btn_state_register_confirm(callback: CallbackQuery,
                                     database: Database,
                                     i18n: I18nContext,
                                     state: FSMContext
                                     ) -> None:
    """Пользователь подтвердил регистрацию.

    Добавляет пользователя в базу данных.
    """
    logger.debug("Подтверждение регистрации.")  # Логирование
    message: Any[InaccessibleMessage, Message] = callback.message
    await state.clear()
    await remove_keyboard(chat_id=callback.from_user.id, 
                          message_id=message.message_id)
    database.add_user(uid=callback.from_user.id)
    logger.info("Зарегистрирован новый пользователь.")  # Логирование
    await message.answer(text=i18n.get("user-registration-confirm-accept"),
                         reply_markup=None)
