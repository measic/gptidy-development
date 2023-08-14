colors = ['b', 'g', 'r', 'k', 'c', 'm', 'y']
index = 0
for segment in segments:
    segDF = data.loc[data['RiverSeg'] == segment]
    segDF = segDF[segDF["lam'"] > 0]
    segDF = segDF.sort_values('Year')
    x = segDF['Year']
    variable_def = segDF['N21']
    variable_def.name = segment
    plt.plot(x, variable_def, colors[index])
    plt.legend(loc=(1.05, 0.2))
    index += 1
plt.title('Hill N21, ' + river + ' River Segments')
plt.xlabel('Year')
plt.ylabel('N21')
plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
plt.xticks(rotation=90)
plt.savefig(output + '\\' + river + '_Hill_N21.png', bbox_inches='tight', dpi=300, size=(2000, 2000))
plt.show()