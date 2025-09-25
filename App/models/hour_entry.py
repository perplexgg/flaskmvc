from App.database import db
import datetime

class HourEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String, nullable=False)
    hours = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, default="pending")  # pending, approved, rejected
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
