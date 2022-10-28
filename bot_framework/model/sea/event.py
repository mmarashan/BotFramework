from abc import ABC
from dataclasses import dataclass
from typing import Union

from bot_framework.model.message import InputMessage
from bot_framework.model.user import BotUser


class BotEvent(ABC):
    """ External event from user to bot """


@dataclass
class StartChat(BotEvent):
    chat_id: Union[int, str]
    user: BotUser


@dataclass
class NewMessage(BotEvent):
    message: InputMessage
