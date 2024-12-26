import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}
        self.__gpa = 0.0

    def input_mark(self, course_id, mark):
        self.__marks[course_id] = math.floor(mark * 10) / 10  # Round down to 1 decimal

    def calculate_gpa(self, courses):
        total_credits = 0
        weighted_sum = 0
        for course_id, mark in self.__marks.items():
            course = next((c for c in courses if c.get_info()[0] == course_id), None)
            if course:
                credits = course.get_credits()
                weighted_sum += mark * credits
                total_credits += credits
        if total_credits > 0:
            self.__gpa = weighted_sum / total_credits

    def get_gpa(self):
        return self.__gpa

    def get_info(self):
        return self.__student_id, self.__name, self.__dob

    def get_marks(self):
        return self.__marks

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, DOB: {self.__dob}, GPA: {self.__gpa:.2f}"


class Course:
    def __init__(self, course_id, name, credits):
        self.__course_id = course_id
        self.__name = name
        self.__credits = credits

    def get_info(self):
        return self.__course_id, self.__name

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"ID: {self.__course_id}, Name: {self.__name}, Credits: {self.__credits}"


class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_students(self, stdscr):
        n = int(stdscr.getstr().decode())
        for _ in range(n):
            stdscr.addstr("Enter student ID: ")
            student_id = stdscr.getstr().decode()
            stdscr.addstr("Enter student name: ")
            name = stdscr.getstr().decode()
            stdscr.addstr("Enter student date of birth: ")
            dob = stdscr.getstr().decode()
            self.__students.append(Student(student_id, name, dob))

    def input_courses(self, stdscr):
        n = int(stdscr.getstr().decode())
        for _ in range(n):
            stdscr.addstr("Enter course ID: ")
            course_id = stdscr.getstr().decode()
            stdscr.addstr("Enter course name: ")
            name = stdscr.getstr().decode()
            stdscr.addstr("Enter course credits: ")
            credits = int(stdscr.getstr().decode())
            self.__courses.append(Course(course_id, name, credits))

    def input_marks(self, stdscr):
        stdscr.addstr("Enter course ID to input marks: ")
        course_id = stdscr.getstr().decode()
        course = next((c for c in self.__courses if c.get_info()[0] == course_id), None)
        if not course:
            stdscr.addstr("Course not found!\n")
            return

        for student in self.__students:
            student_id, name, _ = student.get_info()
            stdscr.addstr(f"Enter mark for {name} (ID: {student_id}): ")
            mark = float(stdscr.getstr().decode())
            student.input_mark(course_id, mark)

    def calculate_gpas(self):
        for student in self.__students:
            student.calculate_gpa(self.__courses)

    def sort_students_by_gpa(self):
        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def list_students(self, stdscr):
        stdscr.addstr("Students:\n")
        for student in self.__students:
            stdscr.addstr(str(student) + "\n")

    def list_courses(self, stdscr):
        stdscr.addstr("Courses:\n")
        for course in self.__courses:
            stdscr.addstr(str(course) + "\n")

    def show_student_marks(self, stdscr):
        stdscr.addstr("Enter course ID to show marks: ")
        course_id = stdscr.getstr().decode()
        course = next((c for c in self.__courses if c.get_info()[0] == course_id), None)
        if not course:
            stdscr.addstr("Course not found!\n")
            return

        stdscr.addstr(f"Marks for course {course.get_info()[1]}:\n")
        for student in self.__students:
            student_id, name, _ = student.get_info()
            marks = student.get_marks()
            mark = marks.get(course_id, "N/A")
            stdscr.addstr(f"{name} (ID: {student_id}): {mark}\n")


def main(stdscr):
    smm = StudentMarkManagement()

    while True:
        stdscr.clear()
        stdscr.addstr("Menu:\n")
        stdscr.addstr("1. Input students\n")
        stdscr.addstr("2. Input courses\n")
        stdscr.addstr("3. Input marks for a course\n")
        stdscr.addstr("4. Calculate GPA and sort students\n")
        stdscr.addstr("5. List students\n")
        stdscr.addstr("6. List courses\n")
        stdscr.addstr("7. Show student marks for a course\n")
        stdscr.addstr("8. Exit\n")
        stdscr.addstr("Choose an option: ")

        choice = stdscr.getstr().decode()
        if choice == "1":
            smm.input_students(stdscr)
        elif choice == "2":
            smm.input_courses(stdscr)
        elif choice == "3":
            smm.input_marks(stdscr)
        elif choice == "4":
            smm.calculate_gpas()
            smm.sort_students_by_gpa()
        elif choice == "5":
            smm.list_students(stdscr)
        elif choice == "6":
            smm.list_courses(stdscr)
        elif choice == "7":
            smm.show_student_marks(stdscr)
        elif choice == "8":
            stdscr.addstr("Exiting...\n")
            stdscr.refresh()
            break
        else:
            stdscr.addstr("Invalid option, please try again.\n")
        stdscr.addstr("Press any key to continue...")
        stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
