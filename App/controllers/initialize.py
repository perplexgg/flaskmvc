from App.controllers import student_controller, staff_controller

def initialize():
    # Create some sample students
    student_controller.create_student("1", "Alice", "alice")
    student_controller.create_student("2", "Bob", "bob")

    # Create one staff
    staff_controller.create_staff("100", "Mr. Smith", "smith", "Community Service")

    print("System initialized with sample data.")
