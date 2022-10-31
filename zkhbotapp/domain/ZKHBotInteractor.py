from abc import ABC

from bot_framework.model.user import BotUser


class ZKHInteractor(ABC):

    def on_new_house_address_create_intent(self, user: BotUser):
        """callback for user intent add new house address"""
