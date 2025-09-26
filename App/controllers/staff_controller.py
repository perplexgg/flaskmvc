# App/controllers/staff_controller.py
from App.models.staff import Staff
from App.models.hour_entry import HourEntry
from App.controllers.storage import load_data, save_data
from App.controllers.student_controller import get_student, add_hours_to_student

def create_staff(id, name, username, department):
    username = username.lower()
    data = load_data()
    data.setdefault("staff", [])
    # avoid duplicate usernames (simple behavior: overwrite if exists)
    for s in data["staff"]:
        if s.get("username") == username:
            s["id"] = str(id)
            s["name"] = name
            s["department"] = department
            save_data(data)
            return Staff(id, name, username, department)

    data["staff"].append({
        "id": str(id),
        "name": name,
        "username": username,
        "department": department
    })
    save_data(data)
    return Staff(id, name, username, department)


def log_hours(student_username, hours, activity, date):
    """
    Create a pending hour entry for a student; persist to disk and return a runtime HourEntry
    (with a Student object attached) for convenience.
    """
    if not student_username:
        return None
    student_username = student_username.lower()
    data = load_data()
    if student_username not in data.get("students", {}):
        return None

    try:
        hrs = float(hours)
    except Exception:
        return None

    data.setdefault("hour_entries", [])
    data["hour_entries"].append({
        "activity": activity,
        "hours": hrs,
        "date": date,
        "student_username": student_username,
        "status": "pending"
    })
    save_data(data)

    # Return a runtime HourEntry that wraps the Student object for CLI display
    student = get_student(student_username)
    entry = HourEntry(activity, hrs, date, student)
    entry.status = "pending"
    return entry


def get_pending_entries():
    """Return a list of HourEntry runtime objects for pending entries (student as Student object)."""
    data = load_data()
    pending = []
    for he in data.get("hour_entries", []):
        if he.get("status") == "pending":
            student = get_student(he["student_username"])
            entry = HourEntry(he.get("activity"), float(he.get("hours")), he.get("date"), student)
            entry.status = "pending"
            pending.append(entry)
    return pending


def approve_hours(entry_index):
    """
    Approve the nth pending entry. This function:
      1. Finds the pending entry in the current file snapshot
      2. Calls add_hours_to_student(...) which loads & saves the students (awarding accolades)
      3. Reloads the file and marks the specific hour_entry as 'approved' then saves again
    This avoids overwriting student updates.
    """
    data = load_data()
    entries = data.get("hour_entries", [])
    # indices of pending entries
    pending_indices = [i for i, e in enumerate(entries) if e.get("status") == "pending"]
    if entry_index < 0 or entry_index >= len(pending_indices):
        return None

    orig_idx = pending_indices[entry_index]
    entry = entries[orig_idx]

    # guard: must be pending
    if entry.get("status") != "pending":
        return None

    # 1) Add hours to student (this function loads & saves data internally)
    added = add_hours_to_student(entry["student_username"], float(entry["hours"]))
    if not added:
        return None

    # 2) Reload file and mark the same pending entry as approved (match on multiple fields)
    data2 = load_data()
    entries2 = data2.get("hour_entries", [])

    found_idx = None
    for i, e in enumerate(entries2):
        if (
            e.get("status") == "pending"
            and e.get("student_username") == entry["student_username"]
            and float(e.get("hours")) == float(entry["hours"])
            and e.get("activity") == entry["activity"]
            and e.get("date") == entry["date"]
        ):
            found_idx = i
            break

    # If we can't find it (unlikely) return a runtime object anyway
    if found_idx is None:
        student = get_student(entry["student_username"])
        return HourEntry(entry["activity"], float(entry["hours"]), entry["date"], student)

    entries2[found_idx]["status"] = "approved"
    data2["hour_entries"] = entries2
    save_data(data2)

    # Return a runtime HourEntry with the updated Student object
    student = get_student(entry["student_username"])
    approved_entry = HourEntry(entry["activity"], float(entry["hours"]), entry["date"], student)
    approved_entry.status = "approved"
    return approved_entry
