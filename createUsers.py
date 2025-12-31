from Person import Person
from hypervisor.Hypervisor import Hypervisor
from messenger.Messenger import Messenger



proxmox = Hypervisor
mattermost = Messenger()

people: list[Person] = []
for person in people:
    hypervisorAccount = proxmox.createAccount(person)
    randomPassword = hypervisorAccount.setRandomPassword()
    person.sendMessage("Your new password is {randomPassword}")