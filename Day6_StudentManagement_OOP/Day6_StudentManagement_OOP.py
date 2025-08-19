class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = 0

    def display_details(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Course: {self.course}, Marks: {self.marks}")

    def add_marks(self, marks):
        self.marks = marks
        print("Marks updated successfully!")

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"


# List to hold multiple students
students = []


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")
    student = Student(name, roll_no, course)
    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
    else:
        for s in students:
            s.display_details()


def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s.roll_no == roll:
            print("Student found:")
            s.display_details()
            print("Grade:", s.calculate_grade())
            return
    print("Student not found.")


def update_marks():
    roll = input("Enter roll number to update marks: ")
    for s in students:
        if s.roll_no == roll:
            marks = int(input("Enter new marks: "))
            s.add_marks(marks)
            return
    print("Student not found.")


def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s.roll_no == roll:
            students.remove(s)
            print("Student deleted successfully.")
            return
    print("Student not found.")


# Menu-driven program
while True:
    print("\n--- Student Management Menu ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
