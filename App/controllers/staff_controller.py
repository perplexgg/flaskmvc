from App.models import HourEntry, Student
from App.database import db

def log_hours(student_id, activity, hours, staff_name):
    entry = HourEntry(student_id=student_id, activity=activity, hours=hours, status="approved")
    db.session.add(entry)
    student = Student.query.get(student_id)
    student.totalHours += hours
    db.session.commit()
    return entry

def approve_hours(entry_id, status="approved"):
    entry = HourEntry.query.get(entry_id)
    if entry:
        entry.approve(status)
        student = Student.query.get(entry.student_id)
        if status == "approved":
            student.totalHours += entry.hours
        db.session.commit()
        return entry
    return None
