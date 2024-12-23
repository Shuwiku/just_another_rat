# -*- coding: utf-8 -*-
"""Инструменты для настройки и получения обработчиков бота."""

import importlib
from pathlib import Path
from types import ModuleType

from aiogram import Router
from loguru import logger


__router_handlers: Router = Router(name="router_handlers")


async def get_router_handlers(
) -> Router:
    """Возвращает объект роутера обработчиков aiogram.

    Returns:
        aiogram.Router: Объект роутера обработчиков aiogram.
    """
    return __router_handlers


async def init(
    handlers: list[str],
    handlers_path: Path
) -> None:
    """Настраивает обработчики бота.

    Использует только те обработчики, которые пользователь добавил в список
    в конфигурации бота.

    Args:
        handlers (list[str]): Список используемых обработчиков.
        handlers_filename_pattern (str): Шаблон названия файлов обработчиков.
        handlers_path (Path): Путь к папке с обработчиками бота.
    """
    global __router_handlers

    # Логирование
    logger.trace(f"Используемые обработчики:")
    for i in handlers:
        logger.trace(f"$ {i}")

    for i in handlers:

        handler_module: ModuleType = importlib.import_module(
            name=f"{handlers_path.name}._{i}"
        )

        __router_handlers.include_router(
            router=handler_module.router
        )

    logger.trace("Обработчики проверены.")  # Логирование
