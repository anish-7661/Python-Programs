# One graph in another graph...

import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
X=np.arange(0.2,5,0.2)
Y = X**2
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax2=fig.add_axes([0.2,0.5,0.4,0.3])
ax1.plot(X,Y,'r')
ax1.set_xlabel('Outer X-axis')
ax1.set_ylabel('Outer y-axis')
ax1.set_title('Outer Graph')
ax2.plot(X,Y,'g')
ax2.set_xlabel('Inner X-axis')
ax2.set_ylabel('Inner y-axis')
ax2.set_title('Inner Graph')
