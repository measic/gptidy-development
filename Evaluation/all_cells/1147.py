#Divide the region into 10 pieces.
l=np.arange(2,10.01,0.8)   
#Real value of the integral
I_real=-16.6728
#N values
N=[100,1000,10000,100000,1000000,10000000]
#Integration results.
results=[]
#Standart deviation values
sigmas=[]
for k in N:
    I=0
    sigma=0
    for i in range (0,len(l)-1):
        temp,temp2=integrate(f,l[i],l[i+1],int(0.1*k),100000)
        I+=temp
        sigma+=temp2
    results.append(I)
    sigmas.append(np.sqrt(sigma))
    print(k,I,I-I_real,np.sqrt(sigma),(I-I_real)/np.sqrt(sigma))
plt.plot(np.log10(N),sigmas,'rd--')
plt.ylabel('Sigma')
plt.xlabel('Log(N)')
plt.show()
