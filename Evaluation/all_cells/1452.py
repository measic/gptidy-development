def nearest(vector, point):
    ''' this function finds the index of the number in the vector which is closest in absolute terms to the 
    point. If there is more than one match, only the 1st is returned. (This is the docstring)'''
    df = np.abs(vector - point)
    print('df',df)
    ind = np.argmin(df) #argmin() finds the index where df is minimum. Only first occurrence returned.
    return ind
    
vector = np.array(range(-5,5))
point = np.array(range(20,10,-1))*1.5
print(vector)
print(point)
print('nearest index', nearest(vector,point))