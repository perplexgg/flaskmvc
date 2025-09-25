from App.database import db
from datetime import datetime

class HourEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    activity = db.Column(db.String, nullable=False)
    hours = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, default="pending")  # pending/approved/rejected
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def approve(self, status="approved"):
        self.status = status
