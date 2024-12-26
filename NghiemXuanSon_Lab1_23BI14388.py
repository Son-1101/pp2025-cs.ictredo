# Student Mark Management System

students = {}
courses = {}
marks = {}

def input_students():
    n = int(input("Enter the number of students: "))
    for _ in range(n):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        students[student_id] = {"name": name, "dob": dob}

def input_courses():
    n = int(input("Enter the number of courses: "))
    for _ in range(n):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses[course_id] = name

def input_marks():
    course_id = input("Enter course ID: ")
    if course_id not in courses:
        print("Course not found!")
        return
    if course_id not in marks:
        marks[course_id] = {}

    for student_id, student in students.items():
        mark = float(input(f"Enter mark for {student['name']} (ID: {student_id}): "))
        marks[course_id][student_id] = mark

def list_students():
    print("List of students:")
    for student_id, student in students.items():
        print(f"ID: {student_id}, Name: {student['name']}, DOB: {student['dob']}")

def list_courses():
    print("List of courses:")
    for course_id, name in courses.items():
        print(f"ID: {course_id}, Name: {name}")

def show_marks():
    course_id = input("Enter course ID: ")
    if course_id not in marks:
        print("No marks available for this course!")
        return

    print(f"Marks for course {courses[course_id]}:")
    for student_id, mark in marks[course_id].items():
        print(f"{students[student_id]['name']} (ID: {student_id}): {mark}")

# Main program
def main():
    while True:
        print("\nMenu:")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "7":
            print("Exiting...")
            break  # Thoát khỏi vòng lặp
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
