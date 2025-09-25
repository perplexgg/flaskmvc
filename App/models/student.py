from App.database import db
from .user import User

class Student(User):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    totalHours = db.Column(db.Float, default=0)

    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }

    def getAccolades(self):
        if self.totalHours >= 50:
            return "Gold"
        elif self.totalHours >= 25:
            return "Silver"
        elif self.totalHours >= 10:
            return "Bronze"
        return "No accolades yet"
