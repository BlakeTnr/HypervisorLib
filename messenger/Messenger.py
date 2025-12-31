from abc import ABC
from Person import Person

class Messenger(ABC):
    def __init__(self):
        pass

    def sendMessage(self, person: Person, message: str):
        pass