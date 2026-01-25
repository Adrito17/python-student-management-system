students = {}

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students available.")
        return
    print("Student List:")
    for roll, info in students.items():
        print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")

def update_student():
    roll = input("Enter roll number to update: ")
    if roll in students:
        marks = input("Enter new marks: ")
        students[roll]["marks"] = marks
        print("Student marks updated!")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
