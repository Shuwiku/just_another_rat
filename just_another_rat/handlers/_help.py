# -*- coding: utf-8 -*-
"""Выводит список команд бота с их кратким описанием."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

import locale_


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["help"])
)
async def command_start(
    message: Message
) -> None:
    """Выводит список команд бота с их кратким описанием."""
    logger.debug("Обработчик:\tcommand_help")  # Логирование

    # Выводит справку по команде
    if message.text == "/help /?":
        await message.answer(text=locale_.HELP_DOC)
        return None

    await message.answer(text=locale_.HELP)
