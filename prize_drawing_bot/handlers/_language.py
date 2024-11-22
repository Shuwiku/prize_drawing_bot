# -*- coding: utf-8 -*-
"""Обработчик состояний/команд смены языка в боте."""

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n.context import I18nContext
from loguru import logger

from filters import CallbackHaveMessage, MessageFromUser, UserRegistered
from keyboards.inline import inline_languages_list
from states import Language
from utils import change_keyboard, delete_message


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["language"]),
    StateFilter(None),
    UserRegistered()
)
async def command_language(
    message: Message,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """Даёт возможность пользователю сменить язык в боте.
    
    Настраивает машину состояний и отправляет пользователю сообщение с
    inline-клавиатурой со списком локалей бота.
    """
    logger.debug("Обработчик 'command_language'.")  # Логирование

    await state.set_state(Language.confirm)
    await message.answer(
        text=i18n.get("language-change"),
        reply_markup=inline_languages_list
    )


@router.callback_query(
    F.data.startswith("set_language_"),
    CallbackHaveMessage(),
    UserRegistered()
)
async def callback_language_change(
    callback: CallbackQuery,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """Пользователь выбрал язык.

    Устанавливает новую локаль и отключает машину состояний.
    """
    logger.debug("Обработчик 'callback_language_change'.")  # Логирование

    message: Message = callback.message  # type: ignore

    # Новая локаль пользователя
    language: str = callback.data[len("set_language_"):]  # type: ignore

    await state.clear()  # Отключает машину состояний

    # Убирает inline-клавиатуру из сообщения бота
    await change_keyboard(
        chat_id=callback.from_user.id,
        message_id=message.message_id,
        reply_markup=None
    )

    # Устанавливает новую локаль пользователю
    await i18n.set_locale(locale=language)

    await message.answer(text=i18n.get("language-change-successfully"))


@router.message(
    StateFilter(Language.confirm),
    MessageFromUser()
)
async def state_language_default(
    message: Message,
    i18n: I18nContext
) -> None:
    """Обработчик по умолчанию.

    Вызывается в случае, если пользователь по какой-либо причине не нажал на
    кнопку из inline-клавиатуры.
    """
    logger.debug("Обработчик 'state_language_default'.")  # Логирование

    # Удаляет сообщение бота с inline-клавиатурой
    await delete_message(
        chat_id=message.from_user.id,  # type: ignore
        message_id=message.message_id - 1
    )
    await message.answer(text=i18n.get("language-change-default"))

    # Повторно отправляет сообщение с inline-клавиатурой со списком локалей
    # По сути, то же самое что и вызов обработчика 'command_language'
    await message.answer(
        text=i18n.get("language-change"),
        reply_markup=inline_languages_list
    )
