import pandas as pd
#Load the dataset
df = pd.read_csv("students.csv")

#Dispaly first 5 rows
print(df.head())

#Find number of rows and columns
print("\nNumber of rows and columns:",df.shape)

#Select name and GPA
print("\n")
print(df[["name","GPA"]])

#Find students with GPA >= 3.5
print("\n",df[df["GPA"] >= 3.5])

#Sort students by GPA
print("\n", df.sort_values("GPA"))

#Find average GPA by major
print("\n", df.groupby("major")["GPA"].mean())

