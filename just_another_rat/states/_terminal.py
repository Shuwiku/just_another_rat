# -*- coding: utf-8 -*-
"""Машина состояний режима терминала."""

from aiogram.fsm.state import State, StatesGroup


class Terminal(StatesGroup):
    """Машина состояний режима терминала."""

    terminal_mode: State = State()
