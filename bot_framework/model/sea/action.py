from dataclasses import dataclass

from bot_framework.model.message import InputMessage, OutputMessage


class BotAction:
    """ Action that bot should perform"""


@dataclass
class SendMessageAction(BotAction):
    output_message: OutputMessage


@dataclass
class ReplyToAction(BotAction):
    received_message: InputMessage
    output_message: OutputMessage
