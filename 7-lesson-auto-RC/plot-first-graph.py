import numpy as np
import matplotlib.pyplot as plt

#чтение данных из data.txt
data_array = np.loadtxt("data.txt", dtype=int)

#сохранение графика
plt.plot(data_array)
plt.show()
plt.savefig("first-graph.png")