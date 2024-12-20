# -*- coding: utf-8 -*-
"""Выполняет переданную команду и отправляет результат её выполнения."""

import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["execute"])
)
async def command_execute(
    message: Message
) -> None:
    """Выполняет переданную команду и отправляет результат её выполнения."""
    logger.debug("Обработчик:\tcommand_execute")  # Логирование

    command: str = message.text[len("/execute"):].strip()  # pyright: ignore
    logger.trace(f"Выполнение команды: {command}")  # Логирование

    result: str = os.popen(command).read()
    logger.trace("Команда выполнена.")  # Логирование

    if bool(result):
        await message.answer(text="💻 Результат выполнения команды:")
        await message.answer(text=result, parse_mode=None)

    else:
        await message.answer(
            text="✅ Команда была выполнена, но ничего не вернула."
        )
