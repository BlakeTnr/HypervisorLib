from Person import Person
from syssec.Team import Team
from hypervisor.Hypervisor import Hypervisor
from messenger.Messenger import Messenger
from hypervisor.implementation.ProxmoxVM import ProxmoxVM


proxmox = Hypervisor()

people: list[Person] = []
for person in people:
    proxmox.createAccount(person)
    person