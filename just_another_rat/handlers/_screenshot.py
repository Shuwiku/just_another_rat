# -*- coding: utf-8 -*-
"""Обработчик команды создания снимка экрана пользователя."""

import os
from pathlib import Path

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from loguru import logger
from mss import mss

import locale_


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["screenshot"])
)
async def command_screenshot(
    message: Message
) -> None:
    """Делает снимок экрана пользователя и отправляет администратору."""
    logger.debug("Обработчик:\tcommand_screenshot")

    # Выводит справку по команде
    if message.text == "/screenshot /?":
        await message.answer(text=locale_.SCREENSHOT_DOC)
        return None

    screenshot_file: str = str(Path("image.png").resolve())

    # Делает снимок экрана пользователя
    with mss() as base:
        base.shot(output=screenshot_file)
    logger.trace("Снимок экрана создан.")  # Логирование

    await message.answer(text=locale_.SCREENSHOT)
    await message.answer_photo(photo=FSInputFile(path=screenshot_file))
    logger.trace("Снимок экрана отправлен администратору.")  # Логирование

    os.remove(screenshot_file)
    logger.trace("Снимок экрана удалён.")  # Логирование
