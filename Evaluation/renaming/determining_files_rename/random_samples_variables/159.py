colors = ['b', 'g', 'r', 'k', 'c', 'm', 'y']
variable_def = 0
for segment in segments:
    segDF = data.loc[data['RiverSeg'] == segment]
    segDF = segDF[segDF["lam'"] > 0]
    segDF = segDF.sort_values('Year')
    x = segDF['Year']
    y = segDF["1-lam'"]
    y.name = segment
    plt.plot(x, y, colors[variable_def])
    plt.legend(loc=(1.05, 0.2))
    variable_def += 1
plt.title("1-Lambda', " + river + ' River Segments')
plt.xlabel('Year')
plt.ylabel("1-Lambda'")
plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
plt.xticks(rotation=90)
plt.savefig(output + '\\' + river + "_1-Lambda'.png", bbox_inches='tight', dpi=300, size=(2000, 2000))
plt.show()