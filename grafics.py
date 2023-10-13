import matplotlib.pyplot as plt
import numpy as np
from numpy import log
fig=plt.figure()
ax=fig.add_subplot(1, 1, 1,  projection='3d')
x,y=np.meshgrid(np.linspace(-5, 5,10), np.linspace(-5,5,10))
z=4*(x-5)**2+(y-6)**2
ax.plot_surface(x, y, z)
plt.show()