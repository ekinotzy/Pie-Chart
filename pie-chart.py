import natplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Charries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, lables = mylabels, explode = myexplode, shadow = True)
plt.show()
