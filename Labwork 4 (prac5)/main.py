import math
import numpy as np

from input import inputStudents
from input import inputCourses
from input import inputMarks
from input import loadStudents
from input import loadCourses
from input import loadMarks

import os
import zipfile

if os.path.exists("students.dat"):
    with zipfile.ZipFile("students.dat", "r") as zipf:
        zipf.extractall()

    Students = loadStudents()
    Courses = loadCourses()
    Marks = loadMarks()

    ns = len(Students)
    nc = len(Courses)

else:
    Students, ns = inputStudents()
    Courses, nc = inputCourses()
    Marks = inputMarks(ns, nc)

def roundMarks(ns, nc):
    for i in range(ns):
        for j in range(nc):
            Marks[i][j] = math.floor(Marks[i][j] * 10) / 10

def calGPA(student_index, nc):
    marks = []
    credits = []

    for i in range(nc):
        marks.append(Marks[student_index][i])
        credits.append(Courses[i].Credits)

    marks = np.array(marks)
    credits = np.array(credits)
    gpa = np.sum(marks * credits) / np.sum(credits)
    return gpa

def getGPA(student):
    return student[1]


def sortedGPA(ns, nc):
    studentGPA = []

    for i in range(1, ns + 1):
        student_id = Students[i - 1].ID
        gpa = calGPA(i - 1, nc)
        studentGPA.append((student_id, gpa))
    studentGPA.sort(key=getGPA, reverse=True)
    return studentGPA

roundMarks(ns, nc)
sg = sortedGPA(ns, nc)

#create student.txt
with open("students.txt", "w") as f:
    for student in Students:
        f.write(str(student.ID) + "," + student.Name + "," + student.DOB + "\n")
#create courses.txt
with open("courses.txt", "w") as f:
    for course in Courses:
        f.write(str(course.ID) + "," + course.Name + "," + str(course.Credits) + "\n")
#create marks.txt
with open("marks.txt", "w") as f:
    for i in range(ns):
        for j in range(nc):
            f.write(str(Marks[i][j]))
            if j < nc - 1:
                f.write(",")
        f.write("\n")
#Zip 3 file .txt
with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write("students.txt")
    zipf.write("courses.txt")
    zipf.write("marks.txt")


