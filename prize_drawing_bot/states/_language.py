# -*- coding: utf-8 -*-
"""Docstring."""

from aiogram.fsm.state import State, StatesGroup


class Language(StatesGroup):
    """Docstring."""

    confirm: State = State()
