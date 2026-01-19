from HypervisorAccount import HypervisorAccount
from Person import Person

class ProxmoxAccount(HypervisorAccount):
    def __init__(self):
        pass

    def setRandomPassword(self):
        password = self.generateRandomPassword()
        # TODO Set password here
        pass

    def resetAndSendCredentials(self, person: Person):
        randomPassword = self.setRandomPassword()

        message = f"""Hello, here are your creds for https://cdr-vm.cse.buffalo.edu:8006/, which is our hypervisor platform.\n
            \n
            username: {self.getUsername()}\n
            password: {randomPassword}\n
            \n
            You can change your password by logging in, clicking you username in the top right, and clicking change password.
            """

        person.sendMessage(message)