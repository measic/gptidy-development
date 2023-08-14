if visualize_dataset == True and round_values == True:
    # Save path
    heatmap_save_path = exportpath + timestamp + "heatmap.png"
    
    # Create correlation Matrix
    correlation_dataframe = data_no_nulls.corr()
    
    # Create mask
    mask = numpy.zeros_like(correlation_dataframe)
    mask[numpy.triu_indices_from(mask)] = True

    # Create heatmap, show and export as .png
    seaborn.heatmap(data = correlation_dataframe,
               cmap = ['#b2182b',
                    '#ef8a62',
                    '#fddbc7',
                    '#f7f7f7',
                    '#d1e5f0',
                    '#67a9cf',
                    '#2166ac'],
               center = 0,
               square = True,
               linewidth = 1,
               mask = mask,
               annot = True).get_figure().savefig(heatmap_save_path)
    
    print("Heatmap saved to '{}'".format(heatmap_save_path))
else:
    print("No heatmap was produced. Dataset contains no numeric features or visualize_dataset variable was set to False.")