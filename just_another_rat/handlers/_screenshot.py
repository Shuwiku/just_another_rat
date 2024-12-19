# -*- coding: utf-8 -*-
"""Обработчик команды создания снимка экрана пользователя."""

import os
from pathlib import Path

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from loguru import logger
from mss import mss


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["screenshot"])
)
async def command_screenshot(
    message: Message
) -> None:
    """Делает снимок экрана пользователя и отправляет администратору."""
    logger.debug("Обработчик:\tcommand_screenshot")

    screenshot_file: str = str(Path("image.png").resolve())

    with mss() as base:
        base.shot(output=screenshot_file)
    logger.trace("Снимок экрана создан.")  # Логирование

    await message.answer(text="🖼️ Снимок экрана успешно создан!")
    await message.answer_photo(photo=FSInputFile(path=screenshot_file))
    logger.trace("Снимок экрана отправлен администратору.")  # Логирование

    os.remove(screenshot_file)
    logger.trace("Снимок экрана удалён.")  # Логирование
