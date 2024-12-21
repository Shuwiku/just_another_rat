# -*- coding: utf-8 -*-
"""Команда, выводящая список директорий и файлов в текущей директории."""

import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

import locale_


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["dir"])
)
async def command_dir(
    message: Message
) -> None:
    """Выводит список директорий и файлов в текущей директории."""
    logger.debug("Обработчик:\tcommand_dir")  # Логирование

    # Выводит справку по команде
    if message.text == "/dir /?":
        await message.answer(text=locale_.DIR_DOC)
        return None

    await message.answer(text=locale_.DIR % os.popen("dir /b").read().strip())
