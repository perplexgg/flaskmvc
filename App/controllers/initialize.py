from App.controllers import student_controller, staff_controller

def initialize():
    student_controller.create_student("1", "Alice", "alice")
    student_controller.create_student("2", "Bob", "bob")

    staff_controller.create_staff("100", "Mr. Smith", "smith", "Community Service")

    staff_controller.log_hours("alice", 50, "Beach Cleanup", "2025-09-24")

    print("✅ System initialized with sample data.")
