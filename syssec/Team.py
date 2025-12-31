from syssec.VM import VM
from Person import Person

class Team:
    members: list[Person] = []

    def __init__(self):
        pass

    def addPerson(self, person: Person):
        pass

    def removePerson(self, person: Person):
        pass

    def deployVM(self, vm: VM):
        vm.deployVM(self)