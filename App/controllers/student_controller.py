import click
from App.database import db
from App.models import Student, HourEntry

@click.command("request-hours")
@click.argument("student_id", type=int)
@click.argument("activity")
@click.argument("hours", type=float)
def request_hours(student_id, activity, hours):
    student = Student.query.get(student_id)
    if not student:
        print("Student not found")
        return
    entry = HourEntry(activity=activity, hours=hours, status="pending", student_id=student_id)
    db.session.add(entry)
    db.session.commit()
    print(f"{student.name} requested {hours}h for '{activity}'")
