colors = ['b', 'g', 'r', 'k', 'c', 'm', 'y']
variable_def = 0
for segment in segments:
    segDF = data.loc[data['RiverSeg'] == segment]
    segDF = segDF[segDF["lam'"] > 0]
    segDF = segDF.sort_values('Year')
    x = segDF['Year']
    y = segDF["N10'"]
    y.name = segment
    plt.plot(x, y, colors[variable_def])
    plt.legend(loc=(1.05, 0.2))
    variable_def += 1
plt.title("Hill N10', " + river + ' River Segments')
plt.xlabel('Year')
plt.ylabel("N10'")
plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
plt.xticks(rotation=90)
plt.savefig(output + '\\' + river + "_Hill_N10'.png", bbox_inches='tight', dpi=300, size=(2000, 2000))
plt.show()