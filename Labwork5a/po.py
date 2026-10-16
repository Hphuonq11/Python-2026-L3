import pandas as pd

class Po:
    def __init__(self):
        self.students = pd.read_csv("students.csv")
        self.courses = pd.read_csv("courses.csv")
        self.marks = pd.read_csv("marks.csv")

    def query(self):
        condition = input('Enter condition (e.g. name == "Max"): ')
        result = self.students.query(condition)
        print(result)