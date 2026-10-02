import math
import numpy as np
Students={"ID":[], "Name":[], "DOB":[]}
Courses={"ID":[], "Name":[], "Credit":[]}
Marks=[]

def inputStudents(Students):
  ns = int(input("Number of students: "))

  for i in range (1,ns + 1):
    print("Enter information for student", i)
    Students["ID"].append(input("Student ID: "))
    Students["Name"].append(input("Student name: "))
    Students["DOB"].append(input("Date of birth: "))
  return ns

def listCourses(Courses):
  nc = int(input("Number of courses: "))

  for i in range (1, nc +1):
    print("Enter information for courses", i)
    Courses["ID"].append(input("Course ID: "))
    Courses["Name"].append(input("Course name: "))
    Courses["Credit"].append(int(input("Course credit: ")))
  return nc

def getMarks(cn, ns):
  for i in range(1, ns + 1):
    mark = float(input("Mark for student " + Students["ID"][i-1] + ": "))
    mark = math.floor(mark * 10)/10
    Marks.append((Students["ID"][i-1], cn, mark))

def showMarks(cn, ns):
  print("Marks for course", cn)
  for i in range(1, ns + 1):
    print("Student ID",Students["ID"][i-1], ":", Marks[i-1][2])

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

ns = inputStudents(Students) #run def and store in ns
nc = listCourses(Courses)
cn = input("Course selected: ")
getMarks(cn, ns)
showMarks(cn, ns)
print("GPA:", calculateGPA(Students["ID"][0]))