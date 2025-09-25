from App.database import db
from App.models.user import User

class Student(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    totalHours = db.Column(db.Float, default=0)

    accolades = db.relationship("Accolade", backref="student", lazy=True)
    hours = db.relationship("HourEntry", backref="student", lazy=True)

    __mapper_args__ = {
        'polymorphic_identity':'student',
    }

    def getAccolades(self):
        return [a.title for a in self.accolades]
