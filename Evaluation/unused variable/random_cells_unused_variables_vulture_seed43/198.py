f1 =  lambda x: 3 - x
f2 =  lambda x: 4 - 2 * x
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()
ax.plot(x, f1(x) , linewidth= 2)
ax.plot(x, f2(x) , linewidth= 2)