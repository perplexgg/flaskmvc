from App.models.student import Student

students = {}

def create_student(id, name, username):
    student = Student(id, name, username)
    students[username] = student
    return student

def get_student(username):
    return students.get(username)

def get_leaderboard():
    return sorted(students.values(), key=lambda s: s.totalHours, reverse=True)

def view_accolades(username):
    student = get_student(username)
    if student:
        return student.getAccolades()
    return []
