from abc import ABC, abstractmethod

from zkhbotapp.api.model.intent import UserIntent
from zkhbotapp.api.model.user_context import UserContext


class IntentClassifier(ABC):

    @abstractmethod
    def extract_intent(self, message: str, user_context: UserContext) -> UserIntent:
        """"""


class IntentClassifierImpl(IntentClassifier):

    def extract_intent(self, message: str, user_context: UserContext) -> UserIntent:
        return UserIntent.PickAddAddress
