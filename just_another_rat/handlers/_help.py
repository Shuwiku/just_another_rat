# -*- coding: utf-8 -*-
"""Обработчик команды начала диалога с ботом."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger


DESCRIPTION: str = \
    "*📄 Команда /help*:\n\n" \
    "Выводит список всех команд бота и их краткое описание."

router: Router = Router(name=__name__)


@router.message(
    Command(commands=["help"])
)
async def command_start(
    message: Message
) -> None:
    """Выводит приветственное сообщение и краткую информацию о боте."""
    logger.debug("Обработчик:\tcommand_help")  # Логирование

    if message.text == "/help /?":
        await message.answer(text=DESCRIPTION)
        return None

    await message.answer(
        text="*📁 /dir*\n"
             "Получить список файлов и каталогов.\n\n"
             "*💻 /execute*\n"
             "Выполнить переданную команду.\n\n"
             "*⚙️ /help*\n"
             "Вывести список команд бота.\n\n"
             "*🖼️ /screenshot*\n"
             "Сделать снимок экрана пользователя.\n\n"
             "*⚙️ /start*\n"
             "Начать диалог с ботом.\n\n"
             "Используйте аргумент `/?`, чтобы получить более подробную"
             " справку по команде. Например: `/help /?`"
    )
