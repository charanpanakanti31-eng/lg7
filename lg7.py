from datetime import datetime

class Course:
    def __init__(self, name, seats, deadline):
        self.name = name
        self.total_seats = seats
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.registered_students = set()

    def is_full(self):
        return len(self.registered_students) >= self.total_seats

    def deadline_passed(self):
        return datetime.now() > self.deadline


class CoreCourse(Course):
    pass

class ElectiveCourse(Course):
    pass


class RegistrationSystem:
    def __init__(self):
        self.courses = set()
        self.registrations = {}

    def add_course(self, course):
        self.courses.add(course)

    def display_courses(self):
        print("\nAvailable Courses:")
        for course in self.courses:
            available_seats = course.total_seats - len(course.registered_students)
            print(f"{course.name} | Seats: {available_seats} | "
                  f"Registered: {len(course.registered_students)} | "
                  f"Deadline: {course.deadline.date()}")

    def register_student(self, student, course_name):
        for course in self.courses:
            if course.name == course_name:

                if course.deadline_passed():
                    return "❌ Deadline passed!"

                if course.is_full():
                    return "❌ Course is full!"

                course.registered_students.add(student)

                if student not in self.registrations:
                    self.registrations[student] = []

                if course.name not in self.registrations[student]:
                    self.registrations[student].append(course.name)

                return "✅ Registration successful!"

        return "❌ Course not found!"

    def display_student_courses(self, student):
        print(f"\nCourses registered by {student}:")
        if student in self.registrations:
            for c in self.registrations[student]:
                print(c)
        else:
            print("No courses registered.")


# Main Program 

system = RegistrationSystem()

course1 = CoreCourse("Mathematics", 50, "2026-03-01")
course2 = ElectiveCourse("Python Programming", 45, "2026-03-01")

system.add_course(course1)
system.add_course(course2)

# Initial Courses
system.display_courses()

# Alice Registration
msg1 = system.register_student("Alice", "Mathematics")
system.register_student("Alice", "Python Programming")
system.display_student_courses("Alice")
print(msg1)

# Updated Courses After Alice
system.display_courses()

# Bob Registration
msg2 = system.register_student("Bob", "Mathematics")
system.register_student("Bob", "Python Programming")
system.display_student_courses("Bob")
print(msg2)

# Updated Courses After Bob
system.display_courses()