# Display matplotlib plots in the notebook
%matplotlib inline

# create a new model to attach piecewise
pm = Model(name='pwl')
pwf1 = pm.piecewise_as_slopes([(0, 0), (0.4, 1000), (0.2, 3000)], lastslope=0.1)
# plot the function
pwf1.plot(lx=-1, rx=4000, k=1, color='b', marker='s', linewidth=2)