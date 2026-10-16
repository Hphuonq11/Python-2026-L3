import math
import numpy as np

from input import inputStudents
from input import inputCourses
from input import inputMarks

Students = inputStudents()
Courses = inputCourses()
Marks = inputMarks()

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

roundMarks(4, 3)
sg = sortedGPA(4, 3)
