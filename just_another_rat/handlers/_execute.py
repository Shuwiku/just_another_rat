# -*- coding: utf-8 -*-
"""Выполняет переданную команду и отправляет результат её выполнения."""

import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

import locale_


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["execute"])
)
async def command_execute(
    message: Message
) -> None:
    """Выполняет переданную команду и отправляет результат её выполнения."""
    logger.debug("Обработчик:\tcommand_execute")  # Логирование

    # Выводит справку по команде
    if message.text == "/execute /?":
        await message.answer(text=locale_.EXECUTE_DOC)
        return None

    command: str = message.text[len("/execute"):].strip()  # pyright: ignore
    logger.trace(f"Выполнение команды: {command}")  # Логирование

    result: str = os.popen(command).read().strip()

    # Если команда вернула хоть что-то
    if bool(result):
        await message.answer(text=locale_.EXECUTE_1 % result)

    else:
        await message.answer(text=locale_.EXECUTE_2)
