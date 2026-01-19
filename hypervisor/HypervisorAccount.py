# Should probably be factory method
# because the initialization process is complex
from Person import Person

class HypervisorAccount:
    username: str

    def __init__(self):
        pass

    def setRandomPassword(self):
        pass

    def getUsername(self) -> str:
        return self.username

    def generateRandomPassword(self) -> str:
        # TODO: Implement here
        return "someRandomPassword"

    def resetAndSendCredentials(self, person: Person):
        pass