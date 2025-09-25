from App.models.user import User

class Staff(User):
    def __init__(self, id, name, username, department):
        super().__init__(id, name, username)
        self.department = department
