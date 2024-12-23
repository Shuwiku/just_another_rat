# -*- coding: utf-8 -*-
"""DOCSTRING."""

from aiogram.fsm.state import State, StatesGroup


class Upload(StatesGroup):
    """DOCSTRING."""

    get_file_name: State = State()
    upload_file: State = State()
