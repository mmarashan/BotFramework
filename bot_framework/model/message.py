from dataclasses import dataclass, field
from typing import Union, List

from bot_framework.model.user import BotUser


@dataclass
class InputMessage:
    """ Input message """
    id: Union[int, str]
    chat_id: Union[int, str]
    from_user: BotUser
    text: str


@dataclass
class AnswerVariance:
    text: str


@dataclass
class OutputMessage:
    """ Output; message """
    chat_id: Union[int, str]
    to_user: BotUser
    text: str
    answer_variances: List[AnswerVariance] = field(default_factory=list)
