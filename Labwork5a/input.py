from domains.student import Student
from domains.course import Course

def inputStudents():
    Students = []

    ns = int(input("Number of students: "))
    for i in range(1, ns + 1):
        print("Student", i)
        ID = int(input("ID: "))
        Name = input("Name: ")
        DOB = input("DOB: ")
        Students.append(Student(ID, Name, DOB))
    return Students, ns

def inputCourses():
    Courses = []

    nc = int(input("Number of courses: "))
    for i in range(1, nc + 1):
        print("Course", i)
        ID = int(input("ID: "))
        Name = input("Name: ")
        Credits = int(input("Credits: "))
        Courses.append(Course(ID, Name, Credits))
    return Courses, nc

def inputMarks(ns, nc):
    Marks = []

    for i in range(1, ns + 1):
        print("Marks for Student", i)
        student_marks = []
        for j in range(nc):
            mark = float(input("Course " + str(j + 1) + ": "))
            student_marks.append(mark)
        Marks.append(student_marks)
    return Marks

def loadStudents():
    Students = []

    with open("students.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            ID = int(data[0])
            Name = data[1]
            DOB = data[2]
            Students.append(Student(ID, Name, DOB))
    return Students

def loadCourses():
    Courses = []

    with open("courses.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            ID = int(data[0])
            Name = data[1]
            Credits = int(data[2])
            Courses.append(Course(ID, Name, Credits))
    return Courses

def loadMarks():
    Marks = []

    with open("marks.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            student_marks = []
            for mark in data:
                student_marks.append(float(mark))
            Marks.append(student_marks)
    return Marks