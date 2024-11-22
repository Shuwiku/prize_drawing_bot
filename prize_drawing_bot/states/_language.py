# -*- coding: utf-8 -*-
"""Машина состояний смены языка пользователя."""

from aiogram.fsm.state import State, StatesGroup


class Language(StatesGroup):
    """Машина состояний смены языка пользователя."""

    confirm: State = State()
