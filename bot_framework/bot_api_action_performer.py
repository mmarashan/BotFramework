from typing import Callable

from bot_framework.model.sea.action import BotApiAction


class BotApiActionPerformer:
    __delegate: Callable = None

    def set_delegate(self, delegate: Callable):
        self.__delegate = delegate

    def perform(self, action: BotApiAction):
        """Perform output action to user (users)"""
        self.__delegate(action)
