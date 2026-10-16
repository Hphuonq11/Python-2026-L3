import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("scores.csv")

plt.scatter(df.index, df["math"], label="Math")
plt.scatter(df.index, df["python"], label="Python")
plt.scatter(df.index, df["database"], label="DB")

plt.title("Student scores scatter plot")
plt.xlabel("Student index")
plt.ylabel("Scores")
#plt.legend()
#plt.grid(True)
plt.savefig("scattered.png")
plt.show()


