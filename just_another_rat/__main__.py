# -*- coding: utf-8 -*-
"""Just Another Rat."""

import asyncio
import sys

from loguru import logger

import bot
import config
import handlers


async def main() -> None:
    """If __name__ == "__main__"."""
    # Настройка логирования
    logger.remove()
    logger.add(
        sink=sys.stderr,
        level=config.LOG_LEVEL,
        format=config.LOG_FORMAT
    )
    logger.add(
        sink=config.LOG_FILES_PATH,
        level=config.LOG_LEVEL,
        format=config.LOG_FORMAT
    )
    logger.trace("Логирование настроено.")  # Логирование

    # Настройка обработчиков
    handlers.init(
        handlers=config.HANDLERS,
        handlers_filename_pattern=config.HANDLERS_FILENAME_PATTERN,
        handlers_path=config.HANDLERS_DIR_PATH
    )

    # Настройка бота
    bot.init(
        bot_token=config.BOT_TOKEN,
        parse_mode=config.PARSE_MODE
    )

    logger.info("Запуск диспетчера.")  # Логирование

    # Запуск диспетчера
    await bot.get_dispatcher().start_polling(
        bot.get_bot(),
        skip_updates=True
    )


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
