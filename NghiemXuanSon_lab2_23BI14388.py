# OOP-based Student Mark Management System

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}

    def input_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def get_marks(self):
        return self.__marks

    def get_info(self):
        return self.__student_id, self.__name, self.__dob

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, DOB: {self.__dob}"


class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name

    def get_info(self):
        return self.__course_id, self.__name

    def __str__(self):
        return f"ID: {self.__course_id}, Name: {self.__name}"


class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_students(self):
        n = int(input("Enter the number of students: "))
        for _ in range(n):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            self.__students.append(Student(student_id, name, dob))

    def input_courses(self):
        n = int(input("Enter the number of courses: "))
        for _ in range(n):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.__courses.append(Course(course_id, name))

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        course = next((c for c in self.__courses if c.get_info()[0] == course_id), None)
        if not course:
            print("Course not found!")
            return

        for student in self.__students:
            student_id, name, _ = student.get_info()
            mark = float(input(f"Enter mark for {name} (ID: {student_id}): "))
            student.input_mark(course_id, mark)

    def list_students(self):
        print("Students:")
        for student in self.__students:
            print(student)

    def list_courses(self):
        print("Courses:")
        for course in self.__courses:
            print(course)

    def show_student_marks(self):
        course_id = input("Enter course ID to show marks: ")
        course = next((c for c in self.__courses if c.get_info()[0] == course_id), None)
        if not course:
            print("Course not found!")
            return

        print(f"Marks for course {course.get_info()[1]}:")
        for student in self.__students:
            student_id, name, _ = student.get_info()
            marks = student.get_marks()
            mark = marks.get(course_id, "N/A")
            print(f"{name} (ID: {student_id}): {mark}")


# Main program
def main():
    smm = StudentMarkManagement()

    while True:
        print("\nMenu:")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a course")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            smm.input_students()
        elif choice == "2":
            smm.input_courses()
        elif choice == "3":
            smm.input_marks()
        elif choice == "4":
            smm.list_students()
        elif choice == "5":
            smm.list_courses()
        elif choice == "6":
            smm.show_student_marks()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
