
import pandas as pd

# Load 2 files: students and scores
students = pd.read_csv("students.csv")
scores = pd.read_csv("scores.csv")

# Checking missing values
print("Missing values in students:")
print(students.isna().sum())
print("Missing values in scores:")
print(scores.isna().sum())

# Fill or remove missing data appropriately
print("Students after removing missing values:")
print(students.dropna())
print("Scores after removing missing values:")
print(scores.dropna())

print("Students after filling missing values:")
students["age"] = students["age"].fillna(students["age"].median())
students["GPA"] = students["GPA"].fillna(students["GPA"].mean())
print(students)

print("Scores after filling missing values:")
scores["math"] = scores["math"].fillna(scores["math"].mean())
scores["database"] = scores["database"].fillna(scores["database"].mean())
print(scores)

# Merge the two datasets
merged = pd.merge(students, scores, on="student_id", how="inner")
print(merged)

# Calculate average score for each student
merged["average_score"] = merged[["python", "math", "database"]].mean(axis=1)
print(merged[["student_id", "name", "average_score"]])

# Find the top 5 students
top5 = merged.sort_values(by="average_score", ascending=False).head(5)
print("Top 5 students:")
print(top5[["student_id", "name", "major", "average_score"]])

# Average score by major
major_average = merged.groupby("major")["average_score"].mean()
print("Average score by major:")
print(major_average)
