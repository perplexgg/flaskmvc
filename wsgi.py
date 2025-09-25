from App.main import app
from App.controllers import student_controller, staff_controller

@app.cli.command("init-data")
def init_data():
    from App.controllers.initialize import initialize
    initialize()

@app.cli.command("create-student")
def create_student():
    id = input("Student ID: ")
    name = input("Name: ")
    username = input("Username: ")
    student_controller.create_student(id, name, username)
    print("Student created!")

@app.cli.command("create-staff")
def create_staff():
    id = input("Staff ID: ")
    name = input("Name: ")
    username = input("Username: ")
    dept = input("Department: ")
    staff_controller.create_staff(id, name, username, dept)
    print("Staff created!")

@app.cli.command("log-hours")
def log_hours():
    username = input("Student username: ")
    hours = float(input("Hours: "))
    activity = input("Activity: ")
    date = input("Date: ")
    entry = staff_controller.log_hours(username, hours, activity, date)
    if entry:
        print("Hours logged (pending approval).")
    else:
        print("Student not found!")

@app.cli.command("approve-hours")
def approve_hours():
    entries = staff_controller.get_pending_entries()
    for i, e in enumerate(entries):
        print(f"{i}. {e.student.username} - {e.hours}h ({e.activity})")
    choice = int(input("Select entry to approve: "))
    entry = staff_controller.approve_hours(choice)
    if entry:
        print("Approved!")
    else:
        print("Invalid choice.")

@app.cli.command("leaderboard")
def leaderboard():
    students = student_controller.get_leaderboard()
    for s in students:
        print(f"{s.username}: {s.totalHours}h")

@app.cli.command("accolades")
def accolades():
    username = input("Student username: ")
    accolades = student_controller.view_accolades(username)
    if accolades:
        for a in accolades:
            print(f"{a.title} - {a.date_awardedOn}")
    else:
        print("No accolades found.")
