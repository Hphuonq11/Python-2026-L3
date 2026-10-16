from domains.student import Student
from domains.course import Course

def inputStudents():
    Students = [
        Student(10668, "Andyy", "19/10/2007"),
        Student(10654, "Demi", "3/06/2007"),
        Student(10699, "Ha", "30/01/2007"),
        Student(10671, "Louis", "12/11/2007")
    ]
    return Students

def inputCourses():
    Courses = [
        Course(902, "Algorithm", 4),
        Course(911, "Mathematic", 4),
        Course(905, "Signal", 3)
    ]
    return Courses

def inputMarks():
    Marks = [
        [18.56, 16.0336, 12],
        [17.90, 11.735, 17.12],
        [19.0267, 15.47, 15],
        [17.23334, 13.40, 14.790]
    ]
    return Marks