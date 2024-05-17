from dataclasses import dataclass
from enum import Enum

class Subscription(Enum):
    FREE = "free tier"
    PREMIUM = "premium tier"

@dataclass
class UserModel:

    id: int
    name: str
    subscription: Subscription
