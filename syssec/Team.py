from hypervisor.VM import VM
from Person import Person
from hypervisor.Hypervisor import Hypervisor

class Team:
    members: list[Person] = []
    hypervisors: list[Hypervisor] = []

    def __init__(self):
        pass

    def addPerson(self, person: Person):
        # TODO Loop through hypervisor, push update
        pass

    def removePerson(self, person: Person):
        pass

    def deployVM(self, vm: VM):
        vm.deployVM(self)