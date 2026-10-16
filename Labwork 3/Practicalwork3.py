import math
import numpy as np

Students=[
    {"ID": 10668, "Name": "Andyy", "DOB": "19/10/2007", "GPA": 0},
    {"ID": 10654, "Name": "Demi", "DOB": "3/06/2007", "GPA": 0},
    {"ID": 10699, "Name": "Ha", "DOB": "30/01/2007", "GPA": 0},
    {"ID": 10671, "Name": "Louis", "DOB": "12/11/2007", "GPA": 0}
]

Courses=[
    {"ID": 902, "Name":"Algorithm", "Credits":4},
    {"ID": 911, "Name":"Mathematic", "Credits":4},
    {"ID": 905, "Name":"Signal", "Credits":3}
]
Marks=[
   [18.56, 16.0336, 12],
   [17.90, 11.735, 17.12],
   [19.0267, 15.47, 15],
   [17.23334, 13.40, 14.790]
]

def listStudent(ns):
    for i in range(1, ns + 1):
        print("Student", i)
        print("ID:", Students[i - 1]["ID"])
        print("Name:", Students[i -1]["Name"])
        print("DOB:", Students[i -1]["DOB"])
        print("---------------------------")

def listCourses(nc):
    for i in range(1, nc + 1):
        print("Course", i)
        print("ID:", Courses[i - 1]["ID"])
        print("Name:", Courses[i - 1]["Name"])
        print("Credits:", Courses[i - 1]["Credits"])
        print("---------------------------")

def roundMarks(ns, nc):
    for i in range(ns):
        for j in range(nc):
            Marks[i][j] = math.floor(Marks[i][j] * 10) / 10

def calGPA(student_index, nc):
    marks = []
    credits = []

    for i in range(nc):
        marks.append(Marks[student_index][i])
        credits.append(Courses[i]["Credits"])

    marks = np.array(marks)
    credits = np.array(credits)
    gpa = np.sum(marks * credits) / np.sum(credits)
    return gpa

def getGPA(student):
    return student[1]

def sortedGPA(ns, nc):
    studentGPA = []

    for i in range(1, ns + 1):
        student_id = Students[i - 1]["ID"]
        gpa = calGPA(i - 1, nc)
        studentGPA.append((student_id, gpa))
    studentGPA.sort(key=getGPA, reverse=True)
    return studentGPA

ns = 4
nc = 3
listStudent(ns)
listCourses(nc)
roundMarks(ns, nc)
sg = sortedGPA(ns, nc)
print("===== GPA RESULT =====")
for student in sg:
    print("Student ID:", student[0], "GPA:", round(student[1], 2))
