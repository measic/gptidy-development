import matplotlib.pyplot as plt
# Using "tab:..." for colors gives alternate colors that are easier on the eyes.
#plt.plot(x, y, 'b-o', color='tab:blue')
#plt.plot(x, z, 'r--', color='tab:red')
# NOTE that the marker conventions are nearly identical.
plt.plot(x, y, 'b-o')
plt.plot(x, z, 'r--')
plt.xlabel('x')
plt.title('a couple of lines')
#note that the legend items need to be in a list
plt.legend(['y=sin(x)','z=0.5+cos(x/2)'])
# Save figure to file.
plt.savefig('Figure.png')  #In JN, must save your figure before using the show() command
#The next line creates a interactive popup if it is in your script (instead of JN where it inserts it in the notebook)
plt.show()
plt.close()  #good form to close (clean up) at end otherwise you might have bad effects on following figures.