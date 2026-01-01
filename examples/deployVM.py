from Person import Person
from syssec.Team import Team
from hypervisor.Hypervisor import Hypervisor
from messenger.Messenger import Messenger
from hypervisor.implementation.ProxmoxVM import ProxmoxVM


proxmox = Hypervisor
mattermost = Messenger()

teams: list[Team] = []
for team in teams:
    vm = ProxmoxVM()
    team.deployVM(vm)