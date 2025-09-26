from datetime import date
from App.models.student import Student
from App.models.accolade import Accolade
from App.controllers.storage import load_data, save_data

MILESTONES = [10, 25, 50]

def create_student(id, name, username):
    username = username.lower()
    data = load_data()
    data.setdefault("students", {})
    data["students"][username] = {
        "id": id,
        "name": name,
        "username": username,
        "totalHours": 0.0,
        "accolades": []
    }
    save_data(data)
    return Student(id, name, username)

def get_student(username):
    if not username:
        return None
    username = username.lower()
    data = load_data()
    sd = data.get("students", {}).get(username)
    if not sd:
        return None
    s = Student(sd.get("id"), sd.get("name"), sd.get("username"))
    s.totalHours = float(sd.get("totalHours", 0.0))
    s.accolades = [Accolade(a.get("id"), a.get("title"), a.get("date_awardedOn")) for a in sd.get("accolades", [])]
    return s

def add_hours_to_student(username, hours):
    username = username.lower()
    data = load_data()
    students = data.setdefault("students", {})
    sd = students.get(username)
    if not sd:
        return False

    try:
        hours = float(hours)
    except Exception:
        return False

    sd["totalHours"] = float(sd.get("totalHours", 0.0)) + hours
    sd.setdefault("accolades", [])

    for m in MILESTONES:
        already = any(a.get("title") == f"{m} Hours" for a in sd["accolades"])
        if sd["totalHours"] >= m and not already:
            new_id = len(sd["accolades"]) + 1
            sd["accolades"].append({
                "id": new_id,
                "title": f"{m} Hours",
                "date_awardedOn": date.today().isoformat()
            })

    students[username] = sd
    data["students"] = students
    save_data(data)
    return True

def get_leaderboard():
    data = load_data()
    students = []
    for uname, sd in data.get("students", {}).items():
        s = Student(sd.get("id"), sd.get("name"), sd.get("username"))
        s.totalHours = float(sd.get("totalHours", 0.0))
        students.append(s)
    if not students:
        print("⚠️ No students found. Run 'flask init-data' first.")
    return sorted(students, key=lambda s: s.totalHours, reverse=True)

def view_accolades(username):
    username = username.lower()
    data = load_data()
    sd = data.get("students", {}).get(username)
    if not sd:
        return []
    return [Accolade(a.get("id"), a.get("title"), a.get("date_awardedOn")) for a in sd.get("accolades", [])]
