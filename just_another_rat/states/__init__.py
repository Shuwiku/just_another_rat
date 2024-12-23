# -*- coding: utf-8 -*-
"""Машины состояний бота."""

# Это позволяет импортировать классы напрямую из модуля
# Вместо:   from states._terminal import Terminal
# Будет:    from states import Terminal
from ._terminal import Terminal  # noqa: F401
from ._upload import Upload  # noqa: F401
