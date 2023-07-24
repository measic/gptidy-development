## Define color list
colors = ['b', 'g', 'r', 'k', 'c', 'm', 'y']

## Define index for iterating through color list
index = 0

## For each river segment
for segment in segments:
    ## Subset df to non-zero values for the current river segment
    segDF = data.loc[data['RiverSeg'] == segment]
    segDF = segDF[segDF["lam'"] > 0]

    ## Sort based on year
    segDF = segDF.sort_values('Year')

    ## Define x, y for plotting
    x = segDF["Year"]
    y = segDF["lam'"]

    ## Change name of y to Riv Seg for legend
    y.name = segment

    ## Build graph...
    ## Plot segment x vs y
    plt.plot(x, y, colors[index])

    ## Locate legend
    plt.legend(loc=(1.05, 0.2))

    ## Advance color index
    index += 1

## Update title
plt.title("Lambda', " + river + " River Segments")

## Label x axis
plt.xlabel('Year')

## Label y axis
plt.ylabel("Lambda'")

## Force x axis to integer values, increment by 1 year
plt.xticks(np.arange(min(x), max(x) + 1, 1.0))

## Rotate year labels 90 degrees
plt.xticks(rotation=90)

## Save figure
plt.savefig(output + "\\" + river + "_Lambda'.png", bbox_inches='tight', dpi=300, size=(2000, 2000))

## Show figure
plt.show()