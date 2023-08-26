sigmas=[]
sigma=0
I=0
for i in range(0,100):
    I=0
    sigma=0
    for i in range (0,len(l)-1):
        temp,temp2=integrate(f,l[i],l[i+1],1000,10000)
        sigma+=temp2
        I+=temp
    sigmas.append(np.sqrt(sigma))

plt.plot(np.arange(0,100,1),sigmas,'r')
plt.ylabel('Sigma')
plt.xlabel('M')
plt.show()
print("Sigma of sigma=",np.sqrt(np.var(sigmas)))