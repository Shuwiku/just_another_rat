# -*- coding: utf-8 -*-
"""Обработчик команды начала диалога с ботом."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

import locale_


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["start"])
)
async def command_start(
    message: Message
) -> None:
    """Выводит приветственное сообщение и краткую информацию о боте."""
    logger.debug("Обработчик:\tcommand_start")  # Логирование

    # Выводит справку по команде
    if message.text == "/start /?":
        await message.answer(text=locale_.START_DOC)
        return None

    await message.answer(text=locale_.START)
