from syssec.Team import Team
from abc import ABC

# TODO Should be a factory method

# Maybe this should be abstract class?

class VM(ABC):
    hidden: bool # This maybe shouldn't be here since hidden is a syssec concept

    def __init__(self):
        pass

    def deployVM(self, team: Team):
        pass