import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0.0, 2.0, 0.01)
y = (np.sin(x-2) ** 2) * (np.e ** (-x ** 2))

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Function Plot")
plt.grid(True)
plt.show()




