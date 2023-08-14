#Calculates the coefficients of linear weight function.    
def findw(f,H,lower,upper,normalize):
    #Find the linear function.
    slope=(f(upper,H)-f(lower,H))/(upper-lower)
    a=slope
    b=-slope*upper+f(upper,H)
    #Normalization.
    A=(a/2)*(upper**2)+b*upper-(a/2)*(lower**2)-b*lower
    if normalize:
        a/=A
        b/=A
    return [a,b]

y=np.arange(2,10.01,0.8)
plt.figure(figsize=(20,10))     
for i in range(0,len(y)-1):
    x = np.arange(y[i], y[i+1], 0.001);
    plt.plot(x,f(x,H),'-b')
    testW=findw(f,H,y[i],y[i+1],False)
    plt.plot(x,testW[0]*x+testW[1],'-r')
    
plt.show()