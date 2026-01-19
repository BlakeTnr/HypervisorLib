from Person import Person
from hypervisor.Hypervisor import Hypervisor
from messenger.Messenger import Messenger
from database.CourseRepository import SysSecRepository, Semester

proxmox = Hypervisor()
mattermost = Messenger()
database = SysSecRepository()

people: list[Person] = database.getSysSecStudents(Semester.SPRING, 2026)

for person in people:
    hypervisorAccount = proxmox.createAccount(person)
    hypervisorAccount.resetAndSendCredentials(person)