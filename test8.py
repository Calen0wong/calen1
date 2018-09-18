import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt

x = np.linspace(0, 5, 10)
y = x ** 2
plt.plot(x, y, 'r')
