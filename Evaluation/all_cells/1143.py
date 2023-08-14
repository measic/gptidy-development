y=np.arange(2,10.01,0.8)
#plt.figure(figsize=(20,10))     
for i in range(0,len(y)-1):
    x = np.arange(y[i], y[i+1], 0.001);
    #plt.plot(x,f(x,H),'-b')
    testW=findw(f,10000,y[i],y[i+1],True)
    plt.plot(x,f(x,10000)/(testW[0]*x+testW[1]),'-r')
    
plt.show()