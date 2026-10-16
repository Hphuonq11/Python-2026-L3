import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("scores.csv")

df[["math", "python", "database"]].plot(kind="box")

plt.title("Student scores box plot")
plt.ylabel("Scores")

plt.savefig("box.png")
plt.show()
