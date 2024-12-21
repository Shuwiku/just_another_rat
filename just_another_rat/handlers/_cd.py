# -*- coding: utf-8 -*-
"""Команда для смены рабочей директории."""

import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

import locale_


router: Router = Router(name=__name__)


@router.message(Command(commands=["cd"]))
async def command_cd(message: Message) -> None:
    """Изменяет рабочую директорию на указанную."""
    logger.debug("Обработчик:\tcommand_cd")  # Логирование

    # Выводит справку по команде
    if message.text == "/cd /?":
        await message.answer(text=locale_.CD_DOC)
        return None

    # Выводит текущую рабочую директорию
    if message.text == "/cd":
        await message.answer(text=locale_.CD_1 % os.getcwd())
        return None

    # Пытается изменить рабочую директорию на указанную
    try:
        os.chdir(str(message.text)[3:].strip())
        await message.answer(text=locale_.CD_2 % os.getcwd())
        logger.trace(f"Директория изменена на: {os.getcwd()}")  # Логирование

    # Скорее всего, администратор передал неверный путь
    except Exception as e:
        await message.answer(text=locale_.CD_3)
        logger.error(e)  # Логирование
