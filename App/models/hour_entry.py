class HourEntry:
    def __init__(self, activity, hours, date, student):
        self.activity = activity
        self.hours = hours
        self.date = date
        self.student = student
        self.status = "pending"

    def approve(self):
        self.status = "approved"
        self.student.addHours(self.hours)

    def reject(self):
        self.status = "rejected"
