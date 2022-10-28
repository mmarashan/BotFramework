from dataclasses import dataclass
from typing import Union

from bot_framework.model.message import InputMessage, OutputMessage


class BotApiAction:
    """ Action that bot should perform"""


@dataclass
class SendMessageAction(BotApiAction):
    output_message: OutputMessage


@dataclass
class ReplyToAction(BotApiAction):
    received_message: InputMessage
    output_message: OutputMessage
