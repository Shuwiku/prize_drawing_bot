# -*- coding: utf-8 -*-
"""Обработчик состояний/команд смены языка в боте."""

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import LazyProxy
from aiogram_i18n.context import I18nContext
from loguru import logger

from filters import CallbackHaveMessage, MessageFromUser
from keyboards.inline import inline_languages_list
from keyboards.reply import reply_menu
from states import Language
from utils import change_keyboard, delete_message, get_locales_list


router: Router = Router(name=__name__)


async def set_language_by_argument(
    i18n: I18nContext,
    language: str,
    message: Message
) -> None:
    """Позволяет пользователю настроить локаль без inline-клавиатуры."""
    logger.debug("Обработчик:\tset_language_by_argument")

    # Проверка, что локаль, переданная пользователем, есть в списке
    if language not in get_locales_list():
        await message.answer(
            text=i18n.get(
                "language-not-found",
                language=language
            )
        )
        return None

    # Устанавливает новую локаль пользователю
    await i18n.set_locale(locale=language)
    await message.answer(
        text=i18n.get(
            "language-change-successfully",
            language=i18n.get(f"locale-{language}")
        ),
        reply_markup=reply_menu
    )


@router.message(
    F.text == LazyProxy("button-language"),
    StateFilter(None)
)
@router.message(
    Command(commands=["language"]),
    StateFilter(None)
)
async def command_language(
    message: Message,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """Даёт возможность пользователю сменить язык в боте.

    Настраивает машину состояний и отправляет пользователю сообщение с
    inline-клавиатурой со списком локалей бота, либо, если в сообщении
    пользователя есть дополнительные аргументы, может установить новую локаль
    без клавиатуры.
    """
    logger.debug("Обработчик:\tcommand_language")  # Логирование

    # Если пользователь написал сообщение по типу: "/locale ru"
    args: list[str] = message.text.split()  # type: ignore
    if len(args) > 1 and args[0] == "/language":
        return await set_language_by_argument(
            i18n=i18n,
            language=args[1],
            message=message
        )

    # В противном случае отправляем inline-клавиатуру с локалями бота
    # и настраиваем машину состояний
    await state.set_state(Language.confirm)
    await message.answer(
        text=i18n.get("language-change"),
        reply_markup=inline_languages_list
    )


@router.callback_query(
    F.data.startswith("set_language_"),
    CallbackHaveMessage()
)
async def callback_language_change(
    callback: CallbackQuery,
    i18n: I18nContext,
    state: FSMContext
) -> None:
    """Пользователь выбрал язык.

    Устанавливает новую локаль и отключает машину состояний.
    """
    logger.debug("Обработчик:\tcallback_language_change")  # Логирование

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

    await message.answer(
        text=i18n.get(
            "language-change-successfully",
            language=i18n.get(f"locale-{language}")
        ),
        reply_markup=reply_menu
    )


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
    logger.debug("Обработчик:\tstate_language_default")  # Логирование

    # Удаляет сообщение бота с inline-клавиатурой
    await delete_message(
        chat_id=message.from_user.id,  # type: ignore
        message_id=message.message_id - 1
    )
    await message.answer(
        text=i18n.get(
            "language-change-default",
            languages=", ".join(get_locales_list())
        )
    )

    # Повторно отправляет сообщение с inline-клавиатурой со списком локалей
    # По сути, то же самое что и вызов обработчика 'command_language'
    await message.answer(
        text=i18n.get("language-change"),
        reply_markup=inline_languages_list
    )
