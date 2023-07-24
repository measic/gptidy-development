datapath = '.'
#file contains data about links in nyc
linkspath = datapath + '/links.csv'
#file contains data about intersections in nyc
nodespath = datapath + '/nodes.csv'
#link in nyc that contains enough info to analysis
full_links_ids_path = datapath + '/full_link_ids.txt'
#kml file that contains boundaries of regions we are trying to parse
#this file needs to be imported from the google maps
regionspath = datapath + '/Manhattan_13.kml'

#actual pandas dataframes
links=pd.read_csv(linkspath)
nodes=pd.read_csv(nodespath)
nodes = nodes[['node_id','xcoord','ycoord']]
