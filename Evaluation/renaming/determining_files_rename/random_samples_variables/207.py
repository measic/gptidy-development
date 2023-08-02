colors = ['b', 'g', 'r', 'k', 'c', 'm', 'y']
index = 0
for segment in segments:
    segDF = data.loc[data['RiverSeg'] == segment]
    segDF = segDF[segDF["lam'"] > 0]
    segDF = segDF.sort_values('Year')
    variable_def = segDF['Year']
    y = segDF['N1']
    y.name = segment
    plt.plot(variable_def, y, colors[index])
    plt.legend(loc=(1.05, 0.2))
    index += 1
plt.title('Hill N1, ' + river + ' River Segments')
plt.xlabel('Year')
plt.ylabel("N1'")
plt.xticks(np.arange(min(variable_def), max(variable_def) + 1, 1.0))
plt.xticks(rotation=90)
plt.savefig(output + '\\' + river + '_Hill_N1.png', bbox_inches='tight', dpi=300, size=(2000, 2000))
plt.show()