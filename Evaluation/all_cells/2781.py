route = pd.read_csv('test/route.csv')


node_df = route.set_index('Sum of Flights_Count').stack().reset_index()
node_df = node_df.groupby(0, as_index=False)[['Sum of Flights_Count']].sum()
node_df.rename(columns = {0: 'airport'}, inplace=True)

force_graph = ForceGraph(links_dataframe = route, 
                         source_column = 'Origin',
                         target_column = 'Dest', 
                         nodes = node_df, 
                         nodes_name_column= 'airport', ##TODO:'
                         nodes_tooltip_column = "Sum of Flights_Count", ##tooltip_column should be moved to addTooltip() method. 
                         canvas_height =800, canvas_width=600)
force_graph.addTooltip().addLinkTooltip()
force_graph.sizeNode(column ='Sum of Flights_Count', scale=1/6035.0)
force_graph.addColor(column="airport", options = {"palette":["#6363FF", "#FF7363", "#0a9700"], 
                                                  "stroke": "true", "fill": "true", "opacity": 0.7,
                                                  "stroke-width":2, "stroke-opacity": 0.5})
force_graph.show()

