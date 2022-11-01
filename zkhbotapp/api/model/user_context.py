from dataclasses import dataclass
from typing import Union

from zkhbotapp.api.model.intent import UserIntent


@dataclass
class UserContext:
    user_id: Union[int, str]
    last_intent: UserIntent
