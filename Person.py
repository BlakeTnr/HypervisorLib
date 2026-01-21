from messenger.Messenger import Messenger, MessengerType
from typing_extensions import deprecated

# Should be a sort of factory method

class Person:
    messenger: Messenger
    preferredMessenger: MessengerType

    def __init__(self, username):
        self.username = username
        self.messsenger = None

    @deprecated("Person shouldn't know about the messenger, use messenger.sendMessage instead")
    def sendMessage(self, message):
        self.messenger.sendMessage(self, message)

    @deprecated("Person shouldn't know about the messenger, use messenger.sendMessage instead")
    def setMessenger(self, messenger: Messenger):
        self.messenger = messenger