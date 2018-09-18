from matplotlib import pyplot as plt
import numpy as np

x = np.random.randint(10, size=10)
y = np.random.randint(20, size=10)

plt.figure()
plt.plot(x, y, "y*-", linewidth=1)
plt.xlabel("time(s)")
plt.ylabel("distance(m)")
plt.show()
plt.savefig("line2.png")