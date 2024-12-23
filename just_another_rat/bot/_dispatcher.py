# -*- coding: utf-8 -*-
"""Функции для создания, настройки и получения объекта диспетчера aiogram."""

from aiogram import Dispatcher, Router
from loguru import logger

from handlers import get_router_handlers


__dispatcher: Dispatcher


async def get_dispatcher(
) -> Dispatcher:
    """Возвращает объект диспетчера aiogram.

    Returns:
        Dispatcher: Объект диспетчера.
    """
    return __dispatcher


async def init(
) -> None:
    """Создаёт и настраивает объект диспетчера aiogram."""
    global __dispatcher

    __dispatcher = Dispatcher()
    routers: Router = await get_router_handlers()
    __dispatcher.include_router(router=routers)

    logger.trace("Объект диспетчера создан.")  # Логирование
