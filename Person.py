from messenger.Messenger import Messenger

class Person:
    messenger: Messenger

    def __init__(self, username):
        self.username = username
        self.messsenger = None

    def sendMessage(self, message):
        self.messenger.sendMessage(self, message)

    def setMessenger(self, messenger: Messenger):
        self.messenger = messenger