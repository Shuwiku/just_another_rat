# -*- coding: utf-8 -*-
"""Обработчик команды начала диалога с ботом."""

import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger


DESCRIPTION: str = \
    "*📄 Команда /dir*:\n\n" \
    "Выводит список файлов и каталогов в текущей директории.\n\n" \
    "*⚠️ Некоторые символы могут быть нечитаемыми из-за проблем с кодировкой.*"

router: Router = Router(name=__name__)


@router.message(
    Command(commands=["dir"])
)
async def command_dir(
    message: Message
) -> None:
    """Выводит приветственное сообщение и краткую информацию о боте."""
    logger.debug("Обработчик:\tcommand_dir")  # Логирование

    if message.text == "/dir /?":
        await message.answer(text=DESCRIPTION)
        return None

    result: str = os.popen("dir /b").read()

    await message.answer(
        text="*📁 Список файлов и каталогов:*\n\n"
             f"```Список\n"
             f"{result}"
             "```"
    )
