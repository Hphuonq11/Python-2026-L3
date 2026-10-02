Students={"ID":[], "Name":[], "DOB":[]}
Courses={"ID":[], "Name":[]}
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
  return nc

def getMarks(cn, ns):
  for i in range(1, ns + 1):
    mark = float(input("Mark for student" + Students["ID"][i-1] + ": "))
    Marks.append((Students["ID"][i-1], cn, mark))

def showMarks(cn, ns):
  print("Marks for course", cn)
  for i in range(1, ns + 1):
    print("Student ID",Students["ID"][i-1], ":", Marks[i-1][2])

ns = inputStudents(Students) #chạy hàm def + lưu vô ns
nc = listCourses(Courses)
cn = input("Course selected: ")
getMarks(cn, ns)
showMarks(cn, ns)
