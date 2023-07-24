#Simple demo with multiple subplots.
import numpy as np
import matplotlib.pyplot as plt

# x data for plots 1 and 2
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
# y data for plots 1 and 2
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

#arrangement of subplots
nrows = 2
ncols = 1
idx = 1
plt.subplot(nrows, ncols, idx)
#the marker/line is specified by the 'o-'
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(nrows, ncols, idx+1)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
# For saving do this
plt.savefig('subplots.png')
plt.show()
plt.close() #do this at end of each plot