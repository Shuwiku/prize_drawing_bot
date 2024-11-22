# -*- coding: utf-8 -*-
"""Обработчик состояний/команд смены языка в боте."""

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n.context import I18nContext
from loguru import logger

from filters import CallbackHaveMessage, UserRegistered, MessageFromUser
from keyboards.inline import inline_languages_list
from states import Language

from utils import change_keyboard


router: Router = Router(name=__name__)


@router.message(
    Command("language"),
    UserRegistered(),
    StateFilter(None)
)
async def command_language(
    message: Message,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """Даёт возможность пользователю сменить язык в боте."""
    logger.debug("Обработка команды \"language\".")

    await state.set_state(Language.confirm)
    await message.answer(
        text=i18n.get("language-change"),
        reply_markup=inline_languages_list
    )


@router.callback_query(F.data.startswith("set_language_"))
@router.message(
    CallbackHaveMessage(),
    UserRegistered()
)
async def callback_language_change(
    callback: CallbackQuery,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """_summary_."""
    logger.debug("Пользователь изменил язык.")

    message: Message = callback.message  # type: ignore
    language: str = callback.data[len("set_language_"):]  # type: ignore
    await change_keyboard(
        chat_id=callback.from_user.id,
        message_id=message.message_id,
        reply_markup=None
    )
    await state.clear()
    await i18n.set_locale(locale=language)
    await message.answer(text=i18n.get("language-change-successfully"))


@router.message(
    MessageFromUser(),
    StateFilter(Language.confirm)
)
async def state_language_default(
    message: Message,
    i18n: I18nContext
) -> None:
    """_summary_."""
    logger.debug("Обработчик смены языка по умолчанию.")  # Логирование

    await change_keyboard(
        chat_id=message.from_user.id,  # type: ignore
        message_id=message.message_id - 1,
        reply_markup=None
    )
    await message.answer(text=i18n.get("user-registration-confirm-default"))

    # Повторно отправляет сообщение с подтверждением регистрации
    # По сути, то же самое что и /language
    await message.answer(
        text=i18n.get("language-change"),
        reply_markup=inline_languages_list
    )
