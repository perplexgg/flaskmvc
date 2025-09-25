from App.controllers import student_controller, staff_controller

def initialize():
    # Create some sample students
    student_controller.create_student("1", "Alice", "alice")
    student_controller.create_student("2", "Bob", "bob")

    # Create one staff
    staff_controller.create_staff("100", "Mr. Smith", "smith", "Community Service")

    # Log hours for Alice
    staff_controller.log_hours("alice", 50, "Beach Cleanup", "2025-09-24")

    print("System initialized with sample data.")
