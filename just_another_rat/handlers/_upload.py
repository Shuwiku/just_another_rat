# -*- coding: utf-8 -*-
"""Загружает файл на устройство пользователя."""

import os
from pathlib import Path
from typing import BinaryIO, Optional

from aiogram import Bot, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import File, Message
from loguru import logger

import bot
import locale_
from states import Upload


file_path: Path = Path(".")
router: Router = Router(name=__name__)


@router.message(
    Command(commands=["upload"]),
    StateFilter(None)
)
async def command_upload(
    message: Message,
    state: FSMContext
) -> None:
    """Загружает файл на устройство пользователя."""
    logger.debug("Обработчик:\tcommand_upload")  # Логирование

    # Выводит справку по команде
    if message.text == "/upload /?":
        await message.answer(text=locale_.START_DOC)
        return None

    await state.set_state(Upload.get_file_name)
    await message.answer(text=locale_.UPLOAD_1)


@router.message(
    StateFilter(Upload.get_file_name)
)
async def get_file_name(
    message: Message,
    state: FSMContext
) -> None:
    """Запрашивает имя загружаемого файла."""
    global file_path

    file_path = Path(str(message.text)).resolve()

    try:
        with open(file_path, mode="w") as f:
            f.write("")
        os.remove(file_path)

    except Exception:
        await message.answer(text=locale_.UPLOAD_2 % file_path)
        return None

    await state.set_state(Upload.upload_file)
    await message.answer(text=locale_.UPLOAD_3)


@router.message(
    StateFilter(Upload.upload_file)
)
async def upload_file(
    message: Message,
    state: FSMContext
) -> None:
    """Загружает полученный файл на устройство пользователя."""
    file_id: Optional[str] = None

    if message.document:
        file_id = message.document.file_id

    if message.photo:
        file_id = message.photo[-1].file_id

    elif message.audio:
        file_id = message.audio.file_id

    elif message.video:
        file_id = message.video.file_id

    if file_id is None:
        await message.answer(text=locale_.UPLOAD_5)
        return None

    bot_: Bot = await bot.get_bot()
    file: File = await bot_.get_file(
        file_id=file_id
    )
    file_data: Optional[BinaryIO] = await bot_.download_file(
        file_path=str(file.file_path)
    )
    with open(file=file_path, mode="wb") as fb:
        fb.write(file_data.getvalue())  # pyright: ignore

    await state.clear()
    await message.answer(text=locale_.UPLOAD_4 % file_path)
