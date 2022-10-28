from dataclasses import dataclass
from typing import Union

from bot_framework.model.user import BotUser


@dataclass
class InputMessage:
    """ Input message """
    id: Union[int, str]
    chat_id: Union[int, str]
    from_user: BotUser
    text: str


@dataclass
class OutputMessage:
    """ Output; message """
    chat_id: Union[int, str]
    to_user: BotUser
    text: str
