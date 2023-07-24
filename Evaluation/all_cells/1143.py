import numpy as np
from numpy.polynomial import Polynomial as P
#import plotly
#import plotly.plotly as py
#import plotly.figure_factory as ff
import matplotlib.pyplot as plt
#Integrand function
H=0
def f(x,H):
    return (x-5)*np.exp(-(x/2-3))+H

x = np.arange(2, 10, 00.1);
plt.plot(x,f(x,H),'b')
plt.show()