# -*- coding: utf-8 -*-
"""Обработчик команды начала диалога с ботом."""

import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger


DESCRIPTION: str = \
    "*📄 Команда /cd*:\n\n" \
    "Меняет текущую рабочую директорию на указанную.\n" \
    "Используйте без аргументов (`/cd`), чтобы получить текущую директорию."

router: Router = Router(name=__name__)


@router.message(
    Command(commands=["cd"])
)
async def command_cd(
    message: Message
) -> None:
    """Выводит приветственное сообщение и краткую информацию о боте."""
    logger.debug("Обработчик:\tcommand_cd")  # Логирование

    if message.text == "/cd /?":
        await message.answer(text=DESCRIPTION)
        return None
    
    if message.text == "/cd":
        await message.answer(
            text="*📁 Текущая директория:*\n\n"
                 "```Директория\n"
                 f"{os.getcwd()}"
                 "```"
        )
        return None

    try:
        os.chdir(message.text[3:].strip())
        await message.answer(
            text="*📁 Установлена директория:*\n\n"
                 "```Директория\n"
                 f"{os.getcwd()}"
                 "```"
        )
    except Exception as e:
        await message.answer(
            text="*❌ Ошибка*\n\n"
                 "Вероятно такой директории не существует."
        )
