# -*- coding: utf-8 -*-
"""Обработчики для режима терминала."""

import os

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from loguru import logger

import locale_
from states import Terminal


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["terminal"]),
    StateFilter(None)
)
async def command_terminal(
    message: Message,
    state: FSMContext
) -> None:
    """Переводит бота в режим терминала."""
    logger.debug("Обработчик:\tcommand_terminal")  # Логирование

    # Выводит справку по команде
    if message.text == "/terminal /?":
        await message.answer(text=locale_.TERMINAL_DOC)
        return None

    await state.set_state(Terminal.terminal_mode)
    await message.answer(text=locale_.TERMINAL_1)
    logger.trace("Включен режим терминала.")  # Логирование


@router.message(
    Command("exit"),
    StateFilter(Terminal.terminal_mode)
)
async def command_exit(
    message: Message,
    state: FSMContext
) -> None:
    """Выходит из состояния терминала."""
    await state.clear()
    await message.answer(text=locale_.TERMINAL_2)
    logger.trace("Режим терминала выключен.")  # Логирование


@router.message(
    StateFilter(Terminal.terminal_mode)
)
async def terminal(
    message: Message
) -> None:
    """Выполняет команды администратора в терминале."""
    command: str = str(message.text)

    # Логирование
    logger.trace(f"Выполнение команды в режиме терминала: {command}")

    # Изменение поведения для команды "cd"
    if command.startswith("cd"):

        # Выводит текущую рабочую директорию
        if command == "cd":
            await message.answer(
                text=locale_.TERMINAL_3 % (command, os.getcwd())
            )
            return None

        # Пытается изменить рабочую директорию на указанную
        try:
            os.chdir(command[2:].strip())
            await message.answer(
                text=locale_.TERMINAL_3 % (command, os.getcwd())
            )

        # Скорее всего, администратор передал неверный путь
        except Exception:
            await message.answer(
                text=locale_.TERMINAL_3 % (command, locale_.CD_3)
            )

        return None

    result: str = os.popen(command).read().strip()

    # Если команда вернула хоть что-то
    if bool(result):
        await message.answer(
            text=locale_.TERMINAL_3 % (command, result)
        )

    else:
        await message.answer(
            text=locale_.TERMINAL_4 % (command)
        )
