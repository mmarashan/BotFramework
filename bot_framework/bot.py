from abc import abstractmethod, ABC
from mailbox import Message

from bot_framework.bot_api_action_performer import BotApiActionPerformer
from bot_framework.model.sea.action import BotApiAction
from bot_framework.model.sea.event import BotEvent
from zkhbotapp.api.zkh_bot_api_model import BotApiModel


class Bot(ABC):
    """ Bot is abstraction. Implementation contains provider specific logic """

    __bot_api_model: BotApiModel = None
    __action_performer: BotApiActionPerformer = BotApiActionPerformer()

    def __init__(self, bot_api_model: BotApiModel):
        """ Your implementation should use this constructor"""
        self.__bot_api_model = bot_api_model
        self.__action_performer.set_delegate(self.perform)
        self.__bot_api_model.set_action_performer(self.__action_performer)

    @abstractmethod
    def launch(self):
        """launch bot"""

    @abstractmethod
    def perform(self, action: BotApiAction):
        """Perform output action to user (users)"""

    def on_new_event(self, event: BotEvent):
        """callback on input user event"""
        self.__bot_api_model.on_new_user_event(event)
