##  define color list
colors = ['b', 'g', 'r', 'k', 'c', 'm', 'y']
##  define index for iterating through color list
index = 0
##  for each river segment
for segment in segments:
    ##  subset df to non-zero values for the current river segment
    segDF = data.loc[data['RiverSeg'] == segment]
    segDF = segDF[segDF["SWI_10"]>0]

    ## sort based on year
    segDF = segDF.sort_values('Year')
    ## define x,y for plotting
    x = segDF["Year"]
    y = segDF["SWI_10"]
    ## change name of y to Riv Seg for legend
    y.name = segment
    ##  build graph...
    ##  plot segment x vs y assigning color based on index
    plt.plot(x,y,colors[index])
    ##  locate legend
    plt.legend(loc=(1.05,0.2))
    ##  advance color index
    index += 1

##  update title
plt.title("S-W Index (Log(10)), " + river + " River Segments")
##  label x axis
plt.xlabel('Year')
##  label y axis
plt.ylabel('SWI Log(10)')
##  force x axis to integer values, increment by 1 year
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
##  rotate year labels 90 degrees
plt.xticks(rotation=90)    
    
    
##  save figure
plt.savefig(output + "\\" + river + "_SWI_10.png", bbox_inches='tight',dpi=300, size=(2000,2000))
##  display figure
plt.show()