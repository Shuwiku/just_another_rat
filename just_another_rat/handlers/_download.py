# -*- coding: utf-8 -*-
"""Скачивает файл с устройства пользователя и отправляет администратору."""

from pathlib import Path

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from loguru import logger

import bot
import locale_


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["download"])
)
async def command_download(
    message: Message
) -> None:
    """Скачивает файл с устройства пользователя и отправляет администратору."""
    logger.debug("Обработчик:\tcommand_download")  # Логирование

    # Выводит справку по команде
    if message.text == "/download /?":
        await message.answer(text=locale_.DOWNLOAD_DOC)
        return None

    # Получает путь к файлу
    file_name: str = message.text[len("/download"):].strip()  # pyright: ignore
    file_path: Path = Path(file_name).resolve()

    # Файл не существует
    if not file_path.is_file():
        await message.answer(text=locale_.DOWNLOAD_1 % str(file_path))
        return None

    # Временное сообщение
    await message.answer(text=locale_.DOWNLOAD_2)

    logger.trace(f"Отправляю файл: {file_path}")  # Логирование

    await message.answer_document(
        document=FSInputFile(file_path),
        caption=locale_.DOWNLOAD_3
    )

    # Удаляет временное сообщение
    await bot.get_bot().delete_message(
        chat_id=message.from_user.id,  # pyright: ignore
        message_id=message.message_id + 1
    )
