import click
from App.database import db
from App.models import Staff, HourEntry, Student

@click.command("approve-hours")
@click.argument("entry_id", type=int)
@click.argument("status")
def approve_hours(entry_id, status):
    entry = HourEntry.query.get(entry_id)
    if not entry:
        print("Hour entry not found")
        return
    entry.status = status
    if status == "approved":
        student = Student.query.get(entry.student_id)
        student.totalHours += entry.hours
    db.session.commit()
    print(f"Hour entry {entry.id} marked as {status}")

@click.command("leaderboard")
def leaderboard():
    students = Student.query.order_by(Student.totalHours.desc()).all()
    for s in students:
        print(f"{s.name} - {s.totalHours}h ({s.getAccolades()})")
