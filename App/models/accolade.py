from App.database import db
from datetime import datetime

class Accolade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    title = db.Column(db.String, nullable=False)
    date_awardedOn = db.Column(db.DateTime, default=datetime.utcnow)
