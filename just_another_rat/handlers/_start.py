# -*- coding: utf-8 -*-
"""Обработчик команды начала диалога с ботом."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger


router: Router = Router(name=__name__)


@router.message(
    Command(commands=["start"])
)
async def command_start(
    message: Message
) -> None:
    """Выводит приветственное сообщение и краткую информацию о боте."""
    logger.debug("Обработчик:\tcommand_start")  # Логирование

    await message.answer(
        text="💻    *Just Another Rat*\n"
             "\n"
             "❗ Используйте данный софт исключительно в образовательных"
             " целях! Разработчик не несёт никакой ответственности за ваши"
             " действия!\n"
             "\n"
             "💡 Используйте команду */help*, чтобы вывести список"
             " доступных команд.\n"
             "\n"
             "🔗 Страница проекта на GitHub -"
             " [Just Another Rat](https://github.com/Shuwiku/just_another_rat)"
    )
