#for s in getListOfFiles('Data1/'):
    #print s
data = getListFromAFile("Data1/mvar-set1.dat")

print data.shape
df = pd.DataFrame(data.T)
print df
print data[0]
createPlots(data.T[0],data.T[2],'x-axis -->','y-axis -->',s)