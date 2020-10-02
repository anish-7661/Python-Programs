import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig=plt.figure()
ax = fig.add_axes([0.3,0.3,0.6,0.6])
X = np.linspace(0,10)
Y = X**2
ax.plot(X,Y,'g')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Simple Line Graph')
