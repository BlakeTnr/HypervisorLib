from Person import Person
from syssec.Team import Team
from hypervisor.Hypervisor import Hypervisor
from messenger.Messenger import Messenger



proxmox = Hypervisor
mattermost = Messenger()

teams: list[Team] = []
for team in teams:
    team.deployVM()