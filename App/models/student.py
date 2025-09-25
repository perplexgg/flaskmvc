from App.models.user import User
from App.models.accolade import Accolade

class Student(User):
    def __init__(self, id, name, username):
        super().__init__(id, name, username)
        self.totalHours = 0
        self.accolades = []

    def getAccolades(self):
        return self.accolades

    def addHours(self, hours):
        self.totalHours += hours
        self.checkAccolades()

    def checkAccolades(self):
        milestones = [10, 25, 50]
        for m in milestones:
            if self.totalHours >= m and not any(a.title == f"{m} Hours" for a in self.accolades):
                accolade = Accolade(len(self.accolades)+1, f"{m} Hours", "Today")
                self.accolades.append(accolade)
