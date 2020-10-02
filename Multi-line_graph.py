import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax = fig.add_axes([0.3,0.3,0.8,0.8])
t = np.arange(0,100,2)
plt.plot(t,t,'rs',t,t**2,'b^',t,t**3,'g--')    # t will act as both X and Y axis values
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Simple Line Graph')
