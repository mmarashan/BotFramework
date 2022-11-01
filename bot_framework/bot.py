from abc import abstractmethod, ABC
from mailbox import Message

from bot_framework.bot_action_performer import BotActionPerformer
from bot_framework.model.sea.action import BotAction
from bot_framework.model.sea.event import BotEvent
from zkhbotapp.api.zkh_bot_api_model import BotModel


class Bot(ABC):
    """ Bot is abstraction. Implementation contains provider specific logic """

    __bot_model: BotModel = None
    __action_performer: BotActionPerformer = BotActionPerformer()

    def __init__(self, bot_model: BotModel):
        """ Your implementation should use this constructor"""
        self.__bot_model = bot_model
        self.__action_performer.set_delegate(self.perform)
        self.__bot_model.set_action_performer(self.__action_performer)

    @abstractmethod
    def launch(self):
        """launch bot"""

    @abstractmethod
    def perform(self, action: BotAction):
        """Perform output action to user (users)"""

    def on_new_event(self, event: BotEvent):
        """callback on input user event"""
        self.__bot_model.on_new_user_event(event)
