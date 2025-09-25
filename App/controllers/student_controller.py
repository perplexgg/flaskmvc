from App.models import Student, HourEntry, Accolade
from App.database import db

def request_hours(student_id, activity, hours):
    entry = HourEntry(student_id=student_id, activity=activity, hours=hours)
    db.session.add(entry)
    db.session.commit()
    return entry

def view_leaderboard():
    students = Student.query.all()
    board = []
    for s in students:
        total = sum(e.hours for e in s.hours if e.status == "approved")
        board.append((s.name, total))
    return sorted(board, key=lambda x: x[1], reverse=True)

def view_accolades(student_id):
    student = Student.query.get(student_id)
    return student.getAccolades()