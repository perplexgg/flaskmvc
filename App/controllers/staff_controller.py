from App.models.staff import Staff
from App.models.hour_entry import HourEntry
from App.controllers.student_controller import get_student

staff_members = []
hour_entries = []

def create_staff(id, name, username, department):
    staff = Staff(id, name, username, department)
    staff_members.append(staff)
    return staff

def log_hours(student_username, hours, activity, date):
    student = get_student(student_username)
    if not student:
        return None
    entry = HourEntry(activity, hours, date, student)
    hour_entries.append(entry)
    return entry

def approve_hours(entry_index):
    if 0 <= entry_index < len(hour_entries):
        entry = hour_entries[entry_index]
        entry.approve()
        return entry
    return None

def get_pending_entries():
    return [e for e in hour_entries if e.status == "pending"]
