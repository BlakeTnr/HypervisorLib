from Person import Person
from hypervisor.Hypervisor import Hypervisor
from messenger.Messenger import Messenger



proxmox = Hypervisor
mattermost = Messenger()

people: list[Person] = []
for person in people:
    person.sendMessage("Some mattermost instructions here...")
    # person.setMessenger(SomeMattermostMessengerHere)