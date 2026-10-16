import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("scores.csv")
df[["python", "math", "database"]].plot (
    kind = "hist",
    bins = 25,
    subplots = True,
   #layout = (3, 1),
   #figsize = (6, 9),
)
#plt.tight_layout()
plt.savefig("histo.png")
plt.show()