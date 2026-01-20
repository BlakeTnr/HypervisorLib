import sys
print(sys.path)

from Person import Person
from hypervisor.Hypervisor import Hypervisor
from messenger.Messenger import Messenger
from database.CourseRepository import SysSecRepository, Semester
from database.implementation.AWSDSQL import AWSDSQL

proxmox = Hypervisor()
mattermost = Messenger()
database = AWSDSQL("a", "a")

people: list[Person] = database.getSysSecStudents(Semester.SPRING, 2026)

for person in people:
    hypervisorAccount = proxmox.createAccount(person)
    hypervisorAccount.resetAndSendCredentials(person)