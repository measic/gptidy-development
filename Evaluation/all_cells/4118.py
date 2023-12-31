plt.figure(figsize=(20,5))
plt.plot(alpha, c='blue')
plt.plot(beta, c='red')
plt.xlabel('time [ms]')
plt.ylabel('angle [deg]')
plt.legend(['alpha', 'beta'])
plt.grid()