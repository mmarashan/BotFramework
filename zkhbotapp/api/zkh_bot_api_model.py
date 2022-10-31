from typing import Union

from bot_framework.bot_api_model import BotApiModel
from bot_framework.model.message import InputMessage, OutputMessage, AnswerVariance
from bot_framework.model.sea.action import ReplyToAction, SendMessageAction
from bot_framework.model.user import BotUser


class ZKHBotApiModelImpl(BotApiModel):

    def _on_start_chat(self, chat_id: Union[int, str], user: BotUser):
        self._perform_action(
            action=SendMessageAction(
                output_message=OutputMessage(
                    text="Hi, " + user.first_name,
                    chat_id=chat_id,
                    to_user=user,
                    answer_variances=[AnswerVariance("a"), AnswerVariance("b"), AnswerVariance("c")]
                )
            )
        )

    def _on_new_input_message(self, message: InputMessage):
        self._perform_action(
            action=ReplyToAction(received_message=message,
                                 output_message=OutputMessage(
                                     text=message.text,
                                     chat_id=message.chat_id,
                                     to_user=message.from_user,
                                     answer_variances=[AnswerVariance("a"), AnswerVariance("b"), AnswerVariance("c")]
                                 )
                                 )
        )
