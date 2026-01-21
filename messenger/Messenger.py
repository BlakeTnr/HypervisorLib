from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum

from abc import ABC

if TYPE_CHECKING:
    from Person import Person

class MessengerType(Enum):
    EMAIL = 1
    MATTERMOST = 2

class Messenger(ABC):
    def __init__(self):
        pass

    def sendMessage(self, person: Person, message: str):
        pass