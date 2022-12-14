from abc import ABC, abstractmethod
from typing import Union

from bot_framework.bot_api_action_performer import BotApiActionPerformer
from bot_framework.model.message import InputMessage
from bot_framework.model.sea.action import BotApiAction
from bot_framework.model.sea.event import BotEvent, NewMessage, StartChat
from bot_framework.model.user import BotUser


class BotApiModel(ABC):
    """
    "Presentation" logic - converting between business logic and bot api
    """

    __action_performer: BotApiActionPerformer

    def on_new_user_event(self, event: BotEvent):
        """callback on new user event"""
        if isinstance(event, NewMessage):
            self._on_new_input_message(event.message)
        if isinstance(event, StartChat):
            self._on_start_chat(event.chat_id, event.user)

    def set_action_performer(self, handler: BotApiActionPerformer):
        """Sets new action handler"""
        self.__action_performer = handler

    """ Methods for implementations """

    def _perform_action(self, action: BotApiAction):
        self.__action_performer.perform(action)

    @abstractmethod
    def _on_new_input_message(self, event: InputMessage):
        """callback on new user event"""

    @abstractmethod
    def _on_start_chat(self, chat_id: Union[int, str], event: BotUser):
        """callback on new user event"""
