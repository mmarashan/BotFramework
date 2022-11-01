from typing import List

import telebot

from bot_framework.bot import Bot
from bot_framework.bot_model import BotModel
from bot_framework.model.message import InputMessage, OutputMessage
from bot_framework.model.sea.action import BotAction, ReplyToAction, SendMessageAction
from bot_framework.model.sea.event import NewMessage, StartChat
from bot_framework.model.user import BotUser
from telebot.types import Message, User, ReplyKeyboardMarkup, KeyboardButton


class TelegramBot(Bot):
    """
    Telegram implementation of bot
    """
    __bot: telebot.TeleBot = None

    def __init__(self, token: str, bot_model: BotModel):
        self.__bot = telebot.TeleBot(token=token, parse_mode=None)
        super().__init__(bot_model=bot_model)

    def perform(self, action: BotAction):
        if isinstance(action, ReplyToAction):
            input_message: InputMessage = action.received_message
            output_message: OutputMessage = action.output_message
            reply_markup = self.__extract_reply_markup(output_message)

            self.__bot.send_message(chat_id=input_message.chat_id,
                                    text=output_message.text,
                                    reply_to_message_id=input_message.id,
                                    reply_markup=reply_markup)

        if isinstance(action, SendMessageAction):
            output_message: OutputMessage = action.output_message
            reply_markup = self.__extract_reply_markup(output_message)

            self.__bot.send_message(chat_id=output_message.chat_id,
                                    text=output_message.text,
                                    reply_markup=reply_markup)

    def launch(self):

        def handle_messages(messages: List[Message]):
            for m in messages:
                message: Message = m
                from_user: User = message.from_user

                if message.text == '/start' or message.text == '/help':
                    self.on_new_event(
                        event=StartChat(
                            chat_id=message.chat.id,
                            user=BotUser(
                                id=from_user.id,
                                first_name=from_user.first_name,
                                last_name=from_user.last_name,
                                username=from_user.username
                            )
                        )
                    )
                    return
                self.on_new_event(
                    event=NewMessage(
                        message=InputMessage(
                            id=message.message_id,
                            from_user=BotUser(
                                id=from_user.id,
                                first_name=from_user.first_name,
                                last_name=from_user.last_name,
                                username=from_user.username
                            ),
                            text=message.text,
                            chat_id=message.chat.id
                        )
                    )
                )

        self.__bot.set_update_listener(handle_messages)
        self.__bot.infinity_polling()

    @staticmethod
    def __extract_reply_markup(output_message: OutputMessage):
        if len(output_message.answer_variances) > 0:
            markup = ReplyKeyboardMarkup(row_width=1)
            for answer_variance in output_message.answer_variances:
                btn = KeyboardButton(answer_variance.text)
                markup.add(btn, row_width=1)
            return markup
        else:
            return None
