if visualize_dataset == True and round_values == True:
    variable_def = exportpath + timestamp + 'heatmap.png'
    correlation_dataframe = data_no_nulls.corr()
    mask = numpy.zeros_like(correlation_dataframe)
    mask[numpy.triu_indices_from(mask)] = True
    seaborn.heatmap(data=correlation_dataframe, cmap=['#b2182b', '#ef8a62', '#fddbc7', '#f7f7f7', '#d1e5f0', '#67a9cf', '#2166ac'], center=0, square=True, linewidth=1, mask=mask, annot=True).get_figure().savefig(variable_def)
    print("Heatmap saved to '{}'".format(variable_def))
else:
    print('No heatmap was produced. Dataset contains no numeric features or visualize_dataset variable was set to False.')