# -*- coding: utf-8 -*-
"""Машина состояний подтверждения регистрации пользователя."""

from aiogram.fsm.state import State, StatesGroup


class Register(StatesGroup):
    """Машина состояний подтверждения регистрации пользователя."""

    confirm: State = State()
