
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,6])
y = np.array([99,86,87,88,86,103,87,94])
colors = np.array([0, 10, 20, 30, 40, 45, 50,60])

plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
plt.show()