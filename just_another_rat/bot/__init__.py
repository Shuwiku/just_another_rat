# -*- coding: utf-8 -*-
"""Инструменты для создания и получения объектов бота и диспетчера."""

from . import _bot, _dispatcher

# Это позволяет импортировать функции напрямую из модуля
# Вместо:   from bot._bot import get_bot
# Будет:    from bot import get_bot
from ._bot import get_bot  # noqa: F401
from ._dispatcher import get_dispatcher  # noqa: F401


def init(
    bot_token: str,
    parse_mode: str
) -> None:
    """Создаёт и настраивает объекты бота и диспетчера.

    Args:
        bot_token (str): Токен телеграм бота.
        parse_mode (str): Режим форматирования текста в сообщениях бота.
    """
    _bot.init(
        bot_token=bot_token,
        parse_mode=parse_mode
    )
    _dispatcher.init()
