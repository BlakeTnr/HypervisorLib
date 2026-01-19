from abc import ABC, abstractmethod
from enum import Enum
from Person import Person
from syssec.SysSecClass import SysSecClass

class Semester(Enum):
    FALL = 1
    SPRING = 2

class SysSecRepository(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def getSysSecStudents(self, semester: Semester, year: int) -> list[Person]:
        pass