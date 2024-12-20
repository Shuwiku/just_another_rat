# -*- coding: utf-8 -*-
"""Выполняет переданную команду и отправляет результат её выполнения."""

import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger


DESCRIPTION: str = \
    "*📄 Команда /execute*:\n\n" \
    "Выполняет переданную команду и отправляет результат её выполнения" \
    " (если он есть).\n\n" \
    "Например: `/execute cd`.\n\n" \
    "*⚠️ Некоторые символы могут быть нечитаемыми из-за проблем с кодировкой.*"

router: Router = Router(name=__name__)


@router.message(
    Command(commands=["execute"])
)
async def command_execute(
    message: Message
) -> None:
    """Выполняет переданную команду и отправляет результат её выполнения."""
    logger.debug("Обработчик:\tcommand_execute")  # Логирование

    if message.text == "/execute /?":
        await message.answer(text=DESCRIPTION)
        return None

    command: str = message.text[len("/execute"):].strip()  # pyright: ignore
    logger.trace(f"Выполнение команды: {command}")  # Логирование

    result: str = os.popen(command).read()
    logger.trace("Команда выполнена.")  # Логирование

    if bool(result):
        await message.answer(
            text="💻 Результат выполнения команды:\n\n"
                 "```Результат\n"
                 f"{result}"
                 "```"
        )

    else:
        await message.answer(
            text="✅ Команда была выполнена, но ничего не вернула."
        )
