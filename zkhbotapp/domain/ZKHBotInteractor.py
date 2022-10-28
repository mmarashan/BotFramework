from abc import ABC

from zkhbotapp.domain.model.user import User


class ZKHInteractor(ABC):

    def on_new_house_address_create_intent(self, user: User):
        """callback for user intent add new house address"""