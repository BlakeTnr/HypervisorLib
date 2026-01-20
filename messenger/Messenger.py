from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC

if TYPE_CHECKING:
    from Person import Person

class Messenger(ABC):
    def __init__(self):
        pass

    def sendMessage(self, person: Person, message: str):
        pass