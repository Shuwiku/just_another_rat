# -*- coding: utf-8 -*-
"""Конфигурация бота."""

from pathlib import Path


_bot_dir: Path = Path("just_another_rat").resolve()

# Настройки бота
BOT_TOKEN: str = "BOT_TOKEN_HERE"
HANDLERS: list[str] = [
    "cd",
    "dir",
    "execute",
    "help",
    "start",
    "screenshot"
]
HANDLERS_FILENAME_PATTERN: str = "_{handler_name}.py"
HANDLERS_DIR_PATH: Path = _bot_dir / "handlers"
PARSE_MODE: str = "Markdown"

# Логирование
LOG_FILES_PATH: str = str(_bot_dir / "logs.log")
LOG_FORMAT: str = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> |" \
                  " <level>{level: <8}</level> | <level>{message}</level>"
LOG_LEVEL: str = "TRACE"
