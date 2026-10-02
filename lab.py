import math
import numpy as np

Students = {"ID": [], "Name": [], "DOB":[]}
Courses = {"ID": [], "Name": [], "Credit": []}
Marks = []


def inputStudents(Students):
    ns = int(input("Number of students: "))

    for i in range(1, ns + 1):
        print("Enter information for student", i)
        Students["ID"].append(input("Student ID: "))
        Students["Name"].append(input("Student name: "))
        Students["DOB"].append(input("Date of birth: "))

    return ns


def listCourses(Courses):
    nc = int(input("Number of courses: "))

    for i in range(1, nc + 1):
        print("Enter information for course", i)
        Courses["ID"].append(input("Course ID: "))
        Courses["Name"].append(input("Course name: "))
        Courses["Credit"].append(int(input("Course credit: ")))

    return nc


def getMarks(ns, nc):

    for j in range(nc):

        cn = Courses["ID"][j]

        print("Enter marks for course", cn)

        for i in range(ns):

            mark = float(input("Mark for student " + Students["ID"][i] + ": "))

            mark = math.floor(mark * 10) / 10

            Marks.append((Students["ID"][i], cn, mark))


def showMarks(ns, nc):

    for i in range(ns):

        student_id = Students["ID"][i]

        print("\nStudent ID:", student_id)

        for mark in Marks:

            if mark[0] == student_id:

                print("Course", mark[1], ":", mark[2])


def calculateGPA(student_id):

    marks = []
    credits = []

    for mark in Marks:

        if mark[0] == student_id:

            course_id = mark[1]
            score = mark[2]

            for i in range(len(Courses["ID"])):

                if Courses["ID"][i] == course_id:

                    credit = Courses["Credit"][i]

                    marks.append(score)
                    credits.append(credit)

    marks = np.array(marks)
    credits = np.array(credits)

    gpa = np.sum(marks * credits) / np.sum(credits)

    return gpa


ns = inputStudents(Students)

nc = listCourses(Courses)

getMarks(ns, nc)

showMarks(ns, nc)

for i in range(ns):

    student_id = Students["ID"][i]

    print("GPA of", student_id, ":", calculateGPA(student_id))