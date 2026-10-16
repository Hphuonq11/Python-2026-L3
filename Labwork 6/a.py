import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 20)
y= 2*x + np.sin(x)**2 +3
plt.plot(x,y, marker="o")
plt.grid()
plt.title("hello, po!")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("po.pdf")
plt.show()