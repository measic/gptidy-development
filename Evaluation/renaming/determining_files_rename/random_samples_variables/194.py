colors = ['b', 'g', 'r', 'k', 'c', 'm', 'y']
index = 0
for segment in segments:
    variable_def = data.loc[data['RiverSeg'] == segment]
    variable_def = variable_def[variable_def["lam'"] > 0]
    variable_def = variable_def.sort_values('Year')
    x = variable_def['Year']
    y = variable_def['N10']
    y.name = segment
    plt.plot(x, y, colors[index])
    plt.legend(loc=(1.05, 0.2))
    index += 1
plt.title('Hill N10, ' + river + ' River Segments')
plt.xlabel('Year')
plt.ylabel('N10')
plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
plt.xticks(rotation=90)
plt.savefig(output + '\\' + river + '_Hill_N10.png', bbox_inches='tight', dpi=300, size=(2000, 2000))
plt.show()